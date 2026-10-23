# S14c standard dining room: the four walls, what stands behind every chair, and the four camera directions (one empty plate each)
import sys
from PIL import Image, ImageDraw, ImageFont
OUT = sys.argv[1]
F = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; FB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
f = lambda n, b=False: ImageFont.truetype(FB if b else F, n)
W, H = 1900, 1470
im = Image.new('RGB', (W, H), (250, 248, 244)); d = ImageDraw.Draw(im)
INK, MUTE, LINE, RED = (34, 34, 34), (105, 100, 95), (60, 60, 60), (190, 30, 30)
WALL = (232, 226, 214)
def box(x0, y0, x1, y1, fill, outline=LINE, r=12, w=2): d.rounded_rectangle((x0, y0, x1, y1), r, fill=fill, outline=outline, width=w)
def ctext(cx, y, s, font, fill=INK):
    d.text((cx - d.textlength(s, font=font) / 2, y), s, font=font, fill=fill)
def wrap(x, y, s, font, width, fill=INK, gap=6):
    words, line = s.split(), ''
    for w_ in words:
        t = (line + ' ' + w_).strip()
        if d.textlength(t, font=font) > width and line:
            d.text((x, y), line, font=font, fill=fill); y += font.size + gap; line = w_
        else: line = t
    if line: d.text((x, y), line, font=font, fill=fill); y += font.size + gap
    return y

d.text((40, 24), "S14c · Phòng ăn chuẩn: 4 bức tường, sau lưng từng ghế", font=f(38, True), fill=INK)
d.text((40, 76), "Dùng chung cho tiệc sinh nhật và tối thứ Sáu. Mỗi hướng máy có 1 ảnh nền trống: hướng ① là ảnh 0A/0C, hướng ②③④ là 3 ảnh của file 0E.", font=f(21), fill=MUTE)

# ---------- plan ----------
X0, Y0, X1, Y1 = 40, 130, 1010, 1160          # outer walls
box(X0, Y0, X1, Y0 + 104, WALL)                # head wall
d.text((X0 + 16, Y0 + 8), "TƯỜNG ĐẦU PHÒNG", font=f(19, True), fill=INK)
for s, x in (("cửa vòm → hành lang", 16), ("tranh nhỏ", 250), ("thìa dĩa gỗ treo", 380), ("băng rôn + bóng bay 71*", 640)):
    d.text((X0 + x, Y0 + 40), s, font=f(18), fill=INK)
d.text((X0 + 16, Y0 + 70), "(thứ Sáu: thùng trơn chồng ở hành lang)", font=f(15), fill=MUTE)
box(X0, Y0 + 110, X0 + 130, Y1 - 110, WALL)    # photo wall
ctext(X0 + 65, Y0 + 122, "TƯỜNG", f(17, True)); ctext(X0 + 65, Y0 + 144, "ẢNH", f(17, True))
box(X1 - 130, Y0 + 110, X1, Y1 - 110, WALL)    # window wall
ctext(X1 - 65, Y0 + 122, "TƯỜNG", f(17, True)); ctext(X1 - 65, Y0 + 144, "CỬA SỔ", f(17, True))
box(X0, Y1 - 104, X1, Y1, WALL)                # foot wall
d.text((X0 + 16, Y1 - 96), "TƯỜNG CUỐI PHÒNG", font=f(19, True), fill=INK)
d.text((X0 + 16, Y1 - 60), "lối mở rộng sang phòng khách: sofa be, chăn móc len, đèn cây sáng ấm", font=f(18), fill=INK)
# sideboard in the head-wall corner on the wife's side
box(X1 - 345, Y0 + 112, X1 - 140, Y0 + 196, (205, 186, 160)); ctext(X1 - 242, Y0 + 118, "TỦ BUFFET", f(17, True))
ctext(X1 - 242, Y0 + 142, "3 túi quà*", f(15)); ctext(X1 - 242, Y0 + 164, "khăn caro + muôi gỗ**", f(15))
# table + seats
TX0, TX1, TY0, TY1 = 420, 630, 400, 820
box(TX0, TY0, TX1, TY1, (255, 255, 255), r=18, w=3); ctext((TX0 + TX1) / 2, (TY0 + TY1) / 2 - 14, "BÀN", f(28, True), MUTE)
def seat(cx, cy, name, sub, fill, w=200, h=74):
    box(cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, fill); ctext(cx, cy - 27, name, f(19, True)); ctext(cx, cy + 4, sub, f(15))
seat((TX0 + TX1) / 2, TY0 - 60, "GLORIA", "ghế đầu bàn", (240, 200, 160), w=220)
seat((TX0 + TX1) / 2, TY1 + 60, "(ghế trống)", "cuối bàn", (238, 238, 238), w=220)
L, R = 275, 775
west = [("TERRANCE", (178, 196, 228), "ảnh cưới cũ", "của Gloria"), ("JADA", (214, 214, 214), "ảnh TN Terrance", "+ ảnh nhà thờ"), ("BÀ DÌ", (214, 186, 214), "tủ chén +", "ảnh Jada, cưới")]
east = [("VỢ TERRANCE", (190, 222, 196), "tranh", "phong cảnh"), ("CẬU BÉ", (226, 226, 200), "cửa sổ", "rèm voan"), ("ÔNG CHÚ", (206, 206, 206), "chậu lan ý", "(góc)")]
for i, (n, c, a, b) in enumerate(west):
    cy = TY0 + 70 + i * 140; seat(L, cy, n, "", c, w=190, h=60)
    ctext(X0 + 65, cy - 22, a, f(15)); ctext(X0 + 65, cy, b, f(15))
for i, (n, c, a, b) in enumerate(east):
    cy = TY0 + 70 + i * 140; seat(R, cy, n, "", c, w=190, h=60)
    ctext(X1 - 65, cy - 22, a, f(15)); ctext(X1 - 65, cy, b, f(15))
# camera directions
def cam(x, y, n, ang_dx, ang_dy, label, lx, ly):
    import math
    ex, ey = x + ang_dx, y + ang_dy
    d.line((x, y, ex, ey), fill=RED, width=5)
    a = math.atan2(ey - y, ex - x); k = 14
    d.polygon([(ex, ey), (ex - k * math.cos(a - 0.5), ey - k * math.sin(a - 0.5)), (ex - k * math.cos(a + 0.5), ey - k * math.sin(a + 0.5))], fill=RED)
    d.ellipse((x - 20, y - 20, x + 20, y + 20), fill=RED, outline=(255, 255, 255), width=3); ctext(x, y - 13, n, f(20, True), (255, 255, 255))
    if label: d.text((lx, ly), label, font=f(16, True), fill=RED)
cam((TX0 + TX1) / 2, Y1 - 130, "1", 0, -70, "① máy chính (ảnh 0C)", (TX0 + TX1) / 2 + 30, Y1 - 150)
cam(TX1 + 26, TY0 + 210, "2", -64, 0, "", 0, 0)
cam(TX0 - 26, TY0 + 350, "3", 64, 0, "", 0, 0)
cam(TX1 + 34, TY0 - 40, "4", 0, 74, "", 0, 0)
d.text((40, 1180), "Hướng máy", font=f(24, True), fill=INK)
y = 1218
for s in ("① Từ cuối bàn nhìn lên đầu bàn: ảnh 0C. Khung rộng và khung phóng gần vào từng người (đang dùng ở F1, F5).",
          "② Từ dãy vợ Terrance nhìn sang tường ảnh: Terrance, Jada, bà dì nhìn thẳng vào máy. Ảnh nền BG_A_WEST.",
          "③ Từ dãy tường ảnh nhìn sang tường cửa sổ: vợ Terrance, ông chú. Ảnh nền BG_A_EAST. Không lấy ghế cậu bé vào khung.",
          "④ Từ đầu bàn nhìn xuống cuối bàn (góc nhìn của Gloria). Ảnh nền BG_A_SOUTH. Không lấy mặt cậu bé vào khung."):
    y = wrap(40, y, s, f(18), 960)
d.text((40, y + 6), "* chỉ hôm sinh nhật   ** chỉ tối thứ Sáu", font=f(16), fill=MUTE)

# ---------- behind every person ----------
RX = 1050
d.text((RX, 130), "Sau lưng từng người", font=f(26, True), fill=INK)
rows = [("Gloria (đầu bàn) · ①", "Thìa dĩa gỗ ngay sau vai, lệch trái; tranh nhỏ và cửa vòm xa hơn bên trái. Bên phải: tủ buffet với 3 túi quà*, băng rôn và bóng bay 71* phía trên."),
        ("Terrance (tường ảnh, sát đầu bàn) · ②", "Ảnh cưới cũ của Gloria với người chồng đã mất."),
        ("Jada (giữa dãy tường ảnh) · ②", "Ảnh tốt nghiệp đại học của Terrance; ảnh Gloria với Terrance và vợ trước nhà thờ."),
        ("Bà dì (gần cuối bàn) · ②", "Tủ chén gỗ cửa kính, bộ chén đĩa đẹp; phía trên là ảnh tốt nghiệp cấp 3 của Jada và một ảnh cưới (đúng như ảnh 0C)."),
        ("Vợ Terrance (tường cửa sổ, sát đầu bàn) · ③", "Tranh phong cảnh đồng quê có ngôi nhà trại trắng, không người, không chữ."),
        ("Cậu bé (giữa dãy) · chỉ thấy tay", "Cửa sổ rèm voan trắng, ngoài trời tối. Hướng ③ ④ đều cắt khung tránh ghế này."),
        ("Ông chú (gần cuối bàn) · ③", "Chậu lan ý cao đặt dưới sàn ở góc phòng."),
        ("Ghế trống cuối bàn · ④", "Lối mở rộng sang phòng khách: sofa be, chăn móc len, đèn cây sáng ấm."),
        ("Đứng ở tủ buffet · ①", "Góc phải tường đầu phòng; băng rôn và bóng bay 71* ngay phía trên; thứ Sáu: khăn caro với vài muôi gỗ."),
        ("Đứng ở cửa vòm · ①", "Hành lang tối dẫn ra bếp; thứ Sáu: thùng trơn chồng ở hành lang.")]
y = 178
for who, what in rows:
    box(RX, y, 1860, y + 8, (250, 248, 244), outline=(250, 248, 244))
    d.text((RX, y), who, font=f(19, True), fill=INK)
    y = wrap(RX + 18, y + 28, what, f(18), 780, fill=(60, 58, 55)) + 12
d.text((RX, y + 4), "Chung cả phòng: tường kem, thảm be, đèn chùm 5 chao kính mờ trên bàn,", font=f(17), fill=MUTE)
d.text((RX, y + 28), "bàn gỗ nâu sẫm phủ khăn ren trắng, 8 ghế gỗ lưng nan.", font=f(17), fill=MUTE)
im.save(OUT, optimize=True); print(im.size, y)
