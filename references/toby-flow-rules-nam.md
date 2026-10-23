# Luật video Acawood / Woodsen của Nam — TobyFlow, Google Flow, Omni, Seedance

> **Reference file** — Đọc trước khi viết prompt ảnh/video, workflow TobyFlow, lời thoại hay hướng dẫn dựng cho Nam (Acawood, Woodsen). Đi cùng skill `toby-workflow`.
> Nguồn: chat cũ của Nam (Script 6B → 13, tháng 10/2026, Nam dán lại ngày 21/10) + skill `toby-workflow` (cập nhật 21/10) + bài học S14c (21/10).
> Thứ tự khi mâu thuẫn: lời Nam mới nhất → skill `toby-workflow` → file này. Còn mâu thuẫn thì **hỏi Nam cái nào thắng**, không tự bỏ yêu cầu nào.

---

## 1. Cách làm việc với Nam

- Trả lời tiếng Việt, ngắn; prompt viết tiếng Anh.
- Không âm thầm bỏ một yêu cầu Nam đã nêu. Hai yêu cầu xung đột → hỏi Nam cái nào thắng.
- Không tự thêm chi tiết Nam không yêu cầu. Muốn thêm → đề xuất riêng, kèm lý do, để Nam chọn.
- Chỉ sửa đúng chỗ Nam bảo sửa.
- Nam đang chạy dở: đưa prompt đã sửa + **tên node chính xác** để dán, không đưa cả file mới. Nam xin prompt đầy đủ → đưa bản copy được nguyên khối.
- Trước khi viết Action cho clip: xem khung `F_xx` Nam đã chọn, viết theo ảnh thật (tay nào cầm, đồ nằm đâu).
- Áp sẵn mọi bài học ngay từ lần đầu: doc 25 (cẩm nang Omni), 05-F7 (luật hình), 47 (prompt đã đạt), 56 (checklist) trong Projects "Woodsen" / "Toby Flow" của Nam. Nam rất khó chịu khi phải sửa lại cùng một lỗi.
- Nhắc nhịp dựng khi nhiều cảnh tĩnh: Titanox ~2,7 s/shot, mẫu bác sĩ ~1,7 s/shot; không cảnh tĩnh nào quá 4–5 s.

## 2. Mặc định khi tạo

| Mục | Mặc định |
|---|---|
| Số ảnh mỗi node (Nano Banana Pro) | x4 — ảnh không tốn credit, "cứ max". Bị UNUSUAL_ACTIVITY thì tăng delay, đừng hạ số ảnh |
| Số video mỗi node | x2 |
| Độ dài video | 6 s mặc định; Flow có 4/6/8/10 s, chọn theo slot. Clip nói: công thức ở mục 4. Clip câm: 4 s |
| Lip-sync bằng file audio của Nam | Dùng nguyên file (không cắt, không đệm); độ dài clip = số giây nguyên kế tiếp, không dùng số lẻ |

> ⚠ **Chưa chốt:** skill `toby-workflow` (21/10) ghi `quantity = 1` mọi node; chat cũ chốt ảnh x4, video x2. S14c (21/10) theo x4/x2. Cần Nam chốt để sửa một trong hai nguồn.

## 3. TobyFlow / Google Flow

- Video chế độ **Frames**: ảnh khung đầu vào `frame_1` (input_3) + `frame_1_source`. Thiếu → Toby báo "Chế độ video theo khung hình cần có ảnh tham chiếu". `image_ref` (input_1) chỉ dùng cho node tạo ảnh.
- **Clip nói không cần giữ dáng (Nam 22/10, S14c):** chỉ `frame_1`, để nhân vật biểu cảm và có động tác như phim. Thay luật cũ "cùng một ảnh vào cả `frame_1` và `frame_2`" (khung cuối ép clip kết thúc đúng ảnh đầu nên người đứng yên nói). Chỉ thêm lại khung cuối cho riêng clip nào mà cả 2 bản đều trôi mặt/đồ, hoặc khi Nam yêu cầu.
- Chế độ **Ingredients** làm đạo cụ nhảy chỗ → dùng **Frames**.
- Toby tải mặc định 360p → đặt `video_download_resolution "1080p"`.
- Tên workflow < ~100 ký tự, không có "/" (tên 145 ký tự lỗi).
- File import: ≤ ~97 KB và ≤ ~85 node mỗi file. Đã lỗi: 193 KB / 167 node, 114–158 KB (S14c). Đã chạy: 97 KB / 85 node, 42 KB.
- Node video trong file JSON phải đúng định dạng file Toby cũ của Nam (Script 11 04b/05): `"video_duration": "6s"` (chữ, có đuôi s, không phải số), `"download_resolution": "1080p"`, có `prompt_mode`/`ref_mode` "all". S14c (22/10) ghi số 6 và "1k": mọi file có node video đều không import được, kể cả file 9 KB; file chỉ có ảnh vẫn vào. Khung: dây vào `frame_1`/`frame_2` + `frame_ref_mode "upstream_node"`, `frame_1_source`. Không dùng node `TAI` trong file import; Auto Download tải 1080p theo `video_download_resolution`.
- Không phụ thuộc trong cùng file: Album / ảnh tham chiếu phải đến từ file chạy **trước**. Character sheet đổi đồ đặt ở file sau, tải sheet gốc đã chọn vào node `IMG_`. S14c (22/10) nối trong cùng file → 7 sheet đổi đồ ra người lạ.
- Luật này áp cả cho khung → clip: **file khung** (chỉ node `F_`, ảnh x4) chạy trước, Nam chọn 1 khung đạt trong 4, tải vào node ảnh của **file clip** (Script 11: file 04b chỉ có clip + node `Album F_xx`; S14c: `F1…F4` rồi `V1…V4`, node `IMG_F_<cảnh>`). Không nối `F_` thẳng vào clip trong cùng file: clip sẽ chạy trên khung chưa duyệt. Clip nào cần khung cuối thì nối cùng node ảnh tải lên vào cả `frame_1` và `frame_2`.
- **Cảnh nhiều người quanh một bàn (Nam 23/10, S14c):** lượt F1 đầu ra mỗi khung một kiểu chỗ ngồi, có người lạ, túi quà và brochure mỗi khung một chỗ. Cách làm:
  - Khóa **sơ đồ chỗ ngồi** (theo docx) và **danh sách người**: "Only these N people…; no other guests, no other children, nobody else in the room."
  - Người phụ docx chỉ ghi chung ("2–3 relatives", "the family") phải tả cố định: vai, tuổi, da, tóc, đồ từng ngày. Không viết "relatives", "the rest of the family" chung chung.
  - Tạo một **ảnh mẫu bàn ăn** ở file setup riêng (0C): sửa từ ảnh nền phòng + sheet, cùng góc máy với ảnh nền, đủ người đúng ghế. Nam chọn ảnh, rồi tải vào mọi khung cảnh bàn ăn: "use it only to know who sits where…". Bữa sau cùng bàn cũng dùng ảnh này.
  - Khung rộng dùng đúng góc máy của ảnh mẫu. Khung cận ghi máy đặt bên nào, ai trong khung, sau lưng ai là gì, và thêm câu "everyone not described here is out of the frame".
  - Đạo cụ quan trọng (quà, brochure, bánh) ghi chỗ cố định và lộ trình theo từng cảnh. Cái chưa xuất hiện thì ghi rõ là chưa có ("No birthday cake on the table yet").
  - Sheet chỉ ghi đồ chung chung ("nice dinner clothes") thì khung lấy đồ từ sheet ("the same outfit as in her character sheet"), không tả lại bằng chữ khác.
  - **Mọi khung trong phòng có bàn đông người phải là ảnh mẫu được sửa (duyệt F1 S14c, 23/10).** Ảnh mẫu chỉ làm "tham chiếu ai ngồi đâu" thì model vẫn tự dựng lại bàn cho từng khung và dựng sai gần hết: Jada ra trước tường băng rôn như ngồi ghế đầu bàn, Terrance sang dãy đối diện, tủ buffet dời tường. Thêm ảnh nền nhìn từ bên kia bàn cũng không cứu được, vì model vẫn tự dựng. Cách làm: Image 1 là ảnh mẫu đã chọn, prompt "Edit Image 1… keep the room, the camera position and its direction, every person's chair…", khung chỉ phóng gần từ cùng chỗ đặt máy và đổi hành động, biểu cảm; sheet nhân vật chỉ để giữ mặt. Bữa khác cùng bàn (tối thứ Sáu) thì sửa ảnh mẫu một lần ra ảnh mẫu mới (đổi đồ, bỏ trang trí) rồi các khung sửa từ ảnh đó. Không quay ngược hướng (từ bên kia bàn).
  - Khung có lời mà tay đưa lên gần miệng (thì thầm, che miệng): ghi "her fingers clear of her lips and her lips in view", không thì Omni không khớp miệng được.
  - **Muốn quay nhiều hướng trong cùng phòng (Nam 23/10):** viết "phòng chuẩn": mỗi bức tường có gì theo thứ tự, sau lưng từng ghế là gì, đồ nào chỉ có ở ngày nào. Làm 1 ảnh nền trống cho mỗi hướng máy, sửa từ ảnh nền gốc và không để đồ trang trí theo ngày, để mọi ngày dùng chung (S14c: 0E, sơ đồ `S14c_PhongAn_4Huong.png`). Khung quay hướng nào thì dùng ảnh nền hướng đó và ghi "behind X: …" đúng phòng chuẩn. Hướng nào lộ mặt trẻ em thì cắt khung tránh ghế đó.
- Rà nối cảnh trước khi giao (bài học rà độc lập S14c, 23/10):
  - Người ngoài khung đang đứng ở chỗ X thì đừng tả X sau lưng người trong khung. Model sẽ kéo người đó vào khung hoặc dời X đi.
  - Đồ đã đặt xuống ở cảnh trước thì cảnh sau tả đúng chỗ đó. Đồ lại nằm trên tay thì phải có động tác cầm lên.
  - Hook thay cảnh mở đầu phải nối được với cảnh chung phía sau: ai đứng, ai ngồi, tay đang cầm gì.
  - Đếm sản phẩm: một món trên tay thì trong ống còn 6, ghi "the rest of the set".
  - Một vật chỉ có một chỗ. Câu đồ ("tote bag on her shoulder") mâu thuẫn với khung thì sửa ngay trong khung.
  - Thẻ chữ thời gian phải phân biệt được ngày (THE FOLLOWING SUNDAY, không chỉ SUNDAY).
- Chia file khung/clip **theo cảnh** (vd. tiệc sinh nhật | bếp, hiên | tối thứ Sáu | Close): sửa một cảnh thì chỉ chạy lại một file.
- **Ánh sáng ảnh nền (Nam 23/10, S14c "quá tối hay quá cổ điển"):** khung nào cũng chép "same light" của ảnh nền, nên một ảnh nền tối làm tối cả chục khung. Duyệt độ sáng, màu ảnh nền trước khi chạy 0B và file khung:
  - Bếp, phòng ở cảnh ban ngày phải sáng, đồ trắng ra trắng (không xám, không ngả xanh), góc phòng không chìm. Cảnh đêm theo docx vẫn được tối, nhưng ghi "faces softly lit… never pitch black" để da nâu không ra xám, mất biểu cảm.
  - Ảnh sửa từ ảnh nền (đổi giờ, thêm thùng, vài tuần sau) phải ghi rõ ánh sáng mới trong "Change only"; chỉ ghi ở dòng Look thì model giữ ánh sáng ảnh gốc.
  - Nhà cổ điển đúng kịch bản (nhà 42 năm, bếp gas cũ) thì giữ đồ đạc. Cảm giác "cũ kỹ" thường do ánh sáng tối, ám vàng cam, chứ không do đồ: sửa ánh sáng, không hiện đại hoá đồ.
  - Ám màu chung (vàng cam) mà ảnh đủ sáng thì chỉnh ở CapCut bằng một lớp điều chỉnh cho cả cảnh, không gen lại. Ảnh tối, góc chìm thì sửa ở gốc, đừng kéo sáng ở CapCut (da ra xám, nhiễu).
  - Làm sáng ảnh nền: sửa một lần từ ảnh gốc (gộp với các sửa khác), không sửa chồng lên ảnh đã sửa.
- Settings: parallel off, delay 15–30 s, Humanized mode, retry 1, Auto Download on, tên file `[Index]_[Date]_[Time]`.
- UNUSUAL_ACTIVITY: khoảng 25 lần nâng cấp (upscale) mỗi giờ. Xoá cookie flow.google.com rồi tải lại trang là reset.
- Tải 1080p hàng loạt: từ lưới project, menu ⋮; đổi tên tile trước để file về đúng thứ tự.
- Flow có chế độ sửa video → video (xoá được phụ đề cháy vào hình).

## 4. Omni 1.1 Flash

**Lời và giọng**
- Lời viết trong ngoặc kép, Omni tự nói để khớp miệng. Dựng xong → ElevenLabs Voice Changer một lượt cho cả đoạn: Multilingual v2 STS, Stability 50, Similarity 85, Style 0, Remove background noise. Voice Changer giữ nhịp nên miệng vẫn khớp. Nhiều nhân vật → tách lời từng người, mỗi người một giọng đích.
- Omni tạo lại một phần tiếng, lệch 0,1–0,3 s.
- ≤ 2,5 chữ/giây; lời bắt đầu ở 0,4 s (1,0 s nếu có động tác trước khi nói); chừa 0,6 s cuối.
- Omni hay ậm ừ, cười khẽ sau câu → thêm "lips close and stay closed, no sound"; khi dựng cắt ở cuối câu + 0,4 s.
- Chế độ sửa video: hễ nhắc tới speech / audio / words là Flow từ chối.

**Prompt**
- 180–300 từ (doc 25). Clip có khối Object lock tới ~600 từ vẫn chạy tốt (skill, S12 v3).
- Một hành động chính mỗi clip, bắt đầu trong giây đầu.
- Clip nói diễn như phim (Nam 22/10): nhịp chính trong giây đầu + cử chỉ theo từng cụm lời (gật, lắc đầu, chỉ, mở tay, nghiêng người) + người nghe trong khung phản ứng không nói + một nhịp im lặng sau câu (mím môi, nhìn xuống, gật). Không viết "đứng yên nói", "giữ nguyên". Động tác trước lời (đứng dậy, ngửi, gục đầu) → lời bắt đầu 1,0 s. Tay không che miệng khi đang nói. Đồ đang cầm: "moves only together with their hand" (không dùng "same grip, length and angle"). Sản phẩm trong ống/trên khăn: "every wooden piece stays exactly in place". Không cử chỉ "sassy" (mục 8).
- "Real-time pace, nothing slow-motion". Cấm: slow motion, slowly, cinematic, smooth camera.
- Không bao giờ dùng chữ "phone" (dùng "handset").
- Máy locked-off giảm trôi đạo cụ. Selfie: khóa tay cầm máy, chỉ đung đưa nhẹ.
- Các khối phải có (mẫu ở mục 11):
  - **Living layer**: chỉ thứ đã có trong khung chuyển động, không thêm gì (không thêm côn trùng, bụi, người).
  - **Physical logic**: không vật nào tự chuyển động. Xoay, khuấy, nhấc, ép, thả đều có bàn tay người; thứ chảy, bốc hơi, sôi phải nằm trên bếp đang bật hoặc trong đồ nóng; vật nằm có trọng lượng; mọi chuyển động có nguyên nhân thấy được.
  - **People lock**: giữ mặt, tuổi, tóc, quần áo; không thêm hay đổi người.
  - **Hands**: năm ngón, cầm tự nhiên, không xuyên qua đồ.
  - **FACIAL PERFORMANCE + EMOTION BEATS** (clip nói): mặt không đơ, biểu cảm theo nghĩa từng cụm lời, có biểu cảm cho lúc im lặng cuối clip.
  - **Biểu cảm đúng ngữ cảnh (Nam 23/10):** mọi khung đầu có người phải ghi mặt từng người theo nhịp truyện: "Expressions true to this moment: …; natural and believable, never exaggerated or posed." Model ảnh không được dặn sẽ tự vẽ mặt cười, kể cả lúc căng, nên cảnh căng ghi "nobody smiles" / "no smile". Clip nhiều người có dòng "Expressions" cho người nghe (người nói đã có giọng điệu ở khối Speech). Tránh biểu cảm sai vai: người bị tổn thương thì đau mà giữ phẩm giá, không giận dữ kiểu định kiến; người nói thật thì không chê bai, ghê tởm; người sai thì thương mà sợ, không phải kẻ xấu; người cố vấn điềm tĩnh, khô hài, không "sassy".
  - Chuyển động tự nhiên, liền mạch; không liệt kê kiểu "uneven / irregular" (gây giật).

## 5. Seedance 2.0 / 2.5 (Higgsfield)

- Độ dài đặt trên giao diện, viết trong prompt không có tác dụng; 2.0: 4–15 s, 2.5: tới 30 s. 4 s quá ngắn cho câu 11 chữ.
- Gán vai cho @Audio1: "spoken ON CAMERA, not voice-over".
- Ghim khung đầu (image-to-video); 2.5 không ghim khung đầu.
- Prompt không chứa lời thoại, tên sản phẩm hay con số (model đổi chữ: "Solid acacia" → "Small leaf acacia").
- Không chữ IN HOA đứng riêng, không câu trong ngoặc kép ở phần timing → thành phụ đề trên hình.
- Thêm "clean plain footage, nothing overlaid"; tắt auto-captions.
- Bản 1080p: cứ 4 khung có 1 khung lặp (giật) → sửa bằng công cụ, không cần gen lại.
- Extend giữ khung hình của clip gốc. Thử ở độ phân giải thấp trước.

## 6. Ảnh (Nano Banana Pro)

- Khối "thật": kiểu máy smartphone / 35mm, da thật. Tránh: 8K, ultra detailed, hyperrealistic, cinematic, masterpiece, HDR, perfect, pristine, glossy, flawless, beautiful. Không ép nét: sharp, crisp, pores, smooth.
- Chép đúng da và khuyên tai từ ảnh mẫu; không làm già, không làm mịn.
- Khớp tỉ lệ người với ảnh mẫu (% đầu, vai trong khung). Dùng sketch bố cục phẳng làm ảnh tham chiếu bố cục.
- Không bao giờ đính khung của đối thủ làm ảnh tham chiếu: model chép cả ảnh.
- Cầm nắm: ngón tay ôm cán, đầu dụng cụ phía trên ngón cái, đuôi cán dưới ngón út; tả hình dạng; lấy lỗ treo làm mốc. Viết screen-left / screen-right, không viết "her left".
- Một tay một việc. Không xoay đồ nhỏ trong tay (xoay cổ tay thì được). Hành động nhiều vật → tách clip.
- Muốn giữ nguyên phần còn lại: dùng Select (sửa cục bộ).
- Mỗi lần sửa xuất phát từ ảnh gốc, không sửa chồng lên ảnh đã sửa (mặt lệch dần).
- Prompt "Edit Image 1" phải tả lại đủ người (tuổi, tông da, tóc, đồ đeo). Thiếu Image 1 thì model vẽ người ngẫu nhiên.
- Câu tham chiếu và Final check viết riêng từng người: chỉ nhắc kính, trang sức với người có đeo. Ghi chung "glasses and jewelry" là model gắn kính cho cả nhà.

## 7. Cụm chữ Google hay chặn

| Tránh | Dùng |
|---|---|
| "no extra or missing fingers" | "each hand has five fingers in natural proportion…" |
| "seen from behind", "from behind", "back to the camera", "bare hand" khi có người | góc nghiêng / over-the-shoulder, chỉ tay + cẳng tay, hoặc bỏ người |
| "woman shopper", "not horror" | tả bằng đồ vật, cánh tay áo |
| Chữ trên biển hiệu cửa hàng | Biển trống, thêm chữ ở CapCut |
| Người + lửa lớn + burn / melt / char | Bỏ lửa lớn hoặc bỏ người |
| "toxic", "poison" | Đổi lời, giữ ý |
| Cận tay người già cầm đồ; đồ ăn lẫn dị vật (ảnh); tả ảnh tham chiếu có người kèm "damaged"; "about 98, deeply wrinkled" | Xem skill `toby-workflow` mục 8 |

## 8. Nội dung

- Không mặt trẻ em: chỉ bàn tay, cẳng tay. Không máu. Không logo, nhãn hiệu thật. Moses không lộ mặt.
- Acawood phải đúng ảnh sản phẩm thật: ACA_set (7 món + ống), ACA_turner, ACA_spoon.
- **[FOOD-ACA]**: cảnh Acawood múc, đảo, lật, xới, bày → đồ ăn tươi, sáng màu, bày gọn; mặt bếp, nồi chảo, bàn sạch. Prompt có [FOOD-ACA] không được có crumbs / burnt / spill / splatter / dirty (kể cả dạng phủ định). Cái xấu chỉ ở cảnh failed solutions.
- Hư hại của failed solutions phải thấy rõ nhưng hợp lý vật lý. Tuỳ kịch bản: "cũ nhưng sạch" (S8) hoặc hỏng nặng, ảnh hưởng rõ tới đồ ăn (S6B, S11).
- B-roll ưu tiên chỉ có tay (S8). Cảnh có mặt (S10): tả như người thật (khối REAL_FACE).
- Màu bình thường, sáng (không tối kiểu phim kinh dị); cảnh Acawood tông ấm.
- Hook: 3 s đầu phải có điểm lạ, rồi cắt cứng.

**Nhân vật người Mỹ da đen** (S14c, 22/10; mẫu và nguồn ở `output/s14c-black-tobyflow-20261021/S14c_Black_NhanVat.md`):
- Không chỉ ghi "Black American". Mỗi người một độ sẫm + undertone riêng; gia đình thật có nhiều tông da. Ghi rõ thứ tự sẫm → sáng để duyệt.
- Tả nét mặt cụ thể và tóc đúng kết cấu: xoăn tít tự nhiên, tapered, TWA, low taper fade, knotless braids; con cháu có nét giống bố mẹ.
- Dấu tuổi của da nâu: ít nếp nhăn sâu, dưới mắt sẫm hơn, vài đốm nhỏ nâu sẫm trên gò má ở người lớn tuổi. Lòng bàn tay sáng hơn mu bàn tay.
- Khối da trong mọi ảnh có người: giữ độ sẫm và undertone, highlight mềm, giữ chi tiết vùng tối; không xám, tro, cam, không làm sáng da.
- Hai nhân vật dễ lẫn (hai bà tóc bạc) phải khác nhau ở tông da, khuôn mặt, chỗ đeo kính, dáng người.
- Ảnh trang trí trong nhà (tường, tủ lạnh, bàn thờ, kệ) phải ghi rõ là ảnh của chính gia đình đó, cùng chủng tộc, chỉ người lớn, ảnh nhỏ, hơi mờ, không chữ. Ghi chung "family photos" là model tự bịa người.
- Không để "the family", "the whole table", "everyone" chung chung: ghi rõ ai, người gì; người nền thêm vào phải ghi chủng tộc.
- Một căn phòng xuất hiện ở nhiều trạng thái (đêm, sáng, đóng thùng…): tạo một ảnh nền gốc, các trạng thái khác sửa từ ảnh gốc đó ở file sau. Tạo riêng từng ảnh từ chữ là mỗi cảnh một căn phòng.
- Đồ được cầm ở mép khung phải ghi rõ tay ai (tông da, tay áo, nhẫn); màn hình điện thoại quay đi hoặc chỉ sáng trơn, không chữ.
- Tránh định kiến: không khăn trùm kiểu người giúp việc, không "Big Momma", không gà rán hay dưa hấu làm trò, không cử chỉ "sassy".

**Không làm:** không clone hay lip-sync lại footage của đối thủ, không che phụ đề của họ; không dùng mặt nhân vật của đối thủ; không lách nhận diện nhạc bản quyền; không giữ API key của Nam; không đưa claim chưa kiểm lên màn hình (vd. "Naturally Antimicrobial", số review bịa).

## 9. Âm thanh và dựng

- ElevenLabs v3/v4 không có thanh tốc độ. Tag kiểu [rushed] nghe dở → không tag, bớt ngắt bằng dấu câu.
- Không viết hoa những chữ trùng chữ viết tắt ("US" bị đọc thành U-S).
- Nhạc −12 / −13 dB dưới giọng; master −14 LUFS, −1 dBTP.
- Xuất 1080p, 30 fps, H.264, AAC 48 kHz.
- Phụ đề giao: mp4 nền xanh chroma + SRT. Kiểu chữ: Montserrat Black trắng viền, 67% (6B); Poppins Bold 55% (S10, S11); hộp trắng chữ đen (S8).
- Banner: "IF … LISTEN CAREFULLY ⚠️", hộp trắng, chữ đỏ Montserrat ExtraBold, y 290–525; 6B có bản Goldie dễ thương.

## 10. Tự kiểm trước khi giao (bằng code)

- Ảnh x4, video x2 (hoặc theo Nam chốt); mọi video có `frame_1` + `frame_1_source` khớp; clip nói không có `frame_2` trừ khi Nam yêu cầu (22/10); tải 1080p.
- Không node nào (ảnh hay clip) lấy ảnh từ node tạo trong cùng file: khung `F_` và clip ở hai file khác nhau; prompt sửa ảnh có đủ mô tả người; chữ "glasses" chỉ xuất hiện với người có đeo kính.
- File ≤ ~97 KB, ≤ ~85 node; tên < 100 ký tự, không "/"; không phụ thuộc trong cùng file.
- Cảnh bàn ăn: mọi khung có ảnh mẫu bàn ăn + sơ đồ chỗ ngồi (khung rộng) hoặc câu "out of the frame" (khung cận); không người lạ; đạo cụ đúng chỗ theo cảnh.
- Mọi khung có người có dòng biểu cảm theo nhịp truyện; cảnh căng có "nobody smiles"; prompt clip ≤ ~600 từ.
- Ảnh nền sửa từ ảnh gốc ghi ánh sáng mới trong "Change only"; khung cảnh ban ngày trong nhà có câu sáng, đồ trắng ra trắng; khung cảnh đêm có câu đủ sáng mặt, "never pitch black".
- Không chữ cấm (mục 4, 6, 7); clip nói có "lips close and stay closed, no sound" và khối mặt; mọi clip có Living layer (dạng "only what is already in the frame…") và Physical logic.
- Có Acawood + đồ ăn → có [FOOD-ACA], không lẫn chữ bẩn.
- ≤ 2,5 chữ/giây, `end + 0,6 ≤ video_duration`; lời ghép lại = 100% kịch bản và SRT.

Code mẫu đã có các phép kiểm này: `output/s14c-black-tobyflow-20261021/code/verify14.py`.

## 11. Khối prompt mẫu (copy nguyên văn)

**Hands (ảnh)**
```
Every hand has five fingers in natural proportion and a natural grip; each person has exactly two arms and two hands; nothing floats.
```

**Physics and props (clip, bản gọn Nam đã duyệt)**
```
Physics and props: every object is solid and keeps its shape, size and place unless the action says otherwise; nothing bends, stretches, multiplies or disappears; hands keep five fingers and a natural grip and never pass through objects; nothing moves without a cause; nothing appears that the action does not bring in.
```

**Object lock (skill `toby-workflow` 5b2, S12 v3: 34 clip không biến dạng)**
```
Object lock: every utensil, container and prop in the picture is a rigid solid object that keeps exactly the same shape, size, length, color, number of pieces and the same wear or damage from the first frame to the last; nothing bends, stretches, melts, warps, splits, breaks, peels further, merges, multiplies, morphs or turns into something else; nothing appears, disappears or swaps places.
```

**Physical logic (S14c)**
```
Physics: real weight and balance; nothing moves on its own: whatever moves is moved by a visible hand or by the action.
```

**People**
```
People: everyone in the start frame keeps the same face, age, hair and clothes; nobody is added or replaced; bodies move with real weight, feet on the floor, joints bending the right way.
```

**Living layer**
```
Living layer (only what is already in the frame moves, nothing is added): every person in frame breathes and shifts weight naturally; reflections and highlights follow the movement; nothing in the frame is frozen.
```

**Sau câu thoại**
```
after the last word she keeps the same feeling in her face, lips close and stay closed, no sound.
```

**Mặt và người, bản gọn (phim nhiều nhân vật; Nam 22/10: biểu cảm rõ, có cử chỉ)**
```
Everyone else stays silent and reacts only with their face and body. Face and body: fully alive and in the moment, like a real person in this family scene; the feeling shows clearly in the eyes, brows, mouth and posture and changes with the meaning of each phrase, each new expression starting a split second before the words that carry it; natural gestures and small movements of the head, shoulders and hands while talking; never frozen, never a fixed smile, never over-acted.
```

**[FOOD-ACA] (S14c)**
```
Food with the wooden utensils: fresh, bright and appetizing, neatly served; the bowl, plates, pot, counter and table are clean and tidy.
```

**Selfie nói vào máy** (Nam đã duyệt; có chữ "smooth" ở chuyển động máy và người, khác với lệnh cấm "smooth camera" ở clip thường)
```
HANDHELD FEEL: because she is holding the camera herself, the camera is never locked still, but its movement is smooth and continuous: a slow, gentle, floating sway, as if it drifts softly with her breathing and the rhythm of her speech. All camera movement is soft and fluid, with no sudden corrections, no jumps, no jerks and no shaking. Her face stays roughly centered and the framing stays about the same distance the whole time.
```
```
NATURAL HUMAN MOTION: she moves like a real person filmed in real time, with smooth, relaxed, continuous movements — never robotic, never twitchy. Natural breathing, natural blinks, small head movements and facial expressions that follow her words. Her skin keeps its real texture in every frame. Real-time speed, smooth natural motion blur.
```
```
FACIAL PERFORMANCE: her face is alive and expressive the whole time, never frozen, never blank, never a fixed smile. Her expressions follow the meaning of what she is saying, moment by moment, and each new expression starts a split second before the words that carry it, the way real people's faces lead their speech. Emotion shows mainly through her eyebrows, eyes, the corners of her mouth, her cheeks and small movements of her head: brows lifting or drawing together, eyes widening, narrowing or softening, a quick glance away while she remembers something and then back to the lens, a small nod or head shake on key words, a slight tilt of the head when she is being sincere. Expressions change smoothly from one to the next, never jumping, never twitching. Her performance is natural and understated, like a real woman telling a story to a friend — never exaggerated, never theatrical, never like an actress in a commercial. Her eyes stay bright and focused, looking into the lens while she talks. Her lips and jaw move clearly and naturally with every word.
```

**EMOTION BEATS** (viết riêng cho từng đoạn, đặt ngay dưới lời thoại; mỗi cụm một cảm xúc chính, nhiều nhất hai; tả nét mặt cụ thể, không chỉ gọi tên cảm xúc)
```
EMOTION BEATS:
- "[cụm lời 1]": [cảm xúc + biểu hiện cụ thể trên mặt]
- "[cụm lời 2]": [cảm xúc + biểu hiện cụ thể trên mặt]
- After the last word: [biểu cảm giữ lại khi im lặng], lips closed.
```
Ví dụ:
```
EMOTION BEATS:
- "I used that black plastic spatula for thirty years,": slightly embarrassed — a small sheepish wince, eyes glancing down for a moment, then back to the lens.
- "and I never once thought about what was coming off it.": serious and a little troubled — brows drawing together, lips pressing for a beat after "it", a slow small shake of the head.
- "My daughter's the one who caught it.": warmth and pride creeping in — her eyes soften, the corners of her mouth lift slightly, a small nod.
- After the last word: she holds a soft, knowing look at the lens, lips closed.
```
