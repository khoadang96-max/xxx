# Split S14c shots like Script 11: frame files (F_ images only) and video files (each clip's chosen frame uploaded
# into an IMG_F_ node), so no node takes a generated image from the same file
import json, random, string, re, os, collections, shutil
CAP = 97000      # Toby imported 97 KB / 85 nodes (Script 11 04b)
MAX_NODES = 85
random.seed(2312)
full = json.load(open('out/workflow_S14c_Black.json'))['workflow']
N = full['nodes']; E = full['edges']
by_id = {n['node_id']: n for n in N}; by_name = {n['node_name']: n for n in N}
OUT = 'out/fv'; shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT + '/mcp')
dump = lambda o: json.dumps(o, ensure_ascii=False, separators=(',', ':'))
def nid(): return 'node_' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
ORDER = (['C-1', 'C-2', 'S02_C', 'B-1', 'S02_B', 'S03_B', 'A-1', 'E-2'] + ['S%02d' % i for i in range(1, 9)] + ['S%02d' % i for i in range(9, 49)]
         + [x for x in ['S%02d' % i for i in range(49, 71)] if x != 'S55'] + ['D-2'] + ['S%02d' % i for i in range(71, 91)])
inc = collections.defaultdict(list)
for e in E: inc[e['target_node_id']].append(e)
def video_of(sid):
    v = [n for n in N if n.get('media_type') == 'Video' and re.fullmatch(rf'S14c_[TV]_{re.escape(sid.replace("-", ""))}', n['node_name'])]
    assert len(v) == 1, sid
    return v[0]

def build(kind, num, sids):
    """kind 'F': prompt + frame image per shot, IMG_ uploads for refs; kind 'V': IMG_F_ upload + prompt + video per clip"""
    nodes, edges, ups = [], [], []
    def upload(name):
        for n, _ in ups:
            if n['node_name'] == name: return n
        n = dict(node_id=nid(), node_type='image', node_name=name, pos_x=0, pos_y=len(ups) * 400, enabled=True, slug=name.lower().replace('-', '_'), slug_auto=False, ref_images=[])
        ups.append((n, name)); return n
    rows = []
    for r, sid in enumerate(sids):
        if kind == 'F':
            f = by_name[f'S14c_F_{sid}']; pf = by_name[f'P_F_{sid}']
            refs = [e for e in inc[f['node_id']] if e['target_port'] == 'image_ref']
            srcs = []
            for e in refs:
                s_ = by_id[e['source_node_id']]['node_name']
                srcs.append(upload(s_ if s_.startswith('IMG_') else 'IMG_' + s_))
            pfn = dict(pf, pos_x=400, pos_y=r * 400); fn = dict(f, pos_x=800, pos_y=r * 400)
            rows.append((pfn, fn, srcs))
        else:
            v = video_of(sid); pv = by_name[f'P_V_{sid}']
            src = by_id[v['frame_1_source']]['node_name']
            fr = upload(src if src.startswith('IMG_') else 'IMG_F_' + sid)
            vn = dict(v, pos_x=800, pos_y=r * 400, frame_1_source=fr['node_id'])
            if v.get('frame_2_source'): vn['frame_2_source'] = fr['node_id']
            rows.append((dict(pv, pos_x=400, pos_y=r * 400), vn, fr))
    nodes = [n for n, _ in ups]
    for row in rows: nodes += [row[0], row[1]]
    pos = {n['node_id']: i + 1 for i, n in enumerate(nodes)}
    def link(a, b, port, dt):
        h = {'image_ref': 'input_1', 'text': 'input_2', 'frame_1': 'input_3', 'frame_2': 'input_4'}[port]
        edges.append(dict(edge_id=f"edge_{pos[a['node_id']]}_output_1_{pos[b['node_id']]}_{h}", source_node_id=a['node_id'], source_handle='output_1',
                          source_port='text' if a['node_type'] == 'prompt' else 'media', target_node_id=b['node_id'], target_handle=h, target_port=port, data_type=dt))
    for row in rows:
        if kind == 'F':
            p, f, srcs = row
            for s_ in srcs: link(s_, f, 'image_ref', 'image')
            link(p, f, 'text', 'text')
        else:
            p, v, fr = row
            link(fr, v, 'frame_1', 'image')
            if v.get('frame_2_source'): link(fr, v, 'frame_2', 'image')
            link(p, v, 'text', 'text')
    real = [n['node_name'] for n, nm in ups if nm in ('IMG_ACA_SET', 'IMG_ACA_HOLDER', 'IMG_ACA_TOWEL', 'IMG_ACA_MACRO', 'IMG_WATERTEST')]
    if kind == 'F':
        name = f'S14c_{num} Khung {sids[0]} den {sids[-1]}'
        desc = (f"S14c (bản da đen), khung đầu {sids[0]} → {sids[-1]}. Tải vào mỗi node IMG_ ảnh đã chọn ở 0A/0B/0C/0D của node cùng tên (bỏ IMG_)"
                + (f"; ảnh thật: {', '.join(real)}" if real else '') + ". Chạy hết, mỗi khung chọn 1 ảnh đạt trong 4, tải về (Auto Download lưu theo tên node).")
    else:
        name = f'S14c_{num} Clip {sids[0]} den {sids[-1]}'
        desc = (f"S14c (bản da đen), clip {sids[0]} → {sids[-1]}. Tải vào mỗi node IMG_F_<cảnh> ảnh khung đã chọn của node S14c_F_<cảnh> ở file khung"
                + (f"; ảnh thật: {', '.join(real)}" if real else '') + ". Chạy hết; Auto Download tải clip 1080p.")
    wf = {"version": "1.0", "type": "workflow", "exported_at": "2026-10-22T10:00:00.000Z",
          "workflow": {"name": name, "description": desc, "settings": full['settings'], "nodes": nodes, "edges": edges}}
    return wf, ups

def pack(kind, seq, prefix):
    seg, size = {}, {}
    for i in range(len(seq)):
        for j in range(i + 1, len(seq) + 1):
            wf, ups = build(kind, '99', seq[i:j])
            if len(dump(wf).encode()) > CAP or len(wf['workflow']['nodes']) > MAX_NODES: break
            seg[(i, j)] = len(ups); size[(i, j)] = len(dump(wf).encode())
    n = len(seq)
    if kind == 'F':   # fewest files, then fewest uploads
        INF = (10 ** 9, 10 ** 9); best = [INF] * (n + 1); prev = [None] * (n + 1); best[0] = (0, 0)
        for j in range(1, n + 1):
            for i in range(j):
                if (i, j) in seg and best[i] != INF:
                    c = (best[i][0] + 1, best[i][1] + seg[(i, j)])
                    if c < best[j]: best[j], prev[j] = c, i
        cuts, j = [], n
        while j: cuts.append((prev[j], j)); j = prev[j]
    else:             # clip files: one upload per clip anyway, so fewest files, then the most even sizes
        INF = 10 ** 12
        for k in range(1, n + 1):
            dp = [[INF] * (n + 1) for _ in range(k + 1)]; arg = [[None] * (n + 1) for _ in range(k + 1)]; dp[0][0] = 0
            for c in range(1, k + 1):
                for j in range(1, n + 1):
                    for i in range(j):
                        if (i, j) in size and dp[c - 1][i] < INF:
                            v = max(dp[c - 1][i], size[(i, j)])
                            if v < dp[c][j]: dp[c][j], arg[c][j] = v, i
            if dp[k][n] < INF: break
        cuts, j, c = [], n, k
        while j: i = arg[c][j]; cuts.append((i, j)); j, c = i, c - 1
    out = []
    for k, (i, j) in enumerate(reversed(cuts), 1):
        num = f'{prefix}{k}'
        wf, ups = build(kind, num, seq[i:j])
        path = f'{OUT}/workflow_S14c_{num}.json'
        open(path, 'w').write(dump(wf))
        w = wf['workflow']; name_of = {n['node_id']: n['node_name'] for n in w['nodes']}
        mcp = dict(name=w['name'], description=w['description'], settings_json=full['settings'],
                   nodes=[{**{kk: vv for kk, vv in n.items() if kk not in ('node_id', 'pos_x', 'pos_y', 'node_type')}, 'ref': n['node_name'], 'type': n['node_type'],
                           **({'frame_1_source': name_of[n['frame_1_source']]} if n.get('frame_1_source') else {}),
                           **({'frame_2_source': name_of[n['frame_2_source']]} if n.get('frame_2_source') else {})} for n in w['nodes']],
                   edges=[{'from': name_of[e['source_node_id']], 'to': name_of[e['target_node_id']], 'port': e['target_port'], 'source_port': e['source_port'],
                           'source_handle': e['source_handle'], 'target_port': e['target_port'], 'target_handle': e['target_handle'], 'data_type': e['data_type']} for e in w['edges']])
        open(f'{OUT}/mcp/mcp_S14c_{num}.json', 'w').write(dump(mcp))
        out.append(dict(num=num, kind=kind, file=os.path.basename(path), name=w['name'], shots=seq[i:j], n_nodes=len(w['nodes']), n_edges=len(w['edges']),
                        kb=round(os.path.getsize(path) / 1024, 1), clips=[n['node_name'] for n in w['nodes'] if n.get('media_type') == 'Video'],
                        frames=[n['node_name'] for n in w['nodes'] if n.get('media_type') == 'Image'],
                        uploads=[(n['node_name'], nm, 'image' if nm in real_names else 'generated') for n, nm in ups]))
    return out
real_names = {'IMG_ACA_SET', 'IMG_ACA_HOLDER', 'IMG_ACA_TOWEL', 'IMG_ACA_MACRO', 'IMG_WATERTEST'}
# files never cross a scene block (Nam 23/10): birthday dinner | kitchen, porches, kitchen | Friday dinner | Close
BLOCKS = [lambda x: x in ORDER[:ORDER.index('S09')], lambda x: ORDER.index('S09') <= ORDER.index(x) < ORDER.index('D-2'),
          lambda x: ORDER.index('D-2') <= ORDER.index(x) < ORDER.index('S82'), lambda x: ORDER.index(x) >= ORDER.index('S82')]
def pack_blocks(kind, seq, prefix, blocks):
    out = []
    for blk in blocks:
        sub = [x for x in seq if blk(x)]
        if not sub: continue
        res = pack(kind, sub, prefix)
        for p_ in res:  # renumber across blocks
            k = len(out) + 1; old = p_['num']; new = f'{prefix}{k}'
            if old != new:
                for path in (f"{OUT}/workflow_S14c_{old}.json", f"{OUT}/mcp/mcp_S14c_{old}.json"):
                    pass
            out.append(dict(p_, _old=old, num=new))
        # write files under final numbers (pack wrote them under per-block numbers)
        for p_ in out[len(out) - len(res):]:
            wf = json.load(open(f"{OUT}/{p_['file']}")); mc = json.load(open(f"{OUT}/mcp/mcp_S14c_{p_['_old']}.json"))
            name = wf['workflow']['name'].replace(f"S14c_{p_['_old']} ", f"S14c_{p_['num']} ")
            wf['workflow']['name'] = name; mc['name'] = name
            os.remove(f"{OUT}/{p_['file']}"); os.remove(f"{OUT}/mcp/mcp_S14c_{p_['_old']}.json")
            p_['file'] = f"workflow_S14c_{p_['num']}.json"; p_['name'] = name
            open(f"{OUT}/tmp_{p_['file']}", 'w').write(dump(wf)); open(f"{OUT}/mcp/tmp_mcp_S14c_{p_['num']}.json", 'w').write(dump(mc))
    for p_ in out:
        os.rename(f"{OUT}/tmp_{p_['file']}", f"{OUT}/{p_['file']}"); os.rename(f"{OUT}/mcp/tmp_mcp_S14c_{p_['num']}.json", f"{OUT}/mcp/mcp_S14c_{p_['num']}.json")
        p_['kb'] = round(os.path.getsize(f"{OUT}/{p_['file']}") / 1024, 1); p_.pop('_old')
    return out
frame_seq = [s for s in ORDER if f'S14c_F_{s}' in by_name]
parts = pack_blocks('F', frame_seq, 'F', BLOCKS) + pack_blocks('V', ORDER, 'V', BLOCKS)
# straight-on variants (Nam 23/10, standard room): extra files F1b / F5b, so F1-F6 and V1-V6 stay as they are; a chosen _H2 frame goes into the same IMG_F_<shot> node
ALT = [s_ for s_ in ORDER if f'S14c_F_{s_}_H2' in by_name]
for num, blk in (('F1b', BLOCKS[0]), ('F5b', BLOCKS[2])):
    sub = [a_ + '_H2' for a_ in ALT if blk(a_)]
    if not sub: continue
    wf, ups = build('F', num, sub)
    w = wf['workflow']
    w['name'] = f"S14c_{num} Khung goc thang {sub[0][:-3]} den {sub[-1][:-3]}"
    w['description'] = ("S14c (bản da đen), khung cận nhìn thẳng từ bên kia bàn, nền là ảnh hướng ② (BG_A_WEST, file 0E). Bản thay thế cho khung cùng cảnh ở "
                        + ('F1' if num == 'F1b' else 'F5') + ": chọn bản đẹp hơn, tải vào node IMG_F_<cảnh> của file clip như thường. Tải vào mỗi node IMG_ ảnh đã chọn ở 0A/0B/0C/0D/0E của node cùng tên (bỏ IMG_).")
    path = f'{OUT}/workflow_S14c_{num}.json'; open(path, 'w').write(dump(wf))
    name_of = {n['node_id']: n['node_name'] for n in w['nodes']}
    mcp = dict(name=w['name'], description=w['description'], settings_json=full['settings'],
               nodes=[{**{kk: vv for kk, vv in n.items() if kk not in ('node_id', 'pos_x', 'pos_y', 'node_type')}, 'ref': n['node_name'], 'type': n['node_type']} for n in w['nodes']],
               edges=[{'from': name_of[e['source_node_id']], 'to': name_of[e['target_node_id']], 'port': e['target_port'], 'source_port': e['source_port'],
                       'source_handle': e['source_handle'], 'target_port': e['target_port'], 'target_handle': e['target_handle'], 'data_type': e['data_type']} for e in w['edges']])
    open(f'{OUT}/mcp/mcp_S14c_{num}.json', 'w').write(dump(mcp))
    parts.append(dict(num=num, kind='Fb', file=os.path.basename(path), name=w['name'], shots=sub, n_nodes=len(w['nodes']), n_edges=len(w['edges']),
                      kb=round(os.path.getsize(path) / 1024, 1), clips=[], frames=[n['node_name'] for n in w['nodes'] if n.get('media_type') == 'Image'],
                      uploads=[(n['node_name'], nm, 'image' if nm in real_names else 'generated') for n, nm in ups]))

# checks: no node takes a generated image from its own file; every clip once; refs match prompt Image n; frame ports wired
err = []
if sorted(c for p in parts for c in p['clips']) != sorted(n['node_name'] for n in N if n.get('media_type') == 'Video'): err.append('clips not covered once')
if sorted(f for p in parts for f in p['frames']) != sorted(n['node_name'] for n in N if n['node_name'].startswith('S14c_F_')): err.append('frames not covered once')
for p in parts:
    w = json.load(open(f"{OUT}/{p['file']}"))['workflow']; ids = {n['node_id']: n for n in w['nodes']}
    ic = collections.defaultdict(list)
    for e in w['edges']:
        if e['source_node_id'] not in ids or e['target_node_id'] not in ids: err.append(p['file'] + ' dangling'); continue
        if ids[e['source_node_id']]['node_type'] == 'generate': err.append(p['file'] + ' same-file generated source')
        ic[e['target_node_id']].append(e)
    if len({e['edge_id'] for e in w['edges']}) != len(w['edges']) or len({n['slug'] for n in w['nodes']}) != len(w['nodes']): err.append(p['file'] + ' dup id/slug')
    if os.path.getsize(f"{OUT}/{p['file']}") > CAP or len(w['nodes']) > MAX_NODES or len(w['name']) >= 100 or '/' in w['name']: err.append(p['file'] + ' limits')
    for n in w['nodes']:
        if n.get('media_type') == 'Video':
            f1 = [e for e in ic[n['node_id']] if e['target_port'] == 'frame_1']; f2 = [e for e in ic[n['node_id']] if e['target_port'] == 'frame_2']
            if len(f1) != 1 or f1[0]['source_node_id'] != n['frame_1_source']: err.append(p['file'] + ' frame1 ' + n['node_name'])
            if len(f2) != int(bool(n.get('frame_2_source'))): err.append(p['file'] + ' frame2 ' + n['node_name'])
            if not re.fullmatch(r'(4|6|8|10)s', n['video_duration']) or n['quantity'] != 2 or n['download_resolution'] != '1080p': err.append(p['file'] + ' video fields ' + n['node_name'])
        if n.get('media_type') == 'Image':
            pr = [ids[e['source_node_id']]['prompt'] for e in ic[n['node_id']] if e['target_port'] == 'text'][0]
            if max([int(x) for x in re.findall(r'Image (\d+)', pr)] or [0]) != len([e for e in ic[n['node_id']] if e['target_port'] == 'image_ref']): err.append(f"{p['file']} refs {n['node_name']}")
            if n['quantity'] != 4: err.append(p['file'] + ' qty ' + n['node_name'])
        if n['node_type'] == 'download': err.append(p['file'] + ' download node')
print('ERRORS', len(err), err[:10])
for p in parts:
    print(f"{p['file']:24s} {p['kb']:5.1f} KB {p['n_nodes']:3d} node {len(p['frames']):3d} khung {len(p['clips']):3d} clip {len(p['uploads']):3d} IMG | {p['shots'][0]}..{p['shots'][-1]}")
print('uploads F', sum(len(p['uploads']) for p in parts if p['kind'] == 'F'), 'V', sum(len(p['uploads']) for p in parts if p['kind'] == 'V'))
json.dump(parts, open(f'{OUT}/_parts.json', 'w'), ensure_ascii=False, indent=1)
