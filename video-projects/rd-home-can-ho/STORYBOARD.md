# RD HOME — "Một vòng căn hộ"

Video 33 giây từ 5 ảnh render, máy quay chậm, không cắt giật.

## Ý tưởng

Không kể chuyện bằng lời. Kể bằng **một chuyển động máy duy nhất kéo dài suốt video** —
người xem đi từ cửa vào, qua bếp, ra khoảng thở bên cửa sổ, rồi quay đầu nhìn lại toàn bộ căn hộ.
Mỗi ảnh là một nhịp thở: máy trôi 7 giây, chuyển cảnh tan chậm 1,2 giây.

Nguyên tắc: **một ảnh = một hướng máy.** Không zoom giật, không xoay, không hiệu ứng trượt.
Chuyển động dùng đường cong smoothstep — vào chậm, giữa đều, ra chậm — đúng nhịp thở.

## Bảng phân cảnh

| # | Ảnh | Máy | Vì sao | Chữ |
|---|-----|-----|--------|-----|
| 1 | Lối vào — tủ giày, gương lượn sóng | **Tilt xuống** | Bắt từ đường cong gương, thả xuống ghế nỉ xanh + đèn hắt dưới tủ | Lối vào / *nơi bắt đầu một ngày* |
| 2 | Bếp — backsplash kính mờ | **Pan phải** | Trôi dọc mặt bếp, để dải đèn hắt chạy ngang khung hình | Bếp / *ấm sáng sau lớp kính mờ* |
| 3 | Sofa + bàn ăn bên cửa sổ | **Push-in** | Tiến chậm về phía rèm voan — điểm sáng nhất khung hình | Khoảng thở / *nắng lọc qua rèm* |
| 4 | Toàn cảnh từ bếp nhìn ra ban công | **Push-in sâu** | Ảnh có chiều sâu nhất, đẩy máy tạo cảm giác bước vào nhà | Liền mạch / *bếp — khách — ngủ trong một nhịp* |
| 5 | Nhìn ngược từ phòng khách về cửa | **Pull-out** | Lùi ra, khép vòng tròn về đúng chỗ mở đầu | Về nhà / — |
| 6 | End card | Tĩnh | Nền kem, logo | RD HOME |

Vòng lặp khép kín: shot 1 nhìn vào cửa, shot 5 nhìn về cửa. Xem lại lần 2 vẫn liền mạch.

## Thông số

- 1080 × 1920 (9:16 — Reels/TikTok). Đổi được sang 16:9 và 4:5.
- 30 fps, H.264, yuv420p.
- Mỗi shot 7,0 s · chuyển cảnh tan 1,2 s · end card 4,0 s → **33,0 s**.
- Biên độ máy: push-in 16 %, pan/tilt 18 % — đủ thấy, không đủ để chóng mặt.
- Ảnh nguồn được upscale 2× trước khi cắt khung nên không bị rung viền (lỗi kinh điển của zoompan).

## Nhạc

Script không tự chèn nhạc. Truyền `--audio nhac.mp3` để ghép, tự fade out 2 s cuối.
Gợi ý: piano/ambient 70–80 BPM, không lời, không trống. Chuyển cảnh rơi vào phách 4 nếu chọn nhạc 4/4 khoảng 72 BPM.
