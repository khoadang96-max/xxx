# Tổng hợp lệnh Skill — Cheat Sheet

> **Mục đích:** một trang duy nhất liệt kê **mọi lệnh** gọi được trong repo này —
> 64 skill (32 VN + 32 Global), 2 foundation, 5 agent, 15 workflow.
> Bản đồ quan hệ giữa các skill xem [`skill-map.md`](skill-map.md).

---

## 1. Bốn cách gọi

| Cách | Cú pháp | Khi nào dùng |
|------|---------|--------------|
| **Tự động** | Gõ tiếng Việt bình thường | Mặc định — skill tự kích hoạt theo trigger |
| **Thủ công** | `/05-copy-quang-cao` | Muốn chỉ định đúng skill, không để AI đoán |
| **Agent** | `Dùng agent mkt-strategist ...` | Việc lớn cần nhiều skill, chạy nền |
| **Workflow** | `Chạy workflow campaign-launch` | Chuỗi 5–7 skill liên tục, có thứ tự |

Ví dụ ba cách cho cùng một việc:

```
> Viết copy quảng cáo cho spa Luna              ← tự động
> /05-copy-quang-cao spa Luna, ngân sách 30tr   ← thủ công
> Dùng agent content-producer viết bộ copy...   ← agent
```

---

## 2. Chạy TRƯỚC TIÊN — Foundation skill

Chạy 1 lần cho mỗi project. Skill ghi file context, mọi skill sau đó tự đọc → khỏi khai lại sản phẩm/audience.

| Lệnh | Ghi ra file | Dùng cho |
|------|-------------|----------|
| `/product-marketing-context` | `.agents/product-marketing-context.md` | Marketing sản phẩm — thị trường VN |
| `/product-marketing-context-global` | `.agents/product-marketing-context-global.md` | Marketing sản phẩm — US / EU / SEA / LATAM |
| `/22-personal-brand-context` | `.agents/personal-brand-context.md` | Thương hiệu cá nhân — VN |
| `/22-personal-brand-context-global` | `.agents/personal-brand-context-global.md` | Thương hiệu cá nhân — Global |

**Auto-detect mode:** có file nào thì agent + skill 04/05 tự chuyển mode tương ứng.
Có cả hai file → skill hỏi 1 câu trước khi làm. Không có file nào → skill gợi ý tạo context trước.

---

## 3. Skill Việt Nam (32 lệnh)

### 3.1 Marketing Core — `00`–`21`

| Lệnh | Làm gì | Trigger mẫu |
|------|--------|-------------|
| `/00-ke-hoach-mkt` | Kế hoạch fullstack — master skill, gọi 08 + 09 + 10 | "lập kế hoạch marketing" |
| `/01-lich-noi-dung` | Lịch nội dung tháng, tỉ lệ phễu, content pillar, repurposing | "lịch đăng bài", "content calendar" |
| `/02-brief-chien-dich` | Brief chiến dịch 9 phần: context → creative → RACI → risk | "brief chiến dịch", "brief campaign" |
| `/03-danh-gia-hieu-suat` | Audit performance ads + organic, root cause, action plan 48h | "đánh giá hiệu suất", "ROAS tụt" |
| `/04-script-video` | Script TikTok / Reels / Shorts — 2 bản A/B, hook, CTA, hướng dẫn quay | "viết script video", "script TikTok" |
| `/05-copy-quang-cao` | 6 biến thể copy theo TOFU / MOFU / BOFU, tuân thủ policy | "viết copy quảng cáo", "copy ads" |
| `/06-brief-ugc-egc` | Brief UGC (khách) / EGC (nhân viên) / KOC — quyền dùng, batch | "brief UGC", "brief KOC" |
| `/07-bao-cao-marketing` | Báo cáo "đọc 5 phút biết làm gì tiếp" — insight trước, số sau | "báo cáo tháng", "tổng kết tuần" |
| `/08-nghien-cuu-doi-thu` | Đối thủ 3 tầng: trực tiếp / gián tiếp / thứ cấp + SWOT + market gap | "nghiên cứu đối thủ" |
| `/09-insight-khach-hang` | Chân dung sâu: Consumer vs Shopper, JTBD, journey, internal monologue | "insight khách hàng", "chân dung KH" |
| `/10-tinh-kpi-nguoc` | KPI ngược từ doanh thu → ngân sách, 3 kịch bản, break-even | "tính KPI ngược", "cần bao nhiêu budget" |
| `/11-thiet-lap-kenh` | Set up kênh A–Z: TikTok, Zalo OA, FB Page, Brevo, GBP — 30 ngày đầu | "thiết lập kênh", "mở Zalo OA" |
| `/12-brief-landing-page` | Brief LP 7 section — 1 page = 1 goal = 1 CTA, mobile-first | "brief landing page" |
| `/13-phan-tich-du-lieu` | Data thô → insight: theo kênh, campaign, creative, audience, thời gian | "phân tích dữ liệu", "đọc số liệu ads" |
| `/14-email-marketing` | Welcome / nurture / promotion / re-engage — tối ưu cho VN | "email marketing", "chuỗi email" |
| `/15-social-listening` | Giám sát brand + đối thủ + trend, cảnh báo khủng hoảng sớm | "social listening", "theo dõi thương hiệu" |
| `/16-marketing-psychology` | 7 nguyên tắc Cialdini áp vào copy / LP / email / ads, chỉnh theo VN | "tâm lý khách hàng", "FOMO", "social proof" |
| `/17-pricing-strategy` | Mô hình giá + chiến thuật định giá + pricing page | "chiến lược giá", "định giá sản phẩm" |
| `/18-referral-program` | Referral 1 chiều / 2 chiều, tracking, chống gian lận | "chương trình giới thiệu", "affiliate" |
| `/19-ab-test-setup` | Chọn biến, tính sample size, setup tracking, đọc significance | "A/B test", "split test" |
| `/20-brief-client-intake` | Form intake cho agency — **20 variant theo ngành** | "brief khách hàng", "onboard client" |
| `/21-audit-ads-performance` | Audit tài khoản ads, Health Score 0–100, Quick Wins (Meta/TikTok/Google/Zalo) | "audit ads", "kiểm tra tài khoản QC" |

### 3.2 Personal Branding — `22`–`28`

| Lệnh | Làm gì |
|------|--------|
| `/22-personal-brand-context` | ★ Foundation PB — niche, story arc, brand voice, visual asset inventory (13+ section) |
| `/23-personal-brand-strategy` | Chiến lược PB 12 tháng — positioning, story arc 3 chương, 4 content pillar, authority ladder 5 nấc |
| `/24-ai-avatar-production` | ⚑ Flagship — pipeline AI Avatar: HeyGen, Synthesia, ElevenLabs, Captions. Anti-detection + disclosure NĐ 147/2024 |
| `/25-voice-clone-podcast` | Voice clone (ElevenLabs / Vbee), podcast, audiobook, voiceover — repurpose 1:10 |
| `/26-thought-leadership-content` | Long-form: LinkedIn / FB / newsletter. 3 cấu trúc + 6 hook formula. **Khác skill 05 (bán hàng)** |
| `/27-personal-brand-monetize` | Funnel kiếm tiền: offer ladder Free → Low → Mid → High, brand deal, thuế & pháp lý VN 2026 |
| `/28-community-building` | Community 3 lớp Public / Member / Inner — Zalo Group, Telegram, FB Group, Skool |

### 3.3 Flagship VN — `29`–`30`

| Lệnh | Làm gì |
|------|--------|
| `/29-xuat-khau-b2b` | Marketing xuất khẩu B2B cho SME Việt — company profile EN, pitch deck, email chào hàng, hội chợ |
| `/30-thiet-ke-master` | 8 loại thiết kế (logo, key visual, social post, infographic, editorial, web mockup, quote graphic) + **Prompt Director mode** cho DALL-E / MidJourney / Leonardo / Imagen |

---

## 4. Skill Global (32 lệnh)

Cùng số thứ tự, hậu tố `-global`, output tiếng Anh. Skill có 🌍 hỗ trợ 4 region **US / EU / SEA / LATAM** qua `variants/` — region lấy từ foundation skill.

| Lệnh | Làm gì | Region variant |
|------|--------|:--------------:|
| `/00-marketing-plan-global` | Marketing plan 7 section | |
| `/01-content-calendar-global` | Content calendar đa kênh | |
| `/02-campaign-brief-global` | Campaign brief 9 section | |
| `/03-performance-eval-global` | Performance diagnosis + 5-Whys + 48h plan. Có mục **Dropshipping KPI** | 🌍 |
| `/04-script-video-global` | Video script TikTok / Reels / Shorts, 6 hook formula | |
| `/05-ad-copy-global` | 6 ad copy (AIDA / PAS / BAB). Có **Dropshipping Mode** 4 template | |
| `/06-ugc-egc-brief-global` | UGC / EGC / KOC brief | |
| `/07-marketing-report-global` | Marketing report insight-first | |
| `/08-competitor-research-global` | Competitor 3 tầng — SimilarWeb, Ahrefs, Semrush, Minea | |
| `/09-customer-insight-global` | Customer profile, JTBD, journey map | |
| `/10-reverse-kpi-global` | Reverse KPI + sensitivity 3 kịch bản | 🌍 |
| `/11-channel-setup-global` | Channel setup — US: Meta+Google+LinkedIn · SEA: TikTok+Shopee+LINE · LATAM: WhatsApp+Mercado Libre | 🌍 |
| `/12-landing-page-brief-global` | LP brief 7 section + Single-Product LP cho dropshipping | |
| `/13-data-analysis-global` | Descriptive → Diagnostic → Predictive → Prescriptive | |
| `/14-email-marketing-global` | Email automation — **compliance: CAN-SPAM / GDPR / PDPA / LGPD** | 🌍 |
| `/15-social-listening-global` | Brand + competitor + trend monitoring | |
| `/16-marketing-psychology-global` | Cialdini 7 principles, ví dụ Apple / Tesla / Patagonia | |
| `/17-pricing-strategy-global` | Pricing + charm / anchor / decoy. Có **Dropshipping Markup Math** | 🌍 |
| `/18-referral-program-global` | Referral + anti-spam TCPA / GDPR / PDPA / LGPD | 🌍 |
| `/19-ab-test-setup-global` | A/B test, sample size, Optimizely / VWO | |
| `/20-client-intake-brief-global` | Client intake 11 section (bản generic, chưa có variant ngành) | |
| `/21-ads-audit-global` | Ads audit Health Score 0–100, **84 checkpoint / 6 dimension** | 🌍 |
| `/22-personal-brand-context-global` | ★ Foundation PB global | 🌍 |
| `/23-personal-brand-strategy-global` | PB strategy 12 tháng — Ikigai + 3x3, 4×7 = 28 topic | |
| `/24-ai-avatar-production-global` | AI Avatar pipeline — **disclosure law: FTC / EU AI Act / SEA / LATAM** | 🌍 |
| `/25-voice-clone-podcast-global` | Voice clone ElevenLabs / Murf / PlayHT, giọng US/UK/AU/SG | |
| `/26-thought-leadership-content-global` | LinkedIn, Twitter/X, Substack, Medium — repurpose 1:5 | |
| `/27-personal-brand-monetize-global` | Monetize + **tax/legal: LLC US / EU / Pte Ltd SEA / MEI LATAM** | 🌍 |
| `/28-community-building-global` | Skool, Mighty Networks, Discord, Circle, Slack | |
| `/29-dropshipping-mastery-global` | ⚑ Flagship — product research → supplier → Shopify → 10 ads/week → scaling → FTC/EU CHRD | |
| `/30-design-master-global` | Design master + Prompt Director (bản EN) | |
| `/product-marketing-context-global` | ★ Foundation marketing global | 🌍 |

---

## 5. Agent (5 lệnh)

Agent = chạy nền, tự chọn và ghép nhiều skill. **Universal** — tự detect cluster VN hay Global theo file trong `.agents/`.

| Lệnh gọi | Vai trò | Skill chính |
|----------|---------|-------------|
| `Dùng agent mkt-strategist ...` | Chiến lược tổng | 00, 02, 08, 09, 10 |
| `Dùng agent content-producer ...` | Sản xuất nội dung | 01, 04, 05, 06 |
| `Dùng agent performance-analyst ...` | Phân tích hiệu suất | 03, 07, 10, 13 |
| `Dùng agent channel-operator ...` | Vận hành kênh | 11, 12, 14, 15 |
| `Dùng agent personal-brand-builder ...` | Personal brand + AI Avatar | 22–28 |

---

## 6. Workflow (15 chuỗi)

Gọi: `Chạy workflow <tên>`. File chi tiết ở `workflows/vi/` và `workflows/en/`.

### Việt Nam — 7 workflow

| Lệnh | Chuỗi skill | Thời gian |
|------|-------------|-----------|
| `client-onboard` | 20 → 09 → 08 → 10 → 00 → 02 → 01 | 5–7 ngày |
| `campaign-launch` | 00 → 02 → 01 → 04 → 05 → 06 → 11 | 1 chiến dịch |
| `monthly-cycle` | 13 → 03 → 07 → 01 → 10 | hàng tháng |
| `content-production` | 09 → 01 → 04 → 06 | 1 batch content |
| `personal-brand-launch` | 22 → 23 → 24 → 25 → 26 → 04 → 27 → 28 → 14 | ra mắt PB |
| `ai-avatar-batch` | 23 → 26 → 04 → 25 → 24 → 01 | batch video AI |
| `personal-brand-monthly` | 13 → 03 → 23 → 27 → 26 → 04 → 07 | hàng tháng PB |

### Global — 8 workflow

| Lệnh | Chuỗi skill |
|------|-------------|
| `client-onboard-global` | 20 → 09 → 08 → 10 → 00 → 02 → 01 |
| `campaign-launch-global` | 08 → 09 → 00 → 02 → 01 + 04 + 05 → 06 → 11 + 12 |
| `monthly-cycle-global` | 13 → 03 → 07 → 10 → 01 |
| `content-production-global` | 01 review → 04 → 05 → 06 |
| `personal-brand-launch-global` | 22 → 23 → 24 → 26 → 04 → 25 → 27 → 05 → 28 → 14 |
| `ai-avatar-batch-global` | 26 → 04 → ElevenLabs → HeyGen → 24 → 01 |
| `personal-brand-monthly-global` | 13 → 03 → 23 → 27 → 26 → 04 → 07 → 28 → 14 |
| `dropshipping-launch-global` | 29 → 12 → 04 → 05 → 21 → 13 → 17 |

---

## 7. Skill chain tự động

Một số skill tự gọi skill khác, không cần gõ thêm lệnh:

```
20-brief-client-intake   → 09 + 08 + 10 + 00
00-ke-hoach-mkt          → 08 + 09 + 10
02-brief-chien-dich      → 05 + 04 + 01
07-bao-cao-marketing     → 03 + 10
22-personal-brand-context→ 23 + 24
26-thought-leadership    → 04 (Personal Brand Mode) → 01
27-personal-brand-monetize → 14 + 18
```

---

## 8. Tra nhanh — "tôi muốn X thì gõ gì"

| Tôi muốn... | Gõ |
|-------------|-----|
| Bắt đầu project mới | `/product-marketing-context` |
| Kế hoạch marketing tổng | `/00-ke-hoach-mkt` |
| Biết cần bao nhiêu tiền để đạt doanh thu Y | `/10-tinh-kpi-nguoc` |
| Lịch đăng bài tháng tới | `/01-lich-noi-dung` |
| Script video TikTok | `/04-script-video` |
| Copy chạy ads | `/05-copy-quang-cao` |
| Ads đang tụt, không biết vì sao | `/03-danh-gia-hieu-suat` rồi `/21-audit-ads-performance` |
| Báo cáo cho sếp / client | `/07-bao-cao-marketing` |
| Biết đối thủ đang làm gì | `/08-nghien-cuu-doi-thu` |
| Xây thương hiệu cá nhân từ đầu | `/22-personal-brand-context` → workflow `personal-brand-launch` |
| Làm video AI không cần lên hình | `/24-ai-avatar-production` |
| Viết bài LinkedIn chuyên sâu | `/26-thought-leadership-content` |
| Thiết kế logo / poster / infographic | `/30-thiet-ke-master` |
| Bán hàng ra nước ngoài (B2B) | `/29-xuat-khau-b2b` |
| Làm dropshipping | `/29-dropshipping-mastery-global` |
| Nhận client mới cho agency | workflow `client-onboard` |

---

## 9. Ngoài phạm vi repo này

Repo này là **post-build marketing**. Việc tech / sản phẩm route sang OPA KIT companion:

| Yêu cầu | Lệnh |
|---------|------|
| PRD sản phẩm / feature | `opa-prd --mode=product` |
| Brief TVC 1-page | `opa-prd --mode=creative` |
| PRD buổi học / module | `opa-prd --mode=lesson` |
| Build end-to-end / ship feature | `opa-pipeline` |
| Track progress, ước tính token cost | `opa-tracker` |
| Deploy production | `opa-deploy` |
| Vẽ diagram workflow / funnel | `opa-diagram` |

Cài: `git clone https://github.com/minhnv0807/opa-kit.git && cd opa-kit && bash install-opa-suite.sh`

---

## 10. MCP — pull data tự động

Khi đã kết nối MCP server cho nền tảng ads, skill **03, 07, 08, 10, 21** tự pull data thay vì bắt paste tay.

| Nền tảng | MCP |
|----------|-----|
| Meta Ads | Meta Official MCP · Pipeboard (29 tools) · brijr/meta-mcp (25 tools) |
| Google Ads | Google Official MCP (read-only) |
| TikTok Ads | AdsMCP/tiktok-ads-mcp-server |
| Cross-platform | Adspirer ads-mcp (175+ tools) |
| Research đối thủ | facebook-ads-library-mcp (15+ tools) |

Chi tiết: [`../references/mcp-ads-integration.md`](../references/mcp-ads-integration.md) · [`../CONNECTORS.md`](../CONNECTORS.md)

---

## 11. Quy ước file output

```
[ten-skill]-[ten-san-pham]-[YYYYMMDD].md
ví dụ: ke-hoach-mkt-spa-luna-20250415.md
```
