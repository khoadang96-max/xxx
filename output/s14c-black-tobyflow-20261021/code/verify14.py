import json,re,collections
from build14 import FORBID, MOVES_ON, FOOD_ACA, SKIN_TONE, SKIN_TONE_FRAME, CH, PEOPLE_LOCK  # rebuild deterministic
wf=json.load(open('out/workflow_S14c_Black.json'))['workflow']
N=wf['nodes'];E=wf['edges'];byid={n['node_id']:n for n in N}
err=[]
# ids/slug
c=collections.Counter(n['slug'] for n in N); err+=[f'dup slug {k}' for k,v in c.items() if v>1]
c=collections.Counter(n['node_id'] for n in N); err+=[f'dup id {k}' for k,v in c.items() if v>1]
for e in E:
    if len(e)!=8: err.append('edge fields '+e['edge_id'])
    if e['source_node_id'] not in byid or e['target_node_id'] not in byid: err.append('dangling '+e['edge_id'])
inc=collections.defaultdict(list)
for e in E: inc[e['target_node_id']].append(e)
for n in N:
    if n.get('media_type')=='Image' and n.get('quantity')!=4: err.append('qty x4 '+n['node_name'])
    if n.get('media_type')=='Video' and n.get('quantity')!=2: err.append('qty x2 '+n['node_name'])
    if n.get('media_type')=='Video':
        f1=[e for e in inc[n['node_id']] if e['target_port']=='frame_1']
        if len(f1)!=1 or f1[0]['source_node_id']!=n['frame_1_source']: err.append('frame1 '+n['node_name'])
        t=[e for e in inc[n['node_id']] if e['target_port']=='text']
        if len(t)!=1: err.append('vtext '+n['node_name'])
        p=byid[t[0]['source_node_id']]['prompt']
        if not p.startswith(re.match(r'^[^,]+',p).group(0)) or f", {n['video_duration']} seconds," not in p: err.append('dur text '+n['node_name'])
        for k in ('Action:','Physics:','Living layer','Object lock'):
            if k not in p: err.append(f'{k} missing '+n['node_name'])
        if n['video_download_resolution']!='1080p': err.append('1080 '+n['node_name'])
        f2=[e for e in inc[n['node_id']] if e['target_port']=='frame_2']
        talk=n['node_name'].startswith('S14c_T_'); sid=[r['id'] for r in json.load(open('out/_rows.json'))['rows'] if r['clip']==n['node_name']][0]
        want=talk and sid not in MOVES_ON
        if want!=bool(n.get('frame_2_source')) or len(f2)!=int(want): err.append('frame2 '+n['node_name'])
        if f2 and (f2[0]['source_node_id']!=n['frame_2_source'] or n['frame_2_source']!=n['frame_1_source'] or f2[0]['target_handle']!='input_4'): err.append('frame2 src '+n['node_name'])
        if 'Living layer (only what is already in the frame moves, nothing is added)' not in p: err.append('living form '+n['node_name'])
        if 'nothing moves on its own' not in p: err.append('phys logic '+n['node_name'])
        if 'the main action starts within the first second' not in p: err.append('first second '+n['node_name'])
        if talk and ('lips close and stay closed, no sound' not in p or 'Face:' not in p): err.append('talk blocks '+n['node_name'])
    if n.get('media_type')=='Image':
        t=[e for e in inc[n['node_id']] if e['target_port']=='text']
        if len(t)!=1: err.append('itext '+n['node_name'])
        p=byid[t[0]['source_node_id']]['prompt']
        refs=[e for e in inc[n['node_id']] if e['target_port']=='image_ref']
        mx=max([int(x) for x in re.findall(r'Image (\d+)',p)] or [0])
        if mx!=len(refs): err.append(f'ref count {n["node_name"]} prompt {mx} edges {len(refs)}')
        if 'IMG_ACA' in ' '.join(byid[e['source_node_id']]['node_name'] for e in refs) and n['node_name'].startswith('S14c_F') and 'Lighting match' not in p: err.append('lightmatch '+n['node_name'])
    if n['node_type']=='download':
        s=[e for e in inc[n['node_id']]]
        if len(s)!=1 or s[0]['target_port']!='media_in' or s[0]['data_type']!='video': err.append('tai '+n['node_name'])
for n in N:
    if n['node_type']=='prompt':
        low=' '+n['prompt'].lower().replace('over-sharpening','')+' '
        for w in FORBID:
            if w in low: err.append(f'forbid "{w}" in {n["node_name"]}')
        if 'WRENFIELD' in n['prompt'] or 'HAPPY 71ST' in n['prompt']:
            if 'no on-screen text' in n['prompt'] or 'no logos' in n['prompt'].replace('No other text, no logos','') : err.append('text kill '+n['node_name'])
# timing + lines
rows=json.load(open('out/_rows.json'))['rows']
src={s['id']:s for s in json.load(open('shots.json'))}
for r in rows:
    if r['kind']=='T':
        if r['end']+0.6>r['dur']: err.append('timing '+r['id'])
        if r['dur']>10: err.append('long '+r['id'])
# all lines covered
spoken={r['txt'] for r in rows if r['txt']}
for sid,s in src.items():
    m=re.match(r'^([A-Z]+)(?: \([^)]*\))?: (.*)$',s['line'])
    if m and m.group(2) not in spoken and sid not in ('D-1',): err.append('line missing '+sid)
# srt == lines
srt=open('out/S14c_Black_H1.srt').read()
for sid,s in src.items():
    if sid.startswith('S'):
        m=re.match(r'^([A-Z]+)(?: \([^)]*\))?: (.*)$',s['line'])
        if m and m.group(2).upper() not in srt: err.append('srt '+sid)
# policy / realism / food rules learned from Nam's chats
POLICY=['from behind','back to the','missing finger','extra finger','extra hand','third hand','woman shopper','not horror','toxic','poison']
REAL=['8k','ultra detailed','hyperrealistic','masterpiece','pristine','flawless','beautiful','perfect','smooth']
FOODW=r'potato|salad|tast|serv|spoonful|\bpot\b'
for n in N:
    if n['node_type']!='prompt': continue
    low=n['prompt'].lower()
    for w in POLICY:
        if w in low: err.append(f'policy "{w}" in {n["node_name"]}')
    for w in REAL:
        if w in low: err.append(f'realism "{w}" in {n["node_name"]}')
    if FOOD_ACA in n['prompt'] and re.search(r'crumb|burnt|spill|splatter|dirty',low): err.append('food-aca dirty '+n['node_name'])
    if ('acacia' in low or 'wooden serving spoon' in low or 'wooden spoon' in low) and re.search(FOODW,low) and n['node_name'].startswith(('P_F_','P_V_')):
        sid=n['node_name'][4:]
        from data14 import SH
        sh=[x for x in SH if x['id']==sid]
        if sh and 'aca' in sh[0]['props'] and re.search(FOODW,sh[0]['frame']+' '+sh[0]['action']) and FOOD_ACA not in n['prompt']: err.append('food-aca missing '+n['node_name'])
# characters: identity in every sheet, no glasses leaking onto people who wear none, brown-skin block, People lock
from data14 import SH as _SH
_sh={x['id']:x for x in _SH}
byname={n['node_name']:n for n in N}
for k,c in CH.items():
    if k=='B': continue
    pn=byname['P_'+c['sheet']]['prompt']
    if 'Black American' not in pn or SKIN_TONE not in pn: err.append('sheet identity '+c['sheet'])
    if c['full'] not in pn: err.append('sheet full text '+c['sheet'])
    if k[0] in 'TJW' or k=='FD':
        if 'glasses' in pn.lower(): err.append('glasses leak '+c['sheet'])
for sid,x in _sh.items():
    pf=byname.get('P_F_'+sid)
    if not pf: continue
    pl=pf['prompt'].lower(); who=set(c[0] for c in x['chars'])
    if re.search(r'(?<!drinking )\bglasses\b', pl) and not (who & {'G','D'}): err.append('glasses leak frame '+sid)
    if (x['chars'] and SKIN_TONE_FRAME not in pf['prompt']) or (x['hands_of'] and 'palms lighter than the backs of the hands' not in pf['prompt']): err.append('skin block '+sid)
    pv=byname['P_V_'+sid]['prompt']
    if x['chars'] and PEOPLE_LOCK not in pv: err.append('people lock '+sid)
from build14 import BOTTLE
if 'church hat' not in byname['P_CS_DOROTHY']['prompt']: err.append('dorothy hat sheet')
for sid,x in _sh.items():
    pf=byname.get('P_F_'+sid)
    if not pf: continue
    hasD='D' in x['chars']
    if hasD != ('church hat' in pf['prompt']): err.append('hat '+sid)
    if ('bottle' in x['props']) != (BOTTLE in pf['prompt']) or ('bottle' not in x['props'] and 'tumbler' in pf['prompt']): err.append('bottle '+sid)
import collections as _c; print('ERRORS',len(err)); print(_c.Counter(e.split(' S14c')[0].split(' P_')[0] for e in err)); print('\n'.join(err[:40]))
lens=[len(byid[e['source_node_id']]['prompt'].split()) for n in N if n.get('media_type')=='Video' for e in inc[n['node_id']] if e['target_port']=='text']
print('video prompt words min/max',min(lens),max(lens))
tl=[(len(byid[e['source_node_id']]['prompt'].split()),n['node_name']) for n in N if n.get('media_type')=='Video' for e in inc[n['node_id']] if e['target_port']=='text']
print('T >370 words:',[x for x in tl if x[1].startswith('S14c_T_') and x[0]>370]); print('V >320 words:',[x for x in tl if x[1].startswith('S14c_V_') and x[0]>320])
print('frame_2 clips:',sum(1 for n in N if n.get('frame_2_source')),'| x4 images:',sum(1 for n in N if n.get('media_type')=='Image' and n.get('quantity')==4),'| x2 videos:',sum(1 for n in N if n.get('media_type')=='Video' and n.get('quantity')==2))
print(collections.Counter(r['dur'] for r in rows), collections.Counter(r['kind'] for r in rows))
