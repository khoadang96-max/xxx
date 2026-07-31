# .agents/ — Context files

Thư mục này chứa **context file** mà các foundation skill ghi ra và mọi skill khác đọc lại.
Mục đích: khai báo sản phẩm / audience / brand **1 lần duy nhất** cho mỗi project, các skill sau
không phải hỏi lại (tiết kiệm ~70% thời gian mỗi session).

| File | Sinh ra bởi skill | Kích hoạt cluster |
|------|-------------------|-------------------|
| `product-marketing-context.md` | `product-marketing-context` | Marketing core — MODE VN |
| `product-marketing-context-global.md` | `product-marketing-context-global` | Marketing core — MODE GLOBAL |
| `personal-brand-context.md` | `22-personal-brand-context` | Personal brand — MODE VN |
| `personal-brand-context-global.md` | `22-personal-brand-context-global` | Personal brand — MODE GLOBAL |
| `export-context.md` | `29-xuat-khau-b2b` | Export B2B (VN) |

## Cách tạo

Chạy skill foundation trước tiên trong project mới:

> "Thiết lập context marketing cho sản phẩm [tên sản phẩm]"

Agent sẽ hỏi tối đa 4 câu rồi ghi file vào thư mục này.

## Lưu ý

- Có `product-marketing-context.md` → agent chạy MODE VN (skill tiếng Việt).
- Có `product-marketing-context-global.md` → agent chạy MODE GLOBAL (skill `-global`).
- Có **cả hai** → agent hỏi 1 câu để chọn cluster.
- Không có file nào → agent gợi ý tạo context trước.

Các file context chứa thông tin kinh doanh cụ thể. Nếu không muốn commit lên remote,
thêm `.agents/*.md` vào `.gitignore` (giữ lại file README này).
