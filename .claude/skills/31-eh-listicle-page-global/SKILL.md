---
name: 31-eh-listicle-page-global
description: "Build a full HTML listicle-style advertorial/presell page (e.g. '5 Reasons', '8 Reasons', '10 Reasons') for any ecom dropship product. Use this skill whenever the user asks to create an advertorial, listicle page, presell page, sales page, or long-form product page in HTML format. Triggers on: 'write an advertorial for my product', 'create a reasons page', 'build a listicle for X product', 'make a presell page', 'EH-listicle page for X'. Always produces a standalone HTML file with alternating image/text layout per reason, comparison table, testimonials, guarantee, and CTA."
metadata:
  version: 2.0.0
  category: content
license: MIT
triggers:
  - "EH-listicle page"
  - "advertorial"
  - "listicle page"
  - "presell page"
  - "reasons page"
  - "sales page HTML"
  - "long-form product page"
  - "write an advertorial for my product"
  - "build a listicle for my product"
related:
  - product-marketing-context-global
  - 29-dropshipping-mastery-global
  - 12-landing-page-brief-global
  - 05-ad-copy-global
  - 17-pricing-strategy-global
  - 30-design-master-global
---

# EH-Listicle Page Skill
## Version 2.0 — Full Presell/Advertorial Builder

Created by Quang Vinh (Dani) — Ecom Hater K3 / Anh Em Shopify VN community.
Modeled on 4 proven reference brands: CoveBalm, Kaoli, Cleaning Insider, Fluff Co.

---

## PART 0 — SELF-CONTAINED EXECUTION RULES

When this skill is triggered, Claude:
1. Reads this entire skill file before writing a single line of HTML
2. Uses the Fast Start Template (Part 12) to map product info
3. Builds the page TOP TO BOTTOM — never skips a section
4. Copies the full CSS from Part 8 verbatim — never abbreviates
5. Every reason MUST have a `.reason-grid` with `.reason-img` + `.reason-text` side by side
6. Odd reasons = `.img-left` class, Even reasons = `.img-right` class
7. Delivers a single self-contained `.html` file — no external CSS except Google Fonts
8. Does NOT ask more than 2 clarifying questions — fills gaps logically from product type

**Repo integration:** if `.agents/product-marketing-context-global.md` exists, read it first and pull
product name, audience, pain point, price, and guarantee from it instead of asking. Write the finished
file to `output/[product-slug]-advertorial.html`.

---

## PART 1 — REFERENCE PATTERN ANALYSIS

### CoveBalm / Kaoli (Skincare, women 50+)
- Angle: "Made for Skin That's Changed (Not for Teenagers)" — identity reframe
- Survey stats upfront: 95%, 93%, 92% — numbers before reasons
- Social proof BEFORE reasons begin in hero
- Mid-page CTA after reason 3 only
- Tone: warm, peer-to-peer

### Cleaning Insider (Shoe cleaning bag)
- Hook: Confessional — "I Tried Every Way... Only One Actually Worked"
- Never mentions brand until after reason 1
- Writes like editorial/journalism, not advertising
- Each reason has in-text link — low friction CTA
- 10 reasons, each a unique angle

### Fluff Co (Luxury pillow)
- Authority stack: hotel supplier → award → Oprah → 500,000+ customers
- Timeline transformation: Week 1 → Week 2 → Month 1+
- Price comparison vs alternatives (chiropractor, hotel pillow) not just competitors
- Invented mechanism word "Tanfurizing" makes product feel proprietary

### Universal patterns across all 4:
1. Hook = personal frustration story, never product pitch
2. Every reason = unique angle — never repeat
3. Numbers always specific: "97,000+" not "thousands"
4. CTA mid-page after reason 3 — never earlier
5. Testimonials: Setup → Trigger → Result — never just a quote
6. Two-path section (WITHOUT vs WITH) before final pricing
7. Guarantee box always visually separate from CTA

---

## PART 2 — PRODUCT INTAKE

| Field | Notes |
|---|---|
| Product name | |
| Product type | Device / supplement / beauty / home / apparel |
| Target audience | Age, gender, pain point, psychographic |
| Core problem solved | The frustration RIGHT NOW |
| Failed alternatives | What they tried that didn't work |
| Root cause narrative | WHY the problem really exists |
| Main mechanism | How product physically/chemically solves it |
| Key features (3–6) | Specific, not generic |
| Social proof numbers | Units sold, reviews, survey %, customer count |
| Competitors / alternatives | Named or category |
| Sale price / original price | |
| Guarantee | Days + terms |
| Tone | Confessional / Authority / Warm / Clinical |
| Number of reasons | 5, 7, 8, or 10 |
| Language | English (default) or bilingual EN+VN |
| CTA URL | Placeholder # if not provided |

---

## PART 3 — ANGLE SELECTION

**Confessional Discovery** ← Default for most ecom products
- "I tried everything. Only this worked."
- Best for: gadgets, home, personal care, cleaning
- Never mentions brand until paragraph 2 of intro

**Identity Reframe**
- "This isn't for [generic person]. It's for [specific identity]."
- Best for: beauty, skincare, wellness for specific demographics

**Authority Discovery**
- Expert/doctor/professional found or created this
- Best for: supplements, medical-adjacent devices, pain relief

**Lifestyle Aspiration**
- "People who [desired outcome] all have one thing in common"
- Best for: fitness, sleep, productivity

---

## PART 4 — 8 UNIVERSAL REASONS

| # | Theme | Copy Focus | Skip? |
|---|---|---|---|
| 1 | Root Cause | Real mechanism ≠ what they think | Never |
| 2 | Failed Alternatives | Named things that don't work + why this is different | Never |
| 3 | Social Proof | Specific number + survey stats. CTA follows | Never |
| 4 | Ease / Habit | X minutes. Fits existing routine. No learning curve | Never |
| 5 | Zero Side Effects | No drugs/chemicals. Works naturally/mechanically | Health only |
| 6 | Ingredients / Versatility | Specific compounds or use cases with mechanism | Adapt to product |
| 7 | Quality / Manufacturing | Clinical-grade supplier. Verified specs. Testing | Never |
| 8 | Risk-Free Guarantee | X-day return. Return rate stat. 7-day micro-commitment | Never |

**Rule:** Never put two social proof reasons back-to-back. Alternate logical → emotional → logical.

---

## PART 5 — FULL PAGE STRUCTURE (never skip a section)

```
1.  TOP BAR           — urgency/sale strip (colored background)
2.  SITE HEADER       — publication name + tagline
3.  BREADCRUMB        — Category › Subcategory › Topic
4.  HERO              — article tag + h1 + author chip + stars + read time
5.  INTRO P1          — personal frustration. No product name yet.
6.  INTRO P2          — moment of discovery. Product name appears here.
7.  INTRO P3          — the surprising result. Understated.
8.  INTRO P4          — why writing this — to share, not to sell.
9.  NOTE BOX          — "Note: I was skeptical..." pre-empts objection
10. RAINBOW BAR       — gradient divider
11. REASON 1          — .reason-grid.img-left
12. RAINBOW BAR
13. REASON 2          — .reason-grid.img-right + comparison table below
14. RAINBOW BAR
15. REASON 3          — .reason-grid.img-left + stats row below
16. MID-PAGE CTA      — appears ONLY after reason 3
17. RAINBOW BAR
18. REASON 4          — .reason-grid.img-right
19. RAINBOW BAR
20. REASON 5          — .reason-grid.img-left
21. RAINBOW BAR
22. REASON 6          — .reason-grid.img-right
23. RAINBOW BAR
24. REASON 7          — .reason-grid.img-left
25. RAINBOW BAR
26. REASON 8          — .reason-grid.img-right
27. RAINBOW BAR
28. TESTIMONIALS      — 3 cards minimum (setup → trigger → result)
29. PRODUCT DARK      — dark bg feature grid
30. TWO-PATH SECTION  — WITHOUT vs WITH (5+ rows each)
31. PROMO BOX         — original price crossed + sale price + CTA
32. GUARANTEE BOX     — separate visual anchor
33. FINAL CTA         — emotional headline + button
34. FOOTER            — disclaimer + links + copyright
```

---

## PART 6 — ALTERNATING IMAGE/TEXT LAYOUT

**This is the most critical pattern. Copy exactly.**

Every reason uses a 2-column grid.
- Odd reasons (1,3,5,7): image LEFT → `.reason-grid.img-left`
- Even reasons (2,4,6,8): image RIGHT → `.reason-grid.img-right`
- Mobile: image always stacks ON TOP, text below — enforced via media query

```html
<!-- ODD reason — image LEFT -->
<div class="reason-section">
  <div class="reason-number-label">Reason 01 · [Category Tag]</div>
  <div class="reason-grid img-left">
    <div class="reason-img">
      <div class="reason-img-placeholder">
        <div class="img-ph-icon">[emoji]</div>
        <div class="img-ph-label">[2-4 word label]</div>
        <div class="img-ph-desc">[Higgsfield AI gen prompt: subject, context, lighting, style]</div>
      </div>
      <div class="img-caption">[Caption]</div>
    </div>
    <div class="reason-text">
      <div class="reason-title">[Headline]</div>
      <div class="reason-body-text">
        <p>[Para 1: common belief / what they think]</p>
        <p>[Para 2: why that's wrong / the real mechanism]</p>
        <p>[Para 3: how product addresses this specifically]</p>
      </div>
      <div class="highlight-box">
        <strong>[Stat label]:</strong> [Specific stat or callout]
      </div>
    </div>
  </div>
</div>

<!-- EVEN reason — image RIGHT -->
<div class="reason-section">
  <div class="reason-number-label">Reason 02 · [Category Tag]</div>
  <div class="reason-grid img-right">
    <div class="reason-text">
      [same content structure as above]
    </div>
    <div class="reason-img">
      [same image structure as above]
    </div>
  </div>
</div>
```

### Image Placeholder — Required Fields
Each `.reason-img-placeholder` MUST have all three:
- `img-ph-icon` — relevant emoji
- `img-ph-label` — 2-4 word label
- `img-ph-desc` — specific Higgsfield/AI gen prompt including: subject, what they're doing, location/context, lighting, mood, style (product photography / lifestyle / editorial / UGC / flat-lay)

### AI Gen Prompt Examples by Reason
| Reason | Example Prompt |
|---|---|
| Root cause | "Clean anatomical illustration of prostate with DHT highlighted in amber — clinical style, white background, educational not graphic" |
| Comparison | "Flat-lay: generic pharmacy bottle (left) vs premium product bottle (right) — white background, soft shadow, product photography" |
| Social proof | "Grid of 8 diverse customer photos (men 50-65), confident expressions, home/outdoor settings — authenticity badge overlay, warm lighting" |
| Ease/habit | "Man 55+ at kitchen table, morning light, holding product bottle next to breakfast — relaxed, lifestyle photography, warm window light" |
| No side effects | "Split visual: crossed-out prescription bottle left, product with 'natural formula' badge right — minimal, white background" |
| Ingredients | "Artistic flat-lay of natural ingredients arranged around product bottle — earth tones, natural lighting, product photography" |
| Manufacturing | "Product bottle with FDA/GMP/third-party tested badges — professional studio lighting, dark background" |
| Guarantee | "Bold 60-day guarantee seal — premium badge design, brand colors, 'No Questions Asked' text, clean vector style" |

> For generating the real images, hand these prompts to skill `30-design-master-global`.

---

## PART 7 — COPYWRITING FORMULAS

### Hero Headline
```
Option A (Confessional):
"[N] Reasons I Stopped [Paying for / Using / Doing X] — And Never Looked Back"

Option B (Identity):
"[N] Reasons [Audience] Who [Desired outcome] All Use This [Category]"

Option C (Discovery):
"I Tried [N] Ways To [Solve Problem]. Only One Actually Worked."
```

### Intro Hook (4 paragraphs — Cleaning Insider pattern)
```
P1: Personal frustration. Time wasted. Money spent. No product name.
P2: Moment of discovery — reluctant, specific. Product name appears here.
P3: The surprising result. Understated. "Six weeks later I wrote this."
P4: Why they're writing — to share, not to sell.
```

### Reason Body (per reason)
```
Para 1: What everyone does / thinks (common belief)
Para 2: Why that's wrong / incomplete (insight)
Para 3: How product addresses this specifically (proof)
Highlight box: 1 specific stat or key callout
```

### Testimonial Formula
```
t-top: name, age, job, city, stars
t-body:
  - Setup (2-3 sentences): who they are + history + what they tried + skepticism
  - Trigger (1 sentence): what made them try
  - Experience (2-3 sentences): first use + surprise + ongoing
t-result box: specific measurable outcome in their words
  Examples: "Saved $340 in 11 weeks" / "Sleeping 7.5 hours straight" / "Stream problem is basically gone"
```

### Stats Row (after reason 3)
```
3 cards:
- [X]% [specific result] within [specific timeframe]
Never use: "most", "many", "thousands" — always specific numbers
```

### Two-Path
```
WITHOUT (✗): current pain / money wasted / symptom worsening / emotional cost / worst case
WITH (✓): pain resolved / money saved / improvement timeline / emotional win / aspiration
Minimum 5 rows each side.
```

### CTA Copy
```
Mid-page (after reason 3):
"Try [Product] Risk-Free — [X]% Off Today →"
Sub: "⏰ [Urgency] · [Guarantee] · [Shipping]"

Final CTA:
"[Emotional verb — Stop / Start / Finally] [Outcome]. [Action]."
Button: "Get [Product] — [X]% Off Today →"
Sub: "⏰ Limited supply · [X]-day guarantee · Ships in [timeframe]"
```

---

## PART 8 — COMPLETE CSS (copy verbatim, do not abbreviate)

### Color Palettes by Niche
```css
/* Supplement / Wellness — deep purple + gold */
--accent: #3d1a6e; --accent2: #c9973a; --green: #1a7d44;
--red: #c0392b; --light: #f6f0ff; --border: #d4c8e8;

/* General Health / Device — navy + orange */
--accent: #1a4b8c; --accent2: #e05b20; --green: #1a7d44;
--red: #c0392b; --light: #f4f7fc; --border: #d8e0ee;

/* Beauty / Skincare Women 40-55 — warm cream + rose */
--accent: #8c3a2a; --accent2: #c9734a; --green: #4a7c59;
--red: #c0392b; --light: #fdf6f0; --border: #e8d5c8;

/* Fitness / Performance — dark + electric blue */
--accent: #1a3a6b; --accent2: #0078d4; --green: #1a7d44;
--red: #c0392b; --light: #f0f5ff; --border: #c8d8f0;

/* Home / Lifestyle — forest green + warm */
--accent: #2c5f2e; --accent2: #c9973a; --green: #1a7d44;
--red: #c0392b; --light: #f4f8f4; --border: #c8dcc8;
```

### Full Required CSS Block
```css
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--sans);color:var(--text);background:#fff;font-size:16px;line-height:1.6}

/* TOP BAR */
.top-bar{background:var(--accent);color:#fff;text-align:center;padding:9px 16px;font-size:13px;font-weight:600}
.top-bar span{color:#ffd166}

/* SITE HEADER */
.site-header{border-bottom:2px solid var(--border);padding:14px 20px;display:flex;align-items:center;justify-content:space-between}
.pub-name{font-family:var(--serif);font-size:19px;font-weight:700;color:var(--accent)}

/* WRAP */
.wrap{max-width:800px;margin:0 auto;padding:0 20px}

/* BREADCRUMB */
.breadcrumb{padding:12px 0;font-size:12px;color:var(--muted);border-bottom:1px solid var(--border)}
.breadcrumb a{color:var(--accent);text-decoration:none}

/* HERO */
.article-tag{display:inline-block;background:var(--accent);color:#fff;font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:4px 10px;border-radius:2px;margin-bottom:16px}
.hero h1{font-family:var(--serif);font-size:clamp(22px,4vw,34px);font-weight:700;line-height:1.25;margin-bottom:16px;color:#1a0a2e}
.hero h1 em{font-style:italic;color:var(--accent2)}
.hero-meta{display:flex;align-items:center;gap:16px;font-size:13px;color:var(--muted);flex-wrap:wrap;margin-bottom:20px;padding-bottom:20px;border-bottom:1px solid var(--border)}
.stars{color:#f5a623}
.author-chip{display:flex;align-items:center;gap:8px}
.author-avatar{width:38px;height:38px;border-radius:50%;background:var(--light);border:2px solid var(--border);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:13px;color:var(--accent)}
.intro-text{font-family:var(--serif);font-size:17px;line-height:1.85;margin-bottom:16px}
.intro-text strong{color:var(--accent)}
.note-box{background:#fffbea;border-left:4px solid #f5a623;padding:14px 18px;font-size:14px;margin-bottom:28px;border-radius:0 4px 4px 0}

/* RAINBOW BAR */
.rainbow-bar{height:4px;background:linear-gradient(90deg,var(--accent),var(--accent2),var(--green),#8c1a6a);margin:32px 0;border-radius:2px}

/* REASON SECTION — CRITICAL: alternating layout */
.reason-section{margin:32px 0}
.reason-number-label{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--accent2);margin-bottom:12px;display:flex;align-items:center;gap:10px}
.reason-number-label::before{content:'';display:inline-block;width:28px;height:2px;background:var(--accent2)}

.reason-grid{display:grid;grid-template-columns:1fr 1fr;gap:0;align-items:stretch;border:1px solid var(--border);border-radius:8px;overflow:hidden;box-shadow:0 2px 12px rgba(0,0,0,0.06)}

/* img-left: image col order 1, text col order 2 */
.reason-grid.img-left .reason-img{order:1}
.reason-grid.img-left .reason-text{order:2}

/* img-right: text col order 1, image col order 2 */
.reason-grid.img-right .reason-text{order:1}
.reason-grid.img-right .reason-img{order:2}

.reason-img{background:#ede8f8;min-height:260px;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:24px}
.reason-img-placeholder{width:100%;min-height:220px;display:flex;flex-direction:column;align-items:center;justify-content:center;background:linear-gradient(135deg,#e0d4f7,#cfc0ee);border-radius:6px;padding:20px;text-align:center;gap:10px}
.img-ph-icon{font-size:34px;opacity:.55}
.img-ph-label{font-size:10px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--accent);opacity:.75}
.img-ph-desc{font-size:11.5px;color:var(--accent);opacity:.6;line-height:1.55}
.img-caption{font-size:11px;color:var(--muted);text-align:center;margin-top:8px;font-style:italic}

.reason-text{padding:28px 26px;background:#fff;display:flex;flex-direction:column;justify-content:center}
.reason-title{font-family:var(--serif);font-size:clamp(16px,2vw,20px);font-weight:700;line-height:1.3;color:#1a0a2e;margin-bottom:14px}
.reason-body-text{font-size:14.5px;line-height:1.78;color:#2a2a2a}
.reason-body-text p{margin-bottom:12px}
.reason-body-text p:last-child{margin-bottom:0}
.highlight-box{background:var(--light);border:1px solid var(--border);border-left:4px solid var(--accent);padding:14px 16px;margin:14px 0 0;border-radius:0 6px 6px 0;font-size:13.5px;line-height:1.6}
.highlight-box strong{color:var(--accent)}

/* STATS ROW */
.stats-row{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;margin:20px 0 0}
.stat-card{background:var(--light);border:1px solid var(--border);padding:20px 14px;text-align:center}
.stat-num{font-family:var(--serif);font-size:36px;font-weight:700;color:var(--accent);line-height:1}
.stat-label{font-size:12px;color:var(--muted);margin-top:6px;line-height:1.45}

/* CTA */
.cta-box{background:linear-gradient(135deg,#1a0a2e,var(--accent));color:#fff;border-radius:8px;padding:28px 24px;text-align:center;margin:32px 0}
.cta-btn{display:inline-block;background:var(--accent2);color:#fff;text-decoration:none;padding:16px 40px;border-radius:4px;font-size:16px;font-weight:700;transition:opacity .15s}
.cta-btn:hover{opacity:.88}
.cta-sub{font-size:12px;opacity:.7;margin-top:10px}

/* COMPARISON TABLE */
.comparison-table{width:100%;border-collapse:collapse;margin:20px 0;font-size:14px}
.comparison-table th{background:var(--accent);color:#fff;padding:12px 14px;text-align:left;font-size:12.5px;font-weight:600}
.comparison-table th:first-child{background:#2a0e4a}
.comparison-table td{padding:12px 14px;border-bottom:1px solid var(--border)}
.comparison-table tr:nth-child(even) td{background:var(--light)}
.comparison-table td:first-child{font-weight:600}
.check{color:var(--green);font-weight:700}
.cross{color:var(--red);font-weight:700}

/* TESTIMONIALS */
.testimonial{background:var(--light);border:1px solid var(--border);border-radius:8px;padding:24px;margin-bottom:16px}
.t-top{display:flex;align-items:center;gap:12px;margin-bottom:14px}
.t-avatar{width:48px;height:48px;border-radius:50%;background:#d4c0f0;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:16px;color:var(--accent);flex-shrink:0}
.t-name{font-weight:700;font-size:15px}
.t-meta{font-size:12px;color:var(--muted)}
.t-stars{color:#f5a623;font-size:13px;margin-top:2px}
.t-body{font-size:14.5px;line-height:1.75;margin-bottom:14px}
.t-result{background:#fff;border:1px solid #b8dfc8;border-left:4px solid var(--green);border-radius:0 6px 6px 0;padding:12px 16px;font-size:14px;font-style:italic;color:var(--green);font-weight:600;line-height:1.5}

/* TWO PATHS */
.two-paths{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:32px 0}
.path{border-radius:8px;padding:22px 20px}
.path-bad{background:#fff5f5;border:1px solid #f0c0be}
.path-good{background:#f0faf4;border:1px solid #b8dfc8}
.path-title{font-family:var(--serif);font-size:15px;font-weight:700;margin-bottom:14px}
.path-bad .path-title{color:var(--red)}
.path-good .path-title{color:var(--green)}
.path-list{list-style:none;font-size:13.5px;line-height:1.6}
.path-list li{padding:5px 0;display:flex;gap:8px;align-items:start}
.path-bad .path-list li::before{content:'✗';color:var(--red);font-weight:700;flex-shrink:0}
.path-good .path-list li::before{content:'✓';color:var(--green);font-weight:700;flex-shrink:0}

/* PRODUCT DARK */
.product-dark{background:#1a0a2e;color:#fff;padding:40px 24px;margin:32px 0;border-radius:8px}
.product-dark h2{font-family:var(--serif);font-size:22px;text-align:center;margin-bottom:28px}
.product-dark h2 span{color:#ffd166}
.feature-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.feature-pill{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.12);border-radius:6px;padding:16px}
.feature-pill-icon{font-size:22px;margin-bottom:8px}
.feature-pill-title{font-size:13.5px;font-weight:700;margin-bottom:4px}
.feature-pill-desc{font-size:12px;color:rgba(255,255,255,.6);line-height:1.5}

/* PROMO */
.promo-box{background:#1a0a2e;color:#fff;border-radius:8px;padding:32px 24px;text-align:center;margin:32px 0}
.promo-label{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#ffd166;margin-bottom:8px}
.price-row{display:flex;align-items:center;justify-content:center;gap:16px;margin-bottom:12px}
.price-orig{font-size:20px;text-decoration:line-through;opacity:.5}
.price-sale{font-size:44px;font-weight:700;color:#ffd166;font-family:var(--serif)}

/* GUARANTEE */
.guarantee-box{border:2px solid var(--green);border-radius:8px;padding:28px 24px;text-align:center;margin:28px 0;background:#f0faf4}
.guarantee-title{font-family:var(--serif);font-size:19px;font-weight:700;color:var(--green);margin-bottom:10px}
.guarantee-text{font-size:14px;line-height:1.7;color:#2d6a45}

/* FINAL CTA */
.final-cta{background:linear-gradient(135deg,#1a0a2e,var(--accent));color:#fff;border-radius:8px;padding:40px 24px;text-align:center;margin:32px 0}
.final-cta h2{font-family:var(--serif);font-size:clamp(20px,3vw,28px);font-weight:700;margin-bottom:8px}
.final-cta p{font-size:15px;opacity:.8;margin-bottom:24px;max-width:500px;margin-left:auto;margin-right:auto}

/* FOOTER */
.site-footer{background:#1a0a2e;color:rgba(255,255,255,.5);padding:28px 20px;text-align:center;font-size:12px;line-height:1.8;margin-top:48px}
.footer-links{display:flex;gap:20px;justify-content:center;flex-wrap:wrap;margin-bottom:12px}

/* MOBILE — CRITICAL: image always stacks on top */
@media(max-width:640px){
  .reason-grid{grid-template-columns:1fr}
  .reason-grid.img-left .reason-img,
  .reason-grid.img-right .reason-img{order:1}
  .reason-grid.img-left .reason-text,
  .reason-grid.img-right .reason-text{order:2}
  .stats-row{grid-template-columns:1fr 1fr}
  .two-paths,.feature-grid{grid-template-columns:1fr}
  .price-sale{font-size:34px}
}
```

---

## PART 9 — BILINGUAL SUPPORT (EN + VN)

Target market is always English-speaking (US/UK/AU/CA). VN used for teaching only.

- Hero, reasons, CTA: English primary
- Reason title: can add VN subtitle in muted smaller font below
- Testimonials: English names + EN-speaking city locations — never translate
- Stats, buttons: English only
- Footer disclaimer: English only

```html
<!-- Bilingual title example -->
<div class="reason-title">
  It Treats The Root Cause — Not Just The Symptom
  <span style="display:block;font-size:13px;font-weight:400;color:#666;margin-top:4px;font-style:italic;">Tác động vào gốc rễ — không chỉ triệu chứng bên ngoài</span>
</div>
```

---

## PART 10 — QUALITY CHECKLIST (verify before delivering)

**Structure:**
- [ ] Top bar has urgency + specific discount %
- [ ] Header reads like a publication, not a store
- [ ] Author chip: avatar + name + job title + "Verified Purchaser"
- [ ] Read time in hero meta

**Reasons:**
- [ ] ALL 8 reasons have `.reason-grid` with image + text columns
- [ ] Odd reasons have `.img-left` class — even reasons have `.img-right` class
- [ ] Every image placeholder has icon + label + specific Higgsfield prompt
- [ ] Every reason has `.highlight-box` with specific stat
- [ ] Rainbow bar between every reason
- [ ] Reason 3 = social proof with stats row below
- [ ] Mid-page CTA appears ONLY after reason 3

**Copy:**
- [ ] Intro paragraph 1 has no product name
- [ ] No two reasons share the same angle
- [ ] All numbers are specific (no "many", "most", "thousands")
- [ ] All 3 testimonials follow Setup → Trigger → Result
- [ ] Each `.t-result` has measurable specific outcome

**Conversion:**
- [ ] Comparison table in reason 2
- [ ] Stats row (3 specific %) after reason 3
- [ ] 3+ testimonials with `.t-result` boxes
- [ ] Two-path section 5+ rows each
- [ ] Promo box: original price struck through + sale price
- [ ] Guarantee box visually separate from CTA
- [ ] 2 CTA buttons: mid-page + final

**Technical:**
- [ ] Single self-contained `.html` file
- [ ] Only external dependency: Google Fonts
- [ ] Mobile responsive: `@media(max-width:640px)` forces image on top
- [ ] Footer has legal disclaimer + "advertorial" disclosure
- [ ] Filename format: `[product-slug]-advertorial.html`, written to `output/`

**Compliance (do not skip):**
- [ ] Testimonials and stats are supplied by the user or clearly marked as placeholder copy to be replaced with real data — never present invented numbers as verified
- [ ] Health/supplement claims carry the standard disclaimer (not evaluated by FDA, not medical advice)
- [ ] "Advertorial / paid promotion" disclosure visible in header or footer (FTC US, EU CHRD)
- [ ] See `references/global-legal-compliance.md`

---

## PART 11 — REFERENCE IMPLEMENTATIONS

Two builds that demonstrate the complete pattern. Recreate either as a worked example when
the user asks for a sample:

**Prosta Flow BPH advertorial** — `output/prostaflow-bph-advertorial.html`
- Product: Prosta Flow supplement
- Audience: Men 50-65, BPH, weak stream, waking at night
- Angle: Authority Discovery
- Palette: Supplement (purple + gold)
- Notable: Clinical ingredient breakdown, prescription comparison table, urologist testimonial

**Massage Gun advertorial** — `output/massage-gun-advertorial.html`
- Product: Percussion Massage Gun
- Audience: Desk workers 30-50, shoulder/back pain
- Angle: Confessional Discovery
- Palette: General Health (navy + orange)
- Notable: Cost comparison table ($3,120/yr vs $70), physical therapist cost math

---

## PART 12 — FAST START (fill this before writing HTML)

```
PRODUCT: [name]
AUDIENCE: [who + specific pain point]
HOOK TYPE: [Confessional / Identity / Authority / Aspiration]
PALETTE: [Supplement / Health / Beauty / Fitness / Home]
8 REASON THEMES: [root-cause, failed-alts, social-proof, ease, side-effects, ingredients, quality, guarantee]
LANGUAGE: [EN / EN+VN]
CTA URL: [# or real URL]
SALE: [original price] → [sale price]
GUARANTEE: [X days]
PUB NAME: [fake editorial name e.g. "Men's Wellness Report" / "Recovery Insider"]
AUTHOR: [name, job, "Verified Purchaser"]
```

**Then build section by section, top to bottom. Never skip. Never merge two reasons.**

---

## Skill chain

| Before this skill | After this skill |
|---|---|
| `product-marketing-context-global` — product, audience, price | `30-design-master-global` — turn image prompts into real visuals |
| `29-dropshipping-mastery-global` — winning product + offer | `05-ad-copy-global` — ads that drive traffic to this page |
| `09-customer-insight-global` — pain points, failed alternatives | `19-ab-test-setup-global` — test hook / headline / price |
| `17-pricing-strategy-global` — markup + anchor price | `21-ads-audit-global` — check landing-page conversion signals |
