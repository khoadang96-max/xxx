# Per-frame checklist for Nam (23/10, "kiểm tra thật kỹ các lỗi vặt"): for every frame, who must be in it, who must stay out (and on which
# side), the props and their count, and what to look at first when picking 1 of the 4 images. Built from the same data as the prompts.
import json, re
from data14 import SH, FRAME_H2
from build14 import HALLWAY, MASTER_OF
FV = json.load(open('out/fv/_parts.json'))
rows = {r['id']: r for r in json.load(open('out/_rows.json'))['rows']}
NAME = {'G': 'Gloria', 'T': 'Terrance', 'J': 'Jada', 'D': 'Dorothy', 'W': 'vợ Terrance', 'B': 'tay cậu bé (không mặt)', 'F': 'con gái Dorothy'}
ROLE = [(r"(her|his) son|her father|the son\b(?!'s wife)", 'T'), (r"(his|her) mother|the grandmother|her grandmother|her friend, the grandmother", 'G'),
        (r"granddaughter|his daughter|her daughter", 'J'), (r"the son's wife|his wife", 'W'), (r"\bthe aunt\b", 'A'), (r"\bthe uncle\b", 'U')]
EXTRA_NAME = {'A': 'bà dì', 'U': 'ông chú'}
SIDE = {'screen-left': 'trái', 'screen-right': 'phải'}

def who_of(code, s):
    if code in EXTRA_NAME: return EXTRA_NAME[code]
    return NAME[code[0]]

def outside(txt, s):
    """the person each "out of the frame" belongs to: the role named right before it, or the one in ", where her son stands" after it"""
    out = []
    for cl in re.split(r';|\. ', txt):
        for m in re.finditer(r'(both )?(just )?out of the frame|not in the room', cl):
            side = re.search(r'screen-(left|right)', cl[m.start():m.start() + 60]) or ([None] + list(re.finditer(r'screen-(left|right)', cl[:m.start()][-100:])))[-1]  # the nearest side before it
            tag = f" ({SIDE[side.group(0)]})" if side else ''
            after = re.match(r'[^,;]*, where (her|his) (son|mother|friend|granddaughter) (stands|sits)', cl[m.end():])
            if after:
                cands = [(0, {'son': 'T', 'mother': 'G', 'granddaughter': 'J', 'friend': 'G' if 'D' in s['chars'] else 'D'}[after.group(2)])]
            else:
                cands = []
                for rx, code in ROLE + [(r'\bher friend\b(?!, the grandmother)', 'FR')]:
                    for r_ in re.finditer(rx, cl[:m.start()]):
                        cands.append((r_.start(), code))
                cands.sort()
                cands = cands[-2:] if m.group(1) else cands[-1:]
            for pos_, code in cands:
                if code == 'FR': code = 'G' if 'D' in s['chars'] else 'D'
                own = re.match(r"[^,;]*?, in the next chair at (screen-left|screen-right)", cl[pos_:])  # "her father, in the next chair at screen-right, and ..."
                out.append(who_of(code, s) + (f" ({SIDE[own.group(1)]})" if own else tag))
    return list(dict.fromkeys(out))

def inside(txt, s):
    names = [NAME[c[0]] if c != 'FD' else NAME['F'] for c in s['chars']]
    names += [NAME[c[0]] + ' (mờ)' for c in s['extra'] if c != 'B'] + (['tay cậu bé (không mặt)'] if 'B' in s['extra'] else [])
    names += [NAME[c[0]] + ' (mép)' for c in s['edge']]
    if s['hands_of']: names.append('tay ' + NAME[s['hands_of'][0]])
    for rx, nm in ((r"the aunt's shoulder|the aunt lifts|the aunt looks|the aunt laughing", 'bà dì (mép)'), (r"the uncle's bald head|the uncle looks|the uncle laugh", 'ông chú (mép)'),
                   (r"only the boy's small hand", 'tay cậu bé (không mặt)')):
        if re.search(rx, txt) and nm not in names: names.append(nm)
    return list(dict.fromkeys(names)) or ['không người']

def props(s, alt):
    p = []
    if 'dish' in s['props']: p.append('tô salad khoai tây')
    if 'dishpot' in s['props']: p.append('tô khoai nóng')
    if 'sil' in s['props']: p.append('đồ silicone xanh ngọc (đúng món trong prompt, không thêm khuôn bánh, không thêm ống thứ hai)')
    if 'bro' in s['props']:
        p.append('brochure: ' + ('chữ WRENFIELD · SENIOR LIVING đọc được' if s['text_on_object'] else 'bìa quay về Gloria, lưng ra máy' if s['bro_ref'] and 'plain back' in s['bro_ref']
                                 else 'bìa ảnh các cụ, dải trên trống không chữ' if s['bro_ref'] else 'đúng bìa'))
    if 'aca' in s['props']:
        c = s['aca_count'] or ''
        p.append('đồ gỗ: ' + ('đủ 7 món' if not c else '1 món trong tay, còn lại ngoài khung' if c.startswith('Only one') or c.startswith('Only the') else
                             'ống chỉ 6 món + 1 món trên tay' if 'holds only the other six' in c else 'muỗng trên tay + vài món trên khăn (không quá 6)' if 'never more than six' in c else c[:60]))
    if 'hold' in s['props']: p.append('ống gỗ tròn')
    if 'towel' in s['props'] or 'checkered towel' in s['frame']: p.append('khăn caro đỏ trắng')
    if 'bottle' in s['props']: p.append('bình hồng của Jada ' + ('trên bàn' if s['bg'] in MASTER_OF else 'trên quầy') + ', không ai cầm')
    if 'water' in s['props']: p.append('ly nước nóng, nước trong')
    if re.search(r'\bbox(es)?\b', s['frame']) or s['bg'] in ('B_BOXES',): p.append('thùng trơn, không chữ')
    return '; '.join(p) or '—'

def watch(s, alt):
    w = []
    talk = rows[s['id']]['kind'] == 'T'
    if s['bg'] in MASTER_OF and s['id'] not in HALLWAY and not alt: w.append('đúng ghế như ảnh mẫu, không người lạ')
    if alt: w.append('không lọ hoa trước mặt, không băng rôn trên tường ảnh, mép dưới là mép bàn')
    if talk: w.append('môi người nói lộ rõ, không tay/ly/nĩa/muỗng che')
    if s['shot'] in ('Extreme close-up', 'Very tight close-up') and talk: w.append('thấy cả miệng')
    if s['plate']: w.append('nền là ảnh 0F (bếp nhìn về phía bếp gas' + (', có cửa)' if 'NIGHT' in s['plate'] else ')'))
    if s['id'] in HALLWAY: w.append('ở hành lang, không thấy bàn ăn')
    if s['chars']: w.append('mặt dưới 1/3 trên khung (chừa banner)')
    if s['bg'] in ('B_MORNING', 'B_BOXES', 'B_CLEAR'): w.append('bếp sáng, tủ trắng ra trắng')
    if s['bg'] == 'B_NIGHT': w.append('đêm nhưng mặt đủ sáng')
    if 'D' in s['chars']: w.append('Dorothy đội mũ, đeo kính trên mặt')
    if 'trash can' in (FRAME_H2[s['id']] if alt else s['frame']): w.append('đúng một thùng rác đạp chân, đứng cạnh tủ lạnh')
    if 'Wide shot' == s['shot'] and s['bg'] in MASTER_OF: w.append('đủ 7 người')
    return '; '.join(w)

L = ["# S14c — Bảng soi từng khung (23/10)\n",
     "Dùng khi chọn 1 trong 4 ảnh mỗi node. Mỗi dòng: ai phải có trong khung, ai phải ở ngoài khung (và ở phía nào của màn hình), đồ nào phải có và đếm, "
     "rồi những chỗ hay sai cần soi trước. Sai một cột là bỏ ảnh đó, chọn ảnh khác; cả 4 ảnh cùng sai một cột thì báo Claude số khung và cột sai, "
     "Claude sửa đúng node đó (không phải chạy lại cả file).\n",
     "Phía trái/phải là trái/phải của màn hình. Bếp: đêm Gloria nhìn sang phải, Terrance sang trái; sáng hôm sau Gloria (ở bếp gas) nhìn sang trái, Jada sang phải; "
     "bếp đóng thùng Gloria đứng bên trái nhìn sang phải, khách (Dorothy, Terrance) bên phải nhìn sang trái.\n"]
for p in FV:
    if p['kind'] not in ('F', 'Fb'): continue
    L.append(f"\n## {p['num']} — {p['name']}\n")
    L.append("| Khung | Trong khung | Ngoài khung | Đồ, đếm | Soi kỹ |\n|---|---|---|---|---|")
    for f in p['frames']:
        sid = f[len('S14c_F_'):]; alt = sid.endswith('_H2'); base = sid[:-3] if alt else sid
        s = next(x for x in SH if x['id'] == base)
        txt = FRAME_H2[base] if alt else s['frame']
        L.append(f"| `{sid}` | {', '.join(inside(txt, s))} | {', '.join(outside(txt, s)) or '—'} | {props(s, alt)} | {watch(s, alt)} |")
open('out/S14c_Black_ChecklistKhung.md', 'w').write('\n'.join(L) + '\n')
print('checklist rows', sum(1 for l in L if l.startswith('| `')))
