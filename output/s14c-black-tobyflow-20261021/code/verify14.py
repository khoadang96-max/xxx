import json,re,collections
from build14 import FORBID  # rebuild deterministic
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
    if n.get('quantity',1)!=1: err.append('qty '+n['node_name'])
    if n.get('media_type')=='Video':
        f1=[e for e in inc[n['node_id']] if e['target_port']=='frame_1']
        if len(f1)!=1 or f1[0]['source_node_id']!=n['frame_1_source']: err.append('frame1 '+n['node_name'])
        t=[e for e in inc[n['node_id']] if e['target_port']=='text']
        if len(t)!=1: err.append('vtext '+n['node_name'])
        p=byid[t[0]['source_node_id']]['prompt']
        if not p.startswith(re.match(r'^[^,]+',p).group(0)) or f", {n['video_duration']} seconds," not in p: err.append('dur text '+n['node_name'])
        for k in ('Action:','Physics:','Living layer:','Object lock'):
            if k not in p: err.append(f'{k} missing '+n['node_name'])
        if n['video_download_resolution']!='1080p': err.append('1080 '+n['node_name'])
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
print('ERRORS',len(err)); print('\n'.join(err[:80]))
lens=[len(byid[e['source_node_id']]['prompt'].split()) for n in N if n.get('media_type')=='Video' for e in inc[n['node_id']] if e['target_port']=='text']
print('video prompt words min/max',min(lens),max(lens))
print(collections.Counter(r['dur'] for r in rows), collections.Counter(r['kind'] for r in rows))
