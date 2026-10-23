# S14c We Talked About This (bản da đen) — Workflow TobyFlow (21-10)

Nguồn: `Editor_Script14_WeTalkedAboutThis_Black_Acawood.docx` (bản 4, sau CD review). Làm theo skill toby-workflow: Nano Banana Pro cho ảnh, **Omni 1.1 Flash** (Frames) cho mọi clip.

## 0. Rà soát trước khi chạy (23/10) — đọc mục này trước

Nam hỏi cách tránh phải làm lại từ đầu mỗi khi có lỗi vặt. Lượt này làm 4 việc:

1. **Rà độc lập toàn bộ prompt trước khi Nam chạy.** 5 người rà riêng, mỗi người một cảnh: bữa sinh nhật; bếp đêm, hiên, bếp sáng; hai đoạn bếp đóng thùng; tối thứ Sáu và đoạn chốt. Mỗi người đọc từng prompt khung và clip, so với docx, với ảnh Nam đã chọn (0C, 4 ảnh phòng, ảnh bếp) và với 13 loại lỗi đã gặp. Kết quả: **151 điểm** (19 rất dễ hỏng, 80 dễ hỏng, 52 nhỏ). Claude kiểm lại từng điểm trên ảnh thật rồi mới sửa; ghi chép ở `code/review/`.
2. **Sửa hết một lượt** (bảng dưới). Mọi file F và V đổi prompt. 0A, 0C, 0E không đổi. 0B chỉ đổi 1 node, không bắt buộc chạy lại. 0D đổi. Thêm file 0F mới.
3. **Thêm 17 phép kiểm tự động**, mỗi loại lỗi một phép (môi bị che, người ở mép khung, đếm món gỗ, ảnh nền sai hướng, chữ băng rôn, chừa chỗ banner…). Lần sau sửa gì, máy kiểm lại cả 111 khung và 98 clip, nên lỗi cũ không quay lại.
4. **Cách chạy mới để không phải làm lại cả file:**
   - Mỗi file có 3–4 **node chạy thử**, nằm ở bảng dưới. Chạy riêng các node đó trước, xem ảnh theo bảng soi. Đạt thì chạy cả file. Không đạt thì gửi Claude tên node và lỗi.
   - Mọi khung có một dòng trong **bảng soi từng khung** `S14c_Black_ChecklistKhung.md`: ai phải có trong khung, ai ở ngoài khung và ở bên nào, đồ gì và đếm bao nhiêu, chỗ hay sai cần soi trước.
   - Có lỗi thì Claude gửi **file sửa chỉ gồm các node đổi**, tên node giữ nguyên. Nam chạy đúng các node đó, các node đạt rồi để yên.

**Lỗi tìm được và cách sửa (chính):**

| Loại lỗi | Ở đâu | Sửa |
|---|---|---|
| Ảnh nền tường ảnh (17.jpg, F1b/F5b) có lọ hoa cao giữa bàn, che miệng người nói; có 2 ghế trống ở tiền cảnh; khung còn ghi "chữ băng rôn giữ nguyên" dù tường này không có băng rôn | 8 khung F1b, 7 khung F5b | ghi rõ bỏ lọ hoa, chỉ đồ ăn thấp; máy sát mép bàn, ghế gần và người ngồi ở đó ở sau máy; tường này không băng rôn, không chữ |
| Miệng bị che trong khung có lời | A-1 (tay thì thầm), S02_C (ly), S21, S23 (nĩa ở môi), S32 (ly cà phê), S42, S62, S64 (muỗng sát mũi), S82, S86 (muôi nâng lên mặt) | đồ cầm ở ngang ngực hoặc lệch một bên, "clear of her lips, lips in view"; clip cắn xong hạ nĩa rồi mới nói |
| Khung cận không thấy miệng mà clip có lời | S17, S24, S69 (chỉ thấy mắt) | khung từ chân mày tới cằm |
| Người lọt mép khung không có mô tả → người lạ (kiểu S05) | A-1, C-2, E-2, S01, S05, S06 (bà dì, ông chú, tay cậu bé); S72–S80 (bà dì, vai Terrance, tóc Jada) | tả người ở mép (vai, tóc, đồ) và đính sheet; hoặc ghi rõ ở ngoài khung |
| Gloria đứng sau ghế vợ Terrance nên bị che | S05, S08 | đứng ở đầu tủ buffet gần ghế của bà, thấy rõ từ đầu tới eo |
| Ảnh nền sai hướng: đòi cửa bếp, hành lang, bếp gas sau lưng mà ảnh nền không có | S10, S12 (cửa bếp), S78, D-2 (hành lang), S85 (Terrance ở bếp gas sau lưng Gloria) | file mới **0F**: 2 ảnh bếp nhìn từ bồn rửa về phía bếp gas có cửa (đêm, vài tuần sau); S78, D-2 chỉ lấy ánh sáng, thùng từ ảnh phòng ăn, máy ở hành lang |
| Đếm sai món gỗ (ra 8 món) | S86, S88 (ống còn đủ 7 + 1 trên tay), S85, S71, S81, S72, S87, S51, S63, S64 | món trên tay thì ống chỉ còn 6; cảnh một món thì "chỉ một món, phần còn lại ngoài khung" |
| Không ghi người kia đứng bên nào → hai người nhìn cùng một phía khi cắt cảnh | toàn bộ bếp đêm, bếp sáng, bếp đóng thùng, hiên | một trục nhìn cho mỗi cảnh, người kia luôn "just out of the frame at screen-left/right" (luật ở đầu bảng soi) |
| Giọng Gloria "strong and steady breath, no tremor" đè mất lúc run, thì thầm, khóc | S07, S11, S14, S17, S24, S34, S40, S79 | riêng các clip này: "a healthy voice, never frail", giọng theo dòng "This time" |
| Lời bắt đầu trong lúc đang làm động tác | S05, S10, S13, S14, S21, S23, S30, S34, S35, S58, S60, S62, S64, S68, S83, S89, C-2, E-2… | lời bắt đầu ít nhất 1,0 s sau động tác (luật của Nam) |
| Thiếu chỗ cho banner (docx: mặt dưới y 560 px) | mọi khung có người | "the top third of the frame holds only background; every face sits below it" |
| Ánh sáng bếp đóng thùng, bếp vài tuần sau, hiên chưa có câu sáng mặt; Living layer cho nắng "chuyển động" (Omni vẽ nhấp nháy) | F3–F4, F6, hiên | thêm câu sáng mặt; nắng đứng yên; cảnh không người ghi "không người, không tay xuất hiện" |
| Ảnh mẫu thứ Sáu (0D) bảo "giữ lọ hoa" mà ảnh 0C không có lọ hoa | 0D | không lọ hoa; thêm ảnh thật bộ gỗ, trên khăn không quá 6 món |
| Brochure: chữ trên bìa lúc phải có, lúc phải trống; xé không có cách cầm | B-1, S04, S05, S07, S16, D-2, S78 | B-1, S16 chữ đọc được; S04 chừa dải trống để ghép chữ; S05, S07 bìa quay về Gloria; D-2, S78 hai ngón cái sát nhau dưới tiêu đề, xé thẳng từ mép trên |
| Bình nước của Jada: ảnh mẫu có bình ngay chỗ Jada nhưng khung cận lúc có lúc không | A-1, C-2, E-2 và các khung thấy chỗ Jada | bình đứng đúng chỗ như ảnh mẫu, không ai cầm |

**Claude đã tự quyết những điểm sau (khác bản trước). Nam thấy không ổn thì báo:**

- S01: Gloria đứng ở góc bàn cạnh ghế Terrance (vừa múc thêm cho anh), Jada ngẩng lên nhìn bà về phía phải. Nếu Gloria đứng sau ghế Jada thì Jada phải quay lưng lại máy mới nói được. S03 vẫn nối được: Gloria đứng giữa bước ở đầu bàn.
- S03 chỉ có Gloria, Terrance ở ngoài khung. Lý do: ở hook C, cảnh trước Terrance đang đứng nâng ly. Docx S03 cũng là cận một mình Gloria.
- S09 (LATER THAT NIGHT) đổi sang toàn cảnh đúng khung ảnh nền, để cả thùng rác lẫn ống silicone đều đúng chỗ, không bị nhân đôi.
- S48: Dorothy đặt khuôn bánh lên quầy ở mép khung, không còn tay cầm. S61: Terrance tự cầm spatula ngửi. Bản trước là tay Gloria, nhưng cận tay người già cầm đồ hay bị Google chặn, và S62 anh cũng đang cầm nó.
- S04: máy đứng yên. Đoạn đẩy máy chậm của docx làm ở CapCut, cùng lúc ghép chữ WRENFIELD.
- S10, S12, S85 dùng ảnh nền mới ở 0F. Muốn giữ đúng một ảnh nền bếp thì phương án khác là Terrance dựa vào đầu quầy thay vì khung cửa (S10). Cách này đổi docx nên Claude chưa làm.
- S54, S86: thêm câu đọc "Acawood" là AH-kah-wood (docx: "A ca Wood"). Nghe vẫn sai thì Voice Changer không sửa được, phải gen lại clip.

**Ảnh nền Nam gửi (23/10, 5 ảnh) và việc phải làm lại:**

- **Bếp sáng (`BG_B_MORNING_FIX`):** sáng đẹp, quạt và ảnh tủ lạnh đúng, nhưng **mất bếp gas và chảo gang**: thùng rác bị vẽ vào đúng chỗ bếp, máy hút mùi treo trên khoảng trống. S13 ("can't smell gas"), S20 (chiên trứng), S85 cần bếp gas. Làm lại `0A2` bản 3: giữ nguyên bếp gas và chảo, thùng rác đạp chân đặt cạnh tủ lạnh (góc dưới bên trái), thấy rõ bàn đạp.
- **Bếp đêm, đóng thùng, vài tuần sau:** đẹp nhưng **không có thùng rác** (S09, S66, S84 cần) và không cùng gốc với ảnh bếp sáng. Làm lại cả 3 ở file mới `0B2`, sửa từ ảnh bếp sáng mới. Bếp đóng thùng: thùng không che bồn rửa, bếp gas, thùng rác; ống silicone không còn spatula.
- **Hiên nhà Dorothy (`BG_D`):** đẹp, nhưng bàn nhỏ đứng trước ghế đu chứ không ở đầu ghế, ghế bị cắt mất đầu bên phải, tờ báo trên bàn có chữ. Sửa ở `0B2` (`BG_D_FIX`, sửa từ ảnh Nam chọn): lùi máy thấy trọn ghế, bàn nhỏ ở đầu bên trái ghế, bỏ tờ báo. Các khung hiên ghi theo đó: Dorothy ngồi đầu trái cạnh bàn, Gloria đầu phải.
- **Tường ảnh (17.jpg, dùng cho F1b, F5b):** nên chạy `0E2` bản mới: bỏ lọ hoa giữa bàn (che miệng người nói) và đổi ảnh treo có trẻ em thành người lớn.
- `IMG_ACA_TOWEL` (ảnh thật khăn + 7 món, khung đầu S49): nên là ảnh chỉ thấy khăn kín khung, không thấy thớt hay nền studio, để cắt sang S50 (mặt quầy bếp) không lệch.
- Chưa xem: `BG_C` (hiên nhà Gloria ban đêm), `BG_A_FRI` (phòng ăn thứ Sáu). Nam gửi thì Claude kiểm.

**So với lần gửi trước (23/10, bản rà soát):**

- Mới: `0B2` (bếp đêm, bếp đóng thùng, bếp vài tuần sau, hiên sửa). `0B` chỉ còn 7 sheet đổi đồ và `BG_A_FRI`, các node này không đổi.
- Đổi prompt: `0A2` bản 3, `0E2` (bỏ lọ hoa), `0F` (chạy sau 0B2; tủ lạnh và thùng rác nằm sau máy), F2 (S18 ghi "trên hiên"), F3 (S29–S35: ảnh nền hiên `IMG_BG_D_FIX`, Dorothy đầu trái cạnh bàn nhìn sang phải, Gloria đầu phải nhìn sang trái).
- Chỉ đổi mô tả (ghi rõ node `IMG_` lấy ảnh ở đâu): F1, F1b, F4, F5, F5b, F6. Không đổi: 0A, 0C, 0D, 0E, V1–V6.
- Prompt khung bếp không đổi, nhưng ảnh nền bếp và hiên làm lại nên mọi khung F có bếp hoặc hiên phải chạy với ảnh nền mới.

**Thứ tự chạy setup (người đã chốt, giữ nguyên sheet 0A, 0B):**

1. `toby/fix/workflow_S14c_0A2_SuaBepSang.json` (bản 3): tải ảnh bếp **gốc** chọn ở 0A (ảnh chưa sửa, còn bếp gas, quạt còn chữ) vào `IMG_BEP_SANG_CU` → chạy `BG_B_MORNING_FIX` → chọn 1 ảnh có đủ bếp gas, chảo gang, thùng rác cạnh tủ lạnh. Ảnh này là bếp sáng: tải vào mọi node `IMG_BG_B_MORNING`.
1. `toby/workflow_S14c_0B2_BepHien.json` (mới): tải bếp sáng mới vào `IMG_BG_B_MORNING`, ảnh hiên Nam đã chọn vào `IMG_BG_D`, ảnh thật ống gỗ vào `IMG_ACA_HOLDER` → chạy `BG_B_NIGHT`, `BG_B_BOXES`, `BG_B_CLEAR`, `BG_D_FIX`.
1. `toby/workflow_S14c_0F_BepNguoc.json`: tải bếp sáng mới, bếp đêm và bếp vài tuần sau (vừa chọn ở 0B2) vào 3 node `IMG_` → chạy 2 ảnh bếp nhìn ngược.
1. `toby/fix/workflow_S14c_0E2_SuaAnhTreo.json`: tải ảnh 17.jpg vào `IMG_BG_A_WEST_CU` (ảnh hướng ④ vào `IMG_BG_A_SOUTH_CU` nếu muốn sửa luôn) → chạy → ảnh `BG_A_WEST_FIX` chọn được tải vào `IMG_BG_A_WEST` ở F1b, F5b.
1. `toby/workflow_S14c_0D_BanAnThuSau.json` → `MASTER_A_FRI`.
1. Rồi F1 → F6, F1b, F5b, mỗi file chạy node thử trước (bảng dưới), rồi V1 → V6.

**Node chạy thử trước (mỗi file):**

| File | Chạy thử trước | Vì sao |
|---|---|---|
| 0A2 | `BG_B_MORNING_FIX` | còn bếp gas và chảo gang ở góc phải; thùng rác có bàn đạp đứng cạnh tủ lạnh |
| 0B2 | `BG_B_NIGHT`, `BG_D_FIX` | đêm vẫn thấy rõ tủ và thùng rác; hiên thấy trọn ghế đu, bàn ở đầu trái, không tờ báo |
| 0F | `BG_B_NIGHT_REV`, `BG_B_CLEAR_REV` | ảnh nền mới, phải có cửa bếp ở cuối, đúng tủ, bếp gas, quạt như ảnh bếp |
| 0E2 | `BG_A_WEST_FIX` | không lọ hoa giữa bàn, ảnh treo toàn người lớn |
| 0D | `MASTER_A_FRI` | không lọ hoa, đúng 7 người đúng ghế, không quá 6 món gỗ trên khăn |
| F1 | `S14c_F_S05`, `S14c_F_S01`, `S14c_F_A-1`, `S14c_F_B-1` | nhiều người nhất, người ở mép, tay thì thầm, brochure nghiêng về máy |
| F1b | `S14c_F_S01_H2`, `S14c_F_S02_C_H2`, `S14c_F_C-1_H2` | lọ hoa đã bỏ chưa, Jada quay mặt về máy |
| F2 | `S14c_F_S09`, `S14c_F_S10`, `S14c_F_S21`, `S14c_F_S20` | toàn cảnh đêm, ảnh nền 0F, nĩa không che môi, bếp gas + xà phòng mới |
| F3 | `S14c_F_S31`, `S14c_F_S28`, `S14c_F_S36`, `S14c_F_S42`, `S14c_F_S33` | hiên mới: Dorothy đầu trái cạnh bàn, Gloria đầu phải; nhìn từ vỉa hè, ống silicone, spatula không che miệng, đĩa trượt trên đùi |
| F4 | `S14c_F_S48`, `S14c_F_S51`, `S14c_F_S66`, `S14c_F_S69` | khuôn bánh trên quầy không tay, một muỗng gỗ, thùng rác, cận sát có miệng |
| F5 | `S14c_F_S72`, `S14c_F_S74`, `S14c_F_S78`, `S14c_F_D-2` | Gloria múc salad, người ở mép, hành lang, tay cầm để xé |
| F5b | `S14c_F_S72_H2`, `S14c_F_S77_H2` | lọ hoa, Gloria sau ghế |
| F6 | `S14c_F_S86`, `S14c_F_S85`, `S14c_F_S84`, `S14c_F_S82` | ống còn 6 + muôi trên tay, ảnh nền 0F, thùng rác, muôi không che môi |
| V1 | `S14c_T_A1`, `S14c_T_S01` | tay không che miệng khi thì thầm; nụ cười Gloria tắt |
| V2 | `S14c_T_S09`, `S14c_T_S21` | nắp thùng mở theo bàn đạp; nói sau khi nuốt |
| V3 | `S14c_T_S41`, `S14c_T_S47` | chỉ Dorothy nói; khuôn bánh đi theo tay |
| V4 | `S14c_T_S56`, `S14c_T_S66` | không tay lạ; nắp đóng khi nhấc chân |
| V5 | `S14c_V_D2`, `S14c_T_S72` | xé thẳng một đường; múc xong mới nói |
| V6 | `S14c_T_S86`, `S14c_V_S88` | muôi không lên mặt; đủ 7 món sau khi cắm |

## 1. Tóm tắt

- **98 clip** (74 T_ có thoại, 24 V_ câm). Không còn node `TAI`: bật **Auto Download** trong Settings của Toby, mỗi clip tự tải 1080p vào thư mục theo tên node clip.
- **Setup 7 file (0A, 0B, 0B2, 0C, 0D, 0E, 0F) + 2 file sửa (0A2, 0E2) + 6 file khung (F1–F6) + 6 file clip (V1–V6), chia theo cảnh.** 0A: sheet nhân vật gốc, đạo cụ, 4 ảnh nền gốc. 0B: sheet đổi đồ và 4 trạng thái khác của cùng hai căn phòng, sửa từ ảnh gốc ở 0A. 0C: ảnh mẫu bàn tiệc (đủ 7 người ngồi đúng chỗ, cùng góc máy với ảnh nền phòng ăn), dùng làm tham chiếu cho mọi khung bàn ăn. 0D: ảnh mẫu bàn ăn tối thứ Sáu, sửa từ ảnh 0C đã chọn (cùng góc máy, cùng chỗ ngồi, đồ thứ Sáu). Mọi khung trong phòng ăn (F1, F5) là ảnh mẫu của ngày đó được sửa: cùng chỗ đặt máy, chỉ phóng gần và đổi hành động, biểu cảm. 0E: 3 ảnh nền trống của phòng ăn nhìn từ 3 hướng còn lại (phòng chuẩn: `S14c_PhongAn_4Huong.png`), để sau này quay từ hướng khác mà vẫn đúng phòng. File F chỉ tạo khung đầu `S14c_F_<cảnh>` (ảnh x4); Nam chọn 1 khung đạt, tải vào node `IMG_F_<cảnh>` của file V; file V chỉ có clip. Không node nào lấy ảnh từ node tạo trong cùng file (cách Script 11: file 04b chỉ có clip, khung tải vào node Album F_).
- Mỗi file ≤ 97 KB và ≤ 85 node (file 04b Script 11 của Nam: 96 KB / 82 node vẫn import được). Node video viết đúng định dạng file Toby cũ của Nam: `video_duration` dạng "6s", `download_resolution` "1080p", có `prompt_mode`/`ref_mode` (bản trước ghi số 6 và "1k" nên Toby không import được); khung nối vào `frame_1` + `frame_1_source`.
- **Nhân vật (22/10):** viết lại theo nghiên cứu gia đình Mỹ da đen, chi tiết ở `S14c_Black_NhanVat.md`. Sheet đổi đồ chuyển sang file 0B (lấy sheet gốc từ 0A) vì bản cũ nối trong cùng file nên ra người lạ.
- **Số lượng:** node ảnh x4 (không tốn credit), node video x2 (98 clip → 196 lượt video).
- **Clip nói diễn như phim (Nam 22/10):** cả 74 clip nói chỉ có khung đầu (frame_1), không còn khung cuối giữ dáng. 42 clip trước đây giữ dáng được viết lại hành động: một nhịp chính trong giây đầu, cử chỉ theo từng cụm lời, người nghe trong khung phản ứng, một nhịp im lặng cuối clip. Dòng Face cho mọi clip nói đổi từ "understated" sang biểu cảm rõ, có cử chỉ, không lố. Đồ đang cầm đi theo tay thay vì giữ nguyên góc.
- **Bàn ăn cố định (Nam 23/10, sau lượt F1):** một sơ đồ chỗ ngồi cho cả bữa sinh nhật và bữa thứ Sáu (docx: Gloria đầu bàn, Terrance bên phải bà, Jada ngay cạnh Terrance, vợ và con út đối diện; thứ Sáu đúng những người đó, đúng chỗ cũ). Chỉ 7 người: Gloria, Terrance, vợ, Jada, cậu bé (chỉ thấy tay), bà dì và ông chú (2 họ hàng docx ghi ở hậu cảnh, giờ tả cố định). Túi quà chỉ ở tủ buffet, brochure đi đúng theo từng cảnh, chưa có bánh kem trên bàn. Mỗi khung bàn ăn ghi rõ máy đặt ở đâu, ai ở trong khung, sau lưng ai là gì. Sơ đồ ở mục 3.
- **Ánh sáng (Nam 23/10, "quá tối hay quá cổ điển"):** đồ đạc cổ điển là đúng docx (bếp 42 năm, bếp gas trắng cũ là lý do Terrance nói "can't smell gas" ở S13), giữ nguyên. Cái làm cảnh trông cũ và tối là ánh sáng: ảnh nền bếp gốc tối (độ sáng trung bình 102/255, góc và tủ dưới chìm, trắng ngả xám xanh), mà khung nào cũng chép "same light" của ảnh nền, nên 58/96 khung là cảnh bếp (đêm 9, sáng 7, đóng thùng 33, vài tuần sau 9, gồm cả đoạn chốt bán hàng) và sẽ tối theo. Sửa ở gốc: 0A2 bản mới làm bếp sáng, trắng ra trắng (vẫn hơi mát buổi sớm như docx); 0B ghi rõ ánh sáng 3 trạng thái bếp; khung bếp sáng và bếp đêm thêm câu đủ sáng mặt. Phòng ăn đủ sáng (ảnh 0C: 137/255), chỉ ám cam: chỉnh màu ở CapCut, không gen lại (mục 5). So sánh: `S14c_AnhSang_TruocSau.png`.
- **Người lạ ở bàn ăn (Nam 23/10, `S14c_F_S05`):** S05 chỉ đính sheet của Gloria trong khi Terrance, Jada, vợ Terrance ngồi ở tiền cảnh, nên model vẽ thành người khác. Giờ ai lọt khung (kể cả mờ ở mép) đều có sheet và mô tả: S05 thêm Terrance, Jada, vợ; S06 thêm Jada; B-1, S02_B, S07 thêm vợ Terrance (ngồi ngay trước tủ buffet); S03 thêm Terrance. Câu tả chỗ kiểu "sau ghế vợ Terrance" đổi thành "tủ buffet ở đầu phòng"; người chỉ được nhìn tới thì ghi rõ ở ngoài khung (S03_B, S77, S79). File `S14c_F1sua` cũ bỏ: rà soát 23/10 sửa mọi khung F1, nên import lại cả F1 (mục 0).
- **Lần ánh sáng (23/10):** 0A2 prompt mới (sửa 4 chỗ + làm sáng bếp, chạy từ ảnh bếp gốc); 0B: `P_BG_B_NIGHT`, `P_BG_B_BOXES`, `P_BG_B_CLEAR`; F2 (S09 → S17), F3 (S20 → S26). Các prompt này đã gộp vào file F bản rà soát 23/10; file txt để dán cũ bỏ.
- **Đổi gì so với bản trước (23/10, duyệt F1 lần 2):** Nam báo gần hết khung F1 vẫn sai chỗ ngồi. Ảnh mẫu 0C chỉ làm "tham chiếu chỗ ngồi" thì model vẫn tự dựng lại bàn ăn cho từng khung và dựng sai. Giờ mọi khung trong phòng ăn là ảnh mẫu được sửa (Image 1 = ảnh 0C, tối thứ Sáu = ảnh 0D): giữ nguyên phòng, chỗ đặt máy, ai ngồi ghế nào, chỉ phóng gần và đổi hành động, biểu cảm. Khung đổi: F1: C-1, C-2, S02_C, B-1, S02_B, S03_B, A-1, E-2, S01, S02, S03, S04, S05, S06, S07, S08; F2: S09, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26; F3: S27, S28, S29, S30, S31, S32, S33, S34, S35, S36, S37, S38, S39, S40, S41, S42, S43, S44, S45, S46; F4: S47, S48, S50, S51, S52, S54, S56, S57, S58, S59, S60, S61, S62, S63, S64, S65, S66, S67, S68, S69, S70; F5: D-2, S71, S72, S73, S74, S75, S76, S77, S78, S79, S80, S81; F6: S82, S83, S84, S85, S86, S87, S88, S89, S90.  không đổi. Clip: P_V_A-1, P_V_B-1, P_V_C-1, P_V_C-2, P_V_D-2, P_V_E-2, P_V_S01, P_V_S02, P_V_S02_B, P_V_S02_C, P_V_S03, P_V_S03_B, P_V_S04, P_V_S05, P_V_S06, P_V_S07, P_V_S08, P_V_S09, P_V_S10, P_V_S11, P_V_S13, P_V_S14, P_V_S15, P_V_S16, P_V_S17, P_V_S18, P_V_S19, P_V_S20, P_V_S21, P_V_S22, P_V_S23, P_V_S24, P_V_S25, P_V_S26, P_V_S27, P_V_S28, P_V_S29, P_V_S30, P_V_S31, P_V_S32, P_V_S33, P_V_S34, P_V_S35, P_V_S36, P_V_S37, P_V_S38, P_V_S39, P_V_S40, P_V_S41, P_V_S42, P_V_S43, P_V_S44, P_V_S45, P_V_S46, P_V_S47, P_V_S48, P_V_S49, P_V_S50, P_V_S51, P_V_S52, P_V_S53, P_V_S54, P_V_S56, P_V_S57, P_V_S58, P_V_S59, P_V_S60, P_V_S61, P_V_S62, P_V_S63, P_V_S64, P_V_S65, P_V_S66, P_V_S67, P_V_S68, P_V_S69, P_V_S70, P_V_S71, P_V_S72, P_V_S74, P_V_S75, P_V_S78, P_V_S79, P_V_S81, P_V_S82, P_V_S83, P_V_S84, P_V_S85, P_V_S86, P_V_S87, P_V_S88, P_V_S89 0D bản trước (tường ảnh nhìn từ bên kia bàn) bỏ, thay bằng 0D ảnh mẫu tối thứ Sáu. F1, F5 đổi node ảnh tải lên nên phải import lại.
- **Biểu cảm đúng ngữ cảnh (Nam 23/10):** 92 khung có người đều có dòng `Expressions true to this moment` tả mặt từng người theo nhịp truyện; cảnh căng ghi rõ "nobody smiles" vì model ảnh hay tự vẽ mặt cười. Clip toàn cảnh và clip nhiều người có dòng `Expressions` cho người nghe; người nói có giọng điệu ở khối Speech. Cột "Biểu cảm" ở mục 6 dùng để duyệt khi chọn 1 trong 4 khung.
- Đã đối chiếu với luật trong chat cũ của Nam (xem mục 1b và `references/toby-flow-rules-nam.md`). **0A, 0B giữ nguyên** (không import lại). 9 file clip cũ 01–09 bỏ hết, thay bằng F1–F6 và V1–V6.
- File import: `toby/workflow_S14c_0A_Setup.json`, `toby/workflow_S14c_0B_DoiDo.json`, `toby/workflow_S14c_0C_BanAn.json`, `toby/workflow_S14c_0D_BanAnThuSau.json`, `toby/workflow_S14c_0E_PhongAn4Huong.json`, `toby/workflow_S14c_0F_BepNguoc.json` (mới, rà soát 23/10), `toby/workflow_S14c_F1.json` … `F6.json`, `toby/workflow_S14c_V1.json` … `V6.json`; sửa và làm sáng bếp buổi sáng: `toby/fix/workflow_S14c_0A2_SuaBepSang.json` (bản 23/10). Payload `create_workflow` cho Toby MCP (Claude Desktop): `toby/mcp/`. Kèm `S14c_Black_prompt_pack.txt` và 6 SRT (H1, A–E).
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
| Bình nước to của Jada (docx) | không có | cốc giữ nhiệt hồng nhạt, không logo, không ai cầm; bữa tối đứng đúng chỗ Jada như ảnh mẫu ở mọi khung thấy chỗ ngồi của Jada (rà soát 23/10), sáng hôm sau trên quầy (S21) |
| Ảnh trang trí là ảnh của gia đình da đen này (Nam, 22/10) | "framed family and graduation photos", "family photos on the fridge" chung chung → model tự bịa người | tường: ảnh cưới của bà và người chồng đã mất, ảnh tốt nghiệp của Terrance, của Jada, ảnh bà với con trai, con dâu trước nhà thờ; tủ lạnh: ảnh bà với bạn nhà thờ, Terrance và vợ, Jada đội mũ tốt nghiệp; toàn người da đen, chỉ người lớn, ảnh nhỏ, hơi mờ, không chữ |
| Quạt giấy nhà thờ | không tả mặt in | in tranh một nhà thờ trắng nhỏ, không người, không chữ |
| Cùng một căn phòng ở nhiều cảnh | phòng ăn thứ Sáu và 4 trạng thái bếp tạo riêng từ chữ → mỗi cảnh một căn phòng, ảnh treo khác nhau | 0A tạo phòng ăn sinh nhật và bếp buổi sáng; 0B sửa từ 2 ảnh đó ra phòng ăn thứ Sáu, bếp đêm, bếp đóng thùng, bếp vài tuần sau, giữ nguyên tường, tủ, ảnh |
| Người ở bàn ăn | "the family", "the whole table" chung chung (C-1, S01, S05, S08, S71, S81) | ghi rõ: gia đình người Mỹ da đen, chỉ người lớn lộ mặt, thêm 2 họ hàng lớn tuổi ở cuối bàn (docx: 2–3 họ hàng mờ hậu cảnh); chỗ ngồi cố định theo docx; C-1 mẹ ngoài khung |
| Món trên bàn (docx) | bỏ sót | rau collard, khoai lang, bánh ngô mờ ở hậu cảnh các cảnh bàn ăn |
| Tay cầm đồ ở mép khung | S42, S48, S61 không nói tay ai; S64 không rõ ai cầm | rà soát 23/10: S42 spatula vào từ mép khung, không tay; S48 khuôn bánh đặt trên quầy, không tay; S61, S64 Terrance tự cầm; tay ở mép (C-2, D-2) ghi tông da, tay áo, chỉ nhẫn người đó đeo |
| Màn hình điện thoại | E-2, S54 không nói màn hình hiện gì | E-2 màn hình quay đi; S54 chỉ sáng trơn, không chữ (giao diện tin nhắn dựng ở CapCut, S55) |
| Khung F_ cũng phải đến từ file chạy trước (Nam chọn 1 trong 4) | 9 file clip: khung F_ tạo và nối thẳng vào clip trong cùng file → clip chạy trên khung chưa duyệt | 4 file khung F1–F4 (chỉ ảnh) + 4 file clip V1–V4; khung đã chọn tải vào `IMG_F_<cảnh>` |
| Chỗ ngồi cố định ở 2 bữa tối (Nam 23/10) | chỉ một câu "Seating" chung chung ở vài khung; khung cận không nói ai ngồi đâu → mỗi khung một kiểu | sơ đồ 7 ghế cố định + ảnh mẫu bàn ăn 0C làm tham chiếu cho mọi khung bàn ăn; khung rộng S08, S71, S81 dùng đúng góc máy của ảnh mẫu; khung cận ghi máy đặt bên kia bàn và sau lưng ai là gì |
| Không bịa người lạ vào bàn (Nam 23/10) | "two older relatives", "the rest of the family" không tả → model thêm người khác nhau mỗi khung | đúng 7 người; bà dì (em gái Gloria) và ông chú tả cố định, đồ sinh nhật và đồ thứ Sáu riêng; khung cận ghi "ai không được tả thì ở ngoài khung, không ai khác trong phòng" |
| Túi quà, brochure, bánh kem (Nam 23/10) | túi quà và brochure chỗ mỗi khung một khác | 3 túi quà chỉ trên tủ buffet (vàng giấy hồng, xanh nhạt, hồng hoa văn) như ảnh nền; brochure: dưới túi vàng (B-1, S04) → trên tay Gloria (S05, S07, S08) → quầy bếp tối đó (S16) → nóc thùng ở hành lang thứ Sáu (D-2, S78); S06 không có brochure trong khung; chưa có bánh kem ("till after cake") |
| Đồ của vợ Terrance | "nice dinner clothes" / "soft knit sweater" → đổi màu mỗi khung | sinh nhật: đúng bộ trong sheet của chị; thứ Sáu: áo len cam gỉ sắt |
| Hiên nhà Dorothy, điện thoại, trứng (rà 23/10) | ghế đu không nói ai ngồi đầu nào; "another handset"; nĩa trứng không rõ lấy đâu | Dorothy ngồi đầu ghế đu cạnh bàn nhỏ có ly cà phê, túi vải bên cạnh, Gloria đầu kia; điện thoại của Gloria trên quầy; Jada nếm trứng từ chảo |
| Rà soát độc lập cả kịch bản (23/10) | S05 nhìn xuống bàn thì lộ mặt cậu bé; B-1 vẽ thêm một bàn đầy người; hook C: Jada vừa nâng ly cảnh trước, cảnh sau đang nhai; hook B: Terrance và Jada đứng ở tủ buffet rồi tự ngồi lại ghế; bóng bay, tủ buffet đặt sau lưng Terrance trong khi Gloria đứng đúng chỗ đó; tối thứ Sáu tô salad lúc đặt xuống, lúc trên tay; S86 thành 8 món; túi vải Dorothy hai chỗ; S50 bộ gỗ nằm cạnh khăn | S05 chỉ thấy dãy dọc tường cửa vòm, dãy kia khuất sau lưng Gloria; B-1 không thấy bàn; C-1 Jada vẫn nhai, tay cầm nĩa, C-2 bố đang đứng; S02_B Terrance dẫn Jada về bàn, S03_B Gloria nhìn con vội về ghế; sau lưng Terrance là tường cửa vòm, tủ buffet ở phía anh nhìn; tô đặt giữa Jada và bố, S72 múc từ tô trên bàn rồi lùi về đầu bàn, S79 bà ngồi, S81 tô cạnh Terrance; S86 tay chỉ "phần còn lại của bộ"; túi vải đặt trên ghế đu ở S31–S32; S50 bộ gỗ nằm trên khăn; Jada có bình nước ở C-1, S72, S80 |
| Khung bàn ăn sửa từ ảnh mẫu (duyệt F1, 23/10) | ảnh mẫu 0C chỉ làm tham chiếu "ai ngồi đâu", mỗi khung tự dựng lại bàn ăn từ ảnh nền trống + sheet → Jada ra trước tường băng rôn như ngồi ghế đầu bàn, Terrance sang dãy đối diện, Gloria ở cuối bàn, bà dì sang dãy vợ, tủ buffet dời tường; lần sửa bằng ảnh nền tường ảnh nhìn từ bên kia bàn vẫn là tự dựng | mọi khung phòng ăn = "Edit Image 1" với Image 1 là ảnh mẫu đã chọn (0C sinh nhật, 0D thứ Sáu sửa từ 0C): giữ phòng, chỗ đặt máy, ai ngồi ghế nào; chỉ phóng gần, đổi hành động, biểu cảm; sheet chỉ để giữ mặt khi phóng gần; khung có lời: ngón tay không che môi |
| Ánh sáng nền (Nam 23/10) | ảnh nền bếp gốc tối, trắng ngả xám xanh; 0B chỉ ghi "night outside the window", "plain daytime light", bếp vài tuần sau không nói ánh sáng → mọi khung bếp chép ánh sáng tối của ảnh gốc | 0A2 làm sáng bếp ngay từ ảnh gốc (một lần sửa, không sửa chồng); 0B ghi rõ: đêm chỉ đèn máy hút mùi nhưng tủ, tủ lạnh vẫn nhìn rõ, không đen kịt; đóng thùng và vài tuần sau sáng, trắng ra trắng; khung bếp sáng thêm "bright and airy… every visible face is clearly lit", khung bếp đêm thêm "falls softly on every visible face"; đồ đạc cổ điển giữ đúng docx |
| Biểu cảm đúng ngữ cảnh (Nam 23/10) | hơn 50 khung không ghi biểu cảm → model tự vẽ mặt cười cả lúc căng; người nghe không có phản ứng | 92 khung có dòng Expressions theo nhịp truyện, cảnh căng ghi "nobody smiles"; người nghe phản ứng trong clip (A-1 nụ cười Gloria tắt dần, S01 nụ cười khựng lại, Terrance nhắm mắt, S66 Terrance chột dạ, S71 cả bàn im lặng căng thẳng); Gloria đau mà giữ phẩm giá, không giận dữ; Jada thật thà, không chê bai; Terrance thương mà sợ, không phải kẻ xấu; Dorothy điềm tĩnh, khô hài, không "sassy" |
| Node video đúng định dạng file Toby của Nam (04b, 05 Script 11) | `video_duration` 6 (số), `download_resolution` "1k", thiếu `prompt_mode`/`ref_mode` → không import được | "6s", "1080p", `prompt_mode`/`ref_mode` "all"; khung vào `frame_1`; không node TAI, Auto Download tải 1080p |

## 2. Ảnh thật cần chuẩn bị

| Ảnh | Cần gì | Tải vào |
|---|---|---|
| `IMG_ACA_SET` | real product photo: the 7 Acawood utensils on white, straight + 3/4 | file 0D, file F4, file F5, file F6, file F5b |
| `IMG_ACA_HOLDER` | real product photo: the full set standing in the round holder | file 0B2, file F6 |
| `IMG_ACA_TOWEL` | real product photo, top view: 7 utensils laid in a row on the red-and-white checkered towel (start frame S49) | file F4, file V3 |
| `IMG_ACA_MACRO` | real macro photo: grain running unbroken from handle to head (start frame S53) | file V4 |
| `IMG_WATERTEST` | a still frame from the real hot-water test clip (water still clear) (ref for F_S87) | file F6 |

## 3. Các file và thứ tự làm

1. **`S14c_0A Setup nhan vat nen`** (26 node, chỉ ảnh, x4, không cần tải ảnh): 6 character sheet gốc (Gloria 1, Terrance 1, Jada 1, Dorothy, vợ Terrance, con gái Dorothy), sheet quần áo cậu bé (không người), 2 sheet đạo cụ, 4 ảnh nền gốc (`BG_A_BDAY`, `BG_B_MORNING`, `BG_C`, `BG_D`). Duyệt theo mục 6 của `S14c_Black_NhanVat.md`, xem ảnh treo tường và ảnh trên tủ lạnh đều là người da đen, chọn 1 ảnh mỗi node, **tải về máy**.
2. **`S14c_0B Doi do`** (20 node, Nam đã chạy, sheet đã chốt): 7 sheet đổi đồ + ảnh nền phòng ăn thứ Sáu `BG_A_FRI`. 3 ảnh nền bếp chuyển sang file `0B2` (23/10).
   **Bếp (bắt buộc, bản 3, 23/10):** chạy file sửa bếp `toby/fix/workflow_S14c_0A2_SuaBepSang.json`: tải ảnh bếp GỐC đã chọn ở 0A (ảnh chưa sửa, còn bếp gas, kể cả khi đã chạy 0A2 bản cũ) vào `IMG_BEP_SANG_CU` → chạy `BG_B_MORNING_FIX` (x4) → chọn 1 ảnh: **bếp gas trắng và chảo gang vẫn ở góc dưới bên phải**, thùng rác đạp chân (thấy bàn đạp) cạnh tủ lạnh, quạt tranh nhà thờ không chữ, ảnh tủ lạnh toàn người lớn da đen, nóc tủ lạnh trống, bếp sáng, tủ trắng ra trắng. Ảnh đó là `BG_B_MORNING`: tải vào mọi node `IMG_BG_B_MORNING` (0B2, 0F và file F).
   **`S14c_0B2 Bep va hien`** (11 node, mới 23/10, chạy sau 0A2): tải bếp sáng mới vào `IMG_BG_B_MORNING`, ảnh hiên nhà Dorothy Nam đã chọn vào `IMG_BG_D`, ảnh thật ống gỗ vào `IMG_ACA_HOLDER` → chạy `BG_B_NIGHT`, `BG_B_BOXES`, `BG_B_CLEAR`, `BG_D_FIX` → chọn: cả 3 bếp cùng bếp với ảnh sáng (bếp gas, chảo, thùng rác cạnh tủ lạnh); đêm vẫn thấy rõ tủ, thùng rác; thùng trơn không chữ, không che bồn rửa, bếp gas, thùng rác; vài tuần sau có ống gỗ, không ống silicone; hiên thấy trọn ghế đu, bàn nhỏ ở đầu trái ghế, không tờ báo. `BG_D_FIX` tải vào `IMG_BG_D_FIX` ở F3.
3. **`S14c_0C Ban an mau`** (7 node, mới): tải 5 ảnh đã chọn ở 0A vào node `IMG_` (`IMG_BG_A_BDAY`, `IMG_CS_GLORIA_1`, `IMG_CS_TERRANCE_1`, `IMG_CS_JADA_1`, `IMG_CS_WIFE`) → chạy `MASTER_A_BDAY` (x4) → chọn 1 ảnh đúng sơ đồ dưới đây → tải về. Ảnh này tải vào node `IMG_MASTER_A_BDAY` ở F1 (mọi khung tiệc sinh nhật sửa từ ảnh này) và 0D (ảnh mẫu tối thứ Sáu sửa từ ảnh này). Không ảnh nào đúng thì chạy lại 0C, đừng chạy F1/F5 với ảnh mẫu sai.
   Sơ đồ có ảnh minh họa: `S14c_SoDoChoNgoi.png` (cùng thư mục với file này).
```
   TƯỜNG ĐẦU PHÒNG: cửa vòm · thìa dĩa gỗ treo · băng rôn + bóng bay 71 (sinh nhật)   [tủ buffet ở góc phải]
                          [ GLORIA · ghế đầu bàn ]
   tường ảnh     TERRANCE   │          │  VỢ TERRANCE
   gia đình      JADA       │   BÀN    │  CẬU BÉ (chỉ thấy tay)
   + tủ chén     BÀ DÌ      │          │  ÔNG CHÚ
                          [ ghế trống · cuối bàn ]
                          ▲ máy quay chính (góc ảnh 0C)
   Mọi khung trong phòng ăn là ảnh mẫu được sửa: máy luôn ở cuối bàn như ảnh 0C, khung cận là phóng gần từ chỗ đó; không còn khung quay từ bên kia bàn. Từ máy nhìn vào: dãy tường ảnh bên trái (bà dì gần máy nhất, rồi Jada, rồi Terrance sát đầu bàn), Gloria ở giữa đầu bàn, dãy vợ Terrance bên phải, tủ buffet sau ghế vợ Terrance.
```
   Duyệt ảnh mẫu: Gloria đứng ở đầu bàn phía tủ buffet, cạnh ghế của bà (ghế đầu bàn, kéo ra một chút), cầm tô potato salad; dãy dọc tường ảnh gia đình và tủ chén là Terrance (sát đầu bàn), Jada, bà dì (tóc bạc xoắn); cửa vòm và thìa dĩa gỗ ở tường đầu phòng sau lưng Gloria; dãy đối diện là vợ Terrance (sát đầu bàn), cậu bé (chỉ thấy tay áo sọc, khuất sau ông chú), ông chú (hói); đúng 7 người, không ai lạ; túi quà chỉ trên tủ buffet; không bánh kem. Nam đã chọn ảnh 1 (23/10); thứ tự dãy đối diện lấy theo ảnh này.
   **`S14c_0D Ban an thu Sau`** (7 node, chạy sau 0B và 0C, trước F5): tải ảnh 0C đã chọn vào `IMG_MASTER_A_BDAY`, 3 sheet đồ thứ Sáu (`IMG_CS_GLORIA_3`, `IMG_CS_TERRANCE_3`, `IMG_CS_JADA_2`) và `IMG_CS_WIFE` → chạy `MASTER_A_FRI` (x4) → chọn 1 ảnh: cùng góc máy và đúng 7 người ở đúng ghế như ảnh 0C; mọi người mặc đồ thứ Sáu; không băng rôn, bóng bay, túi quà; thùng trơn ở hành lang qua cửa vòm; khăn caro với vài muôi gỗ (không quá 6) trên tủ buffet; không lọ hoa giữa bàn (ảnh 0C không có); Gloria đứng đầu bàn cầm tô salad → tải về. Ảnh này tải vào `IMG_MASTER_A_FRI` ở F5. Bản 23/10 thêm ảnh thật `IMG_ACA_SET` vào node thứ 6.
   **`S14c_0F Bep nhin nguoc`** (7 node, mới, chạy sau 0B2): tải `BG_B_MORNING` (ảnh bếp sáng sau 0A2), `BG_B_NIGHT`, `BG_B_CLEAR` (chọn ở 0B2) vào 3 node `IMG_` → chạy `BG_B_NIGHT_REV`, `BG_B_CLEAR_REV` (x4) → mỗi node chọn 1 ảnh: cùng tủ trắng, quầy, bếp gas trắng, máy hút mùi, quạt giấy, điện thoại tường như ảnh bếp; cuối bếp, ngay sau bếp gas, có cửa mở ra hành lang; không người, không chữ. Ảnh đêm dùng cho S10, S12; ảnh vài tuần sau dùng cho S85.
   **`S14c_0E Phong an 4 huong`** (7 node, chạy sau 0A, mới 23/10): tải `BG_A_BDAY` đã chọn ở 0A vào `IMG_BG_A_BDAY` → chạy `BG_A_WEST`, `BG_A_EAST`, `BG_A_SOUTH` (x4) → mỗi node chọn 1 ảnh đúng bức tường theo `S14c_PhongAn_4Huong.png`: cùng màu tường, bàn, khăn ren, ghế như ảnh nền; ghế trống, không người, không trang trí sinh nhật; ảnh treo tường đều là người lớn da đen, không chữ. Nam đã chọn 3 ảnh (23/10). Ảnh hướng ② và ④ có vài ảnh treo có trẻ em, ảnh ② có lọ hoa cao giữa bàn: chạy file sửa `toby/fix/workflow_S14c_0E2_SuaAnhTreo.json` (bản 23/10 bỏ luôn lọ hoa; tải ảnh đã chọn vào `IMG_BG_A_WEST_CU`, `IMG_BG_A_SOUTH_CU`), ảnh sửa xong thay cho `BG_A_WEST`, `BG_A_SOUTH` (tải vào `IMG_BG_A_WEST` ở F1b, F5b).
   **`S14c_F1b`, `S14c_F5b` (khung góc thẳng, mới 23/10):** 15 khung cận có lời ở bàn ăn (F1: C-1, C-2, S02_C, E-2, S01, S02, S03, S06; F5: S72–S77, S80) nhìn thẳng từ bên kia bàn, nền là ảnh hướng ② (`IMG_BG_A_WEST`), ảnh mẫu 0C/0D chỉ để biết ai ngồi đâu. Bản 23/10 ghi rõ bỏ lọ hoa giữa bàn của ảnh nền (che miệng), không băng rôn trên tường ảnh. Đây là bản thêm, F1, F5 giữ nguyên: chạy cả hai, mỗi cảnh chọn bản đẹp hơn (thường bản góc thẳng khớp miệng tốt hơn), tải vào đúng node `IMG_F_<cảnh>` ở file clip.
   Phòng chuẩn, sau lưng từng người (hướng máy theo sơ đồ): Gloria ở đầu bàn ① — thìa dĩa gỗ ngay sau vai lệch trái, tranh nhỏ và cửa vòm xa hơn bên trái, bên phải tủ buffet với túi quà, băng rôn và bóng bay phía trên. Terrance ② — tủ gỗ thấp cửa kính (bình pha lê, ảnh nhỏ trên nóc), phía trên là cụm ảnh: ảnh cưới cũ của Gloria, 2 ảnh tốt nghiệp, ảnh gia đình ở nhà thờ. Jada ② — ảnh tốt nghiệp đại học của Terrance. Bà dì ② — tủ chén gỗ cao cửa kính, 2 ảnh gia đình trên nóc (theo ảnh hướng ② Nam chọn). Vợ Terrance ③ — tranh phong cảnh đồng quê nhà trại trắng. Cậu bé — cửa sổ rèm voan (hướng ③ ④ cắt khung tránh ghế này để không lộ mặt). Ông chú ③ — chậu lan ý ở góc. Ghế cuối bàn ④ — lối mở sang phòng khách: sofa be, chăn móc len, đèn cây. Thứ Sáu: bỏ băng rôn, bóng bay, túi quà; tủ buffet có khăn caro với vài muôi gỗ; qua cửa vòm thấy thùng trơn.
4. **Import thử `V1` ngay** (chưa cần ảnh, import không tốn gì) để chắc node video đã đúng định dạng. Vào được thì để đó, chưa chạy. Không vào được thì chụp dòng báo lỗi của Toby và export một workflow video mới nhất Nam chạy được (menu ⋮ → Export) gửi Claude.
5. **File khung F1 → F6** (chỉ ảnh, x4): tải ảnh đã chọn ở 0A/0B/0C/0D vào node `IMG_` cùng tên (bỏ `IMG_` là ra tên node ở 0A/0B/0C/0D) và ảnh thật theo bảng dưới → chạy hết → mỗi node `S14c_F_<cảnh>` chọn 1 ảnh đạt trong 4 (đúng mặt, tông da, đồ theo sheet; tay đủ ngón; không chữ; thùng trơn) → tải về (Auto Download lưu theo tên node).
6. **File clip V1 → V6**: tải khung đã chọn của `S14c_F_<cảnh>` vào node `IMG_F_<cảnh>` (S49, S53 dùng ảnh thật `IMG_ACA_TOWEL`, `IMG_ACA_MACRO`) → chạy hết; Auto Download tải clip 1080p. Có thể làm F1 → V1 xong rồi mới sang F2 → V2.
7. Có Claude Desktop + Toby MCP thì khỏi tải tay: Nam báo khung nào chọn, Claude đọc kết quả (`get_workflow`) rồi `update_node` gắn ảnh vào các node `IMG_` (MCP tạo tối đa 5 workflow/ngày).

| File | Workflow | Shot | KB | Node | Tạo | Tải ảnh vào node IMG_ |
|---|---|---|---|---|---|---|
| 0A | `S14c_0A Setup nhan vat nen` | character sheet gốc 7 nhân vật + 2 sheet đạo cụ + 4 ảnh nền gốc | 26.5 | 26 | — |  |
| 0B | `S14c_0B Doi do` | 7 sheet đổi đồ (Gloria 2–4, Terrance 2–4, Jada 2) và ảnh nền phòng ăn thứ Sáu sửa từ ảnh gốc ở 0A | 24.2 | 20 | — | `IMG_CS_GLORIA_1` ← `CS_GLORIA_1`<br>`IMG_CS_TERRANCE_1` ← `CS_TERRANCE_1`<br>`IMG_CS_JADA_1` ← `CS_JADA_1`<br>`IMG_BG_A_BDAY` ← `BG_A_BDAY` |
| 0B2 | `S14c_0B2 Bep va hien` | 3 ảnh nền bếp (đêm, đóng thùng, vài tuần sau) sửa từ ảnh bếp sáng mới của 0A2, và ảnh hiên nhà Dorothy sửa từ ảnh BG_D đã chọn | 11.8 | 11 | — | `IMG_BG_B_MORNING` ← `BG_B_MORNING`<br>`IMG_BG_D` ← `BG_D`<br>`IMG_ACA_HOLDER` ← ảnh thật |
| 0C | `S14c_0C Ban an mau` | ảnh mẫu bàn tiệc sinh nhật: đủ 7 người ngồi đúng chỗ, cùng góc máy với ảnh nền BG_A_BDAY | 9.5 | 7 | — | `IMG_BG_A_BDAY` ← `BG_A_BDAY`<br>`IMG_CS_GLORIA_1` ← `CS_GLORIA_1`<br>`IMG_CS_TERRANCE_1` ← `CS_TERRANCE_1`<br>`IMG_CS_JADA_1` ← `CS_JADA_1`<br>`IMG_CS_WIFE` ← `CS_WIFE` |
| 0D | `S14c_0D Ban an thu Sau` | ảnh mẫu bàn ăn tối thứ Sáu: sửa từ ảnh 0C đã chọn, cùng góc máy, cùng chỗ ngồi, đồ thứ Sáu, không trang trí sinh nhật | 9.9 | 8 | — | `IMG_MASTER_A_BDAY` ← `MASTER_A_BDAY`<br>`IMG_CS_GLORIA_3` ← `CS_GLORIA_3`<br>`IMG_CS_TERRANCE_3` ← `CS_TERRANCE_3`<br>`IMG_CS_JADA_2` ← `CS_JADA_2`<br>`IMG_CS_WIFE` ← `CS_WIFE`<br>`IMG_ACA_SET` ← ảnh thật |
| 0E | `S14c_0E Phong an 4 huong` | ảnh nền trống phòng ăn cho 3 hướng máy còn lại (nhìn sang tường ảnh, nhìn sang tường cửa sổ, nhìn từ đầu bàn xuống), sửa từ ảnh nền BG_A_BDAY | 10.1 | 7 | — | `IMG_BG_A_BDAY` ← `BG_A_BDAY` |
| 0F | `S14c_0F Bep nhin nguoc` | ảnh nền trống bếp nhìn từ đầu bồn rửa về phía bếp gas và cửa bếp (ban đêm cho S10, S12; vài tuần sau cho S85), sửa từ ảnh bếp buổi sáng | 8.2 | 7 | — | `IMG_BG_B_MORNING` ← `BG_B_MORNING`<br>`IMG_BG_B_NIGHT` ← `BG_B_NIGHT`<br>`IMG_BG_B_CLEAR` ← `BG_B_CLEAR` |
| F1 | `S14c_F1 Khung C-1 den S08` | C-1 → S08 | 94.4 | 40 | 16 khung | `IMG_MASTER_A_BDAY` ← `MASTER_A_BDAY` (0C)<br>`IMG_CS_TERRANCE_1` ← `CS_TERRANCE_1` (0A)<br>`IMG_CS_JADA_1` ← `CS_JADA_1` (0A)<br>`IMG_CS_WIFE` ← `CS_WIFE` (0A)<br>`IMG_PROP_BROCHURE` ← `PROP_BROCHURE` (0A)<br>`IMG_CS_GLORIA_1` ← `CS_GLORIA_1` (0A)<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE` (0A)<br>`IMG_CS_GRANDSON` ← `CS_GRANDSON` (0A) |
| F2 | `S14c_F2 Khung S09 den S26` | S09 → S26 | 73.7 | 46 | 18 khung | `IMG_BG_B_NIGHT` ← `BG_B_NIGHT` (0B2)<br>`IMG_CS_GLORIA_1` ← `CS_GLORIA_1` (0A)<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE` (0A)<br>`IMG_BG_B_NIGHT_REV` ← `BG_B_NIGHT_REV` (0F)<br>`IMG_CS_TERRANCE_1` ← `CS_TERRANCE_1` (0A)<br>`IMG_PROP_BROCHURE` ← `PROP_BROCHURE` (0A)<br>`IMG_BG_C` ← `BG_C` (0A)<br>`IMG_BG_B_MORNING` ← `BG_B_MORNING` (0A2, ảnh BG_B_MORNING_FIX)<br>`IMG_CS_GLORIA_2` ← `CS_GLORIA_2` (0B)<br>`IMG_CS_JADA_1` ← `CS_JADA_1` (0A) |
| F3 | `S14c_F3 Khung S27 den S46` | S27 → S46 | 83.5 | 46 | 20 khung | `IMG_BG_B_BOXES` ← `BG_B_BOXES` (0B2)<br>`IMG_CS_GLORIA_2` ← `CS_GLORIA_2` (0B)<br>`IMG_BG_D_FIX` ← `BG_D_FIX` (0B2)<br>`IMG_CS_DOROTHY` ← `CS_DOROTHY` (0A)<br>`IMG_CS_FRIEND_DAUGHTER` ← `CS_FRIEND_DAUGHTER` (0A)<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE` (0A) |
| F4 | `S14c_F4 Khung S47 den S70` | S47 → S70 | 92.3 | 49 | 21 khung | `IMG_BG_B_BOXES` ← `BG_B_BOXES` (0B2)<br>`IMG_CS_DOROTHY` ← `CS_DOROTHY` (0A)<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE` (0A)<br>`IMG_CS_GLORIA_2` ← `CS_GLORIA_2` (0B)<br>`IMG_ACA_SET` ← ảnh thật<br>`IMG_ACA_TOWEL` ← ảnh thật<br>`IMG_CS_TERRANCE_2` ← `CS_TERRANCE_2` (0B) |
| F5 | `S14c_F5 Khung D-2 den S81` | D-2 → S81 | 72.3 | 33 | 12 khung | `IMG_BG_A_FRI` ← `BG_A_FRI` (0B)<br>`IMG_CS_TERRANCE_3` ← `CS_TERRANCE_3` (0B)<br>`IMG_PROP_BROCHURE` ← `PROP_BROCHURE` (0A)<br>`IMG_MASTER_A_FRI` ← `MASTER_A_FRI` (0D)<br>`IMG_CS_GLORIA_3` ← `CS_GLORIA_3` (0B)<br>`IMG_CS_JADA_2` ← `CS_JADA_2` (0B)<br>`IMG_CS_WIFE` ← `CS_WIFE` (0A)<br>`IMG_CS_GRANDSON` ← `CS_GRANDSON` (0A)<br>`IMG_ACA_SET` ← ảnh thật |
| F6 | `S14c_F6 Khung S82 den S90` | S82 → S90 | 44.6 | 26 | 9 khung | `IMG_BG_B_CLEAR` ← `BG_B_CLEAR` (0B2)<br>`IMG_CS_GLORIA_4` ← `CS_GLORIA_4` (0B)<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE` (0A)<br>`IMG_ACA_HOLDER` ← ảnh thật<br>`IMG_BG_B_CLEAR_REV` ← `BG_B_CLEAR_REV` (0F)<br>`IMG_CS_TERRANCE_4` ← `CS_TERRANCE_4` (0B)<br>`IMG_ACA_SET` ← ảnh thật<br>`IMG_WATERTEST` ← ảnh thật |
| V1 | `S14c_V1 Clip C-1 den S08` | C-1 → S08 | 69.0 | 48 | 16 clip | 16 khung: `IMG_F_<cảnh>` ← khung đã chọn `S14c_F_<cảnh>` (file F1) |
| V2 | `S14c_V2 Clip S09 den S29` | S09 → S29 | 83.6 | 63 | 21 clip | 21 khung: `IMG_F_<cảnh>` ← khung đã chọn `S14c_F_<cảnh>` (file F2, F3) |
| V3 | `S14c_V3 Clip S30 den S49` | S30 → S49 | 79.7 | 60 | 20 clip | 19 khung: `IMG_F_<cảnh>` ← khung đã chọn `S14c_F_<cảnh>` (file F3, F4)<br>`IMG_ACA_TOWEL` ← ảnh thật |
| V4 | `S14c_V4 Clip S50 den S70` | S50 → S70 | 83.3 | 60 | 20 clip | 19 khung: `IMG_F_<cảnh>` ← khung đã chọn `S14c_F_<cảnh>` (file F4)<br>`IMG_ACA_MACRO` ← ảnh thật |
| V5 | `S14c_V5 Clip D-2 den S81` | D-2 → S81 | 46.6 | 36 | 12 clip | 12 khung: `IMG_F_<cảnh>` ← khung đã chọn `S14c_F_<cảnh>` (file F5) |
| V6 | `S14c_V6 Clip S82 den S90` | S82 → S90 | 38.0 | 27 | 9 clip | 9 khung: `IMG_F_<cảnh>` ← khung đã chọn `S14c_F_<cảnh>` (file F6) |
| F1b | `S14c_F1b Khung goc thang C-1 den S06` | C-1_H2 → S06_H2 | 52.0 | 22 | 8 khung | `IMG_BG_A_WEST` ← `BG_A_WEST` (0E2, ảnh BG_A_WEST_FIX)<br>`IMG_CS_TERRANCE_1` ← `CS_TERRANCE_1` (0A)<br>`IMG_CS_JADA_1` ← `CS_JADA_1` (0A)<br>`IMG_MASTER_A_BDAY` ← `MASTER_A_BDAY` (0C)<br>`IMG_CS_GLORIA_1` ← `CS_GLORIA_1` (0A)<br>`IMG_PROP_SILICONE` ← `PROP_SILICONE` (0A) |
| F5b | `S14c_F5b Khung goc thang S72 den S80` | S72_H2 → S80_H2 | 45.5 | 20 | 7 khung | `IMG_BG_A_WEST` ← `BG_A_WEST` (0E2, ảnh BG_A_WEST_FIX)<br>`IMG_CS_GLORIA_3` ← `CS_GLORIA_3` (0B)<br>`IMG_CS_JADA_2` ← `CS_JADA_2` (0B)<br>`IMG_CS_TERRANCE_3` ← `CS_TERRANCE_3` (0B)<br>`IMG_ACA_SET` ← ảnh thật<br>`IMG_MASTER_A_FRI` ← `MASTER_A_FRI` (0D) |

Tổng số lần tải ảnh nếu làm tay: 180 (0B 4, 0C 3, file khung 48, file clip 98).

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
- **Chỉnh màu (23/10):** cảnh bàn ăn (F1, F5) ám cam hơn bếp. Trong CapCut, đặt một lớp điều chỉnh (Adjustment) phủ hết các clip bàn ăn: nhiệt độ màu khoảng −8 đến −12, vùng tối +8 đến +12, phơi sáng +3 đến +5; chỉnh bằng mắt sao cho tóc bạc của Gloria và khăn ren ra trắng ngà, không vàng cam, da vẫn nâu ấm. Cùng một lớp cho cả tiệc sinh nhật và tối thứ Sáu. Bếp đêm không kéo sáng quá +5 (da nâu ra xám, nhiễu); clip bếp nào còn tối thì chạy lại khung, đừng cứu ở CapCut.
- Thẻ chữ thời gian: S28 dùng **THE FOLLOWING SUNDAY** như storyboard (mục 4 docx ghi SUNDAY, dễ hiểu nhầm là sáng hôm sau, mà sáng hôm sau đã là Chủ nhật). Đề xuất thêm thẻ **A FEW DAYS LATER** ở S27 (docx chỉ ghi trong mô tả shot) để người xem theo kịp mốc hai tuần.

## 6. Bảng clip

Shot dựng = mốc cắt khi dựng (storyboard). Clip dài hơn để nhân vật nói hết câu; cắt phần lặng.

Clip chỉ có khung đầu (frame_1), không khung cuối: nhân vật diễn tự do. Mỗi clip ra 2 bản, chọn bản diễn đạt và giữ đúng mặt, đúng đồ.

| Shot | Khung → Clip | Node clip | Clip | Shot dựng | Lời xong lúc | Ảnh đính khung (Image 1..n) | Lời | Biểu cảm (khung đầu) |
|---|---|---|---|---|---|---|---|---|
| A-1 | F1 → V1 | `S14c_T_A1` | 6 s | — | 4.4 | MASTER_A_BDAY, CS_JADA_1, CS_TERRANCE_1, CS_GLORIA_1 | JADA: Dad. It's the soap thing again. I can't eat this. | the granddaughter embarrassed and uneasy, wincing a little as she whispers, not mean; her father tense; the grandmother in the background still smiling as the proud hostess, not yet aware |
| B-1 | F1 → V1 | `S14c_T_B1` | 6 s | — | 3.6 | MASTER_A_BDAY, CS_TERRANCE_1, CS_JADA_1, CS_WIFE, PROP_BROCHURE | JADA: You're giving her THAT? Over the soap thing? | the son furtive and guilty, his jaw set; his daughter stunned and hurt for her grandmother, her eyes wide; nobody smiles |
| C-1 | F1 → V1 | `S14c_T_C1` | 6 s | — | 2.8 | MASTER_A_BDAY, CS_TERRANCE_1, CS_JADA_1 | TERRANCE: To Mama. Seventy-one and still cooking. | the son proud and warm, smiling at his mother as he toasts; his daughter chewing with a strained, uneasy face, trying not to show it; the aunt smiling, her glass raised |
| C-2 | F1 → V1 | `S14c_T_C2` | 6 s | — | 3.0 | MASTER_A_BDAY, CS_JADA_1, CS_TERRANCE_1 | JADA: Sorry. It's the soap thing. | the granddaughter uncomfortable and apologetic, eyes watering, trying to swallow; no smile |
| D-2 | F5 → V5 | `S14c_V_D2` | 4 s | — | — | BG_A_FRI, CS_TERRANCE_3, PROP_BROCHURE | (câm) | — |
| E-2 | F1 → V1 | `S14c_T_E2` | 6 s | — | 3.8 | MASTER_A_BDAY, CS_JADA_1 | JADA: Dad, I can't. It's the soap thing. | the granddaughter tense and unhappy, done pretending, her brows drawn together; no smile |
| S01 | F1 → V1 | `S14c_T_S01` | 6 s | 3,5 s | 4.0 | MASTER_A_BDAY, CS_GLORIA_1, CS_JADA_1, CS_TERRANCE_1, PROP_SILICONE | JADA: Grandma, why does everything you make taste like SOAP? | the granddaughter's face an apologetic, pained grimace, honest, never disgusted or mocking; her father already tense, bracing himself; the grandmother still smiling proudly as she serves, not yet aware |
| S02 | F1 → V1 | `S14c_T_S02` | 6 s | 2,2 s | 2.4 | MASTER_A_BDAY, CS_TERRANCE_1, CS_JADA_1 | TERRANCE: Jada. We TALKED about this. | the son embarrassed and alarmed, eyes wide, jaw tight, keeping his voice down, not angry; his daughter guilty but stubborn; nobody smiles |
| S02_B | F1 → V1 | `S14c_T_S02_B` | 6 s | 2,2 s | 2.4 | MASTER_A_BDAY, CS_TERRANCE_1, CS_JADA_1, CS_WIFE | TERRANCE: Jada. We TALKED about this. | the son embarrassed and alarmed, eyes wide, jaw tight, keeping his voice down, not angry; his daughter shocked; nobody smiles |
| S02_C | F1 → V1 | `S14c_T_S02_C` | 6 s | 2,2 s | 2.4 | MASTER_A_BDAY, CS_TERRANCE_1, CS_JADA_1 | TERRANCE: Jada. We TALKED about this. | the son embarrassed and alarmed, his glass still raised, jaw tight, keeping his voice down, not angry; his daughter guilty but stubborn; nobody smiles |
| S03 | F1 → V1 | `S14c_T_S03` | 6 s | 1,7 s | 1.6 | MASTER_A_BDAY, CS_GLORIA_1, PROP_SILICONE | GLORIA: Talked about what? | the grandmother's warm hostess smile still on her face, just starting to falter as she senses something is wrong |
| S03_B | F1 → V1 | `S14c_T_S03_B` | 6 s | 1,7 s | 1.6 | MASTER_A_BDAY, CS_GLORIA_1, PROP_SILICONE | GLORIA: Talked about what? | the grandmother's warm hostess smile still on her face, just starting to falter as she senses something is wrong |
| S04 | F1 → V1 | `S14c_V_S04` | 4 s | 1,5 s | — | MASTER_A_BDAY, PROP_BROCHURE | (câm) | — |
| S05 | F1 → V1 | `S14c_T_S05` | 6 s | 2,5 s | 3.4 | MASTER_A_BDAY, CS_GLORIA_1, CS_TERRANCE_1, CS_JADA_1, CS_WIFE, CS_GRANDSON, PROP_BROCHURE | GLORIA: You're putting me in a HOME? | the grandmother stunned and hurt, her face falling, disbelief rising in her eyes, not angry; at the table nobody smiles |
| S06 | F1 → V1 | `S14c_T_S06` | 6 s | 3,3 s | 3.6 | MASTER_A_BDAY, CS_TERRANCE_1, CS_JADA_1 | TERRANCE: Mama. We were gonna wait till after cake. | the son guilty, pleading and cornered, his eyes begging her to understand; no smile |
| S07 | F1 → V1 | `S14c_T_S07` | 6 s | 1,6 s | 1.6 | MASTER_A_BDAY, CS_GLORIA_1, CS_WIFE, PROP_BROCHURE | GLORIA: On my BIRTHDAY? | the grandmother deeply hurt and betrayed, eyes red and wet, chin trembling, holding on to her dignity; no smile |
| S08 | F1 → V1 | `S14c_V_S08` | 4 s | 1,6 s | — | MASTER_A_BDAY, CS_GLORIA_1, CS_TERRANCE_1, CS_JADA_1, CS_WIFE, CS_GRANDSON, PROP_BROCHURE | (câm) | everyone frozen and ashamed: the son stares at his plate, the granddaughter shocked behind her hand, the son's wife, the aunt and the uncle look down, uneasy; the grandmother alone and hurt; nobody smiles |
| S09 | F2 → V2 | `S14c_T_S09` | 6 s | 3,3 s | 4.2 | BG_B_NIGHT, CS_GLORIA_1, PROP_SILICONE | GLORIA: Soap. You think I can't rinse a POT? | the grandmother stung and offended, her mouth set, hiding her hurt behind brisk scraping, not raging; no smile |
| S10 | F2 → V2 | `S14c_T_S10` | 6 s | 2,9 s | 3.8 | BG_B_NIGHT_REV, CS_TERRANCE_1 | TERRANCE: Every dinner since Christmas. We've all noticed. | the son tired and sad, loving but helpless; no smile |
| S11 | F2 → V2 | `S14c_T_S11` | 6 s | 1,7 s | 1.6 | BG_B_NIGHT, CS_GLORIA_1 | GLORIA: All of you? | the grandmother small and wounded as it sinks in that everyone noticed; no smile |
| S12 | F2 → V2 | `S14c_T_S12` | 6 s | 2,9 s | 3.2 | BG_B_NIGHT_REV, CS_TERRANCE_1, CS_GLORIA_1 | TERRANCE: Taste buds go as you get older. | the son gentle and soft-eyed, with a small, kind but pitying look, the way you talk to a child; no grin |
| S13 | F2 → V2 | `S14c_T_S13` | 8 s | 4,9 s | 6.2 | BG_B_NIGHT, CS_TERRANCE_1 | TERRANCE: But if you can't taste soap, what happens when you can't smell gas? | the son worried and careful, his brow knotted; no smile |
| S14 | F2 → V2 | `S14c_T_S14` | 6 s | 3,5 s | 4.2 | BG_B_NIGHT, CS_GLORIA_1 | GLORIA: I've cooked in this kitchen for forty-two years. | the grandmother proud and shaking, chin trembling, holding back tears |
| S15 | F2 → V2 | `S14c_T_S15` | 6 s | 4,4 s | 4.8 | BG_B_NIGHT, CS_TERRANCE_1 | TERRANCE: I know. That's why I don't want you in it alone. | the son honest and scared for her, eyes red and wet; no smile |
| S16 | F2 → V2 | `S14c_T_S16` | 8 s | 4,7 s | 5.8 | BG_B_NIGHT, CS_TERRANCE_1, PROP_BROCHURE | TERRANCE: Wrenfield has a unit opening this month. I put down a deposit. | the son controlled and guilty, avoiding her eyes as if he had rehearsed it; no smile |
| S17 | F2 → V2 | `S14c_T_S17` | 6 s | 1,8 s | 1.6 | BG_B_NIGHT, CS_GLORIA_1 | GLORIA: You already PAID? | the grandmother in disbelief, tears welling, barely breathing |
| S18 | F2 → V2 | `S14c_V_S18` | 4 s | 3,0 s | — | BG_C, CS_TERRANCE_1 | TERRANCE: No, she won't fight it. She's — slipping. | his shoulders slumped and weary |
| S19 | F2 → V2 | `S14c_V_S19` | 4 s | 1,4 s | — | BG_C, CS_GLORIA_1 | (câm) | the grandmother devastated, fighting tears |
| S20 | F2 → V2 | `S14c_V_S20` | 4 s | 1,5 s | — | BG_B_MORNING, CS_GLORIA_2, PROP_SILICONE | (câm) | the grandmother focused and determined, a little hopeful, lips pressed together; no smile |
| S21 | F2 → V2 | `S14c_T_S21` | 6 s | 1,8 s | 3.0 | BG_B_MORNING, CS_JADA_1 | JADA: Grandma, it's still there. | the granddaughter apologetic and gentle, a small wince as she tastes |
| S22 | F2 → V2 | `S14c_T_S22` | 6 s | 4,1 s | 4.4 | BG_B_MORNING, CS_GLORIA_2, PROP_SILICONE | GLORIA: I scrubbed that pan THREE times. New soap. New sponge. | the grandmother frustrated and insistent, her brows drawn together |
| S23 | F2 → V2 | `S14c_T_S23` | 6 s | 2,5 s | 4.0 | BG_B_MORNING, CS_GLORIA_2 | GLORIA: And I can't taste a THING. | the grandmother puzzled and quietly scared as she tastes; no smile |
| S24 | F2 → V2 | `S14c_T_S24` | 6 s | 2,4 s | 2.4 | BG_B_MORNING, CS_GLORIA_2 | GLORIA: Jada, am I losing it? | the grandmother small and frightened, her eyes glistening |
| S25 | F2 → V2 | `S14c_V_S25` | 4 s | 1,4 s | — | BG_B_MORNING, CS_JADA_1, CS_GLORIA_2 | (câm) | the granddaughter tender and sad, lips parted, about to answer; the grandmother waiting, vulnerable; nobody smiles |
| S26 | F2 → V2 | `S14c_V_S26` | 4 s | 2,0 s | — | BG_B_MORNING, CS_JADA_1, CS_GLORIA_2 | JADA: I love you, Grandma. | the grandmother lost and frightened inside the hug, staring into the distance; no smile |
| S27 | F3 → V2 | `S14c_V_S27` | 4 s | 1,6 s | — | BG_B_BOXES, CS_GLORIA_2 | (câm) | the grandmother quiet, sad and resigned, her face closed; no smile |
| S28 | F3 → V2 | `S14c_V_S28` | 4 s | 1,8 s | — | BG_D_FIX, CS_DOROTHY, CS_FRIEND_DAUGHTER, CS_GLORIA_2 | (câm) | the friend and her daughter smiling and waving warmly at each other; the grandmother watching them, wistful and curious |
| S29 | F3 → V2 | `S14c_T_S29` | 6 s | 3,2 s | 4.2 | BG_D_FIX, CS_GLORIA_2 | GLORIA: Wasn't she the one PUSHING you into Wrenfield? | the grandmother surprised and curious, one eyebrow lifting |
| S30 | F3 → V3 | `S14c_T_S30` | 6 s | 1,3 s | 2.4 | BG_D_FIX, CS_DOROTHY | DOROTHY: She sure was. | the friend dry and amused, a knowing little smile |
| S31 | F3 → V3 | `S14c_T_S31` | 6 s | 4,0 s | 4.4 | BG_D_FIX, CS_GLORIA_2, CS_DOROTHY | GLORIA: Now she's here every Sunday, taking plates home. What CHANGED? | the grandmother genuinely curious, searching her friend's face; the friend calm and unhurried |
| S32 | F3 → V3 | `S14c_T_S32` | 6 s | 3,3 s | 4.2 | BG_D_FIX, CS_DOROTHY | DOROTHY: She told me my cooking tasted like soap. | the friend calm and matter-of-fact, as if it were nothing |
| S33 | F3 → V3 | `S14c_V_S33` | 4 s | 1,1 s | — | BG_D_FIX, CS_GLORIA_2 | (câm) | the grandmother stunned and still, the words hitting home |
| S34 | F3 → V3 | `S14c_T_S34` | 6 s | 1,4 s | 2.8 | BG_D_FIX, CS_GLORIA_2 | GLORIA: Mine too. | the grandmother vulnerable, recognition dawning in her eyes; no smile |
| S35 | F3 → V3 | `S14c_T_S35` | 6 s | 1,8 s | 3.6 | BG_D_FIX, CS_DOROTHY | DOROTHY: Show me your kitchen. | the friend calm and decisive |
| S36 | F3 → V3 | `S14c_T_S36` | 6 s | 1,7 s | 2.0 | BG_B_BOXES, CS_DOROTHY, PROP_SILICONE | DOROTHY: When'd you buy these? | the friend focused and probing as she examines the spatula |
| S37 | F3 → V3 | `S14c_T_S37` | 6 s | 4,0 s | 5.0 | BG_B_BOXES, CS_GLORIA_2 | GLORIA: After Thanksgiving. Terrance sent me an article about black plastic. | the grandmother a little defensive, explaining herself; no smile |
| S38 | F3 → V3 | `S14c_T_S38` | 6 s | 2,5 s | 2.8 | BG_B_BOXES, CS_DOROTHY, PROP_SILICONE | DOROTHY: And when did the soap start? | the friend knowing and patient, one eyebrow raised |
| S39 | F3 → V3 | `S14c_V_S39` | 4 s | 1,0 s | — | BG_B_BOXES, CS_GLORIA_2 | (câm) | the grandmother thinking hard, counting back the weeks |
| S40 | F3 → V3 | `S14c_T_S40` | 6 s | 1,3 s | 2.0 | BG_B_BOXES, CS_GLORIA_2 | GLORIA: Christmas. | the grandmother shaken as the realization dawns, her eyes widening; no smile |
| S41 | F3 → V3 | `S14c_T_S41` | 6 s | 1,2 s | 1.2 | BG_B_BOXES, CS_DOROTHY, CS_GLORIA_2, PROP_SILICONE | DOROTHY: Smell it. | the friend firm and serious; the grandmother wary and doubtful; nobody smiles |
| S42 | F3 → V3 | `S14c_T_S42` | 6 s | 1,8 s | 2.6 | BG_B_BOXES, CS_GLORIA_2, PROP_SILICONE | GLORIA: That's my DISH soap. | the grandmother wary, about to sniff; no smile |
| S43 | F3 → V3 | `S14c_T_S43` | 6 s | 2,8 s | 3.2 | BG_B_BOXES, CS_DOROTHY, PROP_SILICONE | DOROTHY: It soaks up whatever soap you use. | the friend calm and plain, like someone who has been through it |
| S44 | F3 → V3 | `S14c_V_S44` | 4 s | 3,2 s | — | BG_B_BOXES, PROP_SILICONE | DOROTHY: The minute it gets hot, out it comes. | — |
| S45 | F3 → V3 | `S14c_T_S45` | 6 s | 2,1 s | 2.4 | BG_B_BOXES, CS_GLORIA_2 | GLORIA: But I can't taste it. | the grandmother troubled, still defending herself; no smile |
| S46 | F3 → V3 | `S14c_T_S46` | 6 s | 3,7 s | 4.0 | BG_B_BOXES, CS_DOROTHY | DOROTHY: Neither could I. Cook's always the last to notice. | the friend gentle, with a sad, knowing smile |
| S47 | F4 → V3 | `S14c_T_S47` | 6 s | 4,2 s | 5.4 | BG_B_BOXES, CS_DOROTHY, PROP_SILICONE | DOROTHY: They tested silicone baking pans. In the oven, chemicals leached out. | the friend serious and plain, not preachy; no smile |
| S48 | F4 → V3 | `S14c_V_S48` | 4 s | 3,3 s | — | BG_B_BOXES, CS_GLORIA_2, PROP_SILICONE | DOROTHY: Some of them are linked to hormone disruption. | the grandmother alarmed: eyes wide and fixed on the pan, lips slightly parted, jaw tight; her skin keeps exactly its warm medium-deep brown tone; no smile |
| S49 | ảnh thật → V3 | `S14c_V_S49` | 4 s | 1,8 s | — | IMG_ACA_TOWEL | (câm) | — |
| S50 | F4 → V4 | `S14c_T_S50` | 6 s | 3,1 s | 3.6 | BG_B_BOXES, CS_DOROTHY, IMG_ACA_SET, IMG_ACA_TOWEL | DOROTHY: I threw all mine out and got these. | the friend plain and confident, a small easy smile |
| S51 | F4 → V4 | `S14c_T_S51` | 6 s | 3,2 s | 3.6 | BG_B_BOXES, CS_GLORIA_2, IMG_ACA_SET | GLORIA: Wood? The cheap ones bleed in the pot. | the grandmother skeptical, with a doubtful frown |
| S52 | F4 → V4 | `S14c_T_S52` | 6 s | 2,4 s | 2.8 | BG_B_BOXES, CS_DOROTHY | DOROTHY: That's the finish, not the wood. | the friend certain and calm |
| S53 | ảnh thật → V4 | `S14c_V_S53` | 6 s | 4,7 s | — | IMG_ACA_MACRO | DOROTHY: Every piece is one block of wood. No glue. Nothing painted on. | — |
| S54 | F4 → V4 | `S14c_T_S54` | 6 s | 3,6 s | 4.6 | BG_B_BOXES, CS_DOROTHY | DOROTHY: They're called Acawood. I just texted you the link. | the friend pleased and practical, with a small smile |
| S56 | F4 → V4 | `S14c_T_S56` | 6 s | 2,2 s | 3.0 | BG_B_BOXES, CS_DOROTHY, IMG_ACA_SET, IMG_ACA_TOWEL | DOROTHY: Keep these till yours come. | the friend kind and matter-of-fact, with a warm look |
| S57 | F4 → V4 | `S14c_T_S57` | 6 s | 2,4 s | 3.4 | BG_B_BOXES, CS_TERRANCE_2 | TERRANCE: Movers come Saturday at nine, Mama. | the son businesslike and tired, not meeting her eyes; no smile |
| S58 | F4 → V4 | `S14c_T_S58` | 6 s | 1,3 s | 2.2 | BG_B_BOXES, CS_GLORIA_2, PROP_SILICONE | GLORIA: Smell this first. | the grandmother calm and firm, chin up; no smile |
| S59 | F4 → V4 | `S14c_T_S59` | 6 s | 2,5 s | 3.4 | BG_B_BOXES, CS_TERRANCE_2 | TERRANCE: Mama. This isn't about a SPATULA. | the son worn out and exasperated, never contemptuous; no smile |
| S60 | F4 → V4 | `S14c_T_S60` | 6 s | 1,4 s | 2.2 | BG_B_BOXES, CS_GLORIA_2 | GLORIA: Smell it, Terrance. | the grandmother hard and steady, not backing down; no smile |
| S61 | F4 → V4 | `S14c_V_S61` | 4 s | 1,2 s | — | BG_B_BOXES, CS_TERRANCE_2, PROP_SILICONE | (câm) | the son reluctant, eyes narrowed as he sniffs; no smile |
| S62 | F4 → V4 | `S14c_T_S62` | 6 s | 1,4 s | 3.2 | BG_B_BOXES, CS_TERRANCE_2, PROP_SILICONE | TERRANCE: That's dish soap. | the son stunned and quiet as the truth sinks in; no smile |
| S63 | F4 → V4 | `S14c_T_S63` | 6 s | 3,3 s | 3.6 | BG_B_BOXES, CS_GLORIA_2, IMG_ACA_SET | GLORIA: Now Dorothy's. She cooks with it every day. | the grandmother calm and composed, quietly confident, testing him |
| S64 | F4 → V4 | `S14c_T_S64` | 6 s | 1,2 s | 2.4 | BG_B_BOXES, CS_TERRANCE_2, IMG_ACA_SET | TERRANCE: Nothing. | the son reluctant, searching hard for something wrong; no smile |
| S65 | F4 → V4 | `S14c_T_S65` | 6 s | 2,5 s | 2.8 | BG_B_BOXES, CS_GLORIA_2 | GLORIA: One sniff. My nose is FINE. | the grandmother dry and proud, chin up |
| S66 | F4 → V4 | `S14c_T_S66` | 6 s | 3,2 s | 4.2 | BG_B_BOXES, CS_GLORIA_2, CS_TERRANCE_2, PROP_SILICONE | GLORIA: You're the one who sent me that article. | the grandmother pointed and a little bitter; her son caught out; nobody smiles |
| S67 | F4 → V4 | `S14c_T_S67` | 6 s | 2,6 s | 3.2 | BG_B_BOXES, CS_TERRANCE_2 | TERRANCE: Smelling's one thing, Mama. Tasting's another. | the son defensive, avoiding her eyes; no smile |
| S68 | F4 → V4 | `S14c_T_S68` | 6 s | 3,6 s | 4.6 | BG_B_BOXES, CS_GLORIA_2 | GLORIA: Friday night, I'm making my potato salad. Everybody comes. | the grandmother measured and in charge, composed; no smile |
| S69 | F4 → V4 | `S14c_T_S69` | 8 s | 5,8 s | 6.4 | BG_B_BOXES, CS_GLORIA_2 | GLORIA: If anybody tastes soap, I'll get in your car Saturday and never say a word. | the grandmother steady and absolute, unblinking; no smile |
| S70 | F4 → V4 | `S14c_T_S70` | 6 s | 1,3 s | 1.4 | BG_B_BOXES, CS_TERRANCE_2 | TERRANCE: Deal. | the son quiet and serious, accepting the bet; no smile |
| S71 | F5 → V5 | `S14c_V_S71` | 4 s | 1,8 s | — | MASTER_A_FRI, CS_GLORIA_3, CS_TERRANCE_3, CS_JADA_2, CS_WIFE, CS_GRANDSON, IMG_ACA_SET | (câm) | everyone at the table quiet and tense, watching the grandmother; the grandmother composed and determined; nobody smiles |
| S72 | F5 → V5 | `S14c_T_S72` | 6 s | 3,1 s | 3.8 | MASTER_A_FRI, CS_GLORIA_3, CS_JADA_2, CS_TERRANCE_3, IMG_ACA_SET | GLORIA: Jada. You first. You're the honest one. | the grandmother steady and loving, looking her granddaughter straight in the eye; the granddaughter nervous; her father tense; nobody smiles yet |
| S73 | F5 → V5 | `S14c_V_S73` | 4 s | 2,0 s | — | MASTER_A_FRI, CS_JADA_2, CS_TERRANCE_3 | (câm) | the granddaughter nervous as she takes the bite; her father tense, holding his breath; nobody smiles |
| S74 | F5 → V5 | `S14c_T_S74` | 6 s | 1,2 s | 1.4 | MASTER_A_FRI, CS_JADA_2, CS_TERRANCE_3 | JADA: Grandma. | the granddaughter amazed, her eyes going wide, not yet smiling |
| S75 | F5 → V5 | `S14c_T_S75` | 6 s | 1,9 s | 2.0 | MASTER_A_FRI, CS_JADA_2, CS_TERRANCE_3 | JADA: There's no soap. NONE. | the granddaughter bursting with relief and joy, laughing, eyes wet |
| S76 | F5 → V5 | `S14c_V_S76` | 4 s | 1,6 s | — | MASTER_A_FRI, CS_TERRANCE_3, CS_JADA_2 | (câm) | the son moved, his eyes reddening as the truth hits him; no smile |
| S77 | F5 → V5 | `S14c_T_S77` | 6 s | 2,0 s | 2.0 | MASTER_A_FRI, CS_TERRANCE_3, CS_JADA_2 | TERRANCE: Mama. I'm so sorry. | the son ashamed and sorry, eyes red, his voice about to break; no smile |
| S78 | F5 → V5 | `S14c_V_S78` | 4 s | 1,6 s | — | BG_A_FRI, CS_TERRANCE_3, PROP_BROCHURE | (câm) | the son resolved and relieved, his jaw set |
| S79 | F5 → V5 | `S14c_T_S79` | 6 s | 1,8 s | 2.0 | MASTER_A_FRI, CS_GLORIA_3 | GLORIA: Unpack my bowls, Terrance. | the grandmother half laughing, half crying, joy and relief together |
| S80 | F5 → V5 | `S14c_T_S80` | 6 s | 1,1 s | 0.8 | MASTER_A_FRI, CS_JADA_2, CS_TERRANCE_3 | JADA: Seconds? | the granddaughter playful and happy, grinning; her father smiling beside her |
| S81 | F5 → V5 | `S14c_V_S81` | 4 s | 1,8 s | — | MASTER_A_FRI, CS_TERRANCE_3, CS_JADA_2, CS_GLORIA_3, CS_WIFE, CS_GRANDSON, IMG_ACA_SET | (câm) | everyone laughing and relaxed, warm and happy |
| S82 | F6 → V6 | `S14c_T_S82` | 6 s | 4,7 s | 5.2 | BG_B_CLEAR, CS_GLORIA_4, PROP_SILICONE, IMG_ACA_HOLDER | GLORIA: My son almost moved me out of my own kitchen. Over THIS. | the grandmother warm and dry, with a slightly mischievous smile |
| S83 | F6 → V6 | `S14c_T_S83` | 6 s | 4,2 s | 5.4 | BG_B_CLEAR, CS_GLORIA_4 | GLORIA: Before anybody tells you you've lost your touch, smell your spatula. | the grandmother warm and knowing, like a friend giving advice |
| S84 | F6 → V6 | `S14c_T_S84` | 6 s | 3,9 s | 5.0 | BG_B_CLEAR, CS_GLORIA_4, PROP_SILICONE, IMG_ACA_HOLDER | GLORIA: If it smells like dish soap, so does your dinner. | the grandmother dry and good-humored |
| S85 | F6 → V6 | `S14c_T_S85` | 8 s | 5,8 s | 7.2 | BG_B_CLEAR_REV, CS_GLORIA_4, CS_TERRANCE_4, IMG_ACA_SET | GLORIA: And if it's your wife's cooking, or your mama's? Smell HERS before you blame her. | the grandmother warm, with a gentle warning in her eyes; her son in the background content as he tastes |
| S86 | F6 → V6 | `S14c_T_S86` | 8 s | 5,7 s | 6.4 | BG_B_CLEAR, CS_GLORIA_4, IMG_ACA_HOLDER | GLORIA: Mine are Acawood now. Seven pieces, each one cut from a single block of wood. | the grandmother proud and clear, with a warm smile |
| S87 | F6 → V6 | `S14c_V_S87` | 6 s | 5,5 s | — | BG_B_CLEAR, IMG_ACA_SET, IMG_WATERTEST | GLORIA: Nothing on them but oil or wax. Here's one in hot water. Still clear. | — |
| S88 | F6 → V6 | `S14c_V_S88` | 4 s | 1,7 s | — | BG_B_CLEAR, CS_GLORIA_4, IMG_ACA_HOLDER | GLORIA: Hand wash, dry, done. | the grandmother calm and content |
| S89 | F6 → V6 | `S14c_T_S89` | 8 s | 6,5 s | 6.8 | BG_B_CLEAR, CS_GLORIA_4, IMG_ACA_HOLDER | GLORIA: Eighty-nine ninety-five with the holder. Free shipping in the U.S., and ninety-day returns. | the grandmother plain and friendly, no sales grin |
| S90 | F6 → V6 | `S14c_T_S90` | 6 s | 3,9 s | 4.0 | BG_B_CLEAR, CS_GLORIA_4 | GLORIA: The link's right below. And my kitchen? Still MINE. | the grandmother warm and triumphant, smiling |

## 7. Rủi ro / cần Nam kiểm

- **Mâu thuẫn cần Nam chốt:** skill toby-workflow (21/10) ghi `quantity 1` mọi node; chat cũ chốt ảnh x4, video x2. Bản này theo chat (x2 video = gấp đôi credit video). Muốn quay về x1 thì báo Claude, hoặc sửa số lượng trên node video.
- Prompt clip nói 472–600 từ, clip câm 206–380 từ: dài hơn mức 180–300 của doc 25 vì giữ nguyên khối Object lock và khối People/da (skill: clip có khối khóa vật thể tới ~600 từ vẫn chạy tốt, S12 v3).
- Bỏ khung cuối thì mặt, đồ dễ trôi hơn khi nhân vật cử động nhiều: mỗi clip có 2 bản để chọn. Clip nào cả 2 bản đều trôi thì báo, Claude thêm lại khung cuối cho riêng clip đó hoặc bớt động tác.
- Nhịp dựng: trung bình 2,65 s/shot (gần Titanox ~2,7 s). 5 shot dài hơn 5 s, dễ thành cảnh đứng: S89 6,5 s, S85 5,8 s, S69 5,8 s, S86 5,7 s, S87 5,5 s → khi dựng chia đôi bằng một lần punch-in hoặc chèn b-roll giữa câu.
- Hai bà cùng tóc bạc ngắn: phân biệt bằng tông da (Dorothy sẫm hơn), mặt (Gloria tròn, Dorothy dài), kính (Gloria treo dây trước ngực, Dorothy đeo trên mặt), dáng (Gloria đầy đặn, Dorothy cao gầy). Sheet ra giống nhau thì báo Claude.
- Nếu V1 vẫn không import được: gửi Claude dòng báo lỗi và file export của một workflow video mới nhất Nam chạy được (menu ⋮ → Export) để so từng trường. File F chỉ có ảnh như 0A/0B nên sẽ vào.
- Trường node video theo file export 04b/05 (Script 11) của Nam; khung nối vào `frame_1` + `frame_1_source` theo luật Script 11 (thiếu frame_1 Toby báo "Chế độ video theo khung hình cần có ảnh tham chiếu"). Không còn node `TAI`.
- Tải tay: 98 khung vào file clip. Có Toby MCP thì Claude gắn hộ.
- Chưa đọc được Doc 56, 25, 47, 63, 72, 80 và Toby Flow 01, 02 (phiên cloud không có Projects); nên rà lại theo checklist Doc 56.
- Claim: "hormone disruption" đã duyệt; Meta từ chối thì thay "Ones you don't want in your food." (chỉ đổi file giọng S48, clip câm không phải gen lại).
- Làm sáng bếp bằng lệnh sửa ảnh có thể đổi nhẹ ảnh tủ lạnh, quạt giấy: duyệt lại như lần sửa 4 chỗ trước (ảnh tủ lạnh toàn người lớn da đen, quạt không chữ). Bếp sáng mà vẫn trông như phòng khác (tủ, cửa sổ đổi chỗ) thì chọn bản khác trong 4 ảnh hoặc chạy lại.
- Ảnh nền hiên nhà đêm (`BG_C`), hiên nhà Dorothy (`BG_D`), phòng ăn thứ Sáu (`BG_A_FRI`) Claude chưa xem ảnh thật: Nam gửi ảnh đã chọn thì Claude kiểm độ sáng, màu như bếp.
- Mọi khung phòng ăn phụ thuộc ảnh mẫu: ảnh 0C (hoặc 0D) có ai ngồi sai thì sai cả file, nên duyệt kỹ ảnh mẫu trước. Model có thể trả lại gần như nguyên ảnh rộng thay vì phóng gần: chọn bản khác trong 4 ảnh; cả 4 đều không phóng thì báo Claude.
- 3 ảnh hướng ②③④ (0E) là phần phòng chưa ảnh nào thấy, model tự vẽ theo phòng chuẩn: chọn ảnh cùng màu tường, bàn, ghế, khăn ren với ảnh 0A; đồ trên tường đúng thứ tự trong sơ đồ.
- Nhân vật AI: bật nhãn nội dung AI khi chạy ads.
