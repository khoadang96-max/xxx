# Character bible for S14c Black: research, per-character spec, what changed, how to review the sheets
import io, contextlib, json
with contextlib.redirect_stdout(io.StringIO()):
    from build14 import CH, SKIN_TONE, outfit_of, BOTTLE, aunt, uncle, WIFE_WEAR, SEATS, GUESTS
L = []
L.append("# S14c — Nhân vật gia đình Mỹ da đen (bản chuẩn 22-10)\n")
L.append("Khung nhân vật cho cả script. Prompt tiếng Anh ở mục 5 là bản đang nằm trong `toby/workflow_S14c_0A_Setup.json` và `0B_DoiDo.json`.\n")
L.append("## 1. Vì sao lượt ảnh trước sai\n")
L.append("1. **Lỗi nối file (lỗi của Claude):** Setup cũ để 7 sheet đổi đồ (Gloria 2–4, Terrance 2–4, Jada 2) lấy ảnh gốc từ node nằm cùng file. "
         "Luật đã chốt là ảnh tham chiếu phải đến từ file chạy trước. Node đổi đồ không nhận được ảnh gốc.")
L.append("2. **Prompt đổi đồ không tả người:** chỉ ghi \"giữ nguyên người trong Image 1 … glasses and jewelry\". Không có Image 1 thì model vẽ người ngẫu nhiên, "
         "đa số là người da trắng, và gắn kính cho tất cả vì có chữ \"glasses\". Đúng như ảnh Nam chụp: áo navy, sơ mi caro, gile xám đều ra người lạ đeo kính.")
L.append("3. **Mô tả gốc quá mỏng:** mọi người đều chỉ có \"Black American\" + \"warm brown skin\", không có kết cấu tóc, nét mặt, khác biệt tông da hay dấu tuổi của da nâu. "
         "Model dễ ra người chung chung, cả nhà cùng một màu da.\n")
L.append("## 2. Nghiên cứu (22-10)\n")
for t in [
 "Model ảnh hay gộp \"da sẫm\" thành một tông. Cách chữa: ghi độ sẫm + undertone riêng từng người, tả nét mặt và kết cấu tóc cụ thể thay vì chỉ ghi chủng tộc ([Neolemon](https://www.neolemon.com/blog/skin-tones-names-prompting-guide/), [ImageGPT](https://imagegpt.cloud/learn/guides/prompting-dark-skin-tones)).",
 "Da nâu dễ ra xám, tro khi cân bằng trắng lệch lạnh; cần ánh sáng mềm, giữ chi tiết vùng tối, không làm sáng da ([SLR Lounge](https://slrlounge.com/photography-tips-3-tips-for-working-with-darker-skin-tones), [Canon](https://canon.co.uk/get-inspired/tips-and-techniques/capturing-natural-skin-tones), [ShootProof](https://shootproof.com/blog/how-to-photograph-a-variety-of-skin-tones)).",
 "Da sẫm ít nếp nhăn sâu và nhăn muộn hơn (khoảng 10–20 năm), nhưng dễ không đều màu, nhất là vùng dưới mắt ([BU Dermatology](https://www.bumc.bu.edu/derm/files/2017/09/Aging-article.pdf), [SkinInc / L'Oréal](https://www.skininc.com/home/article/21835458/loreal-usa-dermal-depths-understanding-aging-in-black-facial-skin)).",
 "Đốm nhỏ nâu sẫm nổi trên gò má (dermatosis papulosa nigra) rất thường gặp ở người Mỹ gốc Phi, tăng theo tuổi, nữ gặp gần gấp đôi nam ([JCAD](https://jcadonline.com/dermatosis-papulosa-nigra-survey/), [PMC review](https://pmc.ncbi.nlm.nih.gov/articles/PMC7158914)).",
 "Phụ nữ da đen 70+ để tóc bạc tự nhiên: TWA, cắt tapered sát hai bên, xoăn tít trên đỉnh ([Latest Hairstyles](https://www.latest-hairstyles.com/galleries/short-haircuts-for-black-women-over-70.html)).",
 "Đàn ông da đen đi làm văn phòng: low taper fade, chân tóc gọn, râu tỉa ([Casting Workbook guide](https://learning.castingworkbook.com/influential-moments/mastering-the-low-taper-fade-for-black-males-a-style-guide.html)).",
 "Gia đình da đen thật có nhiều tông da; quảng cáo hay chọn người da sáng và người da sẫm thấy mình bị bỏ qua ([Cablefax](https://cablefax.com/programming/colorism-a-major-challenge-to-advertisers-and-networks)).",
 "Thang Monk Skin Tone (Google + Ellis Monk, 10 mức, mức 7–10 là sẫm) dùng làm thước để tách tông da từng người khi duyệt ảnh ([Wikipedia](https://en.wikipedia.org/wiki/Monk_Skin_Tone_Scale)); không ghi chữ \"Monk\" vào prompt.",
 "Docx (biên tập viên) đã chốt tránh định kiến: không khăn trùm kiểu người giúp việc, không \"Big Momma\", không gà rán hay dưa hấu làm trò, không cử chỉ \"sassy\"."]:
    L.append("- " + t)
L.append("\n## 3. Bảy nhân vật\n")
L.append("| Nhân vật | Tông da (Monk ≈) | Mặt | Tóc | Đeo / cầm | Dáng | Phân biệt |\n|---|---|---|---|---|---|---|")
for r in [
 ("Gloria, 71", "nâu vừa-sẫm, ấm đỏ-vàng (≈7)", "tròn, má đầy, mũi rộng mềm, môi đầy; ít nếp nhăn sâu, vài đốm nhỏ trên gò má", "bạc trắng, xoăn tít, cắt tapered: sát hai bên, đầy trên đỉnh", "kính gọng vàng **treo dây trước ngực**, khuyên vàng, thánh giá vàng, nhẫn cưới", "tầm thước, đầy đặn, đứng thẳng", "kính treo, không đeo trên mặt"),
 ("Terrance, 46", "nâu sẫm, ấm (≈8), sẫm hơn mẹ", "mắt và mũi giống mẹ, mặt dài hơn, quai hàm căng, vài nếp trán", "đen, chút bạc ở thái dương, low taper fade", "râu muối tiêu tỉa gọn, nhẫn cưới; **không kính**", "cao vừa, chắc", "râu muối tiêu"),
 ("Jada, 19", "nâu vừa, ấm vàng (≈6), sáng hơn bố", "trái xoan, gò má cao, mắt giống bố, lông mày tự nhiên", "tết knotless dài giữa lưng, buộc thấp, viền tóc chải gọn", "khuyên vòng vàng; gần như không trang điểm; **không kính**; bình nước hồng nhạt đặt cạnh chỗ ngồi", "trẻ, nhanh nhẹn", "tóc tết"),
 ("Dorothy, 73", "nâu sẫm nhất nhà, undertone lạnh (≈9)", "dài, gò má cao, miệng điềm tĩnh; vài đốm nhỏ trên gò má", "bạc, afro ngắn tròn, lộ dưới vành mũ", "**mũ đi lễ xanh rêu** (vành vừa hất lên, dải cùng màu, một bông hoa vải, đội hơi nghiêng), kính tròn to gọng đồi mồi **đeo trên mặt**, trâm cài", "cao gầy, chậm rãi", "người duy nhất đội mũ; kính trên mặt"),
 ("Vợ Terrance, 44", "nâu sáng-vừa, ấm vàng (≈5)", "trái xoan, mắt hạnh nhân", "tự nhiên, búi cao gọn", "nhẫn cưới; sinh nhật đồ tối đẹp, thứ Sáu áo len (đúng docx)", "—", "chỉ ở hậu cảnh"),
 ("Cậu bé, 10", "nâu vừa-sẫm", "**không lộ mặt**", "—", "chỉ tay + tay áo: polo sọc (sinh nhật), hoodie xanh (thứ Sáu)", "—", "luật không mặt trẻ em"),
 ("Con gái Dorothy, ~48", "nâu sẫm giống mẹ", "mặt dài giống mẹ", "ngắn, gọn", "váy đi lễ; chỉ thấy qua cửa kính xe", "—", "1 shot (S28)")]:
    L.append("| " + " | ".join(r) + " |")
L.append("\nThứ tự tông da khi duyệt (sẫm → sáng): **Dorothy > Terrance > Gloria > Jada > vợ Terrance**. Hai bà cùng tóc bạc ngắn nên phân biệt bằng tông da, khuôn mặt, chỗ đeo kính và dáng người.\n")
L.append("## 4. So với docx\n")
L.append("Giữ nguyên tuổi, vai, kiểu tóc chính, 4 bộ đồ Gloria, 4 bộ Terrance, 2 bộ Jada, đồ đi lễ của Dorothy. Thêm để nhân vật đúng người thật và không lẫn nhau (Nam bỏ dòng nào thì báo):")
for t in ["tông da + undertone riêng từng người, nét mặt, kết cấu tóc;",
          "dấu tuổi của da nâu (ít nếp nhăn sâu, dưới mắt sẫm hơn, đốm nhỏ trên gò má) cho Gloria và Dorothy;",
          "kính Gloria treo dây trước ngực, kính Dorothy gọng đồi mồi đeo trên mặt; Gloria đầy đặn, Dorothy cao gầy;",
          "vợ Terrance mặc áo len ở bữa thứ Sáu (docx ghi áo len ở bảng tiếng Việt, khối prompt tiếng Anh thì không);",
          "tay ở D-2 là tay Terrance (da nâu sẫm, nhẫn cưới, cổ tay áo caro);",
          "**mũ đi lễ của Dorothy** (Nam duyệt 22/10): mũ xanh rêu cùng màu váy, vành vừa hất lên, dải cùng màu, một bông hoa vải, đội hơi nghiêng; bà đội suốt chiều Chủ nhật, cả ở hiên lẫn trong bếp Gloria vì đi thẳng từ nhà thờ sang. Vành vừa để không che mặt, không chạm người đứng cạnh. Mũ của phụ nữ da đen đi lễ thường có hoa hoặc nơ, hợp màu bộ đồ ([Smithsonian, Crowns](https://si.edu/exhibitions/crowns-portraits-black-women-church-hats%3Aevent-exhib-2880), [Washington Informer](https://www.washingtoninformer.com/sunday-worship-hats-black-women/));",
          "**bình nước của Jada** (docx: \"bình nước to\"): cốc giữ nhiệt to màu hồng nhạt, có quai, nắp, ống hút, không logo, kiểu cốc sinh viên mang theo khắp nơi ([Yahoo](https://sg.news.yahoo.com/stanley-water-bottle-over-gen-100301694.html), [The Ebb Tide](https://theebbtide.com/feature/tumbler-takeover-from-hydration-hub-to-campus-essential/05/2024)). "
          "Không đưa vào sheet và không bao giờ cầm trên tay; chỉ đặt trên bàn ở phía xa đĩa của Jada (S01, S08, S71, S81) và trên quầy cạnh Jada lúc sắp đi học (S21). Cảnh cận và cảnh Jada đẩy đĩa (C-2, E-2, A-1, S72–S80) không có bình để khỏi vướng.",
          ]:
    L.append("- " + t)
L.append("\nBình nước (dán nguyên văn, đã có sẵn trong khung các shot trên):\n```\n" + BOTTLE + "\n```\n")
L.append("## 5. Prompt nhân vật (tiếng Anh, dán nguyên văn)\n")
L.append("Khối da (có trong mọi sheet):\n```\n" + SKIN_TONE + "\n```\n")
seen = set()
for k, c in CH.items():
    if k == 'B' or c['full'] in seen: continue
    seen.add(c['full'])
    outs = [CH[x]['outfit'] for x in CH if CH[x]['full'] == c['full']]
    outs = [o if isinstance(o, str) else ' / '.join(o.values()) for o in outs]
    name = {'G': 'Gloria', 'T': 'Terrance', 'J': 'Jada', 'D': 'Dorothy', 'W': 'Vợ Terrance', 'F': 'Con gái Dorothy'}[k[0]]
    L.append(f"**{name}**\n```\n{c['full']}\n```\nĐồ: " + ' · '.join(outs) + "\n")
L.append("## 6. Duyệt sheet trước khi chạy clip\n")
for t in ["Cả 7 người là người Mỹ da đen, tông da khác nhau đúng thứ tự ở mục 3; không ai bị làm sáng da, da không xám, không bóng nhựa.",
          "Tóc xoăn tít tự nhiên (không thẳng, không xoăn lơi); Gloria cắt tapered, Dorothy afro tròn ngắn, Jada tết knotless.",
          "Chỉ Gloria (kính treo dây) và Dorothy (kính đeo trên mặt) có kính. Terrance, Jada, vợ Terrance không kính.",
          "Dorothy đội mũ đi lễ xanh rêu ở mọi cảnh của bà; không ai khác đội mũ. Bình nước hồng chỉ đứng trên bàn hoặc quầy, không ai cầm.",
          "Terrance có nét mắt, mũi giống Gloria; Jada có nét giống bố.",
          "Sheet đổi đồ ở 0B: cùng mặt, cùng tông da, cùng tóc với sheet gốc; chỉ đổi quần áo.",
          "Không có khăn trùm, trang phục hay cử chỉ làm trò."]:
    L.append("- [ ] " + t)
L.append("\n## 7. Thứ tự chạy mới\n")
L.append("1. Import `workflow_S14c_0A_Setup.json` → chạy (không cần tải ảnh) → mỗi node chọn 1 ảnh đạt theo mục 6 → tải về máy.")
L.append("2. Import `workflow_S14c_0B_DoiDo.json` → tải 3 sheet gốc (`IMG_CS_GLORIA_1`, `IMG_CS_TERRANCE_1`, `IMG_CS_JADA_1`), 2 ảnh nền gốc (`IMG_BG_A_BDAY`, `IMG_BG_B_MORNING`) và ảnh thật bộ trong ống (`IMG_ACA_HOLDER`) → chạy → chọn.")
_fv = json.load(open('out/fv/_parts.json')); _nf = sum(p['kind'] == 'F' for p in _fv); _nv = sum(p['kind'] == 'V' for p in _fv)
L.append("3. Import `workflow_S14c_0C_BanAn.json` → tải 5 ảnh đã chọn ở 0A → chạy ảnh mẫu bàn ăn `MASTER_A_BDAY` → chọn ảnh đúng sơ đồ ở mục 8.")
L.append(f"4. Import {_nf} file khung F1 → F{_nf}, chọn khung, rồi {_nv} file clip V1 → V{_nv}, như hướng dẫn trong `S14c_Black_TobyFlow.md`.")
L.append("\n0A và 0B không đổi: sheet người Nam đã chốt ở 0A dùng tiếp, không chạy lại.")
L.append("\n## 8. Bàn ăn: chỗ ngồi và 2 họ hàng (23-10)\n")
L.append("Lượt F1 đầu tiên: mỗi khung một kiểu chỗ ngồi, có người lạ ngồi vào bàn. Docx chỉ ghi \"2–3 họ hàng mờ hậu cảnh\" nên model tự bịa người khác nhau mỗi khung. "
         "Giờ cố định đúng 7 người, cả bữa sinh nhật và bữa thứ Sáu (docx: thứ Sáu \"đúng những người ở bữa sinh nhật, ngồi đúng chỗ cũ\"). "
         "Hai họ hàng không có sheet riêng: mặt và đồ của họ lấy từ ảnh mẫu bàn ăn 0C. Không đeo kính, không đội mũ.\n")
L.append("| Người | Mô tả | Sinh nhật | Thứ Sáu | Ghế |\n|---|---|---|---|---|")
L.append("| Bà dì (em gái Gloria, ~66) | da nâu vừa, mặt tròn, tóc bạc xám tự nhiên dài ngang vai, xoắn mềm | váy màu mận | cardigan xanh navy, blouse kem | dãy tường cửa vòm, cạnh Jada |")
L.append("| Ông chú (chồng bà dì, ~70) | da nâu sẫm, đầu hói, râu trắng ngắn | áo vest xám, sơ mi xanh nhạt | áo len cổ V nâu, sơ mi có cổ | dãy đối diện, đối diện bà dì |")
L.append("| Vợ Terrance | như sheet | đúng bộ đồ trong sheet của chị | áo len cam gỉ sắt | dãy đối diện, sát đầu bàn, đối diện Terrance |")
L.append("| Cậu bé | chỉ thấy tay | tay áo polo sọc | tay áo hoodie xanh dương | giữa mẹ và ông chú, đối diện Jada; từ máy chính khuất sau ông chú |")
L.append("\nPrompt (dán nguyên văn):\n```\n" + SEATS + "\n" + GUESTS + "\n" + aunt('A_BDAY') + "\n" + uncle('A_BDAY') + "\n" + aunt('A_FRI') + "\n" + uncle('A_FRI') + "\n```\n")
open('out/S14c_Black_NhanVat.md', 'w').write('\n'.join(L) + '\n')
print('ok')
