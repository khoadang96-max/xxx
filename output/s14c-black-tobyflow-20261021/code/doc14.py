# Doc S14c Black TobyFlow (6 workflow parts)
import json, re
R = json.load(open('out/_rows.json')); rows = R['rows']
SETUPS = json.load(open('out/setup/_parts.json'))
P = SETUPS + json.load(open('out/parts2/_parts.json'))
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
L.append("- **Setup tách 2 file + 9 file clip.** 0A: sheet nhân vật gốc, đạo cụ, 4 ảnh nền gốc (phòng ăn sinh nhật, bếp buổi sáng, hiên đêm, hiên Dorothy). 0B: sheet đổi đồ và 4 trạng thái khác của cùng hai căn phòng, sửa từ ảnh gốc ở 0A. Bản một file (818 KB) và bản 5 phần (114–158 KB) không mở được trong Toby. Mỗi file ≤ 95 KB và ≤ 85 node (mức Toby từng import được: 97 KB / 85 node, Script 11). Bản này phá luật \"một kịch bản = một workflow\" vì dung lượng.")
L.append("- **Nhân vật (22/10):** viết lại theo nghiên cứu gia đình Mỹ da đen, chi tiết ở `S14c_Black_NhanVat.md`. Sheet đổi đồ chuyển sang file 0B (lấy sheet gốc từ 0A) vì bản cũ nối trong cùng file nên ra người lạ.")
L.append(f"- **Số lượng:** node ảnh x4 (không tốn credit), node video x2 ({len(rows)} clip → {2 * len(rows)} lượt video). **{sum(1 for r in rows if r.get('f2'))} clip nói** có khung đầu = khung cuối (cùng một ảnh vào frame_1 và frame_2) để người không trôi.")
L.append("- Đã đối chiếu với luật trong chat cũ của Nam (xem mục 1b và `references/toby-flow-rules-nam.md`). Phải import lại cả 11 file: mọi file đều đổi.")
L.append("- File import: `toby/workflow_S14c_0A_Setup.json`, `toby/workflow_S14c_0B_DoiDo.json`, rồi `toby/workflow_S14c_01_HookCB.json` … `workflow_S14c_09_Close.json`. Payload `create_workflow` cho Toby MCP (Claude Desktop): `toby/mcp/`. Kèm `S14c_Black_prompt_pack.txt` và 6 SRT (H1, A–E).")
L.append("- **Chưa tạo trên Toby, chưa chạy gì.**\n")
L.append("## 1b. Đã sửa theo luật Nam (21–22/10)\n")
L.append("| Luật | Bản trước | Bản này |\n|---|---|---|")
for a, b, c in [
 ("Ảnh x4, video x2", "quantity 1 mọi node", "120 node ảnh x4, 98 node video x2 (skill toby-workflow vẫn ghi quantity 1, xem mục 7)"),
 ("Clip nói: cùng một ảnh vào frame_1 và frame_2", "chỉ frame_1", "42 clip nói giữ dáng có frame_2; 32 clip nói có động tác đổi trạng thái (đặt đồ, quay đầu, cắn, xé, đổi nét…) chỉ frame_1"),
 ("Tay viết câu khẳng định (\"missing fingers\" bị Google chặn)", "\"the right number of fingers… no extra hands\"", "\"Every hand has five fingers in natural proportion…\""),
 ("Không mặt trẻ em, không \"seen from behind\" + người", "cậu bé \"seen from behind\"; S12 \"from behind the grandmother's shoulder\"; S18 \"back to the door\"", "cậu bé chỉ thấy bàn tay + tay áo; sheet cậu bé thành sheet quần áo, không người; S12 over-the-shoulder; S18 đứng quay ra phố"),
 ("Living layer: chỉ thứ có sẵn trong khung chuyển động", "con thiêu thân (C), bụi (B_MORNING), giấy báo tự bay (B_BOXES)", "\"(only what is already in the frame moves, nothing is added)\"; bỏ 3 chi tiết thêm vào"),
 ("Physical logic: không vật nào tự chuyển động", "chưa có", "\"nothing moves on its own: whatever moves is moved by a visible hand or by the action\""),
 ("Omni ậm ừ/cười sau câu; mặt không đơ", "\"then stays silent\"", "\"lips close and stay closed, no sound\" + dòng Face (biểu cảm theo lời, không đơ, không lố)"),
 ("Hành động chính trong giây đầu", "chưa ghi", "\"the main action starts within the first second\""),
 ("[FOOD-ACA]: đồ ăn cạnh Acawood tươi, sạch", "chưa có", "S71, S72, S81, S85 có khối FOOD-ACA (ảnh + clip)"),
 ("Giọng: Omni nói, rồi ElevenLabs Voice Changer", "\"dựng thay bằng giọng ElevenLabs\"", "Voice Changer từng nhân vật trên lời Omni (giữ nhịp, khớp miệng)"),
 ("Chữ cấm (smooth, perfect…)", "\"smooth baritone\", \"perfectly clear\"", "\"mellow baritone\", \"completely clear\""),
 ("Ảnh tham chiếu phải đến từ file chạy trước", "7 sheet đổi đồ lấy ảnh gốc trong cùng file Setup → ra người lạ, đa số da trắng, đeo kính", "0A sheet gốc, 0B đổi đồ (tải sheet gốc vào `IMG_CS_*_1`); prompt đổi đồ tả lại đủ người"),
 ("Nhân vật da đen phải giống người thật", "chỉ \"Black American, warm brown skin\" cho mọi người", "tông da + undertone riêng, nét mặt, tóc xoăn tít tự nhiên, dấu tuổi da nâu, khối da không xám/tro; chỉ Gloria và Dorothy có kính"),
 ("People lock trong clip", "chưa có", "\"People: everyone in the start frame keeps the same face, age, skin tone, hair and clothes…\""),
 ("Physical logic (S44)", "spatula tự trộn khoai, không có tay", "spatula nằm yên, hơi nóng bốc lên, máy tiến gần (cận tay người già cầm đồ dễ bị chặn)"),
 ("D-2: tay của ai", "\"a man's two hands\"", "tay Terrance: da nâu sẫm, lòng bàn tay sáng hơn, nhẫn cưới, cổ tay áo caro; đính sheet Terrance 3"),
 ("Mũ đi lễ cho Dorothy (Nam, 22/10)", "không có", "mũ xanh rêu cùng bộ đồ, vành vừa, hoa vải, đội cả chiều Chủ nhật; chỉ mình bà đội mũ"),
 ("Bình nước to của Jada (docx)", "không có", "cốc giữ nhiệt hồng nhạt, không logo, chỉ đặt trên bàn/quầy ở S01, S08, S21, S71, S81; không ai cầm"),
 ("Ảnh trang trí là ảnh của gia đình da đen này (Nam, 22/10)", "\"framed family and graduation photos\", \"family photos on the fridge\" chung chung → model tự bịa người", "tường: ảnh cưới của bà và người chồng đã mất, ảnh tốt nghiệp của Terrance, của Jada, ảnh bà với con trai, con dâu trước nhà thờ; tủ lạnh: ảnh bà với bạn nhà thờ, Terrance và vợ, Jada đội mũ tốt nghiệp; toàn người da đen, chỉ người lớn, ảnh nhỏ, hơi mờ, không chữ"),
 ("Quạt giấy nhà thờ", "không tả mặt in", "in tranh một nhà thờ trắng nhỏ, không người, không chữ"),
 ("Cùng một căn phòng ở nhiều cảnh", "phòng ăn thứ Sáu và 4 trạng thái bếp tạo riêng từ chữ → mỗi cảnh một căn phòng, ảnh treo khác nhau", "0A tạo phòng ăn sinh nhật và bếp buổi sáng; 0B sửa từ 2 ảnh đó ra phòng ăn thứ Sáu, bếp đêm, bếp đóng thùng, bếp vài tuần sau, giữ nguyên tường, tủ, ảnh"),
 ("Người ở bàn ăn", "\"the family\", \"the whole table\" chung chung (C-1, S01, S05, S08, S71, S81)", "ghi rõ: gia đình người Mỹ da đen, chỉ người lớn lộ mặt, thêm 2 họ hàng lớn tuổi ở cuối bàn (docx: 2–3 họ hàng mờ hậu cảnh); chỗ ngồi cố định theo docx; C-1 mẹ ngoài khung"),
 ("Món trên bàn (docx)", "bỏ sót", "rau collard, khoai lang, bánh ngô mờ ở hậu cảnh các cảnh bàn ăn"),
 ("Tay cầm đồ ở mép khung", "S42, S48, S61 không nói tay ai; S64 không rõ ai cầm", "tay Dorothy (S42, S48), tay Gloria (S61), Terrance tự cầm muôi (S64): ghi tông da, tay áo, nhẫn và đính sheet"),
 ("Màn hình điện thoại", "E-2, S54 không nói màn hình hiện gì", "E-2 màn hình quay đi; S54 chỉ sáng trơn, không chữ (giao diện tin nhắn dựng ở CapCut, S55)")]:
    L.append(f"| {a} | {b} | {c} |")
L.append("")
L.append("## 2. Ảnh thật cần chuẩn bị\n")
L.append("| Ảnh | Cần gì | Tải vào |\n|---|---|---|")
imgs = dict(R['imgs'])
for n, d in imgs.items():
    where = ', '.join(f"file {p['num']}" for p in P if any(u[0] == n for u in p['uploads']))
    L.append(f"| `{n}` | {d} | {where} |")
L.append("\n## 3. Mười một file và thứ tự làm\n")
L.append("1. **`S14c_0A Setup nhan vat nen`** (26 node, chỉ ảnh, x4, không cần tải ảnh): 6 character sheet gốc (Gloria 1, Terrance 1, Jada 1, Dorothy, vợ Terrance, con gái Dorothy), sheet quần áo cậu bé (không người), 2 sheet đạo cụ, 4 ảnh nền gốc (`BG_A_BDAY`, `BG_B_MORNING`, `BG_C`, `BG_D`). Duyệt theo mục 6 của `S14c_Black_NhanVat.md`, xem ảnh treo tường và ảnh trên tủ lạnh đều là người da đen, chọn 1 ảnh mỗi node, **tải về máy**.")
L.append("2. **`S14c_0B Doi do`** (28 node): tải 6 ảnh vào node `IMG_`: 3 sheet gốc (`IMG_CS_GLORIA_1`, `IMG_CS_TERRANCE_1`, `IMG_CS_JADA_1`), 2 ảnh nền gốc (`IMG_BG_A_BDAY`, `IMG_BG_B_MORNING`) và ảnh thật bộ Acawood trong ống (`IMG_ACA_HOLDER`) → chạy 7 sheet đổi đồ + 4 ảnh nền (`BG_A_FRI`, `BG_B_NIGHT`, `BG_B_BOXES`, `BG_B_CLEAR`) → chọn, tải về.")
L.append("3. **Import file `01` trước** (hook C + B, 48 KB). Mở được thì định dạng ổn → import tiếp 02–09. Không mở được thì lỗi nằm ở định dạng node clip/tải, không phải dung lượng: chụp màn hình lỗi gửi Claude.")
L.append("4. Mỗi file có cột node `IMG_` bên trái: tải đúng ảnh vào đúng node theo bảng dưới (tên node = `IMG_` + tên node ở Setup).")
L.append("5. Trong từng file: chạy `F_` (xem khung) → `T_/V_` → `TAI`.")
L.append("6. Có Claude Desktop + Toby MCP thì khỏi tải tay: Claude đọc kết quả Setup (`get_workflow`) rồi `update_node` gắn ảnh vào các node `IMG_` (MCP tạo tối đa 5 workflow/ngày).\n")
L.append("| File | Workflow | Shot | KB | Node | Clip | Tải ảnh vào node IMG_ |\n|---|---|---|---|---|---|---|")
for p in P:
    ups = '<br>'.join(f"`{u[0]}` ← {'ảnh thật' if u[2] == 'image' else '`' + u[1] + '`'}" for u in p['uploads'])
    shots = p.get('what') if p['num'].startswith('0') else (p['shots'][0] + ' → ' + p['shots'][-1])
    L.append(f"| {p['num']} | `{p['name']}` | {shots} | {p['kb']} | {p['n_nodes']} | {len(p['clips'])} | {ups} |")
L.append(f"\nTổng số lần tải ảnh nếu làm tay: {sum(len(p['uploads']) for p in P)}.\n")
L.append("## 4. Quyết định so với docx (theo luật TobyFlow đã chốt)\n")
L.append("| Docx | Workflow | Lý do |\n|---|---|---|")
for a, b, c in [
 ("Veo 3.1 / Kling 3.0 + Sync, Seedance", "Omni 1.1 Flash, chế độ Frames, mọi clip", "Mặc định skill"),
 ("Độ dài clip = độ dài shot (1–6,5 s)", "Có thoại: 6/8 s theo công thức 2,5 chữ/s, bắt đầu 0,4 s (1,0 s nếu có động tác trước), chừa 0,6 s. Câm: 4 s (shot > 3,5 s thì 6 s)", "Nhân vật phải nói hết câu; khi dựng cắt đúng độ dài shot ở storyboard"),
 ("Tắt tiếng model, dùng giọng ElevenLabs", "Omni nói câu (khối VOICE từng nhân vật, cho khớp miệng); dựng xong tách lời từng nhân vật, chạy ElevenLabs Voice Changer (Multilingual v2 STS, Stability 50, Similarity 85, Style 0, bỏ tiếng nền) — giữ nhịp nên vẫn khớp miệng", "Không gắn `voice` Flow vào Frames (lỗi cả lô); lời TTS mới sẽ lệch miệng"),
 ("[TAIL]: pores, shallow depth of field, 35mm, cinematic, slow push-in", "Khối máy quay thật + da thật; \"glides a few centimeters closer\"", "Chữ ép nét làm ảnh giả, như nhựa; từ cấm"),
 ("Cậu bé 10 tuổi rõ mặt (S08, S71, S81)", "Chỉ bàn tay + tay áo ở mép khung; sheet chỉ quần áo, không người", "Không mặt trẻ em; \"seen from behind\" + người bị Google chặn"),
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
L.append("Khung cuối \"= đầu\": frame_2 cùng ảnh với frame_1. Clip nào bị đứng im thì báo Claude bỏ khung cuối của clip đó.\n")
L.append("| Shot | File | Node clip | Clip | Shot dựng | Lời xong lúc | Khung cuối | Ảnh đính (Image 1..n) | Lời |\n|---|---|---|---|---|---|---|---|---|")
for r in rows:
    L.append(f"| {r['id']} | {part_of[r['clip']]} | `{r['clip']}` | {r['dur']} s | {shotlen(r['id'])} | {r['end'] or '—'} | {'= đầu' if r.get('f2') else '—'} | {', '.join(r['refs'])} | {(r['spk'] + ': ' + r['txt']) if r['txt'] else '(câm)'} |")
L.append("\n## 7. Rủi ro / cần Nam kiểm\n")
L.append("- **Mâu thuẫn cần Nam chốt:** skill toby-workflow (21/10) ghi `quantity 1` mọi node; chat cũ chốt ảnh x4, video x2. Bản này theo chat (x2 video = gấp đôi credit video). Muốn quay về x1 thì báo Claude, hoặc sửa số lượng trên node video.")
L.append("- Prompt clip nói 374–472 từ, clip câm 222–309 từ: dài hơn mức 180–300 của doc 25 vì giữ nguyên khối Object lock (skill: clip có khối khóa vật thể tới ~600 từ vẫn chạy tốt, S12 v3).")
L.append("- 32 clip nói không có khung cuối (đổi trạng thái): nếu trôi mặt/đồ thì báo, Claude tách thành clip nói giữ dáng + clip động tác.")
L.append("- Nhịp dựng: trung bình 2,65 s/shot (gần Titanox ~2,7 s). 5 shot dài hơn 5 s, dễ thành cảnh đứng: S89 6,5 s, S85 5,8 s, S69 5,8 s, S86 5,7 s, S87 5,5 s → khi dựng chia đôi bằng một lần punch-in hoặc chèn b-roll giữa câu.")
L.append("- Hai bà cùng tóc bạc ngắn: phân biệt bằng tông da (Dorothy sẫm hơn), mặt (Gloria tròn, Dorothy dài), kính (Gloria treo dây trước ngực, Dorothy đeo trên mặt), dáng (Gloria đầy đặn, Dorothy cao gầy). Sheet ra giống nhau thì báo Claude.")
L.append("- File 01 mở được mà 02–09 (78–95 KB) không mở được: giới hạn dung lượng thấp hơn → báo Claude tách nhỏ hơn. File 01 cũng không mở được: lỗi định dạng → gửi câu Toby báo + một file export workflow cũ có node video và node tải (vd. S12 v3) để so từng trường.")
L.append("- Tên trường lấy theo mục 6 của skill (chưa có file export mẫu trong phiên này). Node `download` đã bỏ trường thừa `download`.")
L.append("- Chưa đọc được Doc 56, 25, 47, 63, 72, 80 và Toby Flow 01, 02 (phiên cloud không có Projects); nên rà lại theo checklist Doc 56.")
L.append("- Claim: \"hormone disruption\" đã duyệt; Meta từ chối thì thay \"Ones you don't want in your food.\" (chỉ đổi file giọng S48, clip câm không phải gen lại).")
L.append("- Nhân vật AI: bật nhãn nội dung AI khi chạy ads.")
open('out/S14c_Black_TobyFlow.md', 'w').write('\n'.join(L) + '\n')
print('ok')
