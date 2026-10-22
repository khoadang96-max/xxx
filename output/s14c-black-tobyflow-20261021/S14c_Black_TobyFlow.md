# S14c We Talked About This (bản da đen) — Workflow TobyFlow (21-10)

Nguồn: `Editor_Script14_WeTalkedAboutThis_Black_Acawood.docx` (bản 4, sau CD review). Làm theo skill toby-workflow: Nano Banana Pro cho ảnh, **Omni 1.1 Flash** (Frames) cho mọi clip.

## 1. Tóm tắt

- **98 clip** (74 T_ có thoại, 24 V_ câm). Không còn node `TAI`: bật **Auto Download** trong Settings của Toby, mỗi clip tự tải 1080p vào thư mục theo tên node clip.
- **Setup 2 file (0A, 0B) + 27 file clip nhỏ.** 0A: sheet nhân vật gốc, đạo cụ, 4 ảnh nền gốc. 0B: sheet đổi đồ và 4 trạng thái khác của cùng hai căn phòng, sửa từ ảnh gốc ở 0A. Ngày 22/10 file clip 01 (49 KB, 35 node) không import được trong khi 0B (31 KB, 28 node) vào được, nên mỗi file clip giờ ≤ 32 KB và ≤ 28 node. Bản này phá luật "một kịch bản = một workflow" vì giới hạn import.
- **Nhân vật (22/10):** viết lại theo nghiên cứu gia đình Mỹ da đen, chi tiết ở `S14c_Black_NhanVat.md`. Sheet đổi đồ chuyển sang file 0B (lấy sheet gốc từ 0A) vì bản cũ nối trong cùng file nên ra người lạ.
- **Số lượng:** node ảnh x4 (không tốn credit), node video x2 (98 clip → 196 lượt video). **42 clip nói** có khung đầu = khung cuối (cùng một ảnh vào frame_1 và frame_2) để người không trôi.
- Đã đối chiếu với luật trong chat cũ của Nam (xem mục 1b và `references/toby-flow-rules-nam.md`). Phải import lại cả 11 file: mọi file đều đổi.
- File import: `toby/workflow_S14c_0A_Setup.json`, `toby/workflow_S14c_0B_DoiDo.json`, rồi `toby/workflow_S14c_01_HookCB.json` … `workflow_S14c_09_Close.json`. Payload `create_workflow` cho Toby MCP (Claude Desktop): `toby/mcp/`. Kèm `S14c_Black_prompt_pack.txt` và 6 SRT (H1, A–E).
- **Chưa tạo trên Toby, chưa chạy gì.**

## 1b. Đã sửa theo luật Nam (21–22/10)

| Luật | Bản trước | Bản này |
|---|---|---|
| Ảnh x4, video x2 | quantity 1 mọi node | 120 node ảnh x4, 98 node video x2 (skill toby-workflow vẫn ghi quantity 1, xem mục 7) |
| Clip nói: cùng một ảnh vào frame_1 và frame_2 | chỉ frame_1 | 42 clip nói giữ dáng có frame_2; 32 clip nói có động tác đổi trạng thái (đặt đồ, quay đầu, cắn, xé, đổi nét…) chỉ frame_1 |
| Tay viết câu khẳng định ("missing fingers" bị Google chặn) | "the right number of fingers… no extra hands" | "Every hand has five fingers in natural proportion…" |
| Không mặt trẻ em, không "seen from behind" + người | cậu bé "seen from behind"; S12 "from behind the grandmother's shoulder"; S18 "back to the door" | cậu bé chỉ thấy bàn tay + tay áo; sheet cậu bé thành sheet quần áo, không người; S12 over-the-shoulder; S18 đứng quay ra phố |
| Living layer: chỉ thứ có sẵn trong khung chuyển động | con thiêu thân (C), bụi (B_MORNING), giấy báo tự bay (B_BOXES) | "(only what is already in the frame moves, nothing is added)"; bỏ 3 chi tiết thêm vào |
| Physical logic: không vật nào tự chuyển động | chưa có | "nothing moves on its own: whatever moves is moved by a visible hand or by the action" |
| Omni ậm ừ/cười sau câu; mặt không đơ | "then stays silent" | "lips close and stay closed, no sound" + dòng Face (biểu cảm theo lời, không đơ, không lố) |
| Hành động chính trong giây đầu | chưa ghi | "the main action starts within the first second" |
| [FOOD-ACA]: đồ ăn cạnh Acawood tươi, sạch | chưa có | S71, S72, S81, S85 có khối FOOD-ACA (ảnh + clip) |
| Giọng: Omni nói, rồi ElevenLabs Voice Changer | "dựng thay bằng giọng ElevenLabs" | Voice Changer từng nhân vật trên lời Omni (giữ nhịp, khớp miệng) |
| Chữ cấm (smooth, perfect…) | "smooth baritone", "perfectly clear" | "mellow baritone", "completely clear" |
| Ảnh tham chiếu phải đến từ file chạy trước | 7 sheet đổi đồ lấy ảnh gốc trong cùng file Setup → ra người lạ, đa số da trắng, đeo kính | 0A sheet gốc, 0B đổi đồ (tải sheet gốc vào `IMG_CS_*_1`); prompt đổi đồ tả lại đủ người |
| Nhân vật da đen phải giống người thật | chỉ "Black American, warm brown skin" cho mọi người | tông da + undertone riêng, nét mặt, tóc xoăn tít tự nhiên, dấu tuổi da nâu, khối da không xám/tro; chỉ Gloria và Dorothy có kính |
| People lock trong clip | chưa có | "People: everyone in the start frame keeps the same face, age, skin tone, hair and clothes…" |
| Physical logic (S44) | spatula tự trộn khoai, không có tay | spatula nằm yên, hơi nóng bốc lên, máy tiến gần (cận tay người già cầm đồ dễ bị chặn) |
| D-2: tay của ai | "a man's two hands" | tay Terrance: da nâu sẫm, lòng bàn tay sáng hơn, nhẫn cưới, cổ tay áo caro; đính sheet Terrance 3 |
| Mũ đi lễ cho Dorothy (Nam, 22/10) | không có | mũ xanh rêu cùng bộ đồ, vành vừa, hoa vải, đội cả chiều Chủ nhật; chỉ mình bà đội mũ |
| Bình nước to của Jada (docx) | không có | cốc giữ nhiệt hồng nhạt, không logo, chỉ đặt trên bàn/quầy ở S01, S08, S21, S71, S81; không ai cầm |
| Ảnh trang trí là ảnh của gia đình da đen này (Nam, 22/10) | "framed family and graduation photos", "family photos on the fridge" chung chung → model tự bịa người | tường: ảnh cưới của bà và người chồng đã mất, ảnh tốt nghiệp của Terrance, của Jada, ảnh bà với con trai, con dâu trước nhà thờ; tủ lạnh: ảnh bà với bạn nhà thờ, Terrance và vợ, Jada đội mũ tốt nghiệp; toàn người da đen, chỉ người lớn, ảnh nhỏ, hơi mờ, không chữ |
| Quạt giấy nhà thờ | không tả mặt in | in tranh một nhà thờ trắng nhỏ, không người, không chữ |
| Cùng một căn phòng ở nhiều cảnh | phòng ăn thứ Sáu và 4 trạng thái bếp tạo riêng từ chữ → mỗi cảnh một căn phòng, ảnh treo khác nhau | 0A tạo phòng ăn sinh nhật và bếp buổi sáng; 0B sửa từ 2 ảnh đó ra phòng ăn thứ Sáu, bếp đêm, bếp đóng thùng, bếp vài tuần sau, giữ nguyên tường, tủ, ảnh |
| Người ở bàn ăn | "the family", "the whole table" chung chung (C-1, S01, S05, S08, S71, S81) | ghi rõ: gia đình người Mỹ da đen, chỉ người lớn lộ mặt, thêm 2 họ hàng lớn tuổi ở cuối bàn (docx: 2–3 họ hàng mờ hậu cảnh); chỗ ngồi cố định theo docx; C-1 mẹ ngoài khung |
| Món trên bàn (docx) | bỏ sót | rau collard, khoai lang, bánh ngô mờ ở hậu cảnh các cảnh bàn ăn |
| Tay cầm đồ ở mép khung | S42, S48, S61 không nói tay ai; S64 không rõ ai cầm | tay Dorothy (S42, S48), tay Gloria (S61), Terrance tự cầm muôi (S64): ghi tông da, tay áo, nhẫn và đính sheet |
| Màn hình điện thoại | E-2, S54 không nói màn hình hiện gì | E-2 màn hình quay đi; S54 chỉ sáng trơn, không chữ (giao diện tin nhắn dựng ở CapCut, S55) |

## 2. Ảnh thật cần chuẩn bị

| Ảnh | Cần gì | Tải vào |
|---|---|---|
| `IMG_ACA_SET` | real product photo: the 7 Acawood utensils on white, straight + 3/4 | file 16, file 17, file 18, file 19, file 20, file 22, file 25, file 26, file 27 |
| `IMG_ACA_HOLDER` | real product photo: the full set standing in the round holder | file 0B, file 25, file 26, file 27 |
| `IMG_ACA_TOWEL` | real product photo, top view: 7 utensils laid in a row on the red-and-white checkered towel (start frame S49) | file 16 |
| `IMG_ACA_MACRO` | real macro photo: grain running unbroken from handle to head (start frame S53) | file 17 |
| `IMG_WATERTEST` | a still frame from the real hot-water test clip (water still clear) (ref for F_S87) | file 27 |

## 3. Các file và thứ tự làm

1. **`S14c_0A Setup nhan vat nen`** (26 node, chỉ ảnh, x4, không cần tải ảnh): 6 character sheet gốc (Gloria 1, Terrance 1, Jada 1, Dorothy, vợ Terrance, con gái Dorothy), sheet quần áo cậu bé (không người), 2 sheet đạo cụ, 4 ảnh nền gốc (`BG_A_BDAY`, `BG_B_MORNING`, `BG_C`, `BG_D`). Duyệt theo mục 6 của `S14c_Black_NhanVat.md`, xem ảnh treo tường và ảnh trên tủ lạnh đều là người da đen, chọn 1 ảnh mỗi node, **tải về máy**.
2. **`S14c_0B Doi do`** (28 node): tải 6 ảnh vào node `IMG_`: 3 sheet gốc (`IMG_CS_GLORIA_1`, `IMG_CS_TERRANCE_1`, `IMG_CS_JADA_1`), 2 ảnh nền gốc (`IMG_BG_A_BDAY`, `IMG_BG_B_MORNING`) và ảnh thật bộ Acawood trong ống (`IMG_ACA_HOLDER`) → chạy 7 sheet đổi đồ + 4 ảnh nền (`BG_A_FRI`, `BG_B_NIGHT`, `BG_B_BOXES`, `BG_B_CLEAR`) → chọn, tải về.
3. **Import file `01` trước** (1 clip, 9 KB, nhỏ hơn cả 0A). Vào được thì import tiếp 02 → cuối. Không vào được thì lỗi là định dạng chứ không phải dung lượng: dừng lại, chụp dòng báo lỗi của Toby gửi Claude.
4. Mỗi file có cột node `IMG_` bên trái: tải đúng ảnh vào đúng node theo bảng dưới (tên node = `IMG_` + tên node ở Setup).
5. Trong từng file: chạy `F_` (xem khung) → `T_/V_`; Auto Download tải clip 1080p.
6. Có Claude Desktop + Toby MCP thì khỏi tải tay: Claude đọc kết quả Setup (`get_workflow`) rồi `update_node` gắn ảnh vào các node `IMG_` (MCP tạo tối đa 5 workflow/ngày).

| File | Workflow | Shot | KB | Node | Clip | Tải ảnh vào node IMG_ |
|---|---|---|---|---|---|---|
| 0A | `S14c_0A Setup nhan vat nen` | character sheet gốc 7 nhân vật + 2 sheet đạo cụ + 4 ảnh nền gốc | 26.5 | 26 | 0 |  |
| 0B | `S14c_0B Doi do` | 7 sheet đổi đồ (Gloria 2–4, Terrance 2–4, Jada 2) và 4 ảnh nền cùng phòng (phòng ăn thứ Sáu, bếp đêm, bếp đóng thùng, bếp vài tuần sau) sửa từ ảnh gốc ở 0A | 31.6 | 28 | 0 | `IMG_CS_GLORIA_1` ← `CS_GLORIA_1`<br>`IMG_CS_TERRANCE_1` ← `CS_TERRANCE_1`<br>`IMG_CS_JADA_1` ← `CS_JADA_1`<br>`IMG_BG_A_BDAY` ← `BG_A_BDAY`<br>`IMG_BG_B_MORNING` ← `BG_B_MORNING`<br>`IMG_ACA_HOLDER` ← ảnh thật |
| 01 | `S14c_01 Hook C B` | None | 9.0 | 7 | 1 | `IMG_BG_A_BDAY` ← `BG_A_BDAY`<br>`IMG_CS_TERRANCE_1` ← `CS_TERRANCE_1`<br>`IMG_CS_JADA_1` ← `CS_JADA_1` |
| 02 | `S14c_02 Hook C B` | None | 31.0 | 20 | 4 | `IMG_BG_A_BDAY` ← `BG_A_BDAY`<br>`IMG_CS_TERRANCE_1` ← `CS_TERRANCE_1`<br>`IMG_CS_JADA_1` ← `CS_JADA_1`<br>`IMG_PROP_BROCHURE` ← `PROP_BROCHURE` |
| 03 | `S14c_03 Hook C B - Sinh nhat` | None | 24.0 | 16 | 3 | `IMG_BG_A_BDAY` ← `BG_A_BDAY`<br>`IMG_CS_JADA_1` ← `CS_JADA_1`<br>`IMG_CS_TERRANCE_1` ← `CS_TERRANCE_1`<br>`IMG_CS_GLORIA_1` ← `CS_GLORIA_1` |
| 04 | `S14c_04 Sinh nhat` | None | 25.3 | 17 | 3 | `IMG_BG_A_BDAY` ← `BG_A_BDAY`<br>`IMG_CS_GLORIA_1` ← `CS_GLORIA_1`<br>`IMG_CS_JADA_1` ← `CS_JADA_1`<br>`IMG_CS_TERRANCE_1` ← `CS_TERRANCE_1`<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE` |
| 05 | `S14c_05 Sinh nhat` | None | 28.1 | 20 | 4 | `IMG_BG_A_BDAY` ← `BG_A_BDAY`<br>`IMG_PROP_BROCHURE` ← `PROP_BROCHURE`<br>`IMG_CS_GLORIA_1` ← `CS_GLORIA_1`<br>`IMG_CS_TERRANCE_1` ← `CS_TERRANCE_1` |
| 06 | `S14c_06 Sinh nhat - Bep dem` | None | 30.5 | 24 | 4 | `IMG_BG_A_BDAY` ← `BG_A_BDAY`<br>`IMG_CS_WIFE` ← `CS_WIFE`<br>`IMG_CS_JADA_1` ← `CS_JADA_1`<br>`IMG_CS_GRANDSON` ← `CS_GRANDSON`<br>`IMG_BG_B_NIGHT` ← `BG_B_NIGHT`<br>`IMG_CS_GLORIA_1` ← `CS_GLORIA_1`<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE`<br>`IMG_CS_TERRANCE_1` ← `CS_TERRANCE_1` |
| 07 | `S14c_07 Bep dem` | None | 29.5 | 19 | 4 | `IMG_BG_B_NIGHT` ← `BG_B_NIGHT`<br>`IMG_CS_TERRANCE_1` ← `CS_TERRANCE_1`<br>`IMG_CS_GLORIA_1` ← `CS_GLORIA_1` |
| 08 | `S14c_08 Bep dem - Hien dem` | None | 27.5 | 21 | 4 | `IMG_BG_B_NIGHT` ← `BG_B_NIGHT`<br>`IMG_CS_TERRANCE_1` ← `CS_TERRANCE_1`<br>`IMG_PROP_BROCHURE` ← `PROP_BROCHURE`<br>`IMG_CS_GLORIA_1` ← `CS_GLORIA_1`<br>`IMG_BG_C` ← `BG_C` |
| 09 | `S14c_09 Sang` | None | 28.8 | 20 | 4 | `IMG_BG_B_MORNING` ← `BG_B_MORNING`<br>`IMG_CS_GLORIA_2` ← `CS_GLORIA_2`<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE`<br>`IMG_CS_JADA_1` ← `CS_JADA_1` |
| 10 | `S14c_10 Sang - Dong thung` | S24 → S27 | 27.7 | 20 | 4 | `IMG_BG_B_MORNING` ← `BG_B_MORNING`<br>`IMG_CS_GLORIA_2` ← `CS_GLORIA_2`<br>`IMG_CS_JADA_1` ← `CS_JADA_1`<br>`IMG_BG_B_BOXES` ← `BG_B_BOXES` |
| 11 | `S14c_11 Hien Dorothy` | S28 → S31 | 30.6 | 20 | 4 | `IMG_BG_D` ← `BG_D`<br>`IMG_CS_DOROTHY` ← `CS_DOROTHY`<br>`IMG_CS_FRIEND_DAUGHTER` ← `CS_FRIEND_DAUGHTER`<br>`IMG_CS_GLORIA_2` ← `CS_GLORIA_2` |
| 12 | `S14c_12 Hien Dorothy` | S32 → S35 | 27.5 | 19 | 4 | `IMG_BG_D` ← `BG_D`<br>`IMG_CS_DOROTHY` ← `CS_DOROTHY`<br>`IMG_CS_GLORIA_2` ← `CS_GLORIA_2` |
| 13 | `S14c_13 Co che` | S36 → S38 | 22.7 | 16 | 3 | `IMG_BG_B_BOXES` ← `BG_B_BOXES`<br>`IMG_CS_DOROTHY` ← `CS_DOROTHY`<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE`<br>`IMG_CS_GLORIA_2` ← `CS_GLORIA_2` |
| 14 | `S14c_14 Co che` | S39 → S42 | 29.8 | 20 | 4 | `IMG_BG_B_BOXES` ← `BG_B_BOXES`<br>`IMG_CS_GLORIA_2` ← `CS_GLORIA_2`<br>`IMG_CS_DOROTHY` ← `CS_DOROTHY`<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE` |
| 15 | `S14c_15 Co che` | S43 → S46 | 27.4 | 20 | 4 | `IMG_BG_B_BOXES` ← `BG_B_BOXES`<br>`IMG_CS_DOROTHY` ← `CS_DOROTHY`<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE`<br>`IMG_CS_GLORIA_2` ← `CS_GLORIA_2` |
| 16 | `S14c_16 Co che - San pham` | S47 → S50 | 26.7 | 20 | 4 | `IMG_BG_B_BOXES` ← `BG_B_BOXES`<br>`IMG_CS_DOROTHY` ← `CS_DOROTHY`<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE`<br>`IMG_CS_GLORIA_2` ← `CS_GLORIA_2`<br>`IMG_ACA_TOWEL` ← ảnh thật<br>`IMG_ACA_SET` ← ảnh thật |
| 17 | `S14c_17 San pham` | S51 → S54 | 26.6 | 19 | 4 | `IMG_BG_B_BOXES` ← `BG_B_BOXES`<br>`IMG_CS_GLORIA_2` ← `CS_GLORIA_2`<br>`IMG_ACA_SET` ← ảnh thật<br>`IMG_CS_DOROTHY` ← `CS_DOROTHY`<br>`IMG_ACA_MACRO` ← ảnh thật |
| 18 | `S14c_18 San pham - Loi cuoc` | S56 → S59 | 30.7 | 22 | 4 | `IMG_BG_B_BOXES` ← `BG_B_BOXES`<br>`IMG_CS_DOROTHY` ← `CS_DOROTHY`<br>`IMG_ACA_SET` ← ảnh thật<br>`IMG_CS_TERRANCE_2` ← `CS_TERRANCE_2`<br>`IMG_CS_GLORIA_2` ← `CS_GLORIA_2`<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE` |
| 19 | `S14c_19 Loi cuoc` | S60 → S63 | 30.3 | 21 | 4 | `IMG_BG_B_BOXES` ← `BG_B_BOXES`<br>`IMG_CS_GLORIA_2` ← `CS_GLORIA_2`<br>`IMG_CS_TERRANCE_2` ← `CS_TERRANCE_2`<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE`<br>`IMG_ACA_SET` ← ảnh thật |
| 20 | `S14c_20 Loi cuoc` | S64 → S66 | 24.3 | 17 | 3 | `IMG_BG_B_BOXES` ← `BG_B_BOXES`<br>`IMG_CS_TERRANCE_2` ← `CS_TERRANCE_2`<br>`IMG_ACA_SET` ← ảnh thật<br>`IMG_CS_GLORIA_2` ← `CS_GLORIA_2`<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE` |
| 21 | `S14c_21 Loi cuoc` | S67 → S70 | 28.4 | 19 | 4 | `IMG_BG_B_BOXES` ← `BG_B_BOXES`<br>`IMG_CS_TERRANCE_2` ← `CS_TERRANCE_2`<br>`IMG_CS_GLORIA_2` ← `CS_GLORIA_2` |
| 22 | `S14c_22 Thu Sau` | D-2 → S72 | 28.2 | 20 | 3 | `IMG_BG_A_FRI` ← `BG_A_FRI`<br>`IMG_CS_TERRANCE_3` ← `CS_TERRANCE_3`<br>`IMG_PROP_BROCHURE` ← `PROP_BROCHURE`<br>`IMG_CS_GLORIA_3` ← `CS_GLORIA_3`<br>`IMG_CS_JADA_2` ← `CS_JADA_2`<br>`IMG_CS_WIFE` ← `CS_WIFE`<br>`IMG_CS_GRANDSON` ← `CS_GRANDSON`<br>`IMG_ACA_SET` ← ảnh thật |
| 23 | `S14c_23 Thu Sau` | S73 → S76 | 26.6 | 19 | 4 | `IMG_BG_A_FRI` ← `BG_A_FRI`<br>`IMG_CS_JADA_2` ← `CS_JADA_2`<br>`IMG_CS_TERRANCE_3` ← `CS_TERRANCE_3` |
| 24 | `S14c_24 Thu Sau` | S77 → S80 | 28.6 | 21 | 4 | `IMG_BG_A_FRI` ← `BG_A_FRI`<br>`IMG_CS_TERRANCE_3` ← `CS_TERRANCE_3`<br>`IMG_PROP_BROCHURE` ← `PROP_BROCHURE`<br>`IMG_CS_GLORIA_3` ← `CS_GLORIA_3`<br>`IMG_CS_JADA_2` ← `CS_JADA_2` |
| 25 | `S14c_25 Thu Sau - Close` | S81 → S83 | 29.2 | 23 | 3 | `IMG_BG_A_FRI` ← `BG_A_FRI`<br>`IMG_CS_TERRANCE_3` ← `CS_TERRANCE_3`<br>`IMG_CS_JADA_2` ← `CS_JADA_2`<br>`IMG_CS_GLORIA_3` ← `CS_GLORIA_3`<br>`IMG_CS_WIFE` ← `CS_WIFE`<br>`IMG_CS_GRANDSON` ← `CS_GRANDSON`<br>`IMG_ACA_SET` ← ảnh thật<br>`IMG_BG_B_CLEAR` ← `BG_B_CLEAR`<br>`IMG_CS_GLORIA_4` ← `CS_GLORIA_4`<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE`<br>`IMG_ACA_HOLDER` ← ảnh thật |
| 26 | `S14c_26 Close` | S84 → S86 | 28.4 | 18 | 3 | `IMG_BG_B_CLEAR` ← `BG_B_CLEAR`<br>`IMG_CS_GLORIA_4` ← `CS_GLORIA_4`<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE`<br>`IMG_ACA_HOLDER` ← ảnh thật<br>`IMG_CS_TERRANCE_4` ← `CS_TERRANCE_4`<br>`IMG_ACA_SET` ← ảnh thật |
| 27 | `S14c_27 Close` | S87 → S90 | 30.3 | 21 | 4 | `IMG_BG_B_CLEAR` ← `BG_B_CLEAR`<br>`IMG_ACA_SET` ← ảnh thật<br>`IMG_WATERTEST` ← ảnh thật<br>`IMG_CS_GLORIA_4` ← `CS_GLORIA_4`<br>`IMG_ACA_HOLDER` ← ảnh thật |

Tổng số lần tải ảnh nếu làm tay: 137.

## 4. Quyết định so với docx (theo luật TobyFlow đã chốt)

| Docx | Workflow | Lý do |
|---|---|---|
| Veo 3.1 / Kling 3.0 + Sync, Seedance | Omni 1.1 Flash, chế độ Frames, mọi clip | Mặc định skill |
| Độ dài clip = độ dài shot (1–6,5 s) | Có thoại: 6/8 s theo công thức 2,5 chữ/s, bắt đầu 0,4 s (1,0 s nếu có động tác trước), chừa 0,6 s. Câm: 4 s (shot > 3,5 s thì 6 s) | Nhân vật phải nói hết câu; khi dựng cắt đúng độ dài shot ở storyboard |
| Tắt tiếng model, dùng giọng ElevenLabs | Omni nói câu (khối VOICE từng nhân vật, cho khớp miệng); dựng xong tách lời từng nhân vật, chạy ElevenLabs Voice Changer (Multilingual v2 STS, Stability 50, Similarity 85, Style 0, bỏ tiếng nền) — giữ nhịp nên vẫn khớp miệng | Không gắn `voice` Flow vào Frames (lỗi cả lô); lời TTS mới sẽ lệch miệng |
| [TAIL]: pores, shallow depth of field, 35mm, cinematic, slow push-in | Khối máy quay thật + da thật; "glides a few centimeters closer" | Chữ ép nét làm ảnh giả, như nhựa; từ cấm |
| Cậu bé 10 tuổi rõ mặt (S08, S71, S81) | Chỉ bàn tay + tay áo ở mép khung; sheet chỉ quần áo, không người | Không mặt trẻ em; "seen from behind" + người bị Google chặn |
| S88 cận tay Gloria rửa muôi | Trung cảnh từ eo lên, lau muôi rồi cắm vào ống | Cận tay người già cầm đồ bị chặn (S12) |
| "phone", "dark-wood", "slowly" | "handset", "deep-brown", "at walking pace" | Từ cấm trong prompt |
| Shot lời ngoài khung (S18, S26, S44, S48, S53, S87, S88) | Clip câm V_, giọng đặt ở dựng | Không có miệng để khớp |
| Xé brochure (S78, D-2) | Khóa riêng: chỉ brochure đổi, xé một đường; lỗi thì dùng phương án thả vào thùng giấy (docx) | Chống biến dạng |
| Đồ có sản phẩm | Khối Lighting match + Object lock; S49, S53 dùng thẳng ảnh thật làm khung đầu | Không trông như ghép; đúng 7 món |

## 5. Không gen trong Toby (dựng ở CapCut)

- `S55` màn hình điện thoại + nút BUY NOW · `E-1` group chat FAMILY · `S91` end card · banner, phụ đề, thẻ chữ thời gian, nhãn xanh S86, thẻ offer S89, chữ WRENFIELD ghép ở S04 và thùng KITCHEN — WRENFIELD ở S27.
- Hook D-1 = dùng lại `S14c_T_S79`.

## 6. Bảng clip

Shot dựng = mốc cắt khi dựng (storyboard). Clip dài hơn để nhân vật nói hết câu; cắt phần lặng.

Khung cuối "= đầu": frame_2 cùng ảnh với frame_1. Clip nào bị đứng im thì báo Claude bỏ khung cuối của clip đó.

| Shot | File | Node clip | Clip | Shot dựng | Lời xong lúc | Khung cuối | Ảnh đính (Image 1..n) | Lời |
|---|---|---|---|---|---|---|---|---|
| A-1 | 03 | `S14c_T_A1` | 6 s | — | 4.4 | — | BG_A_BDAY, CS_JADA_1, CS_TERRANCE_1, CS_GLORIA_1 | JADA: Dad. It's the soap thing again. I can't eat this. |
| B-1 | 02 | `S14c_T_B1` | 6 s | — | 3.6 | — | BG_A_BDAY, CS_TERRANCE_1, CS_JADA_1, PROP_BROCHURE | JADA: You're giving her THAT? Over the soap thing? |
| C-1 | 01 | `S14c_T_C1` | 6 s | — | 2.8 | = đầu | BG_A_BDAY, CS_TERRANCE_1, CS_JADA_1 | TERRANCE: To Mama. Seventy-one and still cooking. |
| C-2 | 02 | `S14c_T_C2` | 6 s | — | 2.4 | — | BG_A_BDAY, CS_JADA_1 | JADA: Sorry. It's the soap thing. |
| D-2 | 22 | `S14c_V_D2` | 4 s | — | — | — | BG_A_FRI, CS_TERRANCE_3, PROP_BROCHURE | (câm) |
| E-2 | 03 | `S14c_T_E2` | 6 s | — | 3.6 | — | BG_A_BDAY, CS_JADA_1 | JADA: Dad, I can't. It's the soap thing. |
| S01 | 04 | `S14c_T_S01` | 6 s | 3,5 s | 4.0 | — | BG_A_BDAY, CS_GLORIA_1, CS_JADA_1, CS_TERRANCE_1, PROP_SILICONE | JADA: Grandma, why does everything you make taste like SOAP? |
| S02 | 04 | `S14c_T_S02` | 6 s | 2,2 s | 2.4 | — | BG_A_BDAY, CS_TERRANCE_1, CS_JADA_1 | TERRANCE: Jada. We TALKED about this. |
| S02_B | 02 | `S14c_T_S02_B` | 6 s | 2,2 s | 2.4 | — | BG_A_BDAY, CS_TERRANCE_1, CS_JADA_1 | TERRANCE: Jada. We TALKED about this. |
| S02_C | 02 | `S14c_T_S02_C` | 6 s | 2,2 s | 2.4 | — | BG_A_BDAY, CS_TERRANCE_1, CS_JADA_1 | TERRANCE: Jada. We TALKED about this. |
| S03 | 04 | `S14c_T_S03` | 6 s | 1,7 s | 1.6 | — | BG_A_BDAY, CS_GLORIA_1 | GLORIA: Talked about what? |
| S03_B | 03 | `S14c_T_S03_B` | 6 s | 1,7 s | 1.6 | — | BG_A_BDAY, CS_GLORIA_1 | GLORIA: Talked about what? |
| S04 | 05 | `S14c_V_S04` | 4 s | 1,5 s | — | — | BG_A_BDAY, PROP_BROCHURE | (câm) |
| S05 | 05 | `S14c_T_S05` | 6 s | 2,5 s | 2.8 | — | BG_A_BDAY, CS_GLORIA_1, PROP_BROCHURE | GLORIA: You're putting me in a HOME? |
| S06 | 05 | `S14c_T_S06` | 6 s | 3,3 s | 3.6 | = đầu | BG_A_BDAY, CS_TERRANCE_1 | TERRANCE: Mama. We were gonna wait till after cake. |
| S07 | 05 | `S14c_T_S07` | 6 s | 1,6 s | 1.6 | = đầu | BG_A_BDAY, CS_GLORIA_1, PROP_BROCHURE | GLORIA: On my BIRTHDAY? |
| S08 | 06 | `S14c_V_S08` | 4 s | 1,6 s | — | — | BG_A_BDAY, CS_WIFE, CS_JADA_1, CS_GRANDSON | (câm) |
| S09 | 06 | `S14c_T_S09` | 6 s | 3,3 s | 4.2 | — | BG_B_NIGHT, CS_GLORIA_1, PROP_SILICONE | GLORIA: Soap. You think I can't rinse a POT? |
| S10 | 06 | `S14c_T_S10` | 6 s | 2,9 s | 3.2 | = đầu | BG_B_NIGHT, CS_TERRANCE_1 | TERRANCE: Every dinner since Christmas. We've all noticed. |
| S11 | 06 | `S14c_T_S11` | 6 s | 1,7 s | 1.6 | — | BG_B_NIGHT, CS_GLORIA_1 | GLORIA: All of you? |
| S12 | 07 | `S14c_T_S12` | 6 s | 2,9 s | 3.2 | = đầu | BG_B_NIGHT, CS_TERRANCE_1, CS_GLORIA_1 | TERRANCE: Taste buds go as you get older. |
| S13 | 07 | `S14c_T_S13` | 8 s | 4,9 s | 5.6 | = đầu | BG_B_NIGHT, CS_TERRANCE_1 | TERRANCE: But if you can't taste soap, what happens when you can't smell gas? |
| S14 | 07 | `S14c_T_S14` | 6 s | 3,5 s | 3.6 | — | BG_B_NIGHT, CS_GLORIA_1 | GLORIA: I've cooked in this kitchen for forty-two years. |
| S15 | 07 | `S14c_T_S15` | 6 s | 4,4 s | 4.8 | = đầu | BG_B_NIGHT, CS_TERRANCE_1 | TERRANCE: I know. That's why I don't want you in it alone. |
| S16 | 08 | `S14c_T_S16` | 8 s | 4,7 s | 5.8 | — | BG_B_NIGHT, CS_TERRANCE_1, PROP_BROCHURE | TERRANCE: Wrenfield has a unit opening this month. I put down a deposit. |
| S17 | 08 | `S14c_T_S17` | 6 s | 1,8 s | 1.6 | — | BG_B_NIGHT, CS_GLORIA_1 | GLORIA: You already PAID? |
| S18 | 08 | `S14c_V_S18` | 4 s | 3,0 s | — | — | BG_C, CS_TERRANCE_1 | TERRANCE: No, she won't fight it. She's — slipping. |
| S19 | 08 | `S14c_V_S19` | 4 s | 1,4 s | — | — | BG_C, CS_GLORIA_1 | (câm) |
| S20 | 09 | `S14c_V_S20` | 4 s | 1,5 s | — | — | BG_B_MORNING, CS_GLORIA_2, PROP_SILICONE | (câm) |
| S21 | 09 | `S14c_T_S21` | 6 s | 1,8 s | 2.6 | — | BG_B_MORNING, CS_JADA_1 | JADA: Grandma, it's still there. |
| S22 | 09 | `S14c_T_S22` | 6 s | 4,1 s | 4.4 | = đầu | BG_B_MORNING, CS_GLORIA_2, PROP_SILICONE | GLORIA: I scrubbed that pan THREE times. New soap. New sponge. |
| S23 | 09 | `S14c_T_S23` | 6 s | 2,5 s | 3.4 | — | BG_B_MORNING, CS_GLORIA_2 | GLORIA: And I can't taste a THING. |
| S24 | 10 | `S14c_T_S24` | 6 s | 2,4 s | 2.4 | = đầu | BG_B_MORNING, CS_GLORIA_2 | GLORIA: Jada, am I losing it? |
| S25 | 10 | `S14c_V_S25` | 4 s | 1,4 s | — | — | BG_B_MORNING, CS_JADA_1, CS_GLORIA_2 | (câm) |
| S26 | 10 | `S14c_V_S26` | 4 s | 2,0 s | — | — | BG_B_MORNING, CS_JADA_1, CS_GLORIA_2 | JADA: I love you, Grandma. |
| S27 | 10 | `S14c_V_S27` | 4 s | 1,6 s | — | — | BG_B_BOXES, CS_GLORIA_2 | (câm) |
| S28 | 11 | `S14c_V_S28` | 4 s | 1,8 s | — | — | BG_D, CS_DOROTHY, CS_FRIEND_DAUGHTER, CS_GLORIA_2 | (câm) |
| S29 | 11 | `S14c_T_S29` | 6 s | 3,2 s | 4.2 | — | BG_D, CS_GLORIA_2 | GLORIA: Wasn't she the one PUSHING you into Wrenfield? |
| S30 | 11 | `S14c_T_S30` | 6 s | 1,3 s | 1.6 | = đầu | BG_D, CS_DOROTHY | DOROTHY: She sure was. |
| S31 | 11 | `S14c_T_S31` | 6 s | 4,0 s | 4.4 | — | BG_D, CS_GLORIA_2, CS_DOROTHY | GLORIA: Now she's here every Sunday, taking plates home. What CHANGED? |
| S32 | 12 | `S14c_T_S32` | 6 s | 3,3 s | 4.2 | — | BG_D, CS_DOROTHY | DOROTHY: She told me my cooking tasted like soap. |
| S33 | 12 | `S14c_V_S33` | 4 s | 1,1 s | — | — | BG_D, CS_GLORIA_2 | (câm) |
| S34 | 12 | `S14c_T_S34` | 6 s | 1,4 s | 1.2 | = đầu | BG_D, CS_GLORIA_2 | GLORIA: Mine too. |
| S35 | 12 | `S14c_T_S35` | 6 s | 1,8 s | 2.0 | — | BG_D, CS_DOROTHY | DOROTHY: Show me your kitchen. |
| S36 | 13 | `S14c_T_S36` | 6 s | 1,7 s | 2.0 | — | BG_B_BOXES, CS_DOROTHY, PROP_SILICONE | DOROTHY: When'd you buy these? |
| S37 | 13 | `S14c_T_S37` | 6 s | 4,0 s | 4.4 | = đầu | BG_B_BOXES, CS_GLORIA_2 | GLORIA: After Thanksgiving. Terrance sent me an article about black plastic. |
| S38 | 13 | `S14c_T_S38` | 6 s | 2,5 s | 2.8 | = đầu | BG_B_BOXES, CS_DOROTHY | DOROTHY: And when did the soap start? |
| S39 | 14 | `S14c_V_S39` | 4 s | 1,0 s | — | — | BG_B_BOXES, CS_GLORIA_2 | (câm) |
| S40 | 14 | `S14c_T_S40` | 6 s | 1,3 s | 0.8 | = đầu | BG_B_BOXES, CS_GLORIA_2 | GLORIA: Christmas. |
| S41 | 14 | `S14c_T_S41` | 6 s | 1,2 s | 1.2 | = đầu | BG_B_BOXES, CS_DOROTHY, CS_GLORIA_2, PROP_SILICONE | DOROTHY: Smell it. |
| S42 | 14 | `S14c_T_S42` | 6 s | 1,8 s | 2.6 | — | BG_B_BOXES, CS_GLORIA_2, CS_DOROTHY, PROP_SILICONE | GLORIA: That's my DISH soap. |
| S43 | 15 | `S14c_T_S43` | 6 s | 2,8 s | 3.2 | = đầu | BG_B_BOXES, CS_DOROTHY, PROP_SILICONE | DOROTHY: It soaks up whatever soap you use. |
| S44 | 15 | `S14c_V_S44` | 4 s | 3,2 s | — | — | BG_B_BOXES, PROP_SILICONE | DOROTHY: The minute it gets hot, out it comes. |
| S45 | 15 | `S14c_T_S45` | 6 s | 2,1 s | 2.4 | = đầu | BG_B_BOXES, CS_GLORIA_2 | GLORIA: But I can't taste it. |
| S46 | 15 | `S14c_T_S46` | 6 s | 3,7 s | 4.0 | = đầu | BG_B_BOXES, CS_DOROTHY | DOROTHY: Neither could I. Cook's always the last to notice. |
| S47 | 16 | `S14c_T_S47` | 6 s | 4,2 s | 4.8 | = đầu | BG_B_BOXES, CS_DOROTHY, PROP_SILICONE | DOROTHY: They tested silicone baking pans. In the oven, chemicals leached out. |
| S48 | 16 | `S14c_V_S48` | 4 s | 3,3 s | — | — | BG_B_BOXES, CS_GLORIA_2, CS_DOROTHY | DOROTHY: Some of them are linked to hormone disruption. |
| S49 | 16 | `S14c_V_S49` | 4 s | 1,8 s | — | — | IMG_ACA_TOWEL | (câm) |
| S50 | 16 | `S14c_T_S50` | 6 s | 3,1 s | 3.6 | = đầu | BG_B_BOXES, CS_DOROTHY, IMG_ACA_SET | DOROTHY: I threw all mine out and got these. |
| S51 | 17 | `S14c_T_S51` | 6 s | 3,2 s | 3.6 | = đầu | BG_B_BOXES, CS_GLORIA_2, IMG_ACA_SET | GLORIA: Wood? The cheap ones bleed in the pot. |
| S52 | 17 | `S14c_T_S52` | 6 s | 2,4 s | 2.8 | = đầu | BG_B_BOXES, CS_DOROTHY | DOROTHY: That's the finish, not the wood. |
| S53 | 17 | `S14c_V_S53` | 6 s | 4,7 s | — | — | IMG_ACA_MACRO | DOROTHY: Every piece is one block of wood. No glue. Nothing painted on. |
| S54 | 17 | `S14c_T_S54` | 6 s | 3,6 s | 4.0 | — | BG_B_BOXES, CS_DOROTHY | DOROTHY: They're called Acawood. I just texted you the link. |
| S56 | 18 | `S14c_T_S56` | 6 s | 2,2 s | 3.0 | — | BG_B_BOXES, CS_DOROTHY, IMG_ACA_SET | DOROTHY: Keep these till yours come. |
| S57 | 18 | `S14c_T_S57` | 6 s | 2,4 s | 3.4 | — | BG_B_BOXES, CS_TERRANCE_2 | TERRANCE: Movers come Saturday at nine, Mama. |
| S58 | 18 | `S14c_T_S58` | 6 s | 1,3 s | 1.6 | = đầu | BG_B_BOXES, CS_GLORIA_2, PROP_SILICONE | GLORIA: Smell this first. |
| S59 | 18 | `S14c_T_S59` | 6 s | 2,5 s | 2.8 | = đầu | BG_B_BOXES, CS_TERRANCE_2 | TERRANCE: Mama. This isn't about a SPATULA. |
| S60 | 19 | `S14c_T_S60` | 6 s | 1,4 s | 1.6 | = đầu | BG_B_BOXES, CS_GLORIA_2 | GLORIA: Smell it, Terrance. |
| S61 | 19 | `S14c_V_S61` | 4 s | 1,2 s | — | — | BG_B_BOXES, CS_TERRANCE_2, CS_GLORIA_2, PROP_SILICONE | (câm) |
| S62 | 19 | `S14c_T_S62` | 6 s | 1,4 s | 1.6 | = đầu | BG_B_BOXES, CS_TERRANCE_2, PROP_SILICONE | TERRANCE: That's dish soap. |
| S63 | 19 | `S14c_T_S63` | 6 s | 3,3 s | 3.6 | = đầu | BG_B_BOXES, CS_GLORIA_2, IMG_ACA_SET | GLORIA: Now Dorothy's. She cooks with it every day. |
| S64 | 20 | `S14c_T_S64` | 6 s | 1,2 s | 1.4 | = đầu | BG_B_BOXES, CS_TERRANCE_2, IMG_ACA_SET | TERRANCE: Nothing. |
| S65 | 20 | `S14c_T_S65` | 6 s | 2,5 s | 2.8 | = đầu | BG_B_BOXES, CS_GLORIA_2 | GLORIA: One sniff. My nose is FINE. |
| S66 | 20 | `S14c_T_S66` | 6 s | 3,2 s | 4.2 | — | BG_B_BOXES, CS_GLORIA_2, CS_TERRANCE_2, PROP_SILICONE | GLORIA: You're the one who sent me that article. |
| S67 | 21 | `S14c_T_S67` | 6 s | 2,6 s | 3.2 | = đầu | BG_B_BOXES, CS_TERRANCE_2 | TERRANCE: Smelling's one thing, Mama. Tasting's another. |
| S68 | 21 | `S14c_T_S68` | 6 s | 3,6 s | 4.0 | = đầu | BG_B_BOXES, CS_GLORIA_2 | GLORIA: Friday night, I'm making my potato salad. Everybody comes. |
| S69 | 21 | `S14c_T_S69` | 8 s | 5,8 s | 6.4 | = đầu | BG_B_BOXES, CS_GLORIA_2 | GLORIA: If anybody tastes soap, I'll get in your car Saturday and never say a word. |
| S70 | 21 | `S14c_T_S70` | 6 s | 1,3 s | 0.8 | = đầu | BG_B_BOXES, CS_TERRANCE_2 | TERRANCE: Deal. |
| S71 | 22 | `S14c_V_S71` | 4 s | 1,8 s | — | — | BG_A_FRI, CS_GLORIA_3, CS_TERRANCE_3, CS_JADA_2, CS_WIFE, CS_GRANDSON, IMG_ACA_SET | (câm) |
| S72 | 22 | `S14c_T_S72` | 6 s | 3,1 s | 3.8 | — | BG_A_FRI, CS_GLORIA_3, CS_JADA_2, IMG_ACA_SET | GLORIA: Jada. You first. You're the honest one. |
| S73 | 23 | `S14c_V_S73` | 4 s | 2,0 s | — | — | BG_A_FRI, CS_JADA_2, CS_TERRANCE_3 | (câm) |
| S74 | 23 | `S14c_T_S74` | 6 s | 1,2 s | 0.8 | — | BG_A_FRI, CS_JADA_2 | JADA: Grandma. |
| S75 | 23 | `S14c_T_S75` | 6 s | 1,9 s | 2.0 | = đầu | BG_A_FRI, CS_JADA_2 | JADA: There's no soap. NONE. |
| S76 | 23 | `S14c_V_S76` | 4 s | 1,6 s | — | — | BG_A_FRI, CS_TERRANCE_3 | (câm) |
| S77 | 24 | `S14c_T_S77` | 6 s | 2,0 s | 2.0 | = đầu | BG_A_FRI, CS_TERRANCE_3 | TERRANCE: Mama. I'm so sorry. |
| S78 | 24 | `S14c_V_S78` | 4 s | 1,6 s | — | — | BG_A_FRI, CS_TERRANCE_3, PROP_BROCHURE | (câm) |
| S79 | 24 | `S14c_T_S79` | 6 s | 1,8 s | 2.0 | = đầu | BG_A_FRI, CS_GLORIA_3 | GLORIA: Unpack my bowls, Terrance. |
| S80 | 24 | `S14c_T_S80` | 6 s | 1,1 s | 0.8 | = đầu | BG_A_FRI, CS_JADA_2 | JADA: Seconds? |
| S81 | 25 | `S14c_V_S81` | 4 s | 1,8 s | — | — | BG_A_FRI, CS_TERRANCE_3, CS_JADA_2, CS_GLORIA_3, CS_WIFE, CS_GRANDSON, IMG_ACA_SET | (câm) |
| S82 | 25 | `S14c_T_S82` | 6 s | 4,7 s | 5.2 | = đầu | BG_B_CLEAR, CS_GLORIA_4, PROP_SILICONE, IMG_ACA_HOLDER | GLORIA: My son almost moved me out of my own kitchen. Over THIS. |
| S83 | 25 | `S14c_T_S83` | 6 s | 4,2 s | 4.8 | = đầu | BG_B_CLEAR, CS_GLORIA_4 | GLORIA: Before anybody tells you you've lost your touch, smell your spatula. |
| S84 | 26 | `S14c_T_S84` | 6 s | 3,9 s | 5.0 | — | BG_B_CLEAR, CS_GLORIA_4, PROP_SILICONE, IMG_ACA_HOLDER | GLORIA: If it smells like dish soap, so does your dinner. |
| S85 | 26 | `S14c_T_S85` | 8 s | 5,8 s | 6.8 | = đầu | BG_B_CLEAR, CS_GLORIA_4, CS_TERRANCE_4, IMG_ACA_SET | GLORIA: And if it's your wife's cooking, or your mama's? Smell HERS before you blame her. |
| S86 | 26 | `S14c_T_S86` | 8 s | 5,7 s | 6.4 | = đầu | BG_B_CLEAR, CS_GLORIA_4, IMG_ACA_HOLDER | GLORIA: Mine are Acawood now. Seven pieces, each one cut from a single block of wood. |
| S87 | 27 | `S14c_V_S87` | 6 s | 5,5 s | — | — | BG_B_CLEAR, IMG_ACA_SET, IMG_WATERTEST | GLORIA: Nothing on them but oil or wax. Here's one in hot water. Still clear. |
| S88 | 27 | `S14c_V_S88` | 4 s | 1,7 s | — | — | BG_B_CLEAR, CS_GLORIA_4, IMG_ACA_HOLDER | GLORIA: Hand wash, dry, done. |
| S89 | 27 | `S14c_T_S89` | 8 s | 6,5 s | 5.6 | = đầu | BG_B_CLEAR, CS_GLORIA_4, IMG_ACA_HOLDER | GLORIA: Eighty-nine ninety-five with the holder. Free shipping in the U.S., and ninety-day returns. |
| S90 | 27 | `S14c_T_S90` | 6 s | 3,9 s | 4.0 | — | BG_B_CLEAR, CS_GLORIA_4 | GLORIA: The link's right below. And my kitchen? Still MINE. |

## 7. Rủi ro / cần Nam kiểm

- **Mâu thuẫn cần Nam chốt:** skill toby-workflow (21/10) ghi `quantity 1` mọi node; chat cũ chốt ảnh x4, video x2. Bản này theo chat (x2 video = gấp đôi credit video). Muốn quay về x1 thì báo Claude, hoặc sửa số lượng trên node video.
- Prompt clip nói 374–472 từ, clip câm 222–309 từ: dài hơn mức 180–300 của doc 25 vì giữ nguyên khối Object lock (skill: clip có khối khóa vật thể tới ~600 từ vẫn chạy tốt, S12 v3).
- 32 clip nói không có khung cuối (đổi trạng thái): nếu trôi mặt/đồ thì báo, Claude tách thành clip nói giữ dáng + clip động tác.
- Nhịp dựng: trung bình 2,65 s/shot (gần Titanox ~2,7 s). 5 shot dài hơn 5 s, dễ thành cảnh đứng: S89 6,5 s, S85 5,8 s, S69 5,8 s, S86 5,7 s, S87 5,5 s → khi dựng chia đôi bằng một lần punch-in hoặc chèn b-roll giữa câu.
- Hai bà cùng tóc bạc ngắn: phân biệt bằng tông da (Dorothy sẫm hơn), mặt (Gloria tròn, Dorothy dài), kính (Gloria treo dây trước ngực, Dorothy đeo trên mặt), dáng (Gloria đầy đặn, Dorothy cao gầy). Sheet ra giống nhau thì báo Claude.
- File clip đã chia nhỏ cỡ 0B. Nếu file 01 (9 KB) vẫn không import được thì nguyên nhân là định dạng node video: gửi Claude dòng báo lỗi và một workflow cũ có node video Omni đã chạy được (menu ⋮ → Export) để so từng trường.
- Tên trường lấy theo mục 6 của skill (chưa có file export mẫu trong phiên này). Node `download` đã bỏ trường thừa `download`.
- Chưa đọc được Doc 56, 25, 47, 63, 72, 80 và Toby Flow 01, 02 (phiên cloud không có Projects); nên rà lại theo checklist Doc 56.
- Claim: "hormone disruption" đã duyệt; Meta từ chối thì thay "Ones you don't want in your food." (chỉ đổi file giọng S48, clip câm không phải gen lại).
- Nhân vật AI: bật nhãn nội dung AI khi chạy ads.
