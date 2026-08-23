# RD HOME — video "Một vòng căn hộ"

Dựng video 33 giây từ 5 ảnh render tĩnh. Máy quay chậm kiểu Ken Burns, chuyển cảnh tan, chữ tiếng Việt có scrim.
Concept và bảng phân cảnh: [STORYBOARD.md](STORYBOARD.md).

## Chạy

1. Cài FFmpeg — macOS `brew install ffmpeg`, Ubuntu `sudo apt install ffmpeg`, Windows tải từ ffmpeg.org.
2. Đặt 5 ảnh vào `assets/` **đúng tên** (tên quyết định thứ tự xuất hiện):

```
assets/01-loi-vao.jpg      # sảnh — tủ giày, gương lượn sóng
assets/02-bep.jpg          # bếp — backsplash kính mờ
assets/03-khoang-tho.jpg   # sofa + bàn ăn bên cửa sổ
assets/04-toan-canh.jpg    # nhìn từ bếp ra ban công
assets/05-nhin-lai.jpg     # nhìn ngược từ phòng khách về cửa
```

3. Render:

```bash
./render.sh --draft     # bản nháp, xem nhịp trước (nhanh)
./render.sh             # bản cuối, CRF 17
```

Kết quả nằm ở `renders/rd-home-9x16.mp4`.

## Tuỳ chọn

| Lệnh | Tác dụng |
|------|----------|
| `--ratio 16:9` | Đổi khung: `9:16` (mặc định) · `16:9` · `4:5` · `1:1` |
| `--audio nhac.mp3` | Ghép nhạc nền, tự fade in 2s / fade out 2.5s |
| `--no-text` | Bỏ toàn bộ chữ và scrim, chỉ còn hình |
| `--draft` | CRF 28, preset veryfast — duyệt nhanh |
| `--src thu-muc` | Đọc ảnh từ thư mục khác |
| `--out duong-dan.mp4` | Đổi nơi xuất |

## Sửa nội dung

Mở `render.sh`, sửa mảng `SHOTS` — mỗi dòng là `tên file | hướng máy | dòng 1 | dòng 2`:

```bash
"02-bep.jpg|pan-right|Bếp|ấm sáng sau lớp kính mờ"
```

Hướng máy dùng được: `push-in` · `pull-out` · `pan-left` · `pan-right` · `tilt-up` · `tilt-down`.
Để trống dòng 2 nếu chỉ muốn một dòng. Để trống cả hai thì cảnh đó không có chữ và không có scrim.

Các số chỉnh nhịp nằm ngay đầu file: `DUR` (thời lượng mỗi cảnh), `XF` (độ dài chuyển cảnh),
`PUSH` / `DRIFT` (biên độ máy), `SCRIM` (độ đậm lớp phủ), `BRAND` (chữ end card).

## Ghi chú kỹ thuật

- Ảnh được upscale 2× trước khi `zoompan` cắt khung — đây là cách khử rung viền, đừng bỏ.
- Chuyển động dùng smoothstep `p²(3−2p)` nên vào/ra đều mềm, không giật ở đầu và cuối cảnh.
- Chữ dùng DejaVu Serif (có sẵn trên Linux, đủ dấu tiếng Việt). Trên macOS đổi `FONT`/`FONTB`
  sang `/System/Library/Fonts/Supplemental/Times New Roman.ttf` hoặc font brand của RD Home.
- Script không tự chèn nhạc — tránh dính bản quyền. Tự chọn track rồi truyền `--audio`.
