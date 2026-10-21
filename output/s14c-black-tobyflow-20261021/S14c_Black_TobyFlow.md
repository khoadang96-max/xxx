# S14c We Talked About This (bản da đen) — Workflow TobyFlow (21-10)

Nguồn: `Editor_Script14_WeTalkedAboutThis_Black_Acawood.docx` (bản 4, sau CD review). Làm theo skill toby-workflow: Nano Banana Pro cho ảnh, **Omni 1.1 Flash** (Frames) cho mọi clip.

## 1. Tóm tắt

- **98 clip** (74 T_ có thoại, 24 V_ câm), mỗi clip có node `TAI` tải 1080p riêng.
- **Tách Setup + 9 file clip.** Bản một file (818 KB) và bản 5 phần (114–158 KB) không mở được trong Toby; Setup (42 KB) mở được. Mỗi file clip giờ ≤ 89 KB. Bản này phá luật "một kịch bản = một workflow" vì dung lượng.
- File import: `toby/workflow_S14c_0_Setup.json`, rồi `toby/workflow_S14c_01_HookCB.json` … `workflow_S14c_09_Close.json`. Payload `create_workflow` cho Toby MCP (Claude Desktop): `toby/mcp/`. Kèm `S14c_Black_prompt_pack.txt` và 6 SRT (H1, A–E).
- **Chưa tạo trên Toby, chưa chạy gì.**

## 2. Ảnh thật cần chuẩn bị

| Ảnh | Cần gì | Tải vào |
|---|---|---|
| `IMG_ACA_SET` | real product photo: the 7 Acawood utensils on white, straight + 3/4 | file 06, file 07, file 08, file 09 |
| `IMG_ACA_HOLDER` | real product photo: the full set standing in the round holder | file 0, file 09 |
| `IMG_ACA_TOWEL` | real product photo, top view: 7 utensils laid in a row on the red-and-white checkered towel (start frame S49) | file 06 |
| `IMG_ACA_MACRO` | real macro photo: grain running unbroken from handle to head (start frame S53) | file 06 |
| `IMG_WATERTEST` | a still frame from the real hot-water test clip (water still clear) (ref for F_S87) | file 09 |

## 3. Mười file và thứ tự làm

1. **`S14c_0 Setup`** (đã import được, 49 node, chỉ ảnh): chạy để có 14 character sheet (Gloria 4 bộ đồ, Terrance 4, Jada 2, Dorothy, vợ Terrance, cậu bé, con gái Dorothy), 2 sheet đạo cụ, 8 ảnh nền. Chọn bản đạt, **tải ảnh về máy**.
2. **Import file `01` trước** (hook C + B, 43 KB, cỡ bằng Setup). Mở được thì định dạng ổn → import tiếp 02–09. Không mở được thì lỗi nằm ở định dạng node clip/tải, không phải dung lượng: chụp màn hình lỗi gửi Claude.
3. Mỗi file có cột node `IMG_` bên trái: tải đúng ảnh vào đúng node theo bảng dưới (tên node = `IMG_` + tên node ở Setup).
4. Trong từng file: chạy `F_` (xem khung) → `T_/V_` → `TAI`.
5. Có Claude Desktop + Toby MCP thì khỏi tải tay: Claude đọc kết quả Setup (`get_workflow`) rồi `update_node` gắn ảnh vào các node `IMG_` (MCP tạo tối đa 5 workflow/ngày).

| File | Workflow | Shot | KB | Node | Clip | Tải ảnh vào node IMG_ |
|---|---|---|---|---|---|---|
| 0 | `S14c_0 Setup` | character sheet + đạo cụ + 8 ảnh nền | 42 | 49 | 0 | `IMG_ACA_HOLDER` ← ảnh thật |
| 01 | `S14c_01 Hook C B` | C-1 → S03_B | 43.4 | 35 | 6 | `IMG_BG_A_BDAY` ← `BG_A_BDAY`<br>`IMG_CS_TERRANCE_1` ← `CS_TERRANCE_1`<br>`IMG_CS_JADA_1` ← `CS_JADA_1`<br>`IMG_PROP_BROCHURE` ← `PROP_BROCHURE`<br>`IMG_CS_GLORIA_1` ← `CS_GLORIA_1` |
| 02 | `S14c_02 Sinh nhat` | A-1 → S08 | 72.1 | 58 | 10 | `IMG_BG_A_BDAY` ← `BG_A_BDAY`<br>`IMG_CS_JADA_1` ← `CS_JADA_1`<br>`IMG_CS_TERRANCE_1` ← `CS_TERRANCE_1`<br>`IMG_CS_GLORIA_1` ← `CS_GLORIA_1`<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE`<br>`IMG_PROP_BROCHURE` ← `PROP_BROCHURE`<br>`IMG_CS_WIFE` ← `CS_WIFE`<br>`IMG_CS_GRANDSON` ← `CS_GRANDSON` |
| 03 | `S14c_03 Bep dem - Hien dem` | S09 → S19 | 74.3 | 61 | 11 | `IMG_BG_B_NIGHT` ← `BG_B_NIGHT`<br>`IMG_CS_GLORIA_1` ← `CS_GLORIA_1`<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE`<br>`IMG_CS_TERRANCE_1` ← `CS_TERRANCE_1`<br>`IMG_PROP_BROCHURE` ← `PROP_BROCHURE`<br>`IMG_BG_C` ← `BG_C` |
| 04 | `S14c_04 Sang - Dong thung - Hien Dorothy` | S20 → S29 | 68.6 | 58 | 10 | `IMG_BG_B_MORNING` ← `BG_B_MORNING`<br>`IMG_CS_GLORIA_2` ← `CS_GLORIA_2`<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE`<br>`IMG_CS_JADA_1` ← `CS_JADA_1`<br>`IMG_BG_B_BOXES` ← `BG_B_BOXES`<br>`IMG_BG_D` ← `BG_D`<br>`IMG_CS_DOROTHY` ← `CS_DOROTHY`<br>`IMG_CS_FRIEND_DAUGHTER` ← `CS_FRIEND_DAUGHTER` |
| 05 | `S14c_05 Hien Dorothy - Co che` | S30 → S42 | 86.7 | 70 | 13 | `IMG_BG_D` ← `BG_D`<br>`IMG_CS_DOROTHY` ← `CS_DOROTHY`<br>`IMG_CS_GLORIA_2` ← `CS_GLORIA_2`<br>`IMG_BG_B_BOXES` ← `BG_B_BOXES`<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE` |
| 06 | `S14c_06 Co che - San pham - Loi cuoc` | S43 → S57 | 88.4 | 74 | 14 | `IMG_BG_B_BOXES` ← `BG_B_BOXES`<br>`IMG_CS_DOROTHY` ← `CS_DOROTHY`<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE`<br>`IMG_CS_GLORIA_2` ← `CS_GLORIA_2`<br>`IMG_ACA_TOWEL` ← ảnh thật<br>`IMG_ACA_SET` ← ảnh thật<br>`IMG_ACA_MACRO` ← ảnh thật<br>`IMG_CS_TERRANCE_2` ← `CS_TERRANCE_2` |
| 07 | `S14c_07 Loi cuoc` | S58 → S70 | 88.7 | 70 | 13 | `IMG_BG_B_BOXES` ← `BG_B_BOXES`<br>`IMG_CS_GLORIA_2` ← `CS_GLORIA_2`<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE`<br>`IMG_CS_TERRANCE_2` ← `CS_TERRANCE_2`<br>`IMG_ACA_SET` ← ảnh thật |
| 08 | `S14c_08 Thu Sau` | D-2 → S81 | 87.1 | 68 | 12 | `IMG_BG_A_FRI` ← `BG_A_FRI`<br>`IMG_PROP_BROCHURE` ← `PROP_BROCHURE`<br>`IMG_CS_GLORIA_3` ← `CS_GLORIA_3`<br>`IMG_CS_TERRANCE_3` ← `CS_TERRANCE_3`<br>`IMG_CS_JADA_2` ← `CS_JADA_2`<br>`IMG_CS_WIFE` ← `CS_WIFE`<br>`IMG_CS_GRANDSON` ← `CS_GRANDSON`<br>`IMG_ACA_SET` ← ảnh thật |
| 09 | `S14c_09 Close` | S82 → S90 | 71.0 | 52 | 9 | `IMG_BG_B_CLEAR` ← `BG_B_CLEAR`<br>`IMG_CS_GLORIA_4` ← `CS_GLORIA_4`<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE`<br>`IMG_ACA_HOLDER` ← ảnh thật<br>`IMG_CS_TERRANCE_4` ← `CS_TERRANCE_4`<br>`IMG_ACA_SET` ← ảnh thật<br>`IMG_WATERTEST` ← ảnh thật |

Tổng số lần tải ảnh nếu làm tay: 61.

## 4. Quyết định so với docx (theo luật TobyFlow đã chốt)

| Docx | Workflow | Lý do |
|---|---|---|
| Veo 3.1 / Kling 3.0 + Sync, Seedance | Omni 1.1 Flash, chế độ Frames, mọi clip | Mặc định skill |
| Độ dài clip = độ dài shot (1–6,5 s) | Có thoại: 6/8 s theo công thức 2,5 chữ/s, bắt đầu 0,4 s (1,0 s nếu có động tác trước), chừa 0,6 s. Câm: 4 s (shot > 3,5 s thì 6 s) | Nhân vật phải nói hết câu; khi dựng cắt đúng độ dài shot ở storyboard |
| Tắt tiếng model, dùng giọng ElevenLabs | Omni vẫn nói câu (khối VOICE từng nhân vật, cho khớp miệng); dựng thay bằng file ElevenLabs + Sync nếu lệch | Không gắn `voice` Flow vào Frames (lỗi cả lô) |
| [TAIL]: pores, shallow depth of field, 35mm, cinematic, slow push-in | Khối máy quay thật + da thật; "glides a few centimeters closer" | Chữ ép nét làm ảnh giả, như nhựa; từ cấm |
| Cậu bé 10 tuổi rõ mặt (S08, S71, S81) | Chỉ thấy sau lưng / nghiêng mờ ở hậu cảnh; sheet chỉ góc sau | Mặt trẻ em dễ bị Google chặn |
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

| Shot | File | Node clip | Clip | Shot dựng | Lời xong lúc | Ảnh đính (Image 1..n) | Lời |
|---|---|---|---|---|---|---|---|
| A-1 | 02 | `S14c_T_A1` | 6 s | — | 4.4 | BG_A_BDAY, CS_JADA_1, CS_TERRANCE_1, CS_GLORIA_1 | JADA: Dad. It's the soap thing again. I can't eat this. |
| B-1 | 01 | `S14c_T_B1` | 6 s | — | 3.6 | BG_A_BDAY, CS_TERRANCE_1, CS_JADA_1, PROP_BROCHURE | JADA: You're giving her THAT? Over the soap thing? |
| C-1 | 01 | `S14c_T_C1` | 6 s | — | 2.8 | BG_A_BDAY, CS_TERRANCE_1 | TERRANCE: To Mama. Seventy-one and still cooking. |
| C-2 | 01 | `S14c_T_C2` | 6 s | — | 2.4 | BG_A_BDAY, CS_JADA_1 | JADA: Sorry. It's the soap thing. |
| D-2 | 08 | `S14c_V_D2` | 4 s | — | — | BG_A_FRI, PROP_BROCHURE | (câm) |
| E-2 | 02 | `S14c_T_E2` | 6 s | — | 3.6 | BG_A_BDAY, CS_JADA_1 | JADA: Dad, I can't. It's the soap thing. |
| S01 | 02 | `S14c_T_S01` | 6 s | 3,5 s | 4.0 | BG_A_BDAY, CS_GLORIA_1, CS_JADA_1, PROP_SILICONE | JADA: Grandma, why does everything you make taste like SOAP? |
| S02 | 02 | `S14c_T_S02` | 6 s | 2,2 s | 2.4 | BG_A_BDAY, CS_TERRANCE_1, CS_JADA_1 | TERRANCE: Jada. We TALKED about this. |
| S02_B | 01 | `S14c_T_S02_B` | 6 s | 2,2 s | 2.4 | BG_A_BDAY, CS_TERRANCE_1, CS_JADA_1 | TERRANCE: Jada. We TALKED about this. |
| S02_C | 01 | `S14c_T_S02_C` | 6 s | 2,2 s | 2.4 | BG_A_BDAY, CS_TERRANCE_1, CS_JADA_1 | TERRANCE: Jada. We TALKED about this. |
| S03 | 02 | `S14c_T_S03` | 6 s | 1,7 s | 1.6 | BG_A_BDAY, CS_GLORIA_1 | GLORIA: Talked about what? |
| S03_B | 01 | `S14c_T_S03_B` | 6 s | 1,7 s | 1.6 | BG_A_BDAY, CS_GLORIA_1 | GLORIA: Talked about what? |
| S04 | 02 | `S14c_V_S04` | 4 s | 1,5 s | — | BG_A_BDAY, PROP_BROCHURE | (câm) |
| S05 | 02 | `S14c_T_S05` | 6 s | 2,5 s | 2.8 | BG_A_BDAY, CS_GLORIA_1, PROP_BROCHURE | GLORIA: You're putting me in a HOME? |
| S06 | 02 | `S14c_T_S06` | 6 s | 3,3 s | 3.6 | BG_A_BDAY, CS_TERRANCE_1 | TERRANCE: Mama. We were gonna wait till after cake. |
| S07 | 02 | `S14c_T_S07` | 6 s | 1,6 s | 1.6 | BG_A_BDAY, CS_GLORIA_1, PROP_BROCHURE | GLORIA: On my BIRTHDAY? |
| S08 | 02 | `S14c_V_S08` | 4 s | 1,6 s | — | BG_A_BDAY, CS_WIFE, CS_JADA_1, CS_GRANDSON | (câm) |
| S09 | 03 | `S14c_T_S09` | 6 s | 3,3 s | 4.2 | BG_B_NIGHT, CS_GLORIA_1, PROP_SILICONE | GLORIA: Soap. You think I can't rinse a POT? |
| S10 | 03 | `S14c_T_S10` | 6 s | 2,9 s | 3.2 | BG_B_NIGHT, CS_TERRANCE_1 | TERRANCE: Every dinner since Christmas. We've all noticed. |
| S11 | 03 | `S14c_T_S11` | 6 s | 1,7 s | 1.6 | BG_B_NIGHT, CS_GLORIA_1 | GLORIA: All of you? |
| S12 | 03 | `S14c_T_S12` | 6 s | 2,9 s | 3.2 | BG_B_NIGHT, CS_TERRANCE_1, CS_GLORIA_1 | TERRANCE: Taste buds go as you get older. |
| S13 | 03 | `S14c_T_S13` | 8 s | 4,9 s | 5.6 | BG_B_NIGHT, CS_TERRANCE_1 | TERRANCE: But if you can't taste soap, what happens when you can't smell gas? |
| S14 | 03 | `S14c_T_S14` | 6 s | 3,5 s | 3.6 | BG_B_NIGHT, CS_GLORIA_1 | GLORIA: I've cooked in this kitchen for forty-two years. |
| S15 | 03 | `S14c_T_S15` | 6 s | 4,4 s | 4.8 | BG_B_NIGHT, CS_TERRANCE_1 | TERRANCE: I know. That's why I don't want you in it alone. |
| S16 | 03 | `S14c_T_S16` | 8 s | 4,7 s | 5.8 | BG_B_NIGHT, CS_TERRANCE_1, PROP_BROCHURE | TERRANCE: Wrenfield has a unit opening this month. I put down a deposit. |
| S17 | 03 | `S14c_T_S17` | 6 s | 1,8 s | 1.6 | BG_B_NIGHT, CS_GLORIA_1 | GLORIA: You already PAID? |
| S18 | 03 | `S14c_V_S18` | 4 s | 3,0 s | — | BG_C, CS_TERRANCE_1 | TERRANCE: No, she won't fight it. She's — slipping. |
| S19 | 03 | `S14c_V_S19` | 4 s | 1,4 s | — | BG_C, CS_GLORIA_1 | (câm) |
| S20 | 04 | `S14c_V_S20` | 4 s | 1,5 s | — | BG_B_MORNING, CS_GLORIA_2, PROP_SILICONE | (câm) |
| S21 | 04 | `S14c_T_S21` | 6 s | 1,8 s | 2.6 | BG_B_MORNING, CS_JADA_1 | JADA: Grandma, it's still there. |
| S22 | 04 | `S14c_T_S22` | 6 s | 4,1 s | 4.4 | BG_B_MORNING, CS_GLORIA_2, PROP_SILICONE | GLORIA: I scrubbed that pan THREE times. New soap. New sponge. |
| S23 | 04 | `S14c_T_S23` | 6 s | 2,5 s | 3.4 | BG_B_MORNING, CS_GLORIA_2 | GLORIA: And I can't taste a THING. |
| S24 | 04 | `S14c_T_S24` | 6 s | 2,4 s | 2.4 | BG_B_MORNING, CS_GLORIA_2 | GLORIA: Jada, am I losing it? |
| S25 | 04 | `S14c_V_S25` | 4 s | 1,4 s | — | BG_B_MORNING, CS_JADA_1, CS_GLORIA_2 | (câm) |
| S26 | 04 | `S14c_V_S26` | 4 s | 2,0 s | — | BG_B_MORNING, CS_JADA_1, CS_GLORIA_2 | JADA: I love you, Grandma. |
| S27 | 04 | `S14c_V_S27` | 4 s | 1,6 s | — | BG_B_BOXES, CS_GLORIA_2 | (câm) |
| S28 | 04 | `S14c_V_S28` | 4 s | 1,8 s | — | BG_D, CS_DOROTHY, CS_FRIEND_DAUGHTER, CS_GLORIA_2 | (câm) |
| S29 | 04 | `S14c_T_S29` | 6 s | 3,2 s | 4.2 | BG_D, CS_GLORIA_2 | GLORIA: Wasn't she the one PUSHING you into Wrenfield? |
| S30 | 05 | `S14c_T_S30` | 6 s | 1,3 s | 1.6 | BG_D, CS_DOROTHY | DOROTHY: She sure was. |
| S31 | 05 | `S14c_T_S31` | 6 s | 4,0 s | 4.4 | BG_D, CS_GLORIA_2, CS_DOROTHY | GLORIA: Now she's here every Sunday, taking plates home. What CHANGED? |
| S32 | 05 | `S14c_T_S32` | 6 s | 3,3 s | 4.2 | BG_D, CS_DOROTHY | DOROTHY: She told me my cooking tasted like soap. |
| S33 | 05 | `S14c_V_S33` | 4 s | 1,1 s | — | BG_D, CS_GLORIA_2 | (câm) |
| S34 | 05 | `S14c_T_S34` | 6 s | 1,4 s | 1.2 | BG_D, CS_GLORIA_2 | GLORIA: Mine too. |
| S35 | 05 | `S14c_T_S35` | 6 s | 1,8 s | 2.0 | BG_D, CS_DOROTHY | DOROTHY: Show me your kitchen. |
| S36 | 05 | `S14c_T_S36` | 6 s | 1,7 s | 2.0 | BG_B_BOXES, CS_DOROTHY, PROP_SILICONE | DOROTHY: When'd you buy these? |
| S37 | 05 | `S14c_T_S37` | 6 s | 4,0 s | 4.4 | BG_B_BOXES, CS_GLORIA_2 | GLORIA: After Thanksgiving. Terrance sent me an article about black plastic. |
| S38 | 05 | `S14c_T_S38` | 6 s | 2,5 s | 2.8 | BG_B_BOXES, CS_DOROTHY | DOROTHY: And when did the soap start? |
| S39 | 05 | `S14c_V_S39` | 4 s | 1,0 s | — | BG_B_BOXES, CS_GLORIA_2 | (câm) |
| S40 | 05 | `S14c_T_S40` | 6 s | 1,3 s | 0.8 | BG_B_BOXES, CS_GLORIA_2 | GLORIA: Christmas. |
| S41 | 05 | `S14c_T_S41` | 6 s | 1,2 s | 1.2 | BG_B_BOXES, CS_DOROTHY, CS_GLORIA_2, PROP_SILICONE | DOROTHY: Smell it. |
| S42 | 05 | `S14c_T_S42` | 6 s | 1,8 s | 2.6 | BG_B_BOXES, CS_GLORIA_2, PROP_SILICONE | GLORIA: That's my DISH soap. |
| S43 | 06 | `S14c_T_S43` | 6 s | 2,8 s | 3.2 | BG_B_BOXES, CS_DOROTHY, PROP_SILICONE | DOROTHY: It soaks up whatever soap you use. |
| S44 | 06 | `S14c_V_S44` | 4 s | 3,2 s | — | BG_B_BOXES, PROP_SILICONE | DOROTHY: The minute it gets hot, out it comes. |
| S45 | 06 | `S14c_T_S45` | 6 s | 2,1 s | 2.4 | BG_B_BOXES, CS_GLORIA_2 | GLORIA: But I can't taste it. |
| S46 | 06 | `S14c_T_S46` | 6 s | 3,7 s | 4.0 | BG_B_BOXES, CS_DOROTHY | DOROTHY: Neither could I. Cook's always the last to notice. |
| S47 | 06 | `S14c_T_S47` | 6 s | 4,2 s | 4.8 | BG_B_BOXES, CS_DOROTHY, PROP_SILICONE | DOROTHY: They tested silicone baking pans. In the oven, chemicals leached out. |
| S48 | 06 | `S14c_V_S48` | 4 s | 3,3 s | — | BG_B_BOXES, CS_GLORIA_2 | DOROTHY: Some of them are linked to hormone disruption. |
| S49 | 06 | `S14c_V_S49` | 4 s | 1,8 s | — | IMG_ACA_TOWEL | (câm) |
| S50 | 06 | `S14c_T_S50` | 6 s | 3,1 s | 3.6 | BG_B_BOXES, CS_DOROTHY, IMG_ACA_SET | DOROTHY: I threw all mine out and got these. |
| S51 | 06 | `S14c_T_S51` | 6 s | 3,2 s | 3.6 | BG_B_BOXES, CS_GLORIA_2, IMG_ACA_SET | GLORIA: Wood? The cheap ones bleed in the pot. |
| S52 | 06 | `S14c_T_S52` | 6 s | 2,4 s | 2.8 | BG_B_BOXES, CS_DOROTHY | DOROTHY: That's the finish, not the wood. |
| S53 | 06 | `S14c_V_S53` | 6 s | 4,7 s | — | IMG_ACA_MACRO | DOROTHY: Every piece is one block of wood. No glue. Nothing painted on. |
| S54 | 06 | `S14c_T_S54` | 6 s | 3,6 s | 4.0 | BG_B_BOXES, CS_DOROTHY | DOROTHY: They're called Acawood. I just texted you the link. |
| S56 | 06 | `S14c_T_S56` | 6 s | 2,2 s | 3.0 | BG_B_BOXES, CS_DOROTHY, IMG_ACA_SET | DOROTHY: Keep these till yours come. |
| S57 | 06 | `S14c_T_S57` | 6 s | 2,4 s | 3.4 | BG_B_BOXES, CS_TERRANCE_2 | TERRANCE: Movers come Saturday at nine, Mama. |
| S58 | 07 | `S14c_T_S58` | 6 s | 1,3 s | 1.6 | BG_B_BOXES, CS_GLORIA_2, PROP_SILICONE | GLORIA: Smell this first. |
| S59 | 07 | `S14c_T_S59` | 6 s | 2,5 s | 2.8 | BG_B_BOXES, CS_TERRANCE_2 | TERRANCE: Mama. This isn't about a SPATULA. |
| S60 | 07 | `S14c_T_S60` | 6 s | 1,4 s | 1.6 | BG_B_BOXES, CS_GLORIA_2 | GLORIA: Smell it, Terrance. |
| S61 | 07 | `S14c_V_S61` | 4 s | 1,2 s | — | BG_B_BOXES, CS_TERRANCE_2, PROP_SILICONE | (câm) |
| S62 | 07 | `S14c_T_S62` | 6 s | 1,4 s | 1.6 | BG_B_BOXES, CS_TERRANCE_2, PROP_SILICONE | TERRANCE: That's dish soap. |
| S63 | 07 | `S14c_T_S63` | 6 s | 3,3 s | 3.6 | BG_B_BOXES, CS_GLORIA_2, IMG_ACA_SET | GLORIA: Now Dorothy's. She cooks with it every day. |
| S64 | 07 | `S14c_T_S64` | 6 s | 1,2 s | 1.4 | BG_B_BOXES, CS_TERRANCE_2, IMG_ACA_SET | TERRANCE: Nothing. |
| S65 | 07 | `S14c_T_S65` | 6 s | 2,5 s | 2.8 | BG_B_BOXES, CS_GLORIA_2 | GLORIA: One sniff. My nose is FINE. |
| S66 | 07 | `S14c_T_S66` | 6 s | 3,2 s | 4.2 | BG_B_BOXES, CS_GLORIA_2, CS_TERRANCE_2, PROP_SILICONE | GLORIA: You're the one who sent me that article. |
| S67 | 07 | `S14c_T_S67` | 6 s | 2,6 s | 3.2 | BG_B_BOXES, CS_TERRANCE_2 | TERRANCE: Smelling's one thing, Mama. Tasting's another. |
| S68 | 07 | `S14c_T_S68` | 6 s | 3,6 s | 4.0 | BG_B_BOXES, CS_GLORIA_2 | GLORIA: Friday night, I'm making my potato salad. Everybody comes. |
| S69 | 07 | `S14c_T_S69` | 8 s | 5,8 s | 6.4 | BG_B_BOXES, CS_GLORIA_2 | GLORIA: If anybody tastes soap, I'll get in your car Saturday and never say a word. |
| S70 | 07 | `S14c_T_S70` | 6 s | 1,3 s | 0.8 | BG_B_BOXES, CS_TERRANCE_2 | TERRANCE: Deal. |
| S71 | 08 | `S14c_V_S71` | 4 s | 1,8 s | — | BG_A_FRI, CS_GLORIA_3, CS_TERRANCE_3, CS_JADA_2, CS_WIFE, CS_GRANDSON, IMG_ACA_SET | (câm) |
| S72 | 08 | `S14c_T_S72` | 6 s | 3,1 s | 3.8 | BG_A_FRI, CS_GLORIA_3, CS_JADA_2, IMG_ACA_SET | GLORIA: Jada. You first. You're the honest one. |
| S73 | 08 | `S14c_V_S73` | 4 s | 2,0 s | — | BG_A_FRI, CS_JADA_2, CS_TERRANCE_3 | (câm) |
| S74 | 08 | `S14c_T_S74` | 6 s | 1,2 s | 0.8 | BG_A_FRI, CS_JADA_2 | JADA: Grandma. |
| S75 | 08 | `S14c_T_S75` | 6 s | 1,9 s | 2.0 | BG_A_FRI, CS_JADA_2 | JADA: There's no soap. NONE. |
| S76 | 08 | `S14c_V_S76` | 4 s | 1,6 s | — | BG_A_FRI, CS_TERRANCE_3 | (câm) |
| S77 | 08 | `S14c_T_S77` | 6 s | 2,0 s | 2.0 | BG_A_FRI, CS_TERRANCE_3 | TERRANCE: Mama. I'm so sorry. |
| S78 | 08 | `S14c_V_S78` | 4 s | 1,6 s | — | BG_A_FRI, CS_TERRANCE_3, PROP_BROCHURE | (câm) |
| S79 | 08 | `S14c_T_S79` | 6 s | 1,8 s | 2.0 | BG_A_FRI, CS_GLORIA_3 | GLORIA: Unpack my bowls, Terrance. |
| S80 | 08 | `S14c_T_S80` | 6 s | 1,1 s | 0.8 | BG_A_FRI, CS_JADA_2 | JADA: Seconds? |
| S81 | 08 | `S14c_V_S81` | 4 s | 1,8 s | — | BG_A_FRI, CS_TERRANCE_3, CS_JADA_2, CS_GLORIA_3, CS_WIFE, CS_GRANDSON, IMG_ACA_SET | (câm) |
| S82 | 09 | `S14c_T_S82` | 6 s | 4,7 s | 5.2 | BG_B_CLEAR, CS_GLORIA_4, PROP_SILICONE, IMG_ACA_HOLDER | GLORIA: My son almost moved me out of my own kitchen. Over THIS. |
| S83 | 09 | `S14c_T_S83` | 6 s | 4,2 s | 4.8 | BG_B_CLEAR, CS_GLORIA_4 | GLORIA: Before anybody tells you you've lost your touch, smell your spatula. |
| S84 | 09 | `S14c_T_S84` | 6 s | 3,9 s | 5.0 | BG_B_CLEAR, CS_GLORIA_4, PROP_SILICONE, IMG_ACA_HOLDER | GLORIA: If it smells like dish soap, so does your dinner. |
| S85 | 09 | `S14c_T_S85` | 8 s | 5,8 s | 6.8 | BG_B_CLEAR, CS_GLORIA_4, CS_TERRANCE_4, IMG_ACA_SET | GLORIA: And if it's your wife's cooking, or your mama's? Smell HERS before you blame her. |
| S86 | 09 | `S14c_T_S86` | 8 s | 5,7 s | 6.4 | BG_B_CLEAR, CS_GLORIA_4, IMG_ACA_HOLDER | GLORIA: Mine are Acawood now. Seven pieces, each one cut from a single block of wood. |
| S87 | 09 | `S14c_V_S87` | 6 s | 5,5 s | — | BG_B_CLEAR, IMG_ACA_SET, IMG_WATERTEST | GLORIA: Nothing on them but oil or wax. Here's one in hot water. Still clear. |
| S88 | 09 | `S14c_V_S88` | 4 s | 1,7 s | — | BG_B_CLEAR, CS_GLORIA_4, IMG_ACA_HOLDER | GLORIA: Hand wash, dry, done. |
| S89 | 09 | `S14c_T_S89` | 8 s | 6,5 s | 5.6 | BG_B_CLEAR, CS_GLORIA_4, IMG_ACA_HOLDER | GLORIA: Eighty-nine ninety-five with the holder. Free shipping in the U.S., and ninety-day returns. |
| S90 | 09 | `S14c_T_S90` | 6 s | 3,9 s | 4.0 | BG_B_CLEAR, CS_GLORIA_4 | GLORIA: The link's right below. And my kitchen? Still MINE. |

## 7. Rủi ro / cần Nam kiểm

- File 01 mở được mà 02–09 (69–89 KB) không mở được: giới hạn dung lượng thấp hơn ~70 KB → báo Claude tách nhỏ hơn. File 01 cũng không mở được: lỗi định dạng → gửi câu Toby báo + một file export workflow cũ có node video và node tải (vd. S12 v3) để so từng trường.
- Tên trường lấy theo mục 6 của skill (chưa có file export mẫu trong phiên này). Node `download` đã bỏ trường thừa `download`.
- Chưa đọc được Doc 56, 25, 47, 63, 72, 80 và Toby Flow 01, 02 (phiên cloud không có Projects); nên rà lại theo checklist Doc 56.
- Claim: "hormone disruption" đã duyệt; Meta từ chối thì thay "Ones you don't want in your food." (chỉ đổi file giọng S48, clip câm không phải gen lại).
- Nhân vật AI: bật nhãn nội dung AI khi chạy ads.
