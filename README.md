# ai-business-skills — đã cài vào project này

Bộ **64 skill marketing** + **5 agent** + **15 workflow** (song ngữ Việt / Global) từ
[minhnv0807/ai-business-skills](https://github.com/minhnv0807/ai-business-skills) (MIT),
cài sẵn ở cấp **project** nên bất kỳ ai clone repo này đều dùng được ngay — không cần chạy `install.sh`.

Nguồn: commit [`2c1b802`](https://github.com/minhnv0807/ai-business-skills/commit/2c1b802b5504e14974d0231e1d74cc204bb17858) (2026-06-20) · plugin v3.2.0.

---

## Dùng ngay

Mở Claude Code trong thư mục repo này rồi gõ tiếng Việt bình thường — skill tự kích hoạt theo trigger:

```
> Lập kế hoạch marketing cho khóa AI Kiếm Tiền — target 100 học viên trong 30 ngày
> Viết script TikTok cho spa Luna, hook giữ chân 3 giây đầu
> Đánh giá hiệu suất chiến dịch tháng 6, ROAS đang tụt
> Tính KPI ngược từ doanh thu 500 triệu/tháng
```

Gọi thủ công một skill cụ thể:

```
> /00-ke-hoach-mkt
> /05-copy-quang-cao
> /30-thiet-ke-master
```

Gọi agent chuyên trách:

```
> Dùng agent mkt-strategist phân tích positioning cho sản phẩm X
```

📋 **Danh sách đầy đủ mọi lệnh** (64 skill + 5 agent + 15 workflow): [`docs/lenh-skill.md`](docs/lenh-skill.md)

### Bước đầu tiên nên làm

Chạy skill **foundation** một lần cho mỗi project để khỏi phải khai lại sản phẩm/audience suốt session:

```
> Thiết lập context marketing cho sản phẩm [tên]
```

Skill sẽ ghi `.agents/product-marketing-context.md`. Mọi skill sau đó tự đọc file này.
Chi tiết: [`.agents/README.md`](.agents/README.md).

---

## Cấu trúc đã cài

```
.claude/skills/     64 skill  — 32 VN + 32 Global (mỗi skill 1 SKILL.md + variants/templates)
.claude/agents/      5 agent  — mkt-strategist, content-producer, performance-analyst,
                                channel-operator, personal-brand-builder
references/         21 file   — benchmark VN 2025-2026, benchmark Global, KPI formulas,
                                hook formulas, copy frameworks, legal/compliance, tool stack
workflows/vi|en     15 chuỗi  — client-onboard, campaign-launch, monthly-cycle,
                                content-production, personal-brand-launch, dropshipping-launch...
docs/                         — getting started, skill map, FAQ, best practices, MCP setup
examples/                     — 5 case study mẫu (spa, fashion e-com, personal brand, dropship)
CLAUDE.md                     — hướng dẫn hành vi cho agent (identity, nguyên tắc, skill chain)
AGENTS.md                     — mô tả 5 agent
CONNECTORS.md + .mcp.json     — MCP connector tuỳ chọn (xem lưu ý bên dưới)
.agents/                      — nơi skill ghi context file của project
```

### 4 cụm skill

| Cụm | Skill | Nội dung |
|-----|-------|----------|
| Marketing Core | `00`–`21` (VN) + `-global` | Kế hoạch, brief, content calendar, script video, ad copy, báo cáo, đối thủ, insight, KPI ngược, email, pricing, A/B test, audit ads |
| Personal Branding | `22`–`28` (VN) + `-global` | Chiến lược PB, AI avatar, voice clone/podcast, thought leadership, monetize, community |
| Regional flagship | `29-xuat-khau-b2b` / `29-dropshipping-mastery-global` | Xuất khẩu B2B cho SME Việt / Dropshipping toàn cầu |
| Design Master | `30-thiet-ke-master` / `30-design-master-global` | 8 loại thiết kế: logo, key visual, social post, infographic, editorial, web mockup, quote graphic |

Skill VN dùng tên tiếng Việt (`05-copy-quang-cao`), bản Global có hậu tố `-global`
(`05-ad-copy-global`) và hỗ trợ 4 region US / EU / SEA / LATAM qua thư mục `variants/`.

---

## Lưu ý

**`.mcp.json`** khai báo 10 MCP server tuỳ chọn (Slack, Canva, Figma, HubSpot, Notion, Ahrefs,
Amplitude, Klaviyo, Similarweb, Supermetrics). Claude Code sẽ **hỏi bạn duyệt** trước khi kết nối —
chưa duyệt thì không có gì chạy, và toàn bộ skill vẫn hoạt động bình thường. Entry `slack` còn
`clientId` là `PLACEHOLDER_REPLACE_WITH_OWN`, cần thay bằng OAuth client của bạn nếu muốn dùng.
Không cần thì xoá file. Xem [`CONNECTORS.md`](CONNECTORS.md).

**Benchmark** trong skill VN là số liệu thị trường Việt Nam 2025–2026 do tác giả upstream tổng hợp —
nên đối chiếu lại với dữ liệu thực tế của bạn trước khi đưa vào kế hoạch.

## Cập nhật về sau

```bash
git clone --depth 1 https://github.com/minhnv0807/ai-business-skills.git /tmp/abs
# copy lại các thư mục skill/agent/reference/workflow từ /tmp/abs theo cấu trúc ở trên
```

## Giấy phép

Upstream MIT — xem [`LICENSE`](LICENSE). Bản quyền thuộc Over Powers Agency.
