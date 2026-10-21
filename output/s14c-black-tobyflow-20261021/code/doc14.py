# Doc S14c Black TobyFlow (6 workflow parts)
import json, re
R = json.load(open('out/_rows.json')); rows = R['rows']
SETUP = [p for p in json.load(open('out/parts/_parts.json')) if p['num'] == '0'][0]
P = [SETUP] + json.load(open('out/parts2/_parts.json'))
src = {s['id']: s for s in json.load(open('shots.json'))}
part_of = {c: p['num'] for p in P for c in p['clips']}
def shotlen(i):
    s = src.get(i.split('_')[0]); m = re.search(r'(\d+),(\d) s', s['time']) if s else None
    return (m.group(1) + ',' + m.group(2) + ' s') if m else '—'
L = []
L.append("# S14c We Talked About This (bản da đen) — Workflow TobyFlow (21-10)\n")
L.append("Nguồn: `Editor_Script14_WeTalkedAboutThis_Black_Acawood.docx` (bản 4, sau CD review). Làm theo skill toby-workflow: Nano Banana Pro cho ảnh, **Omni 1.1 Flash** (Frames) cho mọi clip.\n")
L.append("## 1. Tóm tắt\n")
L.append(f"- **{len(rows)} clip** ({sum(r['kind']=='T' for r in rows)} T_ có thoại, {sum(r['kind']=='V' for r in rows)} V_ câm), mỗi clip có node `TAI` tải 1080p riêng.")
L.append("- **Tách Setup + 9 file clip.** Bản một file (818 KB) và bản 5 phần (114–158 KB) không mở được trong Toby; Setup (42 KB) mở được. Mỗi file clip giờ ≤ 89 KB. Bản này phá luật \"một kịch bản = một workflow\" vì dung lượng.")
L.append("- File import: `toby/workflow_S14c_0_Setup.json`, rồi `toby/workflow_S14c_01_HookCB.json` … `workflow_S14c_09_Close.json`. Payload `create_workflow` cho Toby MCP (Claude Desktop): `toby/mcp/`. Kèm `S14c_Black_prompt_pack.txt` và 6 SRT (H1, A–E).")
L.append("- **Chưa tạo trên Toby, chưa chạy gì.**\n")
L.append("## 2. Ảnh thật cần chuẩn bị\n")
L.append("| Ảnh | Cần gì | Tải vào |\n|---|---|---|")
imgs = dict(R['imgs'])
for n, d in imgs.items():
    where = ', '.join(f"file {p['num']}" for p in P if any(u[0] == n for u in p['uploads']))
    L.append(f"| `{n}` | {d} | {where} |")
L.append("\n## 3. Mười file và thứ tự làm\n")
L.append("1. **`S14c_0 Setup`** (đã import được, 49 node, chỉ ảnh): chạy để có 15 character sheet, 2 sheet đạo cụ, 8 ảnh nền. Chọn bản đạt, **tải ảnh về máy**.")
L.append("2. **Import file `01` trước** (hook C + B, 43 KB, cỡ bằng Setup). Mở được thì định dạng ổn → import tiếp 02–09. Không mở được thì lỗi nằm ở định dạng node clip/tải, không phải dung lượng: chụp màn hình lỗi gửi Claude.")
L.append("3. Mỗi file có cột node `IMG_` bên trái: tải đúng ảnh vào đúng node theo bảng dưới (tên node = `IMG_` + tên node ở Setup).")
L.append("4. Trong từng file: chạy `F_` (xem khung) → `T_/V_` → `TAI`.")
L.append("5. Có Claude Desktop + Toby MCP thì khỏi tải tay: Claude đọc kết quả Setup (`get_workflow`) rồi `update_node` gắn ảnh vào các node `IMG_` (MCP tạo tối đa 5 workflow/ngày).\n")
L.append("| File | Workflow | Shot | KB | Node | Clip | Tải ảnh vào node IMG_ |\n|---|---|---|---|---|---|---|")
for p in P:
    ups = '<br>'.join(f"`{u[0]}` ← {'ảnh thật' if u[2] == 'image' else '`' + u[1] + '`'}" for u in p['uploads'])
    shots = p.get('what') if p['num'] == '0' else (p['shots'][0] + ' → ' + p['shots'][-1])
    L.append(f"| {p['num']} | `{p['name']}` | {shots} | {p['kb']} | {p['n_nodes']} | {len(p['clips'])} | {ups} |")
L.append(f"\nTổng số lần tải ảnh nếu làm tay: {sum(len(p['uploads']) for p in P)}.\n")
L.append("## 4. Quyết định so với docx (theo luật TobyFlow đã chốt)\n")
L.append("| Docx | Workflow | Lý do |\n|---|---|---|")
for a, b, c in [
 ("Veo 3.1 / Kling 3.0 + Sync, Seedance", "Omni 1.1 Flash, chế độ Frames, mọi clip", "Mặc định skill"),
 ("Độ dài clip = độ dài shot (1–6,5 s)", "Có thoại: 6/8 s theo công thức 2,5 chữ/s, bắt đầu 0,4 s (1,0 s nếu có động tác trước), chừa 0,6 s. Câm: 4 s (shot > 3,5 s thì 6 s)", "Nhân vật phải nói hết câu; khi dựng cắt đúng độ dài shot ở storyboard"),
 ("Tắt tiếng model, dùng giọng ElevenLabs", "Omni vẫn nói câu (khối VOICE từng nhân vật, cho khớp miệng); dựng thay bằng file ElevenLabs + Sync nếu lệch", "Không gắn `voice` Flow vào Frames (lỗi cả lô)"),
 ("[TAIL]: pores, shallow depth of field, 35mm, cinematic, slow push-in", "Khối máy quay thật + da thật; \"glides a few centimeters closer\"", "Chữ ép nét làm ảnh giả, như nhựa; từ cấm"),
 ("Cậu bé 10 tuổi rõ mặt (S08, S71, S81)", "Chỉ thấy sau lưng / nghiêng mờ ở hậu cảnh; sheet chỉ góc sau", "Mặt trẻ em dễ bị Google chặn"),
 ("S88 cận tay Gloria rửa muôi", "Trung cảnh từ eo lên, lau muôi rồi cắm vào ống", "Cận tay người già cầm đồ bị chặn (S12)"),
 ("\"phone\", \"dark-wood\", \"slowly\"", "\"handset\", \"deep-brown\", \"at walking pace\"", "Từ cấm trong prompt"),
 ("Shot lời ngoài khung (S18, S26, S44, S48, S53, S87, S88)", "Clip câm V_, giọng đặt ở dựng", "Không có miệng để khớp"),
 ("Xé brochure (S78, D-2)", "Khóa riêng: chỉ brochure đổi, xé một đường; lỗi thì dùng phương án thả vào thùng giấy (docx)", "Chống biến dạng"),
 ("Đồ có sản phẩm", "Khối Lighting match + Object lock; S49, S53 dùng thẳng ảnh thật làm khung đầu", "Không trông như ghép; đúng 7 món")]:
    L.append(f"| {a} | {b} | {c} |")
L.append("\n## 5. Không gen trong Toby (dựng ở CapCut)\n")
L.append("- `S55` màn hình điện thoại + nút BUY NOW · `E-1` group chat FAMILY · `S91` end card · banner, phụ đề, thẻ chữ thời gian, nhãn xanh S86, thẻ offer S89, chữ WRENFIELD ghép ở S04 và thùng KITCHEN — WRENFIELD ở S27.")
L.append("- Hook D-1 = dùng lại `S14c_T_S79`.\n")
L.append("## 6. Bảng clip\n")
L.append("Shot dựng = mốc cắt khi dựng (storyboard). Clip dài hơn để nhân vật nói hết câu; cắt phần lặng.\n")
L.append("| Shot | File | Node clip | Clip | Shot dựng | Lời xong lúc | Ảnh đính (Image 1..n) | Lời |\n|---|---|---|---|---|---|---|---|")
for r in rows:
    L.append(f"| {r['id']} | {part_of[r['clip']]} | `{r['clip']}` | {r['dur']} s | {shotlen(r['id'])} | {r['end'] or '—'} | {', '.join(r['refs'])} | {(r['spk'] + ': ' + r['txt']) if r['txt'] else '(câm)'} |")
L.append("\n## 7. Rủi ro / cần Nam kiểm\n")
L.append("- File 01 mở được mà 02–09 (69–89 KB) không mở được: giới hạn dung lượng thấp hơn ~70 KB → báo Claude tách nhỏ hơn. File 01 cũng không mở được: lỗi định dạng → gửi câu Toby báo + một file export workflow cũ có node video và node tải (vd. S12 v3) để so từng trường.")
L.append("- Tên trường lấy theo mục 6 của skill (chưa có file export mẫu trong phiên này). Node `download` đã bỏ trường thừa `download`.")
L.append("- Chưa đọc được Doc 56, 25, 47, 63, 72, 80 và Toby Flow 01, 02 (phiên cloud không có Projects); nên rà lại theo checklist Doc 56.")
L.append("- Claim: \"hormone disruption\" đã duyệt; Meta từ chối thì thay \"Ones you don't want in your food.\" (chỉ đổi file giọng S48, clip câm không phải gen lại).")
L.append("- Nhân vật AI: bật nhãn nội dung AI khi chạy ads.")
open('out/S14c_Black_TobyFlow.md', 'w').write('\n'.join(L) + '\n')
print('ok')
