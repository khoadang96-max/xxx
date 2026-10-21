# Split S14c shots into small importable workflows (<= CAP bytes each); Setup stays as already imported
import json, random, string, re, os, collections, shutil
CAP = 90 * 1024
random.seed(2111)
full = json.load(open('out/workflow_S14c_Black.json'))['workflow']
N = full['nodes']; E = full['edges']
by_id = {n['node_id']: n for n in N}; by_name = {n['node_name']: n for n in N}
OUT = 'out/parts2'; shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT + '/mcp')
dump = lambda o: json.dumps(o, ensure_ascii=False, separators=(',', ':'))

# story order; '|' forces a new file
ORDER = (['C-1', 'C-2', 'S02_C', 'B-1', 'S02_B', 'S03_B', '|',
          'A-1', 'E-2', 'S01', 'S02', 'S03', 'S04', 'S05', 'S06', 'S07', 'S08']
         + ['S%02d' % i for i in range(9, 49)]
         + [x for x in ['S%02d' % i for i in range(49, 71)] if x != 'S55']
         + ['D-2'] + ['S%02d' % i for i in range(71, 91)])
SCENE = {}
for s in ['C-1', 'C-2', 'S02_C', 'B-1', 'S02_B', 'S03_B']: SCENE[s] = 'Hook C B'
for s in ['B-1', 'S02_B', 'S03_B', 'A-1', 'E-2'] + ['S%02d' % i for i in range(1, 9)] + ['S02', 'S03']: SCENE.setdefault(s, 'Sinh nhat')
for i in range(9, 18): SCENE['S%02d' % i] = 'Bep dem'
for i in (18, 19): SCENE['S%02d' % i] = 'Hien dem'
for i in range(20, 27): SCENE['S%02d' % i] = 'Sang'
SCENE['S27'] = 'Dong thung'
for i in range(28, 36): SCENE['S%02d' % i] = 'Hien Dorothy'
for i in range(36, 49): SCENE['S%02d' % i] = 'Co che'
for i in range(49, 57): SCENE['S%02d' % i] = 'San pham'
for i in range(57, 71): SCENE['S%02d' % i] = 'Loi cuoc'
SCENE['D-2'] = 'Thu Sau'
for i in range(71, 82): SCENE['S%02d' % i] = 'Thu Sau'
for i in range(82, 91): SCENE['S%02d' % i] = 'Close'

def nid(): return 'node_' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))

def shot_nodes(sid):
    out = [by_name[nm] for nm in (f'P_F_{sid}', f'S14c_F_{sid}', f'P_V_{sid}') if nm in by_name]
    v = [n for n in N if n.get('media_type') == 'Video' and re.fullmatch(rf'S14c_[TV]_{re.escape(sid.replace("-", ""))}', n['node_name'])]
    assert len(v) == 1, sid
    return out + [v[0], by_name['TAI ' + v[0]['node_name']]]

def make(num, sids, keep_ids=True):
    scenes = list(dict.fromkeys(SCENE[s] for s in sids))
    wname = f'S14c_{num} ' + ' - '.join(scenes)
    core = [n for sid in sids for n in shot_nodes(sid)]
    core_ids = {n['node_id'] for n in core}
    ext = []
    for e in E:
        if e['target_node_id'] in core_ids and e['source_node_id'] not in core_ids and e['source_node_id'] not in ext:
            ext.append(e['source_node_id'])
    imgs, remap = [], {}
    for i, sid_ in enumerate(ext):
        src = by_id[sid_]
        name = src['node_name'] if src['node_name'].startswith('IMG_') else 'IMG_' + src['node_name']
        n = dict(node_id=nid(), node_type='image', node_name=name, pos_x=0, pos_y=i * 400, enabled=True,
                 slug=name.lower(), slug_auto=False, ref_images=[])
        imgs.append((n, src)); remap[sid_] = n['node_id']
    nodes = [n for n, _ in imgs]
    for r, sid in enumerate(sids):
        for n in shot_nodes(sid):
            n = dict(n); nm = n['node_name']
            x = 1200 if nm.startswith('P_V_') else 400 if nm.startswith('P_') else 2000 if nm.startswith('TAI ') else 1600 if n.get('media_type') == 'Video' else 800
            n.update(pos_x=x, pos_y=r * 400)
            if n.get('frame_1_source') in remap: n['frame_1_source'] = remap[n['frame_1_source']]
            nodes.append(n)
    pos = {n['node_id']: i + 1 for i, n in enumerate(nodes)}
    edges = []
    for e in E:
        if e['target_node_id'] not in core_ids: continue
        e = dict(e); e['source_node_id'] = remap.get(e['source_node_id'], e['source_node_id'])
        e['edge_id'] = f"edge_{pos[e['source_node_id']]}_{e['source_handle']}_{pos[e['target_node_id']]}_{e['target_handle']}"
        edges.append({k: e[k] for k in ('edge_id','source_node_id','source_handle','source_port','target_node_id','target_handle','target_port','data_type')})
    up = [f"{n['node_name']} = " + ('ảnh thật' if src['node_type'] == 'image' else f"ảnh của node {src['node_name']} ở S14c_0 Setup") for n, src in imgs]
    desc = (f"S14c We Talked About This (bản da đen), file {num}: {', '.join(sids)}. Tải ảnh vào: " + '; '.join(up)
            + ". Chạy F_ (xem khung) → T_/V_ → TAI.")
    wf = {"version": "1.0", "type": "workflow", "exported_at": "2026-10-21T16:00:00.000Z",
          "workflow": {"name": wname, "description": desc, "settings": full['settings'], "nodes": nodes, "edges": edges}}
    return wf, imgs, wname

# pack: fewest files under CAP, then fewest IMG uploads (DP over story order)
head, rest = ORDER[:ORDER.index('|')], ORDER[ORDER.index('|') + 1:]
seg = {}
for i in range(len(rest)):
    for j in range(i + 1, min(len(rest), i + 16) + 1):
        wf, imgs, _ = make('99', rest[i:j])
        if len(dump(wf).encode()) > CAP: break
        seg[(i, j)] = len(imgs)
INF = (10 ** 9, 10 ** 9)
best = [INF] * (len(rest) + 1); prev = [None] * (len(rest) + 1); best[0] = (0, 0)
for j in range(1, len(rest) + 1):
    for i in range(j):
        if (i, j) in seg and best[i] != INF:
            c = (best[i][0] + 1, best[i][1] + seg[(i, j)])
            if c < best[j]: best[j], prev[j] = c, i
cuts, j = [], len(rest)
while j: cuts.append((prev[j], j)); j = prev[j]
files = [head] + [rest[i:j] for i, j in reversed(cuts)]

parts = []
for i, sids in enumerate(files, 1):
    num = f'{i:02d}'
    wf, imgs, wname = make(num, sids)
    tag = re.sub(r'[^A-Za-z0-9]+', '', wname.split(' ', 1)[1].split(' - ')[0].title())
    path = f'{OUT}/workflow_S14c_{num}_{tag}.json'
    open(path, 'w').write(dump(wf))
    nodes, edges = wf['workflow']['nodes'], wf['workflow']['edges']
    name_of = {n['node_id']: n['node_name'] for n in nodes}
    mcp = dict(name=wname, description=wf['workflow']['description'], settings_json=full['settings'],
               nodes=[{**{k: v for k, v in n.items() if k not in ('node_id', 'pos_x', 'pos_y', 'node_type')}, 'ref': n['node_name'], 'type': n['node_type'],
                       **({'frame_1_source': name_of[n['frame_1_source']]} if n.get('frame_1_source') else {})} for n in nodes],
               edges=[{'from': name_of[e['source_node_id']], 'to': name_of[e['target_node_id']], 'port': e['target_port'], 'source_port': e['source_port'],
                       'source_handle': e['source_handle'], 'target_port': e['target_port'], 'target_handle': e['target_handle'], 'data_type': e['data_type']} for e in edges])
    open(f'{OUT}/mcp/mcp_S14c_{num}_{tag}.json', 'w').write(dump(mcp))
    parts.append(dict(num=num, file=os.path.basename(path), name=wname, shots=sids, n_nodes=len(nodes), n_edges=len(edges),
                      kb=round(os.path.getsize(path) / 1024, 1), clips=[n['node_name'] for n in nodes if n.get('media_type') == 'Video'],
                      uploads=[(n['node_name'], src['node_name'], src['node_type']) for n, src in imgs]))

# checks
err = []
allv = sorted(n['node_name'] for n in N if n.get('media_type') == 'Video')
if sorted(c for p in parts for c in p['clips']) != allv: err.append('clips not covered exactly once')
for p in parts:
    w = json.load(open(f"{OUT}/{p['file']}"))['workflow']
    ids = {n['node_id']: n for n in w['nodes']}
    inc = collections.defaultdict(list)
    for e in w['edges']:
        if e['source_node_id'] not in ids or e['target_node_id'] not in ids: err.append(p['file'] + ' dangling')
        inc[e['target_node_id']].append(e)
    if len({e['edge_id'] for e in w['edges']}) != len(w['edges']): err.append(p['file'] + ' dup edge id')
    if len({n['slug'] for n in w['nodes']}) != len(w['nodes']): err.append(p['file'] + ' dup slug')
    if len({n['node_id'] for n in w['nodes']}) != len(w['nodes']): err.append(p['file'] + ' dup node id')
    if os.path.getsize(f"{OUT}/{p['file']}") > CAP: err.append(p['file'] + ' over cap')
    for n in w['nodes']:
        if n.get('media_type') == 'Video':
            f1 = [e for e in inc[n['node_id']] if e['target_port'] == 'frame_1']
            if len(f1) != 1 or f1[0]['source_node_id'] != n['frame_1_source']: err.append(p['file'] + ' frame1 ' + n['node_name'])
            if len([e for e in inc[n['node_id']] if e['target_port'] == 'text']) != 1: err.append(p['file'] + ' vtext ' + n['node_name'])
        if n.get('media_type') == 'Image':
            pr = [ids[e['source_node_id']]['prompt'] for e in inc[n['node_id']] if e['target_port'] == 'text'][0]
            refs = [e for e in inc[n['node_id']] if e['target_port'] == 'image_ref']
            mx = max([int(x) for x in re.findall(r'Image (\d+)', pr)] or [0])
            if mx != len(refs): err.append(f"{p['file']} refs {n['node_name']}")
        if n['node_type'] == 'download':
            s = inc[n['node_id']]
            if len(s) != 1 or s[0]['target_port'] != 'media_in' or s[0]['data_type'] != 'video': err.append(p['file'] + ' tai ' + n['node_name'])
print('ERRORS', len(err), err[:10])
for p in parts:
    print(f"{p['file']:44s} {p['kb']:5.1f} KB {p['n_nodes']:3d} node {len(p['clips']):2d} clip {len(p['uploads']):2d} IMG | {p['shots'][0]}..{p['shots'][-1]}")
print('total uploads', sum(len(p['uploads']) for p in parts))
json.dump(parts, open(f'{OUT}/_parts.json', 'w'), ensure_ascii=False, indent=1)
