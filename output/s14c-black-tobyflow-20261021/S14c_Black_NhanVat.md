# S14c — Nhân vật gia đình Mỹ da đen (bản chuẩn 22-10)

Khung nhân vật cho cả script. Prompt tiếng Anh ở mục 5 là bản đang nằm trong `toby/workflow_S14c_0A_Setup.json` và `0B_DoiDo.json`.

## 1. Vì sao lượt ảnh trước sai

1. **Lỗi nối file (lỗi của Claude):** Setup cũ để 7 sheet đổi đồ (Gloria 2–4, Terrance 2–4, Jada 2) lấy ảnh gốc từ node nằm cùng file. Luật đã chốt là ảnh tham chiếu phải đến từ file chạy trước. Node đổi đồ không nhận được ảnh gốc.
2. **Prompt đổi đồ không tả người:** chỉ ghi "giữ nguyên người trong Image 1 … glasses and jewelry". Không có Image 1 thì model vẽ người ngẫu nhiên, đa số là người da trắng, và gắn kính cho tất cả vì có chữ "glasses". Đúng như ảnh Nam chụp: áo navy, sơ mi caro, gile xám đều ra người lạ đeo kính.
3. **Mô tả gốc quá mỏng:** mọi người đều chỉ có "Black American" + "warm brown skin", không có kết cấu tóc, nét mặt, khác biệt tông da hay dấu tuổi của da nâu. Model dễ ra người chung chung, cả nhà cùng một màu da.

## 2. Nghiên cứu (22-10)

- Model ảnh hay gộp "da sẫm" thành một tông. Cách chữa: ghi độ sẫm + undertone riêng từng người, tả nét mặt và kết cấu tóc cụ thể thay vì chỉ ghi chủng tộc ([Neolemon](https://www.neolemon.com/blog/skin-tones-names-prompting-guide/), [ImageGPT](https://imagegpt.cloud/learn/guides/prompting-dark-skin-tones)).
- Da nâu dễ ra xám, tro khi cân bằng trắng lệch lạnh; cần ánh sáng mềm, giữ chi tiết vùng tối, không làm sáng da ([SLR Lounge](https://slrlounge.com/photography-tips-3-tips-for-working-with-darker-skin-tones), [Canon](https://canon.co.uk/get-inspired/tips-and-techniques/capturing-natural-skin-tones), [ShootProof](https://shootproof.com/blog/how-to-photograph-a-variety-of-skin-tones)).
- Da sẫm ít nếp nhăn sâu và nhăn muộn hơn (khoảng 10–20 năm), nhưng dễ không đều màu, nhất là vùng dưới mắt ([BU Dermatology](https://www.bumc.bu.edu/derm/files/2017/09/Aging-article.pdf), [SkinInc / L'Oréal](https://www.skininc.com/home/article/21835458/loreal-usa-dermal-depths-understanding-aging-in-black-facial-skin)).
- Đốm nhỏ nâu sẫm nổi trên gò má (dermatosis papulosa nigra) rất thường gặp ở người Mỹ gốc Phi, tăng theo tuổi, nữ gặp gần gấp đôi nam ([JCAD](https://jcadonline.com/dermatosis-papulosa-nigra-survey/), [PMC review](https://pmc.ncbi.nlm.nih.gov/articles/PMC7158914)).
- Phụ nữ da đen 70+ để tóc bạc tự nhiên: TWA, cắt tapered sát hai bên, xoăn tít trên đỉnh ([Latest Hairstyles](https://www.latest-hairstyles.com/galleries/short-haircuts-for-black-women-over-70.html)).
- Đàn ông da đen đi làm văn phòng: low taper fade, chân tóc gọn, râu tỉa ([Casting Workbook guide](https://learning.castingworkbook.com/influential-moments/mastering-the-low-taper-fade-for-black-males-a-style-guide.html)).
- Gia đình da đen thật có nhiều tông da; quảng cáo hay chọn người da sáng và người da sẫm thấy mình bị bỏ qua ([Cablefax](https://cablefax.com/programming/colorism-a-major-challenge-to-advertisers-and-networks)).
- Thang Monk Skin Tone (Google + Ellis Monk, 10 mức, mức 7–10 là sẫm) dùng làm thước để tách tông da từng người khi duyệt ảnh ([Wikipedia](https://en.wikipedia.org/wiki/Monk_Skin_Tone_Scale)); không ghi chữ "Monk" vào prompt.
- Docx (biên tập viên) đã chốt tránh định kiến: không khăn trùm kiểu người giúp việc, không "Big Momma", không gà rán hay dưa hấu làm trò, không cử chỉ "sassy".

## 3. Bảy nhân vật

| Nhân vật | Tông da (Monk ≈) | Mặt | Tóc | Đeo / cầm | Dáng | Phân biệt |
|---|---|---|---|---|---|---|
| Gloria, 71 | nâu vừa-sẫm, ấm đỏ-vàng (≈7) | tròn, má đầy, mũi rộng mềm, môi đầy; ít nếp nhăn sâu, vài đốm nhỏ trên gò má | bạc trắng, xoăn tít, cắt tapered: sát hai bên, đầy trên đỉnh | kính gọng vàng **treo dây trước ngực**, khuyên vàng, thánh giá vàng, nhẫn cưới | tầm thước, đầy đặn, đứng thẳng | kính treo, không đeo trên mặt |
| Terrance, 46 | nâu sẫm, ấm (≈8), sẫm hơn mẹ | mắt và mũi giống mẹ, mặt dài hơn, quai hàm căng, vài nếp trán | đen, chút bạc ở thái dương, low taper fade | râu muối tiêu tỉa gọn, nhẫn cưới; **không kính** | cao vừa, chắc | râu muối tiêu |
| Jada, 19 | nâu vừa, ấm vàng (≈6), sáng hơn bố | trái xoan, gò má cao, mắt giống bố, lông mày tự nhiên | tết knotless dài giữa lưng, buộc thấp, viền tóc chải gọn | khuyên vòng vàng; gần như không trang điểm; **không kính**; bình nước hồng nhạt đặt cạnh chỗ ngồi | trẻ, nhanh nhẹn | tóc tết |
| Dorothy, 73 | nâu sẫm nhất nhà, undertone lạnh (≈9) | dài, gò má cao, miệng điềm tĩnh; vài đốm nhỏ trên gò má | bạc, afro ngắn tròn, lộ dưới vành mũ | **mũ đi lễ xanh rêu** (vành vừa hất lên, dải cùng màu, một bông hoa vải, đội hơi nghiêng), kính tròn to gọng đồi mồi **đeo trên mặt**, trâm cài | cao gầy, chậm rãi | người duy nhất đội mũ; kính trên mặt |
| Vợ Terrance, 44 | nâu sáng-vừa, ấm vàng (≈5) | trái xoan, mắt hạnh nhân | tự nhiên, búi cao gọn | nhẫn cưới; sinh nhật đồ tối đẹp, thứ Sáu áo len (đúng docx) | — | chỉ ở hậu cảnh |
| Cậu bé, 10 | nâu vừa-sẫm | **không lộ mặt** | — | chỉ tay + tay áo: polo sọc (sinh nhật), hoodie xanh (thứ Sáu) | — | luật không mặt trẻ em |
| Con gái Dorothy, ~48 | nâu sẫm giống mẹ | mặt dài giống mẹ | ngắn, gọn | váy đi lễ; chỉ thấy qua cửa kính xe | — | 1 shot (S28) |

Thứ tự tông da khi duyệt (sẫm → sáng): **Dorothy > Terrance > Gloria > Jada > vợ Terrance**. Hai bà cùng tóc bạc ngắn nên phân biệt bằng tông da, khuôn mặt, chỗ đeo kính và dáng người.

## 4. So với docx

Giữ nguyên tuổi, vai, kiểu tóc chính, 4 bộ đồ Gloria, 4 bộ Terrance, 2 bộ Jada, đồ đi lễ của Dorothy. Thêm để nhân vật đúng người thật và không lẫn nhau (Nam bỏ dòng nào thì báo):
- tông da + undertone riêng từng người, nét mặt, kết cấu tóc;
- dấu tuổi của da nâu (ít nếp nhăn sâu, dưới mắt sẫm hơn, đốm nhỏ trên gò má) cho Gloria và Dorothy;
- kính Gloria treo dây trước ngực, kính Dorothy gọng đồi mồi đeo trên mặt; Gloria đầy đặn, Dorothy cao gầy;
- vợ Terrance mặc áo len ở bữa thứ Sáu (docx ghi áo len ở bảng tiếng Việt, khối prompt tiếng Anh thì không);
- tay ở D-2 là tay Terrance (da nâu sẫm, nhẫn cưới, cổ tay áo caro);
- **mũ đi lễ của Dorothy** (Nam duyệt 22/10): mũ xanh rêu cùng màu váy, vành vừa hất lên, dải cùng màu, một bông hoa vải, đội hơi nghiêng; bà đội suốt chiều Chủ nhật, cả ở hiên lẫn trong bếp Gloria vì đi thẳng từ nhà thờ sang. Vành vừa để không che mặt, không chạm người đứng cạnh. Mũ của phụ nữ da đen đi lễ thường có hoa hoặc nơ, hợp màu bộ đồ ([Smithsonian, Crowns](https://si.edu/exhibitions/crowns-portraits-black-women-church-hats%3Aevent-exhib-2880), [Washington Informer](https://www.washingtoninformer.com/sunday-worship-hats-black-women/));
- **bình nước của Jada** (docx: "bình nước to"): cốc giữ nhiệt to màu hồng nhạt, có quai, nắp, ống hút, không logo, kiểu cốc sinh viên mang theo khắp nơi ([Yahoo](https://sg.news.yahoo.com/stanley-water-bottle-over-gen-100301694.html), [The Ebb Tide](https://theebbtide.com/feature/tumbler-takeover-from-hydration-hub-to-campus-essential/05/2024)). Không đưa vào sheet và không bao giờ cầm trên tay; chỉ đặt trên bàn ở phía xa đĩa của Jada (S01, S08, S71, S81) và trên quầy cạnh Jada lúc sắp đi học (S21). Cảnh cận và cảnh Jada đẩy đĩa (C-2, E-2, A-1, S72–S80) không có bình để khỏi vướng.

Bình nước (dán nguyên văn, đã có sẵn trong khung các shot trên):
```
a large light-pink insulated tumbler with a handle, a lid and a straw, plain, with no logo or lettering
```

## 5. Prompt nhân vật (tiếng Anh, dán nguyên văn)

Khối da (có trong mọi sheet):
```
Brown skin true to life: each person keeps their own skin depth and undertone, rich and natural, with soft highlights on the forehead, cheekbones and nose and visible detail in the shadows; palms lighter than the backs of the hands; never grey, ashy, washed out, orange or lightened; every face has enough soft light to read its expression.
```

**Gloria**
```
The grandmother: a 71-year-old Black American woman with medium-deep brown skin and warm red-gold undertones. A round face with full cheeks, warm brown eyes, a broad soft nose and full lips; her skin has few deep wrinkles for her age: soft smile lines, gentle creases at the outer corners of her eyes, slightly deeper-toned skin under her eyes and a few tiny raised deep-brown spots on her upper cheeks, as many older Black women have. Short natural silver-white hair in tight coils, cut in a neat tapered shape, close at the sides and back and fuller on top. Reading glasses with thin gold frames hang on a fine chain against her chest; small gold stud earrings, a small gold cross necklace and a thin gold wedding band. Medium height, a soft, solid build and an upright posture: the proud, healthy, quick-witted matriarch of her family, never frail.
```
Đồ: She wears a copper-colored silk blouse, a pearl necklace, a cream cardigan and a floral cotton apron. · She wears a lavender cardigan over a plain white T-shirt and grey slacks. · She wears a burgundy sweater, small gold earrings and the same floral cotton apron. · She wears a soft blue cardigan over a cream blouse and the same floral cotton apron.

**Terrance**
```
Her son: a 46-year-old Black American man with deep brown skin and warm undertones, a shade deeper than his mother's. He has his mother's warm brown eyes and broad nose in a longer face with a strong, tense jaw and a few faint lines on his forehead. Short black hair with a little grey at the temples, cut in a low taper fade with tight short coils on top and a clean natural hairline; a full, neatly trimmed salt-and-pepper beard with a clean edge along the cheeks; a gold wedding band. Medium-tall with a solid build: an office professional and a dad.
```
Đồ: He wears a navy quarter-zip pullover and chinos. · He wears a grey fleece work vest over a button-down shirt. · He wears a plaid button-down shirt. · He wears a navy crewneck sweater.

**Jada**
```
The granddaughter: a 19-year-old Black American college student with medium brown skin and warm golden undertones, a shade lighter than her father's. An oval face with high round cheekbones, her father's warm brown eyes, a soft broad nose, full lips and natural brows. Long medium-size knotless braids in natural black-brown, reaching the middle of her back and gathered in a low ponytail, with neat laid edges along her hairline; small gold hoop earrings; little or no makeup; a bright, open, expressive face.
```
Đồ: She wears a plain grey hoodie with no logo and leggings. · She wears a green knit sweater.

**Dorothy**
```
The friend: a 73-year-old Black American woman, the grandmother's longtime neighbor from the same church, with deep brown skin and cool undertones, deeper than the grandmother's. A long oval face with high cheekbones and a calm mouth; her skin has few deep wrinkles for her age, with fine lines around the eyes and a few tiny raised deep-brown spots on her cheeks. Short natural silver hair in a soft, rounded close-cropped afro. Large round glasses with tortoiseshell frames, worn on her face. Tall and slender with an unhurried, upright posture; a calm face with quiet authority and a hint of dry humor.
```
Đồ: She is just back from church and keeps her church hat on all afternoon: a moss-green church hat with a medium upturned brim, a matching band and a small fabric flower, worn tilted slightly to one side, her silver hair showing below it; a moss-green dress, a matching cardigan with a small brooch, a canvas tote bag on her shoulder.

**Vợ Terrance**
```
The son's wife: a 44-year-old Black American woman with light-medium brown skin and golden undertones, an oval face with almond-shaped eyes and a warm, composed expression, natural black coily hair pulled up in a neat high bun, and a gold wedding band.
```
Đồ: She wears nice dinner clothes. / She wears a soft knit sweater.

**Con gái Dorothy**
```
The friend's daughter: a Black American woman of about 48 with deep brown skin like her mother's, her mother's long face and short, neatly styled hair, seen only through the car window.
```
Đồ: She wears a church dress.

## 6. Duyệt sheet trước khi chạy clip

- [ ] Cả 7 người là người Mỹ da đen, tông da khác nhau đúng thứ tự ở mục 3; không ai bị làm sáng da, da không xám, không bóng nhựa.
- [ ] Tóc xoăn tít tự nhiên (không thẳng, không xoăn lơi); Gloria cắt tapered, Dorothy afro tròn ngắn, Jada tết knotless.
- [ ] Chỉ Gloria (kính treo dây) và Dorothy (kính đeo trên mặt) có kính. Terrance, Jada, vợ Terrance không kính.
- [ ] Dorothy đội mũ đi lễ xanh rêu ở mọi cảnh của bà; không ai khác đội mũ. Bình nước hồng chỉ đứng trên bàn hoặc quầy, không ai cầm.
- [ ] Terrance có nét mắt, mũi giống Gloria; Jada có nét giống bố.
- [ ] Sheet đổi đồ ở 0B: cùng mặt, cùng tông da, cùng tóc với sheet gốc; chỉ đổi quần áo.
- [ ] Không có khăn trùm, trang phục hay cử chỉ làm trò.

## 7. Thứ tự chạy mới

1. Import `workflow_S14c_0A_Setup.json` → chạy (không cần tải ảnh) → mỗi node chọn 1 ảnh đạt theo mục 6 → tải về máy.
2. Import `workflow_S14c_0B_DoiDo.json` → tải 3 sheet gốc (`IMG_CS_GLORIA_1`, `IMG_CS_TERRANCE_1`, `IMG_CS_JADA_1`), 2 ảnh nền gốc (`IMG_BG_A_BDAY`, `IMG_BG_B_MORNING`) và ảnh thật bộ trong ống (`IMG_ACA_HOLDER`) → chạy → chọn.
3. Import 4 file khung F1 → F4, chọn khung, rồi 4 file clip V1 → V4, như hướng dẫn trong `S14c_Black_TobyFlow.md`.

0A và 0B không đổi: sheet người Nam đã chốt ở 0A dùng tiếp, không chạy lại.
