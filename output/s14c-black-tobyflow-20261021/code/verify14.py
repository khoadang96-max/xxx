import json,re,collections
from build14 import FORBID, HOLD_POSE, FOOD_ACA, SKIN_TONE, SKIN_TONE_FRAME, CH, PEOPLE_LOCK  # rebuild deterministic
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
        if not p.startswith(re.match(r'^[^,]+',p).group(0)) or f", {n['video_duration'].rstrip('s')} seconds," not in p or not re.fullmatch(r'(4|6|8|10)s', n['video_duration']) or n.get('download_resolution')!='1080p' : err.append('dur text '+n['node_name'])
        for k in ('Action:','Physics:','Living layer','Object lock'):
            if k not in p: err.append(f'{k} missing '+n['node_name'])
        if n['video_download_resolution']!='1080p': err.append('1080 '+n['node_name'])
        f2=[e for e in inc[n['node_id']] if e['target_port']=='frame_2']
        talk=n['node_name'].startswith('S14c_T_'); sid=[r['id'] for r in json.load(open('out/_rows.json'))['rows'] if r['clip']==n['node_name']][0]
        want=talk and sid in HOLD_POSE
        if want!=bool(n.get('frame_2_source')) or len(f2)!=int(want): err.append('frame2 '+n['node_name'])
        if f2 and (f2[0]['source_node_id']!=n['frame_2_source'] or n['frame_2_source']!=n['frame_1_source'] or f2[0]['target_handle']!='input_4'): err.append('frame2 src '+n['node_name'])
        if 'Living layer (only what is already in the frame moves, nothing is added)' not in p: err.append('living form '+n['node_name'])
        if 'nothing moves on its own' not in p: err.append('phys logic '+n['node_name'])
        if 'the main action starts within the first second' not in p: err.append('first second '+n['node_name'])
        if talk and ('lips close and stay closed, no sound' not in p or 'Face and body:' not in p or 'never over-acted' not in p): err.append('talk blocks '+n['node_name'])
        if re.search(r'\bwag|neck roll|rolls? (her|his) eyes|hands? on (her|his) hips?|sassy|snaps? (her|his) fingers', p): err.append('stereotype gesture '+n['node_name'])
        act = re.search(r'Action: (.*?) Living layer', p).group(1)
        if talk and (re.search(r'(stays|keeps) (\w+ )?still', act) or 'same grip, length and angle' in p): err.append('hold-pose wording '+n['node_name'])
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
# rooms and photos: every photo shows this Black family; room states are edits of one base image; no unnamed people at the table
from build14 import BG_EDIT, WALL_PHOTOS, FRIDGE_PHOTOS, CHURCH_FAN, TABLE_FOOD
for n in N:
    if n['node_type']!='prompt': continue
    pl=n['prompt']
    if re.search(r'family and graduation photos|family photos on the fridge', pl): err.append('generic photos '+n['node_name'])

if WALL_PHOTOS not in byname['P_BG_A_BDAY']['prompt']: err.append('wall photos')
for k in ('B_MORNING',):
    if FRIDGE_PHOTOS not in byname['P_BG_'+k]['prompt'] or CHURCH_FAN not in byname['P_BG_'+k]['prompt']: err.append('kitchen decor '+k)
from build14 import SEATS, GUESTS, PART_VIEW, GIFTS, FRI_SIDEBOARD, FRI_SIDEBOARD_SOFT, NO_CAKE, OFF_SIDEBOARD, WIFE_WEAR, MASTER_PROMPT, aunt, uncle
from build14 import HALLWAY
def is_dinner(x): return x['bg'] in ('A_BDAY','A_FRI') and bool(x['chars']) and x['id'] not in HALLWAY
for sid,x in _sh.items():
    pf=byname.get('P_F_'+sid)
    if not pf: continue
    p=pf['prompt']
    if is_dinner(x):
        f=byname['S14c_F_'+sid]
        srcs=[byid[e['source_node_id']]['node_name'] for e in inc[f['node_id']] if e['target_port']=='image_ref']
        if 'MASTER_A_BDAY' not in srcs: err.append('dinner ref '+sid)
        wide=x['shot']=='Wide shot'
        if wide and not all(b in p for b in (SEATS, GUESTS, aunt(x['bg']), uncle(x['bg']))): err.append('seat plan '+sid)
        if not wide and PART_VIEW not in p: err.append('part view '+sid)
        if wide and f"framing as Image {srcs.index('MASTER_A_BDAY')+1}" not in p: err.append('main camera '+sid)
        if 'W' in x['chars'] and WIFE_WEAR[x['bg']] not in p: err.append('wife outfit '+sid)
        if x['bg']=='A_BDAY' and 'table' in x['frame'] and NO_CAKE not in p: err.append('no cake '+sid)
        side=bool(re.search(r'gift|sideboard', x['frame'])) and OFF_SIDEBOARD not in x['frame']
        if x['bg']=='A_FRI' and (wide or side) and (FRI_SIDEBOARD if 'aca' in x['props'] else FRI_SIDEBOARD_SOFT) not in p: err.append('friday sideboard '+sid)
        if 'wooden utensils' in p and 'aca' not in x['props'] and 'soft and out of focus' not in p: err.append('wood without product ref '+sid)
        if OFF_SIDEBOARD in x['frame'] and (GIFTS in p or FRI_SIDEBOARD in p or FRI_SIDEBOARD_SOFT in p): err.append('sideboard block off-frame '+sid)
        if re.search(r'behind (him|her), soft, the (gold 71 balloons|corner of the sideboard)', x['frame']): err.append('head of room behind speaker '+sid)
    elif re.search(r'\b(family|whole (birthday )?table|everyone at|relatives|guests)\b', x['frame']) and 'Black American' not in x['frame']: err.append('unnamed people '+sid)
    if x['bg']=='A_BDAY' and re.search(r'gift|sideboard', x['frame']) and OFF_SIDEBOARD not in x['frame'] and GIFTS not in p: err.append('gifts '+sid)
    if 'D' in x['chars'] and 'tote bag on the swing' in x['frame'] and 'on her shoulder' in p: err.append('two tote bags '+sid)
    if re.search(r'wall with the archway|fork and spoon on the wall', x['frame']): err.append('room side mixed up '+sid)
    if x['chars'] and f"Expressions true to this moment: {x['face']};" not in p: err.append('face line '+sid)
    if re.search(r'nobody smiles|no smile', x['face']) and re.search(r'\bsmil|\bgrin|laugh', x['frame'] + ' ' + x['action']) and not re.search(r'smile (fades|freezes|falter)|smile still|still smiling|hostess smile', x['frame'] + ' ' + x['action']): err.append('smile in a no-smile beat '+sid)
    if re.search(r'angr|rage|furious|disgust', x['face']) and not re.search(r'not (angry|raging)|never disgusted|not angry', x['face']): err.append('face tone '+sid)
    if 'full set in the round holder' in x['action'] and 'holding' in x['frame']: err.append('eight pieces '+sid)
    if '{MASTER}' in p or 'framing as :' in p or ('main camera' in x['frame'] and not re.search(r'framing as Image \d', p)) or re.search(r'\bcake\b', p.replace(NO_CAKE, '')): err.append('master/cake text '+sid)
    if x['bg'] in ('A_BDAY','A_FRI') and x['chars'] and not is_dinner(x) and 'hallway' not in x['frame']: err.append('dinner flag '+sid)
    if ('bro' in x['props']) != (sid in ('B-1','S04','S05','S07','S08','S16','D-2','S78')): err.append('brochure place '+sid)
for b in (SEATS, GUESTS, GIFTS, NO_CAKE, aunt('A_BDAY'), uncle('A_BDAY')):
    if b not in MASTER_PROMPT: err.append('master block')
m=byname['MASTER_A_BDAY']
if [byid[e['source_node_id']]['node_name'] for e in inc[m['node_id']] if e['target_port']=='image_ref']!=['BG_A_BDAY','CS_GLORIA_1','CS_TERRANCE_1','CS_JADA_1','CS_WIFE']: err.append('master refs')
if 'no brochure in this frame' not in _sh['S06']['frame']: err.append('S06 brochure')
for k,(base,_,_,_) in BG_EDIT.items():
    im=byname['BG_'+k]
    srcs=[byid[e['source_node_id']]['node_name'] for e in inc[im['node_id']] if e['target_port']=='image_ref']
    if not srcs or srcs[0]!='BG_'+base: err.append('bg edit ref '+k)
for sid,x in _sh.items():
    pf=byname.get('P_F_'+sid)
    if pf and is_dinner(x) and 'table' in x['frame'] and TABLE_FOOD not in pf['prompt']: err.append('table food '+sid)
# physical causes and continuity added in the final review
from build14 import KEEP_DINING, KITCHEN
if 'sideboard' not in KEEP_DINING or 'trash can' not in KITCHEN: err.append('room keep list')
for sid,x in _sh.items():
    t=x['frame']+' '+x['action']
    if re.search(r'\blid\b', t) and 'pedal' not in t: err.append('lid without cause '+sid)
    if re.search(r'steam|simmer|sizzl', t) and not re.search(r'lit burner|boiling|just-boiled|hot|warm', t): err.append('steam without heat '+sid)
    pf=byname.get('P_F_'+sid)
    if pf and x['bg_ref'] and x['bg_ref'].split('{n}')[0] not in pf['prompt']: err.append('bg_ref '+sid)
for n in N:
    if n['node_type']=='prompt' and re.search(r'moving box', n['prompt']) and 'unprinted and unlabeled, with no brand marks' not in n['prompt'] and 'no boxes' not in n['prompt']: err.append('box logos '+n['node_name'])
import collections as _c; print('ERRORS',len(err)); print(_c.Counter(e.split(' S14c')[0].split(' P_')[0] for e in err)); print('\n'.join(err[:40]))
lens=[len(byid[e['source_node_id']]['prompt'].split()) for n in N if n.get('media_type')=='Video' for e in inc[n['node_id']] if e['target_port']=='text']
print('video prompt words min/max',min(lens),max(lens))
if max(lens)>600: err.append('clip prompt over 600 words'); print('ERROR clip prompt over 600 words')
tl=[(len(byid[e['source_node_id']]['prompt'].split()),n['node_name']) for n in N if n.get('media_type')=='Video' for e in inc[n['node_id']] if e['target_port']=='text']
print('T >370 words:',[x for x in tl if x[1].startswith('S14c_T_') and x[0]>370]); print('V >320 words:',[x for x in tl if x[1].startswith('S14c_V_') and x[0]>320])
print('frame_2 clips:',sum(1 for n in N if n.get('frame_2_source')),'| x4 images:',sum(1 for n in N if n.get('media_type')=='Image' and n.get('quantity')==4),'| x2 videos:',sum(1 for n in N if n.get('media_type')=='Video' and n.get('quantity')==2))
print(collections.Counter(r['dur'] for r in rows), collections.Counter(r['kind'] for r in rows))
