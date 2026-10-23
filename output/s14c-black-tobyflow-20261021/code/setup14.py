# Split the S14c setup images into importable workflows with no same-file reference:
#   0A = base character sheets + prop sheets + backgrounds; 0B = outfit sheets made from the 0A base sheets (uploaded as IMG_CS_*_1)
#   0C = the dinner table reference MASTER_A_BDAY (Nam 23/10): the 0A room plate with everyone in their seats, used by every dinner frame
import json, random, string, re, os, collections, shutil
random.seed(2210)
full = json.load(open('out/workflow_S14c_Black.json'))['workflow']
N = full['nodes']; E = full['edges']
by_id = {n['node_id']: n for n in N}; by_name = {n['node_name']: n for n in N}
OUT = 'out/setup'; shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT + '/mcp')
dump = lambda o: json.dumps(o, ensure_ascii=False, separators=(',', ':'))
def nid(): return 'node_' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))

VIEWS = ('BG_A_WEST', 'BG_A_EAST', 'BG_A_SOUTH')  # the standard room's other camera directions (0E), edits of the 0A dining plate
KREV = ('BG_B_NIGHT_REV', 'BG_B_CLEAR_REV')       # the kitchen seen from the sink end (0F, review 23/10), edits of the morning kitchen
images = [n for n in N if n.get('media_type') == 'Image' and n['node_name'].startswith(('CS_', 'PROP_', 'BG_')) and n['node_name'] not in VIEWS + KREV]
inc = collections.defaultdict(list)
for e in E: inc[e['target_node_id']].append(e)
def is_edit(n):  # outfit sheet: its reference is another generated sheet
    return any(e['target_port'] == 'image_ref' and by_id[e['source_node_id']].get('media_type') == 'Image' for e in inc[n['node_id']])
GROUPS = [('0A', 'Setup', 'S14c_0A Setup nhan vat nen', 'character sheet gốc 7 nhân vật + 2 sheet đạo cụ + 4 ảnh nền gốc', [n for n in images if not is_edit(n)]),
          ('0B', 'DoiDo', 'S14c_0B Doi do', '7 sheet đổi đồ (Gloria 2–4, Terrance 2–4, Jada 2) và 4 ảnh nền cùng phòng (phòng ăn thứ Sáu, bếp đêm, bếp đóng thùng, bếp vài tuần sau) sửa từ ảnh gốc ở 0A', [n for n in images if is_edit(n)]),
          ('0C', 'BanAn', 'S14c_0C Ban an mau', 'ảnh mẫu bàn tiệc sinh nhật: đủ 7 người ngồi đúng chỗ, cùng góc máy với ảnh nền BG_A_BDAY', [n for n in N if n['node_name'] == 'MASTER_A_BDAY']),
          # 0D (23/10): the Friday master, edited from the chosen birthday master with the Friday outfit sheets; every Friday table frame edits it
          ('0D', 'BanAnThuSau', 'S14c_0D Ban an thu Sau', 'ảnh mẫu bàn ăn tối thứ Sáu: sửa từ ảnh 0C đã chọn, cùng góc máy, cùng chỗ ngồi, đồ thứ Sáu, không trang trí sinh nhật', [n for n in N if n['node_name'] == 'MASTER_A_FRI']),
          ('0E', 'PhongAn4Huong', 'S14c_0E Phong an 4 huong', 'ảnh nền trống phòng ăn cho 3 hướng máy còn lại (nhìn sang tường ảnh, nhìn sang tường cửa sổ, nhìn từ đầu bàn xuống), sửa từ ảnh nền BG_A_BDAY', [n for n in N if n['node_name'] in VIEWS]),
          # 0F (review 23/10): the kitchen photo has no doorway and the range is in its foreground; S10, S12 (night) and S85 (Close) look toward the range end
          ('0F', 'BepNguoc', 'S14c_0F Bep nhin nguoc', 'ảnh nền trống bếp nhìn từ đầu bồn rửa về phía bếp gas và cửa bếp (ban đêm cho S10, S12; vài tuần sau cho S85), sửa từ ảnh bếp buổi sáng', [n for n in N if n['node_name'] in KREV])]
SRC_FILE = {n['node_name']: g[0] for g in GROUPS for n in g[4]}
parts = []
for num, tag, wname, what, imgs in GROUPS:
    core = []
    for im in imgs:
        core += [by_id[e['source_node_id']] for e in inc[im['node_id']] if e['target_port'] == 'text'] + [im]
    core_ids = {n['node_id'] for n in core}
    ext = []
    for e in E:
        if e['target_node_id'] in core_ids and e['source_node_id'] not in core_ids and e['source_node_id'] not in ext:
            ext.append(e['source_node_id'])
    up, remap = [], {}
    for i, s_ in enumerate(ext):
        src = by_id[s_]
        name = src['node_name'] if src['node_name'].startswith('IMG_') else 'IMG_' + src['node_name']
        n = dict(node_id=nid(), node_type='image', node_name=name, pos_x=0, pos_y=i * 400, enabled=True, slug=name.lower(), slug_auto=False, ref_images=[])
        up.append((n, src)); remap[s_] = n['node_id']
    nodes = [n for n, _ in up]
    for r, im in enumerate(imgs):
        for n in [by_id[e['source_node_id']] for e in inc[im['node_id']] if e['target_port'] == 'text'] + [im]:
            n = dict(n); n.update(pos_x=400 if n['node_type'] == 'prompt' else 800, pos_y=r * 400); nodes.append(n)
    pos = {n['node_id']: i + 1 for i, n in enumerate(nodes)}
    edges = []
    for e in E:
        if e['target_node_id'] not in core_ids: continue
        e = dict(e); e['source_node_id'] = remap.get(e['source_node_id'], e['source_node_id'])
        e['edge_id'] = f"edge_{pos[e['source_node_id']]}_{e['source_handle']}_{pos[e['target_node_id']]}_{e['target_handle']}"
        edges.append({k: e[k] for k in ('edge_id','source_node_id','source_handle','source_port','target_node_id','target_handle','target_port','data_type')})
    upl = [f"{n['node_name']} = " + ('ảnh thật' if src['node_type'] == 'image' else f"ảnh đã chọn của node {src['node_name']} ở S14c_{SRC_FILE[src['node_name']]}") for n, src in up]
    desc = (f"S14c We Talked About This (bản da đen), {what}. " + ("Tải ảnh vào: " + '; '.join(upl) + '. ' if upl else '')
            + ("Chạy hết, chọn 1 ảnh đạt cho mỗi node, tải về máy; 0B cần 3 sheet gốc (Gloria, Terrance, Jada) và 2 ảnh nền gốc (BG_A_BDAY, BG_B_MORNING)." if num == '0A'
               else "Chỉ chạy sau khi đã chọn sheet gốc ở 0A." if num == '0B'
               else "Chạy sau 0A. Chọn 1 ảnh đúng sơ đồ chỗ ngồi (mục 3 của S14c_Black_TobyFlow.md), tải về; ảnh này tải vào node IMG_MASTER_A_BDAY ở các file khung có cảnh bàn ăn." if num == '0C'
               else "Chạy sau 0B và 0C. Chọn 1 ảnh: cùng góc máy, cùng 7 người ở đúng ghế như ảnh 0C, mặc đồ thứ Sáu, không băng rôn, bóng bay, túi quà, không lọ hoa giữa bàn, trên khăn ở tủ buffet không quá 6 món gỗ; tải về, ảnh này tải vào node IMG_MASTER_A_FRI ở F5." if num == '0D'
               else "Chạy sau 0B. Mỗi node chọn 1 ảnh: cùng tủ trắng, quầy, bếp gas trắng, máy hút mùi, quạt giấy và điện thoại tường như ảnh bếp; cuối bếp, ngay sau bếp gas, có cửa mở ra hành lang; không người, không chữ; tải về dùng cho S10, S12 (ảnh đêm) và S85 (ảnh vài tuần sau)." if num == '0F'
               else "Chạy sau 0A. Mỗi node chọn 1 ảnh đúng bức tường theo S14c_PhongAn_4Huong.png: cùng màu tường, bàn, khăn ren, ghế như ảnh nền; ghế trống, không người, không trang trí sinh nhật; tải về để dùng cho khung quay từ hướng đó."))
    wf = {"version": "1.0", "type": "workflow", "exported_at": "2026-10-22T03:00:00.000Z",
          "workflow": {"name": wname, "description": desc, "settings": full['settings'], "nodes": nodes, "edges": edges}}
    path = f'{OUT}/workflow_S14c_{num}_{tag}.json'
    open(path, 'w').write(dump(wf))
    name_of = {n['node_id']: n['node_name'] for n in nodes}
    mcp = dict(name=wname, description=desc, settings_json=full['settings'],
               nodes=[{**{k: v for k, v in n.items() if k not in ('node_id', 'pos_x', 'pos_y', 'node_type')}, 'ref': n['node_name'], 'type': n['node_type']} for n in nodes],
               edges=[{'from': name_of[e['source_node_id']], 'to': name_of[e['target_node_id']], 'port': e['target_port'], 'source_port': e['source_port'],
                       'source_handle': e['source_handle'], 'target_port': e['target_port'], 'target_handle': e['target_handle'], 'data_type': e['data_type']} for e in edges])
    open(f'{OUT}/mcp/mcp_S14c_{num}_{tag}.json', 'w').write(dump(mcp))
    parts.append(dict(num=num, file=os.path.basename(path), name=wname, what=what, n_nodes=len(nodes), n_edges=len(edges),
                      kb=round(os.path.getsize(path) / 1024, 1), clips=[], uploads=[(n['node_name'], src['node_name'], src['node_type']) for n, src in up]))

# checks: no generated image feeds another node in the same file; Image n count matches refs
err = []
for p in parts:
    w = json.load(open(f"{OUT}/{p['file']}"))['workflow']
    ids = {n['node_id']: n for n in w['nodes']}
    for e in w['edges']:
        if e['source_node_id'] not in ids or e['target_node_id'] not in ids: err.append(p['file'] + ' dangling')
        elif ids[e['source_node_id']].get('media_type') == 'Image': err.append(p['file'] + ' same-file ref ' + ids[e['target_node_id']]['node_name'])
    for n in w['nodes']:
        if n.get('media_type') == 'Image':
            pr = [ids[e['source_node_id']]['prompt'] for e in w['edges'] if e['target_node_id'] == n['node_id'] and e['target_port'] == 'text'][0]
            refs = [e for e in w['edges'] if e['target_node_id'] == n['node_id'] and e['target_port'] == 'image_ref']
            if max([int(x) for x in re.findall(r'Image (\d+)', pr)] or [0]) != len(refs): err.append(f"{p['file']} refs {n['node_name']}")
    if len({n['slug'] for n in w['nodes']}) != len(w['nodes']) or len(w['nodes']) > 85 or os.path.getsize(f"{OUT}/{p['file']}") > 97000: err.append(p['file'] + ' size/slug')
print('ERRORS', len(err), err[:10])
for p in parts: print(p['file'], p['n_nodes'], 'node', p['n_edges'], 'edge', p['kb'], 'KB', len(p['uploads']), 'IMG', [u[0] for u in p['uploads']])
json.dump(parts, open(f'{OUT}/_parts.json', 'w'), ensure_ascii=False, indent=1)
