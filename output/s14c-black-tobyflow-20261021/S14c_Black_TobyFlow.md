# S14c We Talked About This (bản da đen) — Workflow TobyFlow (21-10)

Nguồn: `Editor_Script14_WeTalkedAboutThis_Black_Acawood.docx` (bản 4, sau CD review). Làm theo skill toby-workflow: Nano Banana Pro cho ảnh, **Omni 1.1 Flash** (Frames) cho mọi clip.

## 1. Tóm tắt

- **98 clip** (74 T_ có thoại, 24 V_ câm). Không còn node `TAI`: bật **Auto Download** trong Settings của Toby, mỗi clip tự tải 1080p vào thư mục theo tên node clip.
- **Setup 3 file (0A, 0B, 0C) + 6 file khung (F1–F6) + 6 file clip (V1–V6), chia theo cảnh.** 0A: sheet nhân vật gốc, đạo cụ, 4 ảnh nền gốc. 0B: sheet đổi đồ và 4 trạng thái khác của cùng hai căn phòng, sửa từ ảnh gốc ở 0A. 0C: ảnh mẫu bàn tiệc (đủ 7 người ngồi đúng chỗ, cùng góc máy với ảnh nền phòng ăn), dùng làm tham chiếu cho mọi khung bàn ăn. File F chỉ tạo khung đầu `S14c_F_<cảnh>` (ảnh x4); Nam chọn 1 khung đạt, tải vào node `IMG_F_<cảnh>` của file V; file V chỉ có clip. Không node nào lấy ảnh từ node tạo trong cùng file (cách Script 11: file 04b chỉ có clip, khung tải vào node Album F_).
- Mỗi file ≤ 97 KB và ≤ 85 node (file 04b Script 11 của Nam: 96 KB / 82 node vẫn import được). Node video viết đúng định dạng file Toby cũ của Nam: `video_duration` dạng "6s", `download_resolution` "1080p", có `prompt_mode`/`ref_mode` (bản trước ghi số 6 và "1k" nên Toby không import được); khung nối vào `frame_1` + `frame_1_source`.
- **Nhân vật (22/10):** viết lại theo nghiên cứu gia đình Mỹ da đen, chi tiết ở `S14c_Black_NhanVat.md`. Sheet đổi đồ chuyển sang file 0B (lấy sheet gốc từ 0A) vì bản cũ nối trong cùng file nên ra người lạ.
- **Số lượng:** node ảnh x4 (không tốn credit), node video x2 (98 clip → 196 lượt video).
- **Clip nói diễn như phim (Nam 22/10):** cả 74 clip nói chỉ có khung đầu (frame_1), không còn khung cuối giữ dáng. 42 clip trước đây giữ dáng được viết lại hành động: một nhịp chính trong giây đầu, cử chỉ theo từng cụm lời, người nghe trong khung phản ứng, một nhịp im lặng cuối clip. Dòng Face cho mọi clip nói đổi từ "understated" sang biểu cảm rõ, có cử chỉ, không lố. Đồ đang cầm đi theo tay thay vì giữ nguyên góc.
- **Bàn ăn cố định (Nam 23/10, sau lượt F1):** một sơ đồ chỗ ngồi cho cả bữa sinh nhật và bữa thứ Sáu (docx: Gloria đầu bàn, Terrance bên phải bà, Jada ngay cạnh Terrance, vợ và con út đối diện; thứ Sáu đúng những người đó, đúng chỗ cũ). Chỉ 7 người: Gloria, Terrance, vợ, Jada, cậu bé (chỉ thấy tay), bà dì và ông chú (2 họ hàng docx ghi ở hậu cảnh, giờ tả cố định). Túi quà chỉ ở tủ buffet, brochure đi đúng theo từng cảnh, chưa có bánh kem trên bàn. Mỗi khung bàn ăn ghi rõ máy đặt ở đâu, ai ở trong khung, sau lưng ai là gì. Sơ đồ ở mục 3.
- **Đổi gì so với bản trước:** 0A, 0B giữ nguyên. Thêm 0C. Khung: F1 (C-1 → S08): chạy lại hết; F2 (S09 → S19): không đổi, khung đã có dùng tiếp; F3 (S20 → S41): chỉ chạy lại S21, S31, S32; F4 (S42 → S70): chỉ chạy lại S50, S54; F5 (D-2 → S81): chỉ chạy lại S71, S72, S73, S74, S75, S76, S77, S79, S80, S81; F6 (S82 → S90): không đổi, khung đã có dùng tiếp. Clip: import lại cả 6 file V (chia theo cảnh như F), xoá V cũ.
- Đã đối chiếu với luật trong chat cũ của Nam (xem mục 1b và `references/toby-flow-rules-nam.md`). **0A, 0B giữ nguyên** (không import lại). 9 file clip cũ 01–09 bỏ hết, thay bằng F1–F6 và V1–V6.
- File import: `toby/workflow_S14c_0A_Setup.json`, `toby/workflow_S14c_0B_DoiDo.json`, `toby/workflow_S14c_0C_BanAn.json`, `toby/workflow_S14c_F1.json` … `F6.json`, `toby/workflow_S14c_V1.json` … `V6.json`; sửa riêng bếp buổi sáng: `toby/fix/workflow_S14c_0A2_SuaBepSang.json`. Payload `create_workflow` cho Toby MCP (Claude Desktop): `toby/mcp/`. Kèm `S14c_Black_prompt_pack.txt` và 6 SRT (H1, A–E).
- **Chưa tạo trên Toby, chưa chạy gì.**

## 1b. Đã sửa theo luật Nam (21–23/10)

| Luật | Bản trước | Bản này |
|---|---|---|
| Ảnh x4, video x2 | quantity 1 mọi node | 120 node ảnh x4, 98 node video x2 (skill toby-workflow vẫn ghi quantity 1, xem mục 7) |
| Clip nói không cần giữ dáng, nhân vật diễn và có động tác như phim (Nam 22/10; thay luật cũ "cùng một ảnh vào frame_1 và frame_2") | 42 clip nói giữ dáng (frame_2 = frame_1), hành động kiểu "đứng yên nói"; dòng Face "understated" | bỏ frame_2 cả 42 clip; viết lại hành động: nhịp chính trong giây đầu, cử chỉ theo lời, người nghe phản ứng, nhịp im lặng cuối; Face: biểu cảm rõ, có cử chỉ, không lố; không cử chỉ "sassy" |
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
| Khung F_ cũng phải đến từ file chạy trước (Nam chọn 1 trong 4) | 9 file clip: khung F_ tạo và nối thẳng vào clip trong cùng file → clip chạy trên khung chưa duyệt | 4 file khung F1–F4 (chỉ ảnh) + 4 file clip V1–V4; khung đã chọn tải vào `IMG_F_<cảnh>` |
| Chỗ ngồi cố định ở 2 bữa tối (Nam 23/10) | chỉ một câu "Seating" chung chung ở vài khung; khung cận không nói ai ngồi đâu → mỗi khung một kiểu | sơ đồ 7 ghế cố định + ảnh mẫu bàn ăn 0C làm tham chiếu cho mọi khung bàn ăn; khung rộng S08, S71, S81 dùng đúng góc máy của ảnh mẫu; khung cận ghi máy đặt bên kia bàn và sau lưng ai là gì |
| Không bịa người lạ vào bàn (Nam 23/10) | "two older relatives", "the rest of the family" không tả → model thêm người khác nhau mỗi khung | đúng 7 người; bà dì (em gái Gloria) và ông chú tả cố định, đồ sinh nhật và đồ thứ Sáu riêng; khung cận ghi "ai không được tả thì ở ngoài khung, không ai khác trong phòng" |
| Túi quà, brochure, bánh kem (Nam 23/10) | túi quà và brochure chỗ mỗi khung một khác | 3 túi quà chỉ trên tủ buffet (vàng giấy hồng, xanh nhạt, hồng hoa văn) như ảnh nền; brochure: dưới túi vàng (B-1, S04) → trên tay Gloria (S05, S07, S08) → quầy bếp tối đó (S16) → nóc thùng ở hành lang thứ Sáu (D-2, S78); S06 không có brochure trong khung; chưa có bánh kem ("till after cake") |
| Đồ của vợ Terrance | "nice dinner clothes" / "soft knit sweater" → đổi màu mỗi khung | sinh nhật: đúng bộ trong sheet của chị; thứ Sáu: áo len cam gỉ sắt |
| Hiên nhà Dorothy, điện thoại, trứng (rà 23/10) | ghế đu không nói ai ngồi đầu nào; "another handset"; nĩa trứng không rõ lấy đâu | Dorothy ngồi đầu ghế đu cạnh bàn nhỏ có ly cà phê, túi vải bên cạnh, Gloria đầu kia; điện thoại của Gloria trên quầy; Jada nếm trứng từ chảo |
| Rà soát độc lập cả kịch bản (23/10) | S05 nhìn xuống bàn thì lộ mặt cậu bé; B-1 vẽ thêm một bàn đầy người; hook C: Jada vừa nâng ly cảnh trước, cảnh sau đang nhai; hook B: Terrance và Jada đứng ở tủ buffet rồi tự ngồi lại ghế; bóng bay, tủ buffet đặt sau lưng Terrance trong khi Gloria đứng đúng chỗ đó; tối thứ Sáu tô salad lúc đặt xuống, lúc trên tay; S86 thành 8 món; túi vải Dorothy hai chỗ; S50 bộ gỗ nằm cạnh khăn | S05 chỉ thấy dãy dọc tường cửa vòm, dãy kia khuất sau lưng Gloria; B-1 không thấy bàn; C-1 Jada vẫn nhai, tay cầm nĩa, C-2 bố đang đứng; S02_B Terrance dẫn Jada về bàn, S03_B Gloria nhìn con vội về ghế; sau lưng Terrance là tường cửa vòm, tủ buffet ở phía anh nhìn; tô đặt giữa Jada và bố, S72 múc từ tô trên bàn rồi lùi về đầu bàn, S79 bà ngồi, S81 tô cạnh Terrance; S86 tay chỉ "phần còn lại của bộ"; túi vải đặt trên ghế đu ở S31–S32; S50 bộ gỗ nằm trên khăn; Jada có bình nước ở C-1, S72, S80 |
| Node video đúng định dạng file Toby của Nam (04b, 05 Script 11) | `video_duration` 6 (số), `download_resolution` "1k", thiếu `prompt_mode`/`ref_mode` → không import được | "6s", "1080p", `prompt_mode`/`ref_mode` "all"; khung vào `frame_1`; không node TAI, Auto Download tải 1080p |

## 2. Ảnh thật cần chuẩn bị

| Ảnh | Cần gì | Tải vào |
|---|---|---|
| `IMG_ACA_SET` | real product photo: the 7 Acawood utensils on white, straight + 3/4 | file F4, file F5, file F6 |
| `IMG_ACA_HOLDER` | real product photo: the full set standing in the round holder | file 0B, file F6 |
| `IMG_ACA_TOWEL` | real product photo, top view: 7 utensils laid in a row on the red-and-white checkered towel (start frame S49) | file V3 |
| `IMG_ACA_MACRO` | real macro photo: grain running unbroken from handle to head (start frame S53) | file V4 |
| `IMG_WATERTEST` | a still frame from the real hot-water test clip (water still clear) (ref for F_S87) | file F6 |

## 3. Các file và thứ tự làm

1. **`S14c_0A Setup nhan vat nen`** (26 node, chỉ ảnh, x4, không cần tải ảnh): 6 character sheet gốc (Gloria 1, Terrance 1, Jada 1, Dorothy, vợ Terrance, con gái Dorothy), sheet quần áo cậu bé (không người), 2 sheet đạo cụ, 4 ảnh nền gốc (`BG_A_BDAY`, `BG_B_MORNING`, `BG_C`, `BG_D`). Duyệt theo mục 6 của `S14c_Black_NhanVat.md`, xem ảnh treo tường và ảnh trên tủ lạnh đều là người da đen, chọn 1 ảnh mỗi node, **tải về máy**.
2. **`S14c_0B Doi do`** (28 node): tải 6 ảnh vào node `IMG_`: 3 sheet gốc (`IMG_CS_GLORIA_1`, `IMG_CS_TERRANCE_1`, `IMG_CS_JADA_1`), 2 ảnh nền gốc (`IMG_BG_A_BDAY`, `IMG_BG_B_MORNING`) và ảnh thật bộ Acawood trong ống (`IMG_ACA_HOLDER`) → chạy 7 sheet đổi đồ + 4 ảnh nền (`BG_A_FRI`, `BG_B_NIGHT`, `BG_B_BOXES`, `BG_B_CLEAR`) → chọn, tải về.
   Nếu đã chạy file sửa bếp `S14c_0A2 Sua bep buoi sang` và dùng ảnh `BG_B_MORNING_FIX`, thì ảnh đó là ảnh tải vào mọi node `IMG_BG_B_MORNING` (0B và file F).
3. **`S14c_0C Ban an mau`** (7 node, mới): tải 5 ảnh đã chọn ở 0A vào node `IMG_` (`IMG_BG_A_BDAY`, `IMG_CS_GLORIA_1`, `IMG_CS_TERRANCE_1`, `IMG_CS_JADA_1`, `IMG_CS_WIFE`) → chạy `MASTER_A_BDAY` (x4) → chọn 1 ảnh đúng sơ đồ dưới đây → tải về. Ảnh này tải vào node `IMG_MASTER_A_BDAY` ở F1 (tiệc sinh nhật) và F5 (tối thứ Sáu). Không ảnh nào đúng thì chạy lại 0C, đừng chạy F1/F5 với ảnh mẫu sai.
```
        Tường sau: cửa vòm ··· thìa dĩa gỗ treo tường ··· tủ buffet + 3 túi quà, bóng bay 71, băng rôn
              ┌────────────┬────────────┬────────────┐
              │   Bà dì    │    Jada    │  Terrance  │
  CUỐI BÀN    │            │            │            │   ĐẦU BÀN: Gloria
  (ghế trống) │   Ông chú  │ Vợ Terrance│ Cậu bé (chỉ│   (đứng/ngồi trước tủ buffet)
              │            │            │ thấy tay)  │
              └────────────┴────────────┴────────────┘
                     Máy quay chính (góc của ảnh nền BG_A_BDAY)
```
   Duyệt ảnh mẫu: Gloria đứng ở đầu bàn sát tủ buffet, cầm tô potato salad; dãy dọc tường có cửa vòm là Terrance (sát đầu bàn), Jada, bà dì; dãy gần máy là cậu bé (chỉ thấy bàn tay ở mép khung), vợ Terrance, ông chú; ghế cuối bàn trống; đúng 7 người, không ai lạ; túi quà chỉ trên tủ buffet; không bánh kem.
4. **Import thử `V1` ngay** (chưa cần ảnh, import không tốn gì) để chắc node video đã đúng định dạng. Vào được thì để đó, chưa chạy. Không vào được thì chụp dòng báo lỗi của Toby và export một workflow video mới nhất Nam chạy được (menu ⋮ → Export) gửi Claude.
5. **File khung F1 → F6** (chỉ ảnh, x4): tải ảnh đã chọn ở 0A/0B/0C vào node `IMG_` cùng tên (bỏ `IMG_` là ra tên node ở 0A/0B/0C) và ảnh thật theo bảng dưới → chạy hết → mỗi node `S14c_F_<cảnh>` chọn 1 ảnh đạt trong 4 (đúng mặt, tông da, đồ theo sheet; tay đủ ngón; không chữ; thùng trơn) → tải về (Auto Download lưu theo tên node).
6. **File clip V1 → V6**: tải khung đã chọn của `S14c_F_<cảnh>` vào node `IMG_F_<cảnh>` (S49, S53 dùng ảnh thật `IMG_ACA_TOWEL`, `IMG_ACA_MACRO`) → chạy hết; Auto Download tải clip 1080p. Có thể làm F1 → V1 xong rồi mới sang F2 → V2.
7. Có Claude Desktop + Toby MCP thì khỏi tải tay: Nam báo khung nào chọn, Claude đọc kết quả (`get_workflow`) rồi `update_node` gắn ảnh vào các node `IMG_` (MCP tạo tối đa 5 workflow/ngày).

| File | Workflow | Shot | KB | Node | Tạo | Tải ảnh vào node IMG_ |
|---|---|---|---|---|---|---|
| 0A | `S14c_0A Setup nhan vat nen` | character sheet gốc 7 nhân vật + 2 sheet đạo cụ + 4 ảnh nền gốc | 26.5 | 26 | — |  |
| 0B | `S14c_0B Doi do` | 7 sheet đổi đồ (Gloria 2–4, Terrance 2–4, Jada 2) và 4 ảnh nền cùng phòng (phòng ăn thứ Sáu, bếp đêm, bếp đóng thùng, bếp vài tuần sau) sửa từ ảnh gốc ở 0A | 31.6 | 28 | — | `IMG_CS_GLORIA_1` ← `CS_GLORIA_1`<br>`IMG_CS_TERRANCE_1` ← `CS_TERRANCE_1`<br>`IMG_CS_JADA_1` ← `CS_JADA_1`<br>`IMG_BG_A_BDAY` ← `BG_A_BDAY`<br>`IMG_BG_B_MORNING` ← `BG_B_MORNING`<br>`IMG_ACA_HOLDER` ← ảnh thật |
| 0C | `S14c_0C Ban an mau` | ảnh mẫu bàn tiệc sinh nhật: đủ 7 người ngồi đúng chỗ, cùng góc máy với ảnh nền BG_A_BDAY | 9.3 | 7 | — | `IMG_BG_A_BDAY` ← `BG_A_BDAY`<br>`IMG_CS_GLORIA_1` ← `CS_GLORIA_1`<br>`IMG_CS_TERRANCE_1` ← `CS_TERRANCE_1`<br>`IMG_CS_JADA_1` ← `CS_JADA_1`<br>`IMG_CS_WIFE` ← `CS_WIFE` |
| F1 | `S14c_F1 Khung C-1 den S08` | C-1 → S08 | 80.6 | 41 | 16 khung | `IMG_BG_A_BDAY` ← `BG_A_BDAY` (0A)<br>`IMG_CS_TERRANCE_1` ← `CS_TERRANCE_1` (0A)<br>`IMG_CS_JADA_1` ← `CS_JADA_1` (0A)<br>`IMG_MASTER_A_BDAY` ← `MASTER_A_BDAY` (0C)<br>`IMG_PROP_BROCHURE` ← `PROP_BROCHURE` (0A)<br>`IMG_CS_GLORIA_1` ← `CS_GLORIA_1` (0A)<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE` (0A)<br>`IMG_CS_WIFE` ← `CS_WIFE` (0A)<br>`IMG_CS_GRANDSON` ← `CS_GRANDSON` (0A) |
| F2 | `S14c_F2 Khung S09 den S19` | S09 → S19 | 37.5 | 28 | 11 khung | `IMG_BG_B_NIGHT` ← `BG_B_NIGHT` (0B)<br>`IMG_CS_GLORIA_1` ← `CS_GLORIA_1` (0A)<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE` (0A)<br>`IMG_CS_TERRANCE_1` ← `CS_TERRANCE_1` (0A)<br>`IMG_PROP_BROCHURE` ← `PROP_BROCHURE` (0A)<br>`IMG_BG_C` ← `BG_C` (0A) |
| F3 | `S14c_F3 Khung S20 den S41` | S20 → S41 | 78.8 | 52 | 22 khung | `IMG_BG_B_MORNING` ← `BG_B_MORNING` (0A)<br>`IMG_CS_GLORIA_2` ← `CS_GLORIA_2` (0B)<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE` (0A)<br>`IMG_CS_JADA_1` ← `CS_JADA_1` (0A)<br>`IMG_BG_B_BOXES` ← `BG_B_BOXES` (0B)<br>`IMG_BG_D` ← `BG_D` (0A)<br>`IMG_CS_DOROTHY` ← `CS_DOROTHY` (0A)<br>`IMG_CS_FRIEND_DAUGHTER` ← `CS_FRIEND_DAUGHTER` (0A) |
| F4 | `S14c_F4 Khung S42 den S70` | S42 → S70 | 92.5 | 58 | 26 khung | `IMG_BG_B_BOXES` ← `BG_B_BOXES` (0B)<br>`IMG_CS_GLORIA_2` ← `CS_GLORIA_2` (0B)<br>`IMG_CS_DOROTHY` ← `CS_DOROTHY` (0A)<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE` (0A)<br>`IMG_ACA_SET` ← ảnh thật<br>`IMG_CS_TERRANCE_2` ← `CS_TERRANCE_2` (0B) |
| F5 | `S14c_F5 Khung D-2 den S81` | D-2 → S81 | 64.1 | 33 | 12 khung | `IMG_BG_A_FRI` ← `BG_A_FRI` (0B)<br>`IMG_CS_TERRANCE_3` ← `CS_TERRANCE_3` (0B)<br>`IMG_PROP_BROCHURE` ← `PROP_BROCHURE` (0A)<br>`IMG_CS_GLORIA_3` ← `CS_GLORIA_3` (0B)<br>`IMG_CS_JADA_2` ← `CS_JADA_2` (0B)<br>`IMG_CS_WIFE` ← `CS_WIFE` (0A)<br>`IMG_CS_GRANDSON` ← `CS_GRANDSON` (0A)<br>`IMG_ACA_SET` ← ảnh thật<br>`IMG_MASTER_A_BDAY` ← `MASTER_A_BDAY` (0C) |
| F6 | `S14c_F6 Khung S82 den S90` | S82 → S90 | 39.8 | 25 | 9 khung | `IMG_BG_B_CLEAR` ← `BG_B_CLEAR` (0B)<br>`IMG_CS_GLORIA_4` ← `CS_GLORIA_4` (0B)<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE` (0A)<br>`IMG_ACA_HOLDER` ← ảnh thật<br>`IMG_CS_TERRANCE_4` ← `CS_TERRANCE_4` (0B)<br>`IMG_ACA_SET` ← ảnh thật<br>`IMG_WATERTEST` ← ảnh thật |
| V1 | `S14c_V1 Clip C-1 den S08` | C-1 → S08 | 66.3 | 48 | 16 clip | 16 khung: `IMG_F_<cảnh>` ← khung đã chọn `S14c_F_<cảnh>` (file F1) |
| V2 | `S14c_V2 Clip S09 den S29` | S09 → S29 | 81.6 | 63 | 21 clip | 21 khung: `IMG_F_<cảnh>` ← khung đã chọn `S14c_F_<cảnh>` (file F2, F3) |
| V3 | `S14c_V3 Clip S30 den S50` | S30 → S50 | 82.9 | 63 | 21 clip | 20 khung: `IMG_F_<cảnh>` ← khung đã chọn `S14c_F_<cảnh>` (file F3, F4)<br>`IMG_ACA_TOWEL` ← ảnh thật |
| V4 | `S14c_V4 Clip S51 den S70` | S51 → S70 | 78.7 | 57 | 19 clip | 18 khung: `IMG_F_<cảnh>` ← khung đã chọn `S14c_F_<cảnh>` (file F4)<br>`IMG_ACA_MACRO` ← ảnh thật |
| V5 | `S14c_V5 Clip D-2 den S81` | D-2 → S81 | 45.4 | 36 | 12 clip | 12 khung: `IMG_F_<cảnh>` ← khung đã chọn `S14c_F_<cảnh>` (file F5) |
| V6 | `S14c_V6 Clip S82 den S90` | S82 → S90 | 37.9 | 27 | 9 clip | 9 khung: `IMG_F_<cảnh>` ← khung đã chọn `S14c_F_<cảnh>` (file F6) |

Tổng số lần tải ảnh nếu làm tay: 154 (0B 6, 0C 5, file khung 45, file clip 98).

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
- Thẻ chữ thời gian: S28 dùng **THE FOLLOWING SUNDAY** như storyboard (mục 4 docx ghi SUNDAY, dễ hiểu nhầm là sáng hôm sau, mà sáng hôm sau đã là Chủ nhật). Đề xuất thêm thẻ **A FEW DAYS LATER** ở S27 (docx chỉ ghi trong mô tả shot) để người xem theo kịp mốc hai tuần.

## 6. Bảng clip

Shot dựng = mốc cắt khi dựng (storyboard). Clip dài hơn để nhân vật nói hết câu; cắt phần lặng.

Clip chỉ có khung đầu (frame_1), không khung cuối: nhân vật diễn tự do. Mỗi clip ra 2 bản, chọn bản diễn đạt và giữ đúng mặt, đúng đồ.

| Shot | Khung → Clip | Node clip | Clip | Shot dựng | Lời xong lúc | Ảnh đính khung (Image 1..n) | Lời |
|---|---|---|---|---|---|---|---|
| A-1 | F1 → V1 | `S14c_T_A1` | 6 s | — | 4.4 | BG_A_BDAY, CS_JADA_1, CS_TERRANCE_1, CS_GLORIA_1, MASTER_A_BDAY | JADA: Dad. It's the soap thing again. I can't eat this. |
| B-1 | F1 → V1 | `S14c_T_B1` | 6 s | — | 3.6 | BG_A_BDAY, CS_TERRANCE_1, CS_JADA_1, PROP_BROCHURE, MASTER_A_BDAY | JADA: You're giving her THAT? Over the soap thing? |
| C-1 | F1 → V1 | `S14c_T_C1` | 6 s | — | 2.8 | BG_A_BDAY, CS_TERRANCE_1, CS_JADA_1, MASTER_A_BDAY | TERRANCE: To Mama. Seventy-one and still cooking. |
| C-2 | F1 → V1 | `S14c_T_C2` | 6 s | — | 2.4 | BG_A_BDAY, CS_JADA_1, MASTER_A_BDAY | JADA: Sorry. It's the soap thing. |
| D-2 | F5 → V5 | `S14c_V_D2` | 4 s | — | — | BG_A_FRI, CS_TERRANCE_3, PROP_BROCHURE | (câm) |
| E-2 | F1 → V1 | `S14c_T_E2` | 6 s | — | 3.6 | BG_A_BDAY, CS_JADA_1, MASTER_A_BDAY | JADA: Dad, I can't. It's the soap thing. |
| S01 | F1 → V1 | `S14c_T_S01` | 6 s | 3,5 s | 4.0 | BG_A_BDAY, CS_GLORIA_1, CS_JADA_1, CS_TERRANCE_1, PROP_SILICONE, MASTER_A_BDAY | JADA: Grandma, why does everything you make taste like SOAP? |
| S02 | F1 → V1 | `S14c_T_S02` | 6 s | 2,2 s | 2.4 | BG_A_BDAY, CS_TERRANCE_1, CS_JADA_1, MASTER_A_BDAY | TERRANCE: Jada. We TALKED about this. |
| S02_B | F1 → V1 | `S14c_T_S02_B` | 6 s | 2,2 s | 2.4 | BG_A_BDAY, CS_TERRANCE_1, CS_JADA_1, MASTER_A_BDAY | TERRANCE: Jada. We TALKED about this. |
| S02_C | F1 → V1 | `S14c_T_S02_C` | 6 s | 2,2 s | 2.4 | BG_A_BDAY, CS_TERRANCE_1, CS_JADA_1, MASTER_A_BDAY | TERRANCE: Jada. We TALKED about this. |
| S03 | F1 → V1 | `S14c_T_S03` | 6 s | 1,7 s | 1.6 | BG_A_BDAY, CS_GLORIA_1, PROP_SILICONE, MASTER_A_BDAY | GLORIA: Talked about what? |
| S03_B | F1 → V1 | `S14c_T_S03_B` | 6 s | 1,7 s | 1.6 | BG_A_BDAY, CS_GLORIA_1, MASTER_A_BDAY | GLORIA: Talked about what? |
| S04 | F1 → V1 | `S14c_V_S04` | 4 s | 1,5 s | — | BG_A_BDAY, PROP_BROCHURE | (câm) |
| S05 | F1 → V1 | `S14c_T_S05` | 6 s | 2,5 s | 2.8 | BG_A_BDAY, CS_GLORIA_1, PROP_BROCHURE, MASTER_A_BDAY | GLORIA: You're putting me in a HOME? |
| S06 | F1 → V1 | `S14c_T_S06` | 6 s | 3,3 s | 3.6 | BG_A_BDAY, CS_TERRANCE_1, MASTER_A_BDAY | TERRANCE: Mama. We were gonna wait till after cake. |
| S07 | F1 → V1 | `S14c_T_S07` | 6 s | 1,6 s | 1.6 | BG_A_BDAY, CS_GLORIA_1, PROP_BROCHURE, MASTER_A_BDAY | GLORIA: On my BIRTHDAY? |
| S08 | F1 → V1 | `S14c_V_S08` | 4 s | 1,6 s | — | BG_A_BDAY, CS_GLORIA_1, CS_TERRANCE_1, CS_JADA_1, CS_WIFE, CS_GRANDSON, PROP_BROCHURE, MASTER_A_BDAY | (câm) |
| S09 | F2 → V2 | `S14c_T_S09` | 6 s | 3,3 s | 4.2 | BG_B_NIGHT, CS_GLORIA_1, PROP_SILICONE | GLORIA: Soap. You think I can't rinse a POT? |
| S10 | F2 → V2 | `S14c_T_S10` | 6 s | 2,9 s | 3.2 | BG_B_NIGHT, CS_TERRANCE_1 | TERRANCE: Every dinner since Christmas. We've all noticed. |
| S11 | F2 → V2 | `S14c_T_S11` | 6 s | 1,7 s | 1.6 | BG_B_NIGHT, CS_GLORIA_1 | GLORIA: All of you? |
| S12 | F2 → V2 | `S14c_T_S12` | 6 s | 2,9 s | 3.2 | BG_B_NIGHT, CS_TERRANCE_1, CS_GLORIA_1 | TERRANCE: Taste buds go as you get older. |
| S13 | F2 → V2 | `S14c_T_S13` | 8 s | 4,9 s | 5.6 | BG_B_NIGHT, CS_TERRANCE_1 | TERRANCE: But if you can't taste soap, what happens when you can't smell gas? |
| S14 | F2 → V2 | `S14c_T_S14` | 6 s | 3,5 s | 3.6 | BG_B_NIGHT, CS_GLORIA_1 | GLORIA: I've cooked in this kitchen for forty-two years. |
| S15 | F2 → V2 | `S14c_T_S15` | 6 s | 4,4 s | 4.8 | BG_B_NIGHT, CS_TERRANCE_1 | TERRANCE: I know. That's why I don't want you in it alone. |
| S16 | F2 → V2 | `S14c_T_S16` | 8 s | 4,7 s | 5.8 | BG_B_NIGHT, CS_TERRANCE_1, PROP_BROCHURE | TERRANCE: Wrenfield has a unit opening this month. I put down a deposit. |
| S17 | F2 → V2 | `S14c_T_S17` | 6 s | 1,8 s | 1.6 | BG_B_NIGHT, CS_GLORIA_1 | GLORIA: You already PAID? |
| S18 | F2 → V2 | `S14c_V_S18` | 4 s | 3,0 s | — | BG_C, CS_TERRANCE_1 | TERRANCE: No, she won't fight it. She's — slipping. |
| S19 | F2 → V2 | `S14c_V_S19` | 4 s | 1,4 s | — | BG_C, CS_GLORIA_1 | (câm) |
| S20 | F3 → V2 | `S14c_V_S20` | 4 s | 1,5 s | — | BG_B_MORNING, CS_GLORIA_2, PROP_SILICONE | (câm) |
| S21 | F3 → V2 | `S14c_T_S21` | 6 s | 1,8 s | 2.6 | BG_B_MORNING, CS_JADA_1 | JADA: Grandma, it's still there. |
| S22 | F3 → V2 | `S14c_T_S22` | 6 s | 4,1 s | 4.4 | BG_B_MORNING, CS_GLORIA_2, PROP_SILICONE | GLORIA: I scrubbed that pan THREE times. New soap. New sponge. |
| S23 | F3 → V2 | `S14c_T_S23` | 6 s | 2,5 s | 3.4 | BG_B_MORNING, CS_GLORIA_2 | GLORIA: And I can't taste a THING. |
| S24 | F3 → V2 | `S14c_T_S24` | 6 s | 2,4 s | 2.4 | BG_B_MORNING, CS_GLORIA_2 | GLORIA: Jada, am I losing it? |
| S25 | F3 → V2 | `S14c_V_S25` | 4 s | 1,4 s | — | BG_B_MORNING, CS_JADA_1, CS_GLORIA_2 | (câm) |
| S26 | F3 → V2 | `S14c_V_S26` | 4 s | 2,0 s | — | BG_B_MORNING, CS_JADA_1, CS_GLORIA_2 | JADA: I love you, Grandma. |
| S27 | F3 → V2 | `S14c_V_S27` | 4 s | 1,6 s | — | BG_B_BOXES, CS_GLORIA_2 | (câm) |
| S28 | F3 → V2 | `S14c_V_S28` | 4 s | 1,8 s | — | BG_D, CS_DOROTHY, CS_FRIEND_DAUGHTER, CS_GLORIA_2 | (câm) |
| S29 | F3 → V2 | `S14c_T_S29` | 6 s | 3,2 s | 4.2 | BG_D, CS_GLORIA_2 | GLORIA: Wasn't she the one PUSHING you into Wrenfield? |
| S30 | F3 → V3 | `S14c_T_S30` | 6 s | 1,3 s | 1.6 | BG_D, CS_DOROTHY | DOROTHY: She sure was. |
| S31 | F3 → V3 | `S14c_T_S31` | 6 s | 4,0 s | 4.4 | BG_D, CS_GLORIA_2, CS_DOROTHY | GLORIA: Now she's here every Sunday, taking plates home. What CHANGED? |
| S32 | F3 → V3 | `S14c_T_S32` | 6 s | 3,3 s | 4.2 | BG_D, CS_DOROTHY | DOROTHY: She told me my cooking tasted like soap. |
| S33 | F3 → V3 | `S14c_V_S33` | 4 s | 1,1 s | — | BG_D, CS_GLORIA_2 | (câm) |
| S34 | F3 → V3 | `S14c_T_S34` | 6 s | 1,4 s | 1.2 | BG_D, CS_GLORIA_2 | GLORIA: Mine too. |
| S35 | F3 → V3 | `S14c_T_S35` | 6 s | 1,8 s | 2.0 | BG_D, CS_DOROTHY | DOROTHY: Show me your kitchen. |
| S36 | F3 → V3 | `S14c_T_S36` | 6 s | 1,7 s | 2.0 | BG_B_BOXES, CS_DOROTHY, PROP_SILICONE | DOROTHY: When'd you buy these? |
| S37 | F3 → V3 | `S14c_T_S37` | 6 s | 4,0 s | 4.4 | BG_B_BOXES, CS_GLORIA_2 | GLORIA: After Thanksgiving. Terrance sent me an article about black plastic. |
| S38 | F3 → V3 | `S14c_T_S38` | 6 s | 2,5 s | 2.8 | BG_B_BOXES, CS_DOROTHY | DOROTHY: And when did the soap start? |
| S39 | F3 → V3 | `S14c_V_S39` | 4 s | 1,0 s | — | BG_B_BOXES, CS_GLORIA_2 | (câm) |
| S40 | F3 → V3 | `S14c_T_S40` | 6 s | 1,3 s | 1.4 | BG_B_BOXES, CS_GLORIA_2 | GLORIA: Christmas. |
| S41 | F3 → V3 | `S14c_T_S41` | 6 s | 1,2 s | 1.2 | BG_B_BOXES, CS_DOROTHY, CS_GLORIA_2, PROP_SILICONE | DOROTHY: Smell it. |
| S42 | F4 → V3 | `S14c_T_S42` | 6 s | 1,8 s | 2.6 | BG_B_BOXES, CS_GLORIA_2, CS_DOROTHY, PROP_SILICONE | GLORIA: That's my DISH soap. |
| S43 | F4 → V3 | `S14c_T_S43` | 6 s | 2,8 s | 3.2 | BG_B_BOXES, CS_DOROTHY, PROP_SILICONE | DOROTHY: It soaks up whatever soap you use. |
| S44 | F4 → V3 | `S14c_V_S44` | 4 s | 3,2 s | — | BG_B_BOXES, PROP_SILICONE | DOROTHY: The minute it gets hot, out it comes. |
| S45 | F4 → V3 | `S14c_T_S45` | 6 s | 2,1 s | 2.4 | BG_B_BOXES, CS_GLORIA_2 | GLORIA: But I can't taste it. |
| S46 | F4 → V3 | `S14c_T_S46` | 6 s | 3,7 s | 4.0 | BG_B_BOXES, CS_DOROTHY | DOROTHY: Neither could I. Cook's always the last to notice. |
| S47 | F4 → V3 | `S14c_T_S47` | 6 s | 4,2 s | 4.8 | BG_B_BOXES, CS_DOROTHY, PROP_SILICONE | DOROTHY: They tested silicone baking pans. In the oven, chemicals leached out. |
| S48 | F4 → V3 | `S14c_V_S48` | 4 s | 3,3 s | — | BG_B_BOXES, CS_GLORIA_2, CS_DOROTHY | DOROTHY: Some of them are linked to hormone disruption. |
| S49 | ảnh thật → V3 | `S14c_V_S49` | 4 s | 1,8 s | — | IMG_ACA_TOWEL | (câm) |
| S50 | F4 → V3 | `S14c_T_S50` | 6 s | 3,1 s | 3.6 | BG_B_BOXES, CS_DOROTHY, IMG_ACA_SET | DOROTHY: I threw all mine out and got these. |
| S51 | F4 → V4 | `S14c_T_S51` | 6 s | 3,2 s | 3.6 | BG_B_BOXES, CS_GLORIA_2, IMG_ACA_SET | GLORIA: Wood? The cheap ones bleed in the pot. |
| S52 | F4 → V4 | `S14c_T_S52` | 6 s | 2,4 s | 2.8 | BG_B_BOXES, CS_DOROTHY | DOROTHY: That's the finish, not the wood. |
| S53 | ảnh thật → V4 | `S14c_V_S53` | 6 s | 4,7 s | — | IMG_ACA_MACRO | DOROTHY: Every piece is one block of wood. No glue. Nothing painted on. |
| S54 | F4 → V4 | `S14c_T_S54` | 6 s | 3,6 s | 4.0 | BG_B_BOXES, CS_DOROTHY | DOROTHY: They're called Acawood. I just texted you the link. |
| S56 | F4 → V4 | `S14c_T_S56` | 6 s | 2,2 s | 3.0 | BG_B_BOXES, CS_DOROTHY, IMG_ACA_SET | DOROTHY: Keep these till yours come. |
| S57 | F4 → V4 | `S14c_T_S57` | 6 s | 2,4 s | 3.4 | BG_B_BOXES, CS_TERRANCE_2 | TERRANCE: Movers come Saturday at nine, Mama. |
| S58 | F4 → V4 | `S14c_T_S58` | 6 s | 1,3 s | 1.6 | BG_B_BOXES, CS_GLORIA_2, PROP_SILICONE | GLORIA: Smell this first. |
| S59 | F4 → V4 | `S14c_T_S59` | 6 s | 2,5 s | 3.4 | BG_B_BOXES, CS_TERRANCE_2 | TERRANCE: Mama. This isn't about a SPATULA. |
| S60 | F4 → V4 | `S14c_T_S60` | 6 s | 1,4 s | 1.6 | BG_B_BOXES, CS_GLORIA_2 | GLORIA: Smell it, Terrance. |
| S61 | F4 → V4 | `S14c_V_S61` | 4 s | 1,2 s | — | BG_B_BOXES, CS_TERRANCE_2, CS_GLORIA_2, PROP_SILICONE | (câm) |
| S62 | F4 → V4 | `S14c_T_S62` | 6 s | 1,4 s | 1.6 | BG_B_BOXES, CS_TERRANCE_2, PROP_SILICONE | TERRANCE: That's dish soap. |
| S63 | F4 → V4 | `S14c_T_S63` | 6 s | 3,3 s | 3.6 | BG_B_BOXES, CS_GLORIA_2, IMG_ACA_SET | GLORIA: Now Dorothy's. She cooks with it every day. |
| S64 | F4 → V4 | `S14c_T_S64` | 6 s | 1,2 s | 1.4 | BG_B_BOXES, CS_TERRANCE_2, IMG_ACA_SET | TERRANCE: Nothing. |
| S65 | F4 → V4 | `S14c_T_S65` | 6 s | 2,5 s | 2.8 | BG_B_BOXES, CS_GLORIA_2 | GLORIA: One sniff. My nose is FINE. |
| S66 | F4 → V4 | `S14c_T_S66` | 6 s | 3,2 s | 4.2 | BG_B_BOXES, CS_GLORIA_2, CS_TERRANCE_2, PROP_SILICONE | GLORIA: You're the one who sent me that article. |
| S67 | F4 → V4 | `S14c_T_S67` | 6 s | 2,6 s | 3.2 | BG_B_BOXES, CS_TERRANCE_2 | TERRANCE: Smelling's one thing, Mama. Tasting's another. |
| S68 | F4 → V4 | `S14c_T_S68` | 6 s | 3,6 s | 4.0 | BG_B_BOXES, CS_GLORIA_2 | GLORIA: Friday night, I'm making my potato salad. Everybody comes. |
| S69 | F4 → V4 | `S14c_T_S69` | 8 s | 5,8 s | 6.4 | BG_B_BOXES, CS_GLORIA_2 | GLORIA: If anybody tastes soap, I'll get in your car Saturday and never say a word. |
| S70 | F4 → V4 | `S14c_T_S70` | 6 s | 1,3 s | 1.4 | BG_B_BOXES, CS_TERRANCE_2 | TERRANCE: Deal. |
| S71 | F5 → V5 | `S14c_V_S71` | 4 s | 1,8 s | — | BG_A_FRI, CS_GLORIA_3, CS_TERRANCE_3, CS_JADA_2, CS_WIFE, CS_GRANDSON, IMG_ACA_SET, MASTER_A_BDAY | (câm) |
| S72 | F5 → V5 | `S14c_T_S72` | 6 s | 3,1 s | 3.8 | BG_A_FRI, CS_GLORIA_3, CS_JADA_2, CS_TERRANCE_3, IMG_ACA_SET, MASTER_A_BDAY | GLORIA: Jada. You first. You're the honest one. |
| S73 | F5 → V5 | `S14c_V_S73` | 4 s | 2,0 s | — | BG_A_FRI, CS_JADA_2, CS_TERRANCE_3, MASTER_A_BDAY | (câm) |
| S74 | F5 → V5 | `S14c_T_S74` | 6 s | 1,2 s | 0.8 | BG_A_FRI, CS_JADA_2, MASTER_A_BDAY | JADA: Grandma. |
| S75 | F5 → V5 | `S14c_T_S75` | 6 s | 1,9 s | 2.0 | BG_A_FRI, CS_JADA_2, MASTER_A_BDAY | JADA: There's no soap. NONE. |
| S76 | F5 → V5 | `S14c_V_S76` | 4 s | 1,6 s | — | BG_A_FRI, CS_TERRANCE_3, MASTER_A_BDAY | (câm) |
| S77 | F5 → V5 | `S14c_T_S77` | 6 s | 2,0 s | 2.0 | BG_A_FRI, CS_TERRANCE_3, MASTER_A_BDAY | TERRANCE: Mama. I'm so sorry. |
| S78 | F5 → V5 | `S14c_V_S78` | 4 s | 1,6 s | — | BG_A_FRI, CS_TERRANCE_3, PROP_BROCHURE | (câm) |
| S79 | F5 → V5 | `S14c_T_S79` | 6 s | 1,8 s | 2.0 | BG_A_FRI, CS_GLORIA_3, MASTER_A_BDAY | GLORIA: Unpack my bowls, Terrance. |
| S80 | F5 → V5 | `S14c_T_S80` | 6 s | 1,1 s | 0.8 | BG_A_FRI, CS_JADA_2, CS_TERRANCE_3, MASTER_A_BDAY | JADA: Seconds? |
| S81 | F5 → V5 | `S14c_V_S81` | 4 s | 1,8 s | — | BG_A_FRI, CS_TERRANCE_3, CS_JADA_2, CS_GLORIA_3, CS_WIFE, CS_GRANDSON, IMG_ACA_SET, MASTER_A_BDAY | (câm) |
| S82 | F6 → V6 | `S14c_T_S82` | 6 s | 4,7 s | 5.2 | BG_B_CLEAR, CS_GLORIA_4, PROP_SILICONE, IMG_ACA_HOLDER | GLORIA: My son almost moved me out of my own kitchen. Over THIS. |
| S83 | F6 → V6 | `S14c_T_S83` | 6 s | 4,2 s | 4.8 | BG_B_CLEAR, CS_GLORIA_4 | GLORIA: Before anybody tells you you've lost your touch, smell your spatula. |
| S84 | F6 → V6 | `S14c_T_S84` | 6 s | 3,9 s | 5.0 | BG_B_CLEAR, CS_GLORIA_4, PROP_SILICONE, IMG_ACA_HOLDER | GLORIA: If it smells like dish soap, so does your dinner. |
| S85 | F6 → V6 | `S14c_T_S85` | 8 s | 5,8 s | 6.8 | BG_B_CLEAR, CS_GLORIA_4, CS_TERRANCE_4, IMG_ACA_SET | GLORIA: And if it's your wife's cooking, or your mama's? Smell HERS before you blame her. |
| S86 | F6 → V6 | `S14c_T_S86` | 8 s | 5,7 s | 6.4 | BG_B_CLEAR, CS_GLORIA_4, IMG_ACA_HOLDER | GLORIA: Mine are Acawood now. Seven pieces, each one cut from a single block of wood. |
| S87 | F6 → V6 | `S14c_V_S87` | 6 s | 5,5 s | — | BG_B_CLEAR, IMG_ACA_SET, IMG_WATERTEST | GLORIA: Nothing on them but oil or wax. Here's one in hot water. Still clear. |
| S88 | F6 → V6 | `S14c_V_S88` | 4 s | 1,7 s | — | BG_B_CLEAR, CS_GLORIA_4, IMG_ACA_HOLDER | GLORIA: Hand wash, dry, done. |
| S89 | F6 → V6 | `S14c_T_S89` | 8 s | 6,5 s | 5.6 | BG_B_CLEAR, CS_GLORIA_4, IMG_ACA_HOLDER | GLORIA: Eighty-nine ninety-five with the holder. Free shipping in the U.S., and ninety-day returns. |
| S90 | F6 → V6 | `S14c_T_S90` | 6 s | 3,9 s | 4.0 | BG_B_CLEAR, CS_GLORIA_4 | GLORIA: The link's right below. And my kitchen? Still MINE. |

## 7. Rủi ro / cần Nam kiểm

- **Mâu thuẫn cần Nam chốt:** skill toby-workflow (21/10) ghi `quantity 1` mọi node; chat cũ chốt ảnh x4, video x2. Bản này theo chat (x2 video = gấp đôi credit video). Muốn quay về x1 thì báo Claude, hoặc sửa số lượng trên node video.
- Prompt clip nói 470–584 từ, clip câm 224–344 từ: dài hơn mức 180–300 của doc 25 vì giữ nguyên khối Object lock và khối People/da (skill: clip có khối khóa vật thể tới ~600 từ vẫn chạy tốt, S12 v3).
- Bỏ khung cuối thì mặt, đồ dễ trôi hơn khi nhân vật cử động nhiều: mỗi clip có 2 bản để chọn. Clip nào cả 2 bản đều trôi thì báo, Claude thêm lại khung cuối cho riêng clip đó hoặc bớt động tác.
- Nhịp dựng: trung bình 2,65 s/shot (gần Titanox ~2,7 s). 5 shot dài hơn 5 s, dễ thành cảnh đứng: S89 6,5 s, S85 5,8 s, S69 5,8 s, S86 5,7 s, S87 5,5 s → khi dựng chia đôi bằng một lần punch-in hoặc chèn b-roll giữa câu.
- Hai bà cùng tóc bạc ngắn: phân biệt bằng tông da (Dorothy sẫm hơn), mặt (Gloria tròn, Dorothy dài), kính (Gloria treo dây trước ngực, Dorothy đeo trên mặt), dáng (Gloria đầy đặn, Dorothy cao gầy). Sheet ra giống nhau thì báo Claude.
- Nếu V1 vẫn không import được: gửi Claude dòng báo lỗi và file export của một workflow video mới nhất Nam chạy được (menu ⋮ → Export) để so từng trường. File F chỉ có ảnh như 0A/0B nên sẽ vào.
- Trường node video theo file export 04b/05 (Script 11) của Nam; khung nối vào `frame_1` + `frame_1_source` theo luật Script 11 (thiếu frame_1 Toby báo "Chế độ video theo khung hình cần có ảnh tham chiếu"). Không còn node `TAI`.
- Tải tay: 98 khung vào file clip. Có Toby MCP thì Claude gắn hộ.
- Chưa đọc được Doc 56, 25, 47, 63, 72, 80 và Toby Flow 01, 02 (phiên cloud không có Projects); nên rà lại theo checklist Doc 56.
- Claim: "hormone disruption" đã duyệt; Meta từ chối thì thay "Ones you don't want in your food." (chỉ đổi file giọng S48, clip câm không phải gen lại).
- Nhân vật AI: bật nhãn nội dung AI khi chạy ads.
