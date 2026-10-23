# Fix-only files (Nam 23/10: "cứ có lỗi gì tôi lại phải làm lại từ đầu"): a file with only the frames or clips that changed, same node names,
# so Nam reruns those nodes and leaves the approved ones alone.
#   python3 fix_files.py                 -> list the frame/clip nodes whose prompt or references differ from the delivered files in DELIVERED
#   python3 fix_files.py F2:S09,S10 V2:S09  -> write out/fix/workflow_S14c_F2sua.json (frames S09, S10) and ..._V2sua.json (clip S09)
import json, glob, os, re, sys
# the toby/ folder Nam imported from (repo: output/s14c-black-tobyflow-20261021/toby); set S14C_DELIVERED when running elsewhere
DELIVERED = os.environ.get('S14C_DELIVERED', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'toby'))
src = open('split_fv.py').read()
g = {}
_head = src.split("def pack(kind, seq, prefix):")[0]
_wipe = "shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT + '/mcp')"
assert _head.count(_wipe) == 1
exec(_head.replace(_wipe, "pass"), g)  # build() and the full workflow, without re-splitting and without clearing out/fv

def wired(path):
    w = json.load(open(path))['workflow']; ids = {n['node_id']: n for n in w['nodes']}
    out = {}
    for n in w['nodes']:
        if n['node_type'] != 'generate': continue
        ins = [e for e in w['edges'] if e['target_node_id'] == n['node_id']]
        txt = [ids[e['source_node_id']]['prompt'] for e in ins if e['target_port'] == 'text']
        refs = [ids[e['source_node_id']]['node_name'] for e in ins if e['target_port'] == 'image_ref']
        out[n['node_name']] = (txt[0] if txt else '', refs)
    return out

if len(sys.argv) == 1:
    old, new = {}, {}
    for f in glob.glob(DELIVERED + '/workflow_S14c_[FV]*.json'): old.update(wired(f))
    for f in glob.glob('out/fv/workflow_S14c_[FV]*.json'):
        num = re.search(r'S14c_(\w+)\.json', f).group(1)
        for k, v in wired(f).items(): new[k] = (num, v)
    for k, (num, v) in sorted(new.items(), key=lambda x: x[1][0]):
        if old.get(k) != v: print(num, k, 'prompt' if old.get(k, ('', []))[0] != v[0] else 'refs')
    sys.exit()
os.makedirs('out/fix', exist_ok=True)
for arg in sys.argv[1:]:
    num, ids = arg.split(':'); ids = ids.split(',')
    kind = 'V' if num.startswith('V') else 'F'
    wf, ups = g['build'](kind, num + 'sua', ids)
    w = wf['workflow']
    w['name'] = f"S14c_{num}sua " + ', '.join(ids)
    w['description'] = (f"S14c (bản da đen), file sửa cho {num}: chỉ {len(ids)} {'clip' if kind == 'V' else 'khung'} đổi ({', '.join(ids)}), tên node trùng {num}. "
                        f"Chạy file này thay cho các node cùng tên ở {num}; các node khác ở {num} giữ nguyên. Tải ảnh vào node IMG_ như file {num}.")
    path = f'out/fix/workflow_S14c_{num}sua.json'
    open(path, 'w').write(g['dump'](wf))
    print(path, round(os.path.getsize(path) / 1024, 1), 'KB', len(w['nodes']), 'node')
