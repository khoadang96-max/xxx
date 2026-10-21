# Split S14c full workflow into 6 importable workflows (setup + 5 scene groups)
import json, random, string, re, os, collections
random.seed(2110)
full = json.load(open('out/workflow_S14c_Black.json'))['workflow']
N = full['nodes']; E = full['edges']
by_id = {n['node_id']: n for n in N}; by_name = {n['node_name']: n for n in N}
OUT = 'out/parts'; os.makedirs(OUT + '/mcp', exist_ok=True)

GROUPS = [
 ('0', 'Setup', 'S14c_0 Setup', 'character sheet + đạo cụ + 8 ảnh nền', None),
 ('1', 'SinhNhat', 'S14c_1 Sinh nhat', 'tiệc sinh nhật + 5 hook + bản S02/S03 cho hook B, C',
  ['A-1','B-1','C-1','C-2','E-2','S01','S02','S02_B','S02_C','S03','S03_B','S04','S05','S06','S07','S08']),
 ('2', 'DemSang', 'S14c_2 Dem Sang', 'bếp đêm, hiên đêm, sáng hôm sau',
  ['S%02d' % i for i in range(9, 27)]),
 ('3', 'ChuNhat', 'S14c_3 Chu nhat', 'đóng thùng, hiên Dorothy, Dorothy trong bếp (cơ chế)',
  ['S27'] + ['S%02d' % i for i in range(28, 49)]),
 ('4', 'LoiCuoc', 'S14c_4 Loi cuoc', 'sản phẩm, gửi link, con trai ngửi, lời cược',
  [x for x in ['S%02d' % i for i in range(49, 71)] if x != 'S55']),
 ('5', 'ThuSauClose', 'S14c_5 Thu Sau Close', 'bữa tối thứ Sáu + hook D-2 + Close nói vào máy',
  ['D-2'] + ['S%02d' % i for i in range(71, 91)]),
]
SETUP_PREFIX = ('P_CS_', 'CS_', 'P_PROP_', 'PROP_', 'P_BG_', 'BG_')

def nid(): return 'node_' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))

def shot_nodes(sid):
    out = []
    for nm in (f'P_F_{sid}', f'S14c_F_{sid}', f'P_V_{sid}'):
        if nm in by_name: out.append(by_name[nm])
    vid = [n for n in N if n.get('media_type') == 'Video' and re.fullmatch(rf'S14c_[TV]_{re.escape(sid.replace("-", ""))}', n['node_name'])]
    assert len(vid) == 1, sid
    v = vid[0]; out.append(v)
    out.append(by_name['TAI ' + v['node_name']])
    return out

parts = []
seen_clips = []
for num, fname, wname, what, sids in GROUPS:
    if sids is None:
        core = [n for n in N if n['node_name'].startswith(SETUP_PREFIX)]
    else:
        core = [n for sid in sids for n in shot_nodes(sid)]
    core_ids = {n['node_id'] for n in core}
    # external sources -> local image nodes Nam fills
    ext_order = []
    for e in E:
        if e['target_node_id'] in core_ids and e['source_node_id'] not in core_ids and e['source_node_id'] not in ext_order:
            ext_order.append(e['source_node_id'])
    img_nodes, remap = [], {}
    for i, sid_ in enumerate(ext_order):
        src = by_id[sid_]
        name = src['node_name'] if src['node_name'].startswith('IMG_') else 'IMG_' + src['node_name']
        n = dict(node_id=nid(), node_type='image', node_name=name, pos_x=0, pos_y=i * 400, enabled=True,
                 slug=name.lower(), slug_auto=False, ref_images=[])
        img_nodes.append((n, src)); remap[sid_] = n['node_id']
    nodes = [n for n, _ in img_nodes]
    # layout core: one row per shot / sheet
    rows = collections.OrderedDict()
    for n in core:
        key = re.sub(r'^(P_F_|S14c_F_|P_V_|S14c_[TV]_|TAI S14c_[TV]_|P_)', '', n['node_name'])
        rows.setdefault(key.replace('-', ''), []).append(n)
    col = {'prompt_F': 400, 'F': 800, 'prompt_V': 1200, 'V': 1600, 'TAI': 2000}
    for r, (key, ns) in enumerate(rows.items()):
        for n in ns:
            n = dict(n); y = r * 400
            nm = n['node_name']
            if nm.startswith('P_V_'): x = 1200
            elif nm.startswith('P_'): x = 400
            elif nm.startswith('TAI '): x = 2000
            elif n.get('media_type') == 'Video': x = 1600
            else: x = 800
            n.update(pos_x=x, pos_y=y)
            if n.get('frame_1_source') in remap: n['frame_1_source'] = remap[n['frame_1_source']]
            nodes.append(n)
    ids = {n['node_id'] for n in nodes}
    pos = {n['node_id']: i + 1 for i, n in enumerate(nodes)}
    edges = []
    for e in E:
        if e['target_node_id'] not in core_ids: continue
        e = dict(e); e['source_node_id'] = remap.get(e['source_node_id'], e['source_node_id'])
        assert e['source_node_id'] in ids
        e['edge_id'] = f"edge_{pos[e['source_node_id']]}_{e['source_handle']}_{pos[e['target_node_id']]}_{e['target_handle']}"
        edges.append(e)
    edges = [{k: e[k] for k in ('edge_id','source_node_id','source_handle','source_port','target_node_id','target_handle','target_port','data_type')} for e in edges]
    # description: what to upload
    up = []
    for n, src in img_nodes:
        if src['node_type'] == 'image': up.append(f"{n['node_name']} = ảnh thật (xem doc mục 2)")
        else: up.append(f"{n['node_name']} = ảnh kết quả node {src['node_name']} ở S14c_0 Setup")
    desc = (f"S14c We Talked About This (bản da đen) — phần {num}/5: {what}. "
            + ("Trước khi chạy, tải ảnh vào: " + '; '.join(up) + '. ' if up else '')
            + "Chạy: ảnh F_ (xem khung) → clip T_/V_ → TAI. Clip có thoại: Omni nói để khớp miệng, dựng thay bằng giọng ElevenLabs.")
    wf = {"version": "1.0", "type": "workflow", "exported_at": "2026-10-21T15:00:00.000Z",
          "workflow": {"name": wname, "description": desc, "settings": full['settings'], "nodes": nodes, "edges": edges}}
    path = f'{OUT}/workflow_S14c_{num}_{fname}.json'
    json.dump(wf, open(path, 'w'), ensure_ascii=False, separators=(',', ':'))
    # MCP payload
    name_of = {n['node_id']: n['node_name'] for n in nodes}
    mcp = dict(name=wname, description=desc, settings_json=full['settings'],
               nodes=[{**{k: v for k, v in n.items() if k not in ('node_id', 'pos_x', 'pos_y', 'node_type')}, 'ref': n['node_name'], 'type': n['node_type'],
                       **({'frame_1_source': name_of[n['frame_1_source']]} if n.get('frame_1_source') else {})} for n in nodes],
               edges=[{'from': name_of[e['source_node_id']], 'to': name_of[e['target_node_id']], 'port': e['target_port'], 'source_port': e['source_port'],
                       'source_handle': e['source_handle'], 'target_port': e['target_port'], 'target_handle': e['target_handle'], 'data_type': e['data_type']} for e in edges])
    json.dump(mcp, open(f'{OUT}/mcp/mcp_S14c_{num}_{fname}.json', 'w'), ensure_ascii=False, separators=(',', ':'))
    clips = [n['node_name'] for n in nodes if n.get('media_type') == 'Video']
    seen_clips += clips
    parts.append(dict(num=num, file=os.path.basename(path), name=wname, what=what, n_nodes=len(nodes), n_edges=len(edges),
                      kb=round(os.path.getsize(path) / 1024), clips=clips, uploads=[(n['node_name'], src['node_name'], src['node_type']) for n, src in img_nodes]))

# ---- checks ----
err = []
allv = [n['node_name'] for n in N if n.get('media_type') == 'Video']
if sorted(seen_clips) != sorted(allv): err.append('clips not covered exactly once')
for p in parts:
    w = json.load(open(f"{OUT}/{p['file']}"))['workflow']
    ids = {n['node_id']: n for n in w['nodes']}
    inc = collections.defaultdict(list)
    for e in w['edges']:
        if e['source_node_id'] not in ids or e['target_node_id'] not in ids: err.append(p['file'] + ' dangling')
        inc[e['target_node_id']].append(e)
    if len({e['edge_id'] for e in w['edges']}) != len(w['edges']): err.append(p['file'] + ' dup edge id')
    if len({n['slug'] for n in w['nodes']}) != len(w['nodes']): err.append(p['file'] + ' dup slug')
    if len(w['nodes']) > 125: err.append(p['file'] + ' too many nodes')
    for n in w['nodes']:
        if n.get('media_type') == 'Video':
            f1 = [e for e in inc[n['node_id']] if e['target_port'] == 'frame_1']
            if len(f1) != 1 or f1[0]['source_node_id'] != n['frame_1_source']: err.append(p['file'] + ' frame1 ' + n['node_name'])
        if n.get('media_type') == 'Image':
            pr = [ids[e['source_node_id']]['prompt'] for e in inc[n['node_id']] if e['target_port'] == 'text'][0]
            refs = [e for e in inc[n['node_id']] if e['target_port'] == 'image_ref']
            mx = max([int(x) for x in re.findall(r'Image (\d+)', pr)] or [0])
            if mx != len(refs): err.append(f"{p['file']} refs {n['node_name']}")
        if n['node_type'] == 'download' and 'download' in n: err.append('stray download field')
print('ERRORS', len(err), err[:20])
for p in parts: print(p['file'], p['n_nodes'], 'node', p['n_edges'], 'edge', p['kb'], 'KB', len(p['clips']), 'clip', len(p['uploads']), 'IMG')
json.dump(parts, open(f'{OUT}/_parts.json', 'w'), ensure_ascii=False, indent=1)
