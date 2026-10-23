# Seating chart for S14c dinners: top-down plan + Nam's chosen 0C image with labels + legend
import sys
from PIL import Image, ImageDraw, ImageFont
SHOT, OUT = sys.argv[1], sys.argv[2]
F = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; FB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
f = lambda n, b=False: ImageFont.truetype(FB if b else F, n)
W, H = 1900, 1520
im = Image.new('RGB', (W, H), (250, 248, 244)); d = ImageDraw.Draw(im)
INK, MUTE, LINE = (34, 34, 34), (105, 100, 95), (60, 60, 60)
def box(x0, y0, x1, y1, fill, outline=LINE, r=14, w=2): d.rounded_rectangle((x0, y0, x1, y1), r, fill=fill, outline=outline, width=w)
def ctext(cx, y, s, font, fill=INK):
    tw = d.textlength(s, font=font); d.text((cx - tw / 2, y), s, font=font, fill=fill)

d.text((40, 26), "S14c · Sơ đồ chỗ ngồi bàn ăn", font=f(40, True), fill=INK)
d.text((40, 80), "Tiệc sinh nhật và tối thứ Sáu: cùng người, cùng ghế. Đúng 7 người — có người lạ là loại ảnh.", font=f(23), fill=MUTE)

# ---------- left: plan seen from above, main camera at the bottom ----------
PX = 40
box(PX, 130, PX + 900, 230, (232, 226, 214))
d.text((PX + 18, 138), "TƯỜNG ĐẦU PHÒNG (sau lưng Gloria)", font=f(20, True), fill=INK)
items = [("cửa vòm → hành lang", 18), ("thìa dĩa gỗ treo", 270), ("băng rôn + bóng bay 71*", 480)]
for s, x in items: d.text((PX + x, 176), s, font=f(19), fill=INK)
box(PX + 700, 236, PX + 900, 330, (205, 186, 160)); ctext(PX + 800, 246, "TỦ BUFFET", f(19, True)); ctext(PX + 800, 274, "3 túi quà*", f(17)); ctext(PX + 800, 298, "khăn + đồ gỗ**", f(17))
box(PX, 236, PX + 112, 880, (232, 226, 214))
for i, s in enumerate(["TƯỜNG", "BÊN", "", "ảnh", "gia đình", "", "", "", "", "tủ chén"]):
    ctext(PX + 56, 300 + i * 40, s, f(18, i < 2))
# table
TX0, TX1, TY0, TY1 = PX + 400, PX + 660, 400, 820
box(TX0, TY0, TX1, TY1, (255, 255, 255), r=18, w=3)
ctext((TX0 + TX1) / 2, (TY0 + TY1) / 2 - 14, "BÀN", f(30, True), MUTE)
def seat(cx, cy, name, sub, fill, w=230, h=86):
    box(cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, fill)
    ctext(cx, cy - 30, name, f(22, True)); ctext(cx, cy + 4, sub, f(17))
seat((TX0 + TX1) / 2, TY0 - 62, "GLORIA", "ghế đầu bàn", (240, 200, 160), w=250)
seat((TX0 + TX1) / 2, TY1 + 62, "(ghế trống)", "cuối bàn", (238, 238, 238), w=250)
L, R = TX0 - 135, TX1 + 135
for i, (n, s, c) in enumerate([("TERRANCE", "sát đầu bàn", (178, 196, 228)), ("JADA", "cạnh bố", (214, 214, 214)), ("BÀ DÌ", "cạnh Jada", (214, 186, 214))]):
    seat(L, TY0 + 70 + i * 140, n, s, c)
for i, (n, s, c) in enumerate([("VỢ TERRANCE", "sát đầu bàn", (190, 222, 196)), ("CẬU BÉ", "chỉ thấy tay", (226, 226, 200)), ("ÔNG CHÚ", "cuối dãy", (206, 206, 206))]):
    seat(R, TY0 + 70 + i * 140, n, s, c)
ctext((TX0 + TX1) / 2, 960, "▲  MÁY QUAY CHÍNH  (góc của ảnh 0C)", f(22, True))
ctext((TX0 + TX1) / 2, 996, "Khung toàn cảnh S08, S71, S81 đặt máy ở đây.", f(18), MUTE)
d.text((PX, 1040), "Khung cận \"from across the table\": máy đặt ở dãy Vợ–Cậu bé–Ông chú,", font=f(18), fill=MUTE)
d.text((PX, 1066), "nhìn sang Terrance–Jada–bà dì; sau lưng họ là tường ảnh gia đình,", font=f(18), fill=MUTE)
d.text((PX, 1092), "tủ buffet và bóng bay ở phía đầu bàn.", font=f(18), fill=MUTE)
d.text((PX, 1128), "* chỉ hôm sinh nhật   ** chỉ tối thứ Sáu (khăn kẻ ô đỏ trắng của Dorothy + vài món gỗ)", font=f(17), fill=MUTE)

# ---------- right: Nam's chosen 0C image (image 1), labelled ----------
src = Image.open(SHOT).convert('RGB').crop((645, 217, 988, 560))
S = 800; ph = src.resize((S, S), Image.LANCZOS); IX, IY = 1000, 130
im.paste(ph, (IX, IY)); d.rectangle((IX, IY, IX + S, IY + S), outline=LINE, width=3)
k = S / 343
def tag(px, py, s, tx, ty):
    x, y = IX + px * k, IY + py * k; X, Y = IX + tx * k, IY + ty * k
    tw = d.textlength(s, font=f(20, True))
    d.line((x, y, X + tw / 2 + 10, Y + 16), fill=(255, 255, 255), width=5); d.line((x, y, X + tw / 2 + 10, Y + 16), fill=(200, 30, 30), width=3)
    d.ellipse((x - 7, y - 7, x + 7, y + 7), fill=(200, 30, 30), outline=(255, 255, 255), width=2)
    box(X, Y, X + tw + 20, Y + 32, (255, 255, 255), outline=(200, 30, 30), r=8, w=2); d.text((X + 10, Y + 4), s, font=f(20, True), fill=(160, 20, 20))
tag(173, 175, "Gloria", 205, 140)
tag(107, 220, "Terrance", 60, 180)
tag(57, 255, "Jada", 5, 222)
tag(20, 285, "Bà dì", 8, 305)
tag(263, 225, "Vợ Terrance", 245, 185)
tag(300, 283, "Cậu bé (tay)", 222, 302)
tag(325, 250, "Ông chú", 268, 262)
tag(237, 210, "Tủ buffet", 205, 98)
d.text((IX, IY + S + 12), "Ảnh 0C Nam chọn (ảnh 1). Ghế đầu bàn của Gloria bị che sau lưng bà;", font=f(19), fill=MUTE)
d.text((IX, IY + S + 38), "các khung A-1, S05, S08, S71, S79, S81 đã ghi rõ ghế này.", font=f(19), fill=MUTE)

# ---------- bottom: who wears what ----------
Y0 = 1180
d.text((40, Y0), "Ai mặc gì", font=f(26, True), fill=INK)
cols = [40, 360, 990, 1500]
heads = ["Người", "Tiệc sinh nhật", "Tối thứ Sáu", ""]
rows = [("Gloria, 71", "sơ mi lụa màu đồng, ngọc trai, cardigan kem, tạp dề hoa", "áo len đỏ rượu, tạp dề hoa"),
        ("Terrance, 46", "áo quarter-zip xanh than", "sơ mi kẻ ô"),
        ("Jada, 19", "hoodie xám, bình nước hồng cạnh đĩa", "áo len xanh lá, bình nước hồng"),
        ("Bà dì (em gái Gloria)", "váy màu mận; tóc bạc xoắn ngang vai", "cardigan xanh navy, blouse kem"),
        ("Vợ Terrance, 44", "như sheet (ảnh 0C: áo xanh lá), tóc búi cao", "áo len cam gỉ sắt"),
        ("Cậu bé, 10 (chỉ thấy tay)", "tay áo polo sọc", "tay áo hoodie xanh dương"),
        ("Ông chú (chồng bà dì)", "vest xám, sơ mi xanh nhạt; hói, râu trắng", "áo len cổ V nâu")]
y = Y0 + 42
for i, h in enumerate(heads[:3]): d.text((cols[i], y), h, font=f(19, True), fill=MUTE)
for r in rows:
    y += 33
    for i, s in enumerate(r): d.text((cols[i], y), s, font=f(19, i == 0), fill=INK)
im.save(OUT, optimize=True)
print('saved', im.size)
