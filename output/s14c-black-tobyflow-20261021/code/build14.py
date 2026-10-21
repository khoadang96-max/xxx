# Build S14c (Black) TobyFlow workflow: Toby export JSON + MCP payload + prompt pack + SRT
import json, random, re, string, os
from data14 import SH

OUT = 'out'
os.makedirs(OUT, exist_ok=True)
SCRIPT = 'S14c'
WF_NAME = 'S14c Black'
src = {s['id']: s for s in json.load(open('shots.json'))}

# ---------- characters (editor doc mục 5 + research 22/10) ----------
# Each person gets their own skin depth and undertone (real families vary), hair texture, individual features and the age signs
# of brown skin (few deep wrinkles, uneven tone under the eyes, small raised spots on the cheeks in older adults).
# FULL text goes into the character sheets, SHORT text into the shot frames (the sheet carries the face).
SKIN_TONE = ("Brown skin true to life: each person keeps their own skin depth and undertone, rich and natural, with soft highlights on the forehead, "
    "cheekbones and nose and visible detail in the shadows; palms lighter than the backs of the hands; never grey, ashy, washed out, orange or lightened; "
    "every face has enough soft light to read its expression.")
GLORIA_FULL = ("The grandmother: a 71-year-old Black American woman with medium-deep brown skin and warm red-gold undertones. "
    "A round face with full cheeks, warm brown eyes, a broad soft nose and full lips; her skin has few deep wrinkles for her age: soft smile lines, "
    "gentle creases at the outer corners of her eyes, slightly deeper-toned skin under her eyes and a few tiny raised deep-brown spots on her upper cheeks, "
    "as many older Black women have. Short natural silver-white hair in tight coils, cut in a neat tapered shape, close at the sides and back and fuller on top. "
    "Reading glasses with thin gold frames hang on a fine chain against her chest; small gold stud earrings, a small gold cross necklace and a thin gold wedding band. "
    "Medium height, a soft, solid build and an upright posture: the proud, healthy, quick-witted matriarch of her family, never frail.")
GLORIA_SHORT = ("The grandmother: a 71-year-old Black American woman with medium-deep brown skin and warm undertones, a round face, short tapered silver-white coily hair, "
    "gold-framed reading glasses hanging on a chain at her chest, small gold earrings and a small gold cross.")
TERR_FULL = ("Her son: a 46-year-old Black American man with deep brown skin and warm undertones, a shade deeper than his mother's. "
    "He has his mother's warm brown eyes and broad nose in a longer face with a strong, tense jaw and a few faint lines on his forehead. "
    "Short black hair with a little grey at the temples, cut in a low taper fade with tight short coils on top and a clean natural hairline; "
    "a full, neatly trimmed salt-and-pepper beard with a clean edge along the cheeks; a gold wedding band. "
    "Medium-tall with a solid build: an office professional and a dad.")
TERR_SHORT = ("Her son: a 46-year-old Black American man with deep brown skin, a low taper fade with a little grey at the temples, "
    "a neatly trimmed salt-and-pepper beard, a tense jaw and a gold wedding band.")
JADA_FULL = ("The granddaughter: a 19-year-old Black American college student with medium brown skin and warm golden undertones, a shade lighter than her father's. "
    "An oval face with high round cheekbones, her father's warm brown eyes, a soft broad nose, full lips and natural brows. "
    "Long medium-size knotless braids in natural black-brown, reaching the middle of her back and gathered in a low ponytail, with neat laid edges along her hairline; "
    "small gold hoop earrings; little or no makeup; a bright, open, expressive face.")
JADA_SHORT = ("The granddaughter: a 19-year-old Black American woman with medium brown skin, long knotless braids gathered in a low ponytail, "
    "small gold hoop earrings and a bright, expressive face.")
DOROTHY_FULL = ("The friend: a 73-year-old Black American woman, the grandmother's longtime neighbor from the same church, with deep brown skin and cool undertones, "
    "deeper than the grandmother's. A long oval face with high cheekbones and a calm mouth; her skin has few deep wrinkles for her age, with fine lines around the eyes "
    "and a few tiny raised deep-brown spots on her cheeks. Short natural silver hair in a soft, rounded close-cropped afro. "
    "Large round glasses with tortoiseshell frames, worn on her face. Tall and slender with an unhurried, upright posture; "
    "a calm face with quiet authority and a hint of dry humor.")
DOROTHY_SHORT = ("The friend: a 73-year-old Black American woman with deep brown skin, a long oval face, short close-cropped silver natural hair "
    "and large round tortoiseshell glasses worn on her face; tall and slender.")
WIFE_FULL = ("The son's wife: a 44-year-old Black American woman with light-medium brown skin and golden undertones, an oval face with almond-shaped eyes "
    "and a warm, composed expression, natural black coily hair pulled up in a neat high bun, and a gold wedding band.")
WIFE_SHORT = "The son's wife: a 44-year-old Black American woman with light-medium brown skin and natural hair in a neat high bun."
BOY = ("The son's youngest child, a 10-year-old Black American boy with medium-deep brown skin: only his small hands and forearms appear, "
    "at the edge of the table; his face stays out of the frame.")
FD_FULL = ("The friend's daughter: a Black American woman of about 48 with deep brown skin like her mother's, her mother's long face and short, neatly styled hair, "
    "seen only through the car window.")

G_REF = "Image {n} is the grandmother's character sheet: use it only for her face, skin tone, silver hair, glasses on the chain, jewelry and clothes."
G_FIN = "the grandmother is the same woman as in her character sheet, with the same skin tone, silver hair, glasses on the chain and gold jewelry"
G_KEEP = "the same face, skin tone, age, silver coily hair, gold-framed reading glasses on the chain, gold earrings, gold cross and wedding band"
T_REF = "Image {n} is her son's character sheet: use it only for his face, skin tone, haircut, beard and clothes."
T_FIN = "her son is the same man as in his character sheet, with the same skin tone, haircut and beard"
T_KEEP = "the same face, skin tone, age, haircut, salt-and-pepper beard and wedding band"
J_REF = "Image {n} is the granddaughter's character sheet: use it only for her face, skin tone, braids, earrings and clothes."
J_FIN = "the granddaughter is the same young woman as in her character sheet, with the same skin tone and braids"
J_KEEP = "the same face, skin tone, age, knotless braids and gold hoop earrings"
SKIN_TONE_FRAME = ("Brown skin true to life: each person keeps their own skin depth and undertone, with soft natural highlights and visible detail in the shadows; "
    "palms lighter than the backs of the hands; never grey, ashy or lightened.")
SKIN_TONE_HANDS = ("Brown skin true to life: rich, natural undertones with soft highlights on the knuckles and visible detail in the shadows; "
    "palms lighter than the backs of the hands; never grey, ashy, washed out, orange or lightened.")
def ch(who, full, short, outfit, sheet, ref, final, keep=None, expr=None, pr='she'):
    return dict(who=who, full=full, short=short, outfit=outfit, sheet=sheet, ref=ref, final=final, keep=keep, expr=expr, pr=pr)
G_EXPR, T_EXPR, J_EXPR = ("neutral, proud smile, hurt, tearful laugh", "neutral, tense jaw, pleading, tearful apology",
                          "neutral, bright laugh, uncomfortable wince, nervous hope")
CH = {
 'G1': ch('the grandmother', GLORIA_FULL, GLORIA_SHORT, "She wears a copper-colored silk blouse, a pearl necklace, a cream cardigan and a floral cotton apron.", 'CS_GLORIA_1', G_REF, G_FIN, G_KEEP, G_EXPR),
 'G2': ch('the grandmother', GLORIA_FULL, GLORIA_SHORT, "She wears a lavender cardigan over a plain white T-shirt and grey slacks.", 'CS_GLORIA_2', G_REF, G_FIN, G_KEEP, G_EXPR),
 'G3': ch('the grandmother', GLORIA_FULL, GLORIA_SHORT, "She wears a burgundy sweater, small gold earrings and the same floral cotton apron.", 'CS_GLORIA_3', G_REF, G_FIN, G_KEEP, G_EXPR),
 'G4': ch('the grandmother', GLORIA_FULL, GLORIA_SHORT, "She wears a soft blue cardigan over a cream blouse and the same floral cotton apron.", 'CS_GLORIA_4', G_REF, G_FIN, G_KEEP, G_EXPR),
 'T1': ch('her son', TERR_FULL, TERR_SHORT, "He wears a navy quarter-zip pullover and chinos.", 'CS_TERRANCE_1', T_REF, T_FIN, T_KEEP, T_EXPR, 'he'),
 'T2': ch('her son', TERR_FULL, TERR_SHORT, "He wears a grey fleece work vest over a button-down shirt.", 'CS_TERRANCE_2', T_REF, T_FIN, T_KEEP, T_EXPR, 'he'),
 'T3': ch('her son', TERR_FULL, TERR_SHORT, "He wears a plaid button-down shirt.", 'CS_TERRANCE_3', T_REF, T_FIN, T_KEEP, T_EXPR, 'he'),
 'T4': ch('her son', TERR_FULL, TERR_SHORT, "He wears a navy crewneck sweater.", 'CS_TERRANCE_4', T_REF, T_FIN, T_KEEP, T_EXPR, 'he'),
 'J1': ch('the granddaughter', JADA_FULL, JADA_SHORT, "She wears a plain grey hoodie with no logo and leggings.", 'CS_JADA_1', J_REF, J_FIN, J_KEEP, J_EXPR),
 'J2': ch('the granddaughter', JADA_FULL, JADA_SHORT, "She wears a green knit sweater.", 'CS_JADA_2', J_REF, J_FIN, J_KEEP, J_EXPR),
 'D':  ch('the friend', DOROTHY_FULL, DOROTHY_SHORT,
          "She is just back from church: a moss-green dress, a matching cardigan with a small brooch, a canvas tote bag on her shoulder.", 'CS_DOROTHY',
          "Image {n} is the friend's character sheet: use it only for her face, skin tone, silver hair, round glasses and clothes.",
          "the friend is the same woman as in her character sheet, with the same skin tone, silver hair and round glasses",
          expr="neutral, knowing smile, one raised eyebrow, calm and serious"),
 'W':  ch("the son's wife", WIFE_FULL, WIFE_SHORT, {'A_BDAY': "She wears nice dinner clothes.", 'A_FRI': "She wears a soft knit sweater."}, 'CS_WIFE',
          "Image {n} is the son's wife's character sheet: use it only for her face, skin tone and hair.",
          "the son's wife is the same woman as in her character sheet", expr="neutral, warm smile, worried, laughing"),
 'B':  ch('the boy', BOY, BOY, {'A_BDAY': "His sleeves belong to a striped polo shirt.", 'A_FRI': "His sleeves belong to a plain blue hoodie."}, 'CS_GRANDSON',
          "Image {n} shows the boy's clothes: use it only for his sleeves.", '', pr='he'),
 'FD': ch("the friend's daughter", FD_FULL, FD_FULL, "She wears a church dress.", 'CS_FRIEND_DAUGHTER',
          "Image {n} is the friend's daughter's character sheet: use it only for her face, skin tone and hair.",
          "the friend's daughter is the same woman as in her character sheet"),
}
def outfit_of(c, bg=None):
    o = CH[c]['outfit']
    return o if isinstance(o, str) else o.get(bg, next(iter(o.values())))
LOOKS = {
 'A_BDAY': "warm evening light from a small chandelier, soft shadows, warm family-film color",
 'A_FRI': "warm evening light from a small chandelier, soft shadows, warm family-film color",
 'B_NIGHT': "night, the kitchen lit only by the warm yellow range-hood light, the rest of the room falling into soft shadow, quiet and tense",
 'B_MORNING': "early morning, slanted sunlight through the window over the sink, soft and a little cool",
 'B_BOXES': "plain daylight in a lived-in kitchen, natural color",
 'B_CLEAR': "bright, clean, warm daylight kitchen",
 'C': "night, a yellow porch light against the deep blue night",
 'D': "soft late-afternoon sun, warm and calm",
}
KITCHEN = ("Her own kitchen, lived in for 42 years: painted white cabinets, a laminate counter, an old white gas range with a range hood "
    "and a seasoned cast-iron skillet on one burner, family photos on the fridge, a paper church hand fan hanging by the old corded wall receiver.")
SIL = "a matching set of new-looking teal silicone kitchen utensils (spatula, ladle, serving spoon) with teal handles, no chips, no damage"
BG = {
 'A_BDAY': ("Photorealistic vertical 9:16 photo of an empty room, no people. The dining room of a well-kept family home in a mid-size American city: "
    "a long deep-brown wooden table with a white lace tablecloth over a solid cloth, eight chairs, a warm chandelier, a china hutch holding the good china, "
    "an artificial flower centerpiece, framed family and graduation photos on the wall, a large decorative carved wooden fork and spoon hanging on the wall. "
    "Birthday decorations: a gold banner reading \"HAPPY 71ST, MAMA\", gold number balloons \"7\" and \"1\", gift bags tied with bows on the sideboard."),
 'A_FRI': ("Photorealistic vertical 9:16 photo of an empty room, no people. The same dining room on a Friday night with no decorations: "
    "the deep-brown wooden table with the lace tablecloth, the china hutch, the carved wooden fork and spoon on the wall; "
    "cardboard moving boxes stacked in the hallway, visible through an archway."),
 'B_NIGHT': "Photorealistic vertical 9:16 photo of an empty kitchen, no people. " + KITCHEN + " A white ceramic crock of " + SIL + " stands beside the stove. At night.",
 'B_MORNING': "Photorealistic vertical 9:16 photo of an empty kitchen, no people. " + KITCHEN + " A white ceramic crock of " + SIL + " stands beside the stove. Morning.",
 'B_BOXES': "Photorealistic vertical 9:16 photo of an empty kitchen, no people. " + KITCHEN + " A white ceramic crock of " + SIL + " stands beside the stove. Half-packed: cardboard moving boxes, newspaper and packing tape on the counter and floor.",
 'B_CLEAR': ("Photorealistic vertical 9:16 photo of an empty kitchen, no people. " + KITCHEN + " Weeks later: no boxes, the counter clean; the white crock and the teal silicone utensils are gone; "
    "a round acacia wood utensil holder with the wooden utensil set stands on the counter by the stove. Image 1 is the real product photo of the holder with the set: "
    "use it only for the holder and utensils' shapes, number, grain and color; ignore its lighting and background."),
 'C': "Photorealistic vertical 9:16 photo, no people, seen from inside the house through the screen door. The front porch of her house at night: a screen door, a yellow porch light, two porch chairs, a potted fern, a quiet residential street beyond.",
 'D': "Photorealistic vertical 9:16 photo, no people. The friend's front porch on the same street, Sunday afternoon after church: a white porch swing, hanging Boston ferns, a small side table with a coffee mug, a short driveway.",
}
BG_DESC = {'A_BDAY':'the empty birthday dining room','A_FRI':'the empty dining room on Friday night','B_NIGHT':'the empty kitchen at night',
 'B_MORNING':'the empty kitchen in the morning','B_BOXES':'the empty half-packed kitchen','B_CLEAR':'the empty clean kitchen weeks later',
 'C':'the empty front porch at night seen through the screen door','D':"the friend's empty front porch"}

CAMERA_LOOK = ("looking like an ordinary frame from a real camera with a normal lens, not a render; true-to-life gentle colors and soft natural contrast; "
    "fine natural grain; the far background a touch softer than the foreground. No over-sharpening, no HDR, no CGI look.")
SKIN = ("Skin as a real camera sees it from a couple of meters away: natural, with subtle texture and slight unevenness, not retouched, not over-detailed; "
    "no airbrushed, waxy or plastic skin.")
ACA = ("ACAWOOD SET: solid deep-brown acacia wood utensils with visible natural grain, each carved from a single piece, matte oiled finish (not glossy, not varnished), "
    "a small hanging hole near the end of each handle. Exactly seven utensils in the full set: a ladle, a wok spatula, a slotted spoon, a turner, a serving spoon, "
    "a mixing spoon and a small spoon. The utensils keep the exact shape of the real product photo.")
TOWEL = "one red-and-white checkered cotton kitchen towel (the same towel in every shot)"
BRO = "a glossy senior-living brochure whose cover photo shows smiling seniors at a communal dining table"
DISH = "a large glass bowl of homemade potato salad (potatoes, chopped egg, celery, relish, a light dusting of paprika on top)"
DISHPOT = "a large mixing bowl of warm, just-boiled potatoes and chopped egg with mayonnaise"
FOOD_ACA = "Food with the wooden utensils: fresh, bright and appetizing, neatly served; the bowl, plates, pot, counter and table are clean and tidy."
def food_aca(s):
    return 'aca' in s['props'] and bool(re.search(r'potato|salad|tast|serv|spoonful|\bpot\b', s['frame'] + ' ' + s['action']))

def lighting_match(n):
    return ("Lighting match: the wooden utensils are lit by exactly the same light as the rest of the scene: the same direction, color temperature, softness and exposure, "
        "with soft highlights on the side facing the main light and matching shade on the far side, a soft contact shadow where they touch the counter, towel or a hand. "
        f"The same grain, softness and color grade as the rest of the photo, the same perspective, and a realistic size (the ladle about 33 cm long). Use Image {n} only for the shapes, number, grain and color of the wood; "
        "ignore its lighting, background and shadows. It must look photographed together in one shot, never pasted in or cut out.")

VOICE = {
 'GLORIA': "the voice of a Black American woman in her early seventies with soft Southern roots: a warm, rich alto with a gentle Southern lilt in her vowels, strong and steady breath, no tremor; natural film-dialogue delivery, not an announcer, not salesy",
 'TERRANCE': "the voice of a Black American man in his mid-forties, a professional: a mellow, even baritone, tired and controlled; natural film-dialogue delivery, not an announcer, not salesy",
 'JADA': "the voice of a nineteen-year-old Black American college student: bright, casual, honest and direct, warm with her grandmother; natural, not an announcer, not salesy",
 'DOROTHY': "the voice of a Black American woman in her early seventies with Southern roots: a low, warm, unhurried alto with the calm authority of an elder and a dry wit; natural, not an announcer, not salesy",
}
SPK_WHO = {'GLORIA':'the grandmother','TERRANCE':'her son','JADA':'the granddaughter','DOROTHY':'the friend'}
AMB = {'A_BDAY':'a family dining room, faint cutlery','A_FRI':'a quiet family dining room, a wall clock ticking',
 'B_NIGHT':'a quiet kitchen at night, the range hood humming softly','B_MORNING':'a morning kitchen, birds outside the window',
 'B_BOXES':'a quiet daytime kitchen','B_CLEAR':'a quiet bright kitchen','C':'crickets outside','D':'birds and a quiet street'}
LIVING = {'A_BDAY':'anyone in the soft background breathes and shifts a little; a balloon ribbon in the frame sways slightly',
 'A_FRI':'anyone in the soft background breathes and shifts a little; the chandelier light stays steady',
 'B_NIGHT':'the range-hood light glows steady; nothing else in the room moves',
 'B_MORNING':'the slanted morning light shifts a little on the counter',
 'B_BOXES':'the daylight shifts a little across the boxes',
 'B_CLEAR':'daylight stays steady on the counter',
 'C':'the porch light glows steady; the potted fern stirs slightly in the night air','D':'the hanging ferns stir slightly in the breeze'}
OBJECT_LOCK = ("Object lock: every utensil, bowl, plate, glass, brochure and prop in the picture is a rigid solid object that keeps exactly the same shape, size, length, color "
    "and number of pieces from the first frame to the last; nothing bends, stretches, melts, warps, splits, merges, multiplies, morphs or turns into something else; "
    "nothing appears, disappears or swaps places.")
PEOPLE_LOCK = ("People: everyone in the start frame keeps the same face, age, skin tone, hair and clothes; nobody is added or replaced; "
    "bodies move with real weight, feet on the floor.")
HOLD_LOCK = "Whatever anyone holds stays in exactly the same grip, length and angle as in the start frame and never slides through or passes through their fingers."
PICTURE = "Keep the look, lighting and natural skin of the start frame to the last second."
# talking clips whose action leaves a different end picture (prop set down, turn, bite, tear, focus shift): no frame_2
MOVES_ON = {'A-1', 'B-1', 'C-2', 'E-2', 'S01', 'S02', 'S02_B', 'S02_C', 'S03', 'S03_B', 'S05', 'S09', 'S11', 'S14', 'S16', 'S17', 'S21',
            'S23', 'S29', 'S31', 'S32', 'S35', 'S36', 'S42', 'S54', 'S56', 'S57', 'S66', 'S72', 'S74', 'S84', 'S90'}
FORBID = ['slow motion','slowly','cinematic','smooth camera','shallow depth','studio lighting','dirty','stained','blood',' dark ','dark,','dark.','moody',
          'phone','filming','sharp','crisp','pores','cracks open','tears away','slides off','comes loose','turns it so','small shake','small push','dementia']

def nid():
    return 'node_' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
random.seed(1421)

def line_of(sid):
    l = src[sid]['line']
    m = re.match(r'^([A-Z]+)(?: \([^)]*\))?: (.*)$', l)
    return (m.group(1), m.group(2)) if m else (None, None)

def words(t): return len(t.replace('—', ' ').split())

def dur_for(s, spk, txt):
    shot_len = None
    m = re.search(r'(\d+),(\d) s', src[s['id'] if s['id'] in src else s['line_from']]['time'])
    if m: shot_len = float(m.group(1) + '.' + m.group(2))
    if s['kind'] == 'T':
        end = s['start'] + words(txt) / 2.5
        for d in (6, 8, 10):
            if end + 0.6 <= d: return d, round(end, 1)
        raise SystemExit(f"{s['id']} line too long")
    return (6 if (shot_len or 0) > 3.5 else 4), None

# ---------------- nodes ----------------
nodes, edges, mcp_nodes, mcp_edges = [], [], [], []
idx = {}
def add(name, ntype, x, y, **f):
    n = dict(node_id=nid(), node_type=ntype, node_name=name, pos_x=x, pos_y=y, enabled=f.pop('enabled', True),
             slug=name.lower().replace(' ', '_').replace('-', '_'), slug_auto=False)
    n.update(f); nodes.append(n); idx[name] = n; return n
def prompt_node(name, x, y, text):
    return add(name, 'prompt', x, y, prompt_mode='all', ref_mode='all', prompt=text, use_ai=False, ai_fallback=True, ai_delete_after_run=True, timeout_sec=60)
def image_node(name, x, y, ratio='9:16'):
    return add(name, 'generate', x, y, media_type='Image', prompt_source='upstream_node', multi_prompt=False, model='Nano Banana Pro',
               ratio=ratio, quantity=4, download_resolution='2k')
def video_node(name, x, y, dur, frame_src, enabled=True, same_end=False):
    # same_end: talking clip gets its start image on frame_2 as well, so the people do not drift
    return add(name, 'generate', x, y, enabled=enabled, media_type='Video', prompt_source='upstream_node', multi_prompt=False, model='Omni 1.1 Flash',
               ratio='9:16', quantity=2, video_input_type='Frames', video_resolution='720p', download_resolution='1k',
               video_download_resolution='1080p', video_duration=dur, frame_ref_mode='upstream_node', frame_1_source=frame_src,
               **({'frame_2_source': frame_src} if same_end else {}))
def tai_node(clip, x, y, enabled=True):
    name = f'TAI {SCRIPT}_{clip}'
    return add(name, 'download', x, y, enabled=enabled, download_file_template=f'{SCRIPT}_{clip}', video_download_resolution='1080p')

PORT = {'image_ref': 'input_1', 'text': 'input_2', 'frame_1': 'input_3', 'frame_2': 'input_4'}
def link(a, b, port):
    src_port = 'text' if a['node_type'] == 'prompt' else 'media'
    dt = 'text' if src_port == 'text' else ('video' if a.get('media_type') == 'Video' else 'image')
    edges.append(dict(source_node_id=a['node_id'], source_handle='output_1', source_port=src_port,
                      target_node_id=b['node_id'], target_handle=PORT[port], target_port=port, data_type=dt))

# --- row 0: real photos Nam uploads ---
IMGS = [('IMG_ACA_SET', 'real product photo: the 7 Acawood utensils on white, straight + 3/4'),
        ('IMG_ACA_HOLDER', 'real product photo: the full set standing in the round holder'),
        ('IMG_ACA_TOWEL', 'real product photo, top view: 7 utensils laid in a row on the red-and-white checkered towel (start frame S49)'),
        ('IMG_ACA_MACRO', 'real macro photo: grain running unbroken from handle to head (start frame S53)'),
        ('IMG_WATERTEST', 'a still frame from the real hot-water test clip (water still clear) (ref for F_S87)')]
for i, (n, _) in enumerate(IMGS):
    add(n, 'image', i * 400, 0, ref_images=[])

# --- character sheets + prop sheets ---
SHEET_TAIL = ("Plain light-grey background, soft even daylight, " + CAMERA_LOOK + " " + SKIN + " No text, no labels, no logos.")
sheet_specs = []  # (name, prompt, ref_names)
def sheet_prompt(key):
    c = CH[key]
    if key == 'B':  # no child's face anywhere: clothes only, no person
        return ("Photorealistic wardrobe reference sheet, 16:9, no person: a 10-year-old boy's clothes laid flat side by side on a plain light-grey background: "
                "a striped polo shirt and a plain blue hoodie, both with no logo, each shown front and back. Soft even daylight, " + CAMERA_LOOK + " No text, no labels, no logos.")
    views = (f"front view, three-quarter view, profile, and four expressions ({c['expr']})"
             if key != 'FD' else "front view and three-quarter view, as seen through a car window")
    return f"Photorealistic character reference sheet, 16:9, of one person: {views}. {c['full']} {outfit_of(key, 'A_BDAY')} {SKIN_TONE} {SHEET_TAIL}"
def edit_prompt(k):
    # outfit change of a base sheet; restates the whole person so a missing Image 1 cannot turn into a stranger
    c = CH[k]
    return (f"Edit Image 1. Image 1 is the character reference sheet of {c['who']}. {c['full']} Keep this exact same person: {c['keep']}; "
            f"keep the same views, poses, expressions and layout. Change only the clothes: {c['pr']} now wears {c['outfit'][c['outfit'].index(' wears ') + 7:]} "
            f"{SKIN_TONE} {SHEET_TAIL} Final check: the same person as in Image 1, with the same face, skin tone and hair; only the clothes changed.")
for key, first in (('G', 'G1'), ('T', 'T1'), ('J', 'J1')):
    sheet_specs.append((CH[first]['sheet'], sheet_prompt(first), []))
    for k in [k for k in CH if k.startswith(key) and k != first]:
        sheet_specs.append((CH[k]['sheet'], edit_prompt(k), [CH[first]['sheet']]))
for k in ('D', 'W', 'B', 'FD'):
    sheet_specs.append((CH[k]['sheet'], sheet_prompt(k), []))
sheet_specs.append(('PROP_SILICONE', ("Photorealistic product reference sheet, 16:9, plain light-grey background, soft even daylight: " + SIL +
    ", plus a matching teal silicone muffin pan and the white ceramic crock they stand in at home; each item shown separately, front and side. " + CAMERA_LOOK + " No text, no logos."), []))
sheet_specs.append(('PROP_BROCHURE', ("Photorealistic product reference sheet, 16:9, plain light-grey background, soft even daylight: " + BRO +
    ", letter size, shown closed from the front and at an angle; the cover reads \"WRENFIELD · SENIOR LIVING\" in clean simple print at the top. " + CAMERA_LOOK +
    " No other text, no logos, no address. The lettering on the cover stays exactly \"WRENFIELD · SENIOR LIVING\"."), []))
for i, (name, pr, refs) in enumerate(sheet_specs):
    y = 400 + i * 400
    p = prompt_node('P_' + name, 400, y, pr)
    im = image_node(name, 800, y, ratio='16:9')
    for r in refs: link(idx[r], im, 'image_ref')
    link(p, im, 'text')

# --- backgrounds ---
base_y = 400 + len(sheet_specs) * 400
for i, (k, pr) in enumerate(BG.items()):
    y = base_y + i * 400
    look = ' Look: ' + LOOKS[k] + '. ' + CAMERA_LOOK
    tail = (' No people. No subtitles, no captions, no text overlays; the lettering on the banner and the gold number balloons stays.' if k == 'A_BDAY'
            else ' No people. No subtitles, no captions, no on-screen text, no logos.')
    p = prompt_node(f'P_BG_{k}', 400, y, pr + look + tail)
    im = image_node(f'BG_{k}', 800, y)
    if k == 'B_CLEAR': link(idx['IMG_ACA_HOLDER'], im, 'image_ref')
    link(p, im, 'text')

# --- shots ---
shot_y = base_y + len(BG) * 400 + 400
rows, pack, qa = [], [], []
for r, s in enumerate(SH):
    y = shot_y + r * 400
    spk, txt = line_of(s['line_from'])
    off_screen = s['id'] in ('S18', 'S26', 'S44', 'S48', 'S53', 'S87', 'S88')
    s['kind'] = 'T' if (txt and not off_screen) else 'V'
    dur, end = dur_for(s, spk, txt)
    clip = f"{s['kind']}_{s['id'].replace('-', '')}"
    # ----- frame -----
    if s['src']:
        frame = idx[s['src']]; fprompt = None; refs = []
    else:
        refs = [('BG_' + s['bg'], f"Image {{n}} is {BG_DESC[s['bg']]}: the shot takes place in exactly this room, same furniture, same light; keep the background exactly as in Image {{n}}.")]
        for c in s['chars']:
            refs.append((CH[c]['sheet'], CH[c]['ref']))
        if s['hands_of']:
            refs.append((CH[s['hands_of']]['sheet'], f"Image {{n}} is {CH[s['hands_of']]['who']}'s character sheet: use it only for the skin tone of the hands, the ring and the sleeves."))
        if 'sil' in s['props']: refs.append(('PROP_SILICONE', "Image {n} shows the teal silicone utensils: use it only for their shape and teal color."))
        if 'bro' in s['props']: refs.append(('PROP_BROCHURE', "Image {n} shows the brochure: use it only for its size and cover."))
        if 'aca' in s['props']: refs.append(('IMG_ACA_HOLDER' if 'hold' in s['props'] else 'IMG_ACA_SET', "Image {n} is the real product photo of the wooden utensils."))
        if 'water' in s['props']: refs.append(('IMG_WATERTEST', "Image {n} is a frame from the real hot-water test: match its container, water and light."))
        img_lines = [d.format(n=i + 1) for i, (_, d) in enumerate(refs)]
        blocks = [CH[c]['short'] + ' ' + outfit_of(c, s['bg']) for c in s['chars']]
        prop_txt = []
        if 'dish' in s['props']: prop_txt.append('The bowl is ' + DISH + '.')
        if 'dishpot' in s['props']: prop_txt.append('The bowl is ' + DISHPOT + '.')
        if 'towel' in s['props']: prop_txt.append('The towel is ' + TOWEL + '.')
        if 'bro' in s['props']: prop_txt.append('The brochure is ' + BRO + '.')
        if 'aca' in s['props']:
            n_aca = [i for i, (nm, _) in enumerate(refs) if nm.startswith('IMG_ACA')][0] + 1
            prop_txt.append(ACA); prop_txt.append(lighting_match(n_aca))
            if food_aca(s): prop_txt.append(FOOD_ACA)
        people = bool(s['chars'] or s['hands_of'])
        hands = ("Every hand has five fingers in natural proportion and a natural grip; each person has exactly two arms and two hands; nothing floats."
                 if people else '')
        eyes = ("She looks straight into the lens, as if talking to a friend across the counter." if s['cam'] == 'to'
                else ("Everyone's eyes stay off-lens; nobody looks into the camera." if s['chars'] else ''))
        final = ''
        if [c for c in s['chars'] if c != 'B']:
            final = 'Final check: ' + '; '.join(CH[c]['final'] for c in s['chars'] if c != 'B') + '.'
        end_txt = ("No subtitles, no captions, no text overlays; " + s['text_on_object'] + " stays." if s['text_on_object']
                   else ("No subtitles, no captions, no text overlays; the banner lettering in the background stays." if s['bg'] in ('A_BDAY',)
                   else "No subtitles, no captions, no on-screen text."))
        fprompt = ' '.join(x for x in [
            "Photorealistic vertical 9:16 photo, the first frame of a video shot, " + CAMERA_LOOK,
            ' '.join(img_lines),
            f"{s['shot']}. The photo shows {s['frame']}.",
            ' '.join(blocks), ' '.join(prop_txt), hands, eyes,
            ("Look: " + LOOKS[s['bg']] + '.') if s['bg'] else '', (SKIN + ' ' + (SKIN_TONE_FRAME if s['chars'] else SKIN_TONE_HANDS)) if people else '', final, end_txt] if x)
        pf = prompt_node(f'P_F_{s["id"]}', 400, y, fprompt)
        frame = image_node(f'{SCRIPT}_F_{s["id"]}', 800, y)
        for nm, _ in refs: link(idx[nm], frame, 'image_ref')
        link(pf, frame, 'text')
    # ----- video -----
    cam = {'locked': 'Camera: standing on a tripod, locked off, no movement.',
           'push': 'Camera: glides a few centimeters closer over the whole shot, nothing else.',
           'pullback': 'Camera: eases back a few centimeters in the first second, then holds still.',
           'to': 'Camera: standing on the counter at chest height, locked off.'}[s['cam']]
    phys = ["Physics: real weight and balance; nothing moves on its own: whatever moves is moved by a visible hand or by the action.", OBJECT_LOCK + (' ' + s['lock_extra'] if s['lock_extra'] else '')]
    if s['chars']: phys += [HOLD_LOCK, PEOPLE_LOCK]
    if 'aca' in s['props']: phys.append("The wooden pieces stay lit by the same light as everything else, with real shadows; exactly the same number of wooden pieces as in the start frame.")
    if 'water' in s['props']: phys.append("The water itself stays completely clear and colorless the whole time.")
    if food_aca(s): phys.append(FOOD_ACA)
    living = 'Living layer (only what is already in the frame moves, nothing is added): ' + ('the people breathe and blink naturally; ' if s['chars'] else '') + ('the daylight shifts a little across the wood' if s['src'] else LIVING.get(s['bg'] or 'B_BOXES', '')) + '.'
    amb = s['amb'] or AMB.get(s['bg'] or 'B_BOXES')
    if s['kind'] == 'T':
        who = SPK_WHO[spk]
        pr, pos = ('he', 'his') if spk == 'TERRANCE' else ('she', 'her')
        speech = (f"Speech: {who} speaks with clear lip-sync in {VOICE[spk]}. This is the one voice used for {who} in every clip of this video: keep exactly this voice, accent, age, pitch and pace. "
                  f"This time: {s['tone']}. Exactly these words, word for word, nothing added or repeated: \"{txt}\" "
                  f"{who[0].upper() + who[1:]} starts speaking at about {s['start']} seconds and has finished the whole line by about {end} seconds at the latest; "
                  f"after the last word {pr} keeps the same feeling in {pos} face, lips close and stay closed, no sound. Everyone else stays silent. "
                  f"Face: alive the whole time, never frozen, never a fixed smile; the expression follows the words through the brows, eyes and mouth corners; understated, never theatrical.")
        audio = f"Audio: only {who}'s voice and quiet room tone of {amb}; no music."
    else:
        speech = "Nobody speaks; mouths stay closed or only show expressions."
        audio = f"Audio: no voice, no speech, no singing, no humming, no music; only quiet natural room sound: {amb}."
    eyes_v = ("She looks straight into the lens, as if talking to a friend across the counter." if s['cam'] == 'to'
              else ("Everyone's eyes stay off-lens; nobody looks into the camera." if s['chars'] else ''))
    end_v = ("No subtitles, no captions, no text overlays; " + s['text_on_object'] + " stays and never changes." if s['text_on_object']
             else "No subtitles, no captions, no on-screen text.")
    vprompt = ' '.join(x for x in [
        f"{s['shot']}, {dur} seconds, one continuous shot, no cuts. The image is the start frame; the shot begins exactly on it.",
        cam, ' '.join(phys), f"Action: {s['action']}", living, speech, eyes_v, "Real-time pace, nothing slow-motion; the main action starts within the first second.", PICTURE, audio, end_v] if x)
    pv = prompt_node(f'P_V_{s["id"]}', 1200, y, vprompt)
    same_end = s['kind'] == 'T' and s['id'] not in MOVES_ON
    v = video_node(f'{SCRIPT}_{clip}', 1600, y, dur, frame['node_id'], enabled=s['enabled'], same_end=same_end)
    link(frame, v, 'frame_1')
    if same_end: link(frame, v, 'frame_2')
    link(pv, v, 'text')
    t = tai_node(clip, 2000, y, enabled=s['enabled'])
    link(v, t, 'image_ref')  # placeholder, fixed below
    edges[-1].update(target_handle='input_1', target_port='media_in', data_type='video')
    rows.append(dict(id=s['id'], clip=f'{SCRIPT}_{clip}', kind=s['kind'], dur=dur, end=end, spk=spk, txt=txt, src=s['src'], f2=same_end,
                     refs=[n for n, _ in refs] if not s['src'] else [s['src']]))
    pack.append((s['id'], f'{SCRIPT}_{clip}', fprompt, vprompt, [n for n, _ in refs] if not s['src'] else [s['src'] + ' (khung đầu)'], dur))

# ---------- edges ids ----------
pos = {n['node_id']: i + 1 for i, n in enumerate(nodes)}
for e in edges:
    e_id = f"edge_{pos[e['source_node_id']]}_{e['source_handle']}_{pos[e['target_node_id']]}_{e['target_handle']}"
    e.update({'edge_id': e_id});
edges = [{k: e[k] for k in ('edge_id','source_node_id','source_handle','source_port','target_node_id','target_handle','target_port','data_type')} for e in edges]

desc = ("S14c We Talked About This, bản da đen. Ảnh thật cần tải vào: " + '; '.join(f'{n} = {d}' for n, d in IMGS) +
        ". Thứ tự chạy: IMG_ → CS_/PROP_ (character sheet) → BG_ → F_ từng shot (xem khung) → T_/V_ → TAI. "
        "Ảnh x4, clip x2. Clip nói giữ dáng: khung đầu = khung cuối (frame_1 + frame_2 cùng một ảnh). "
        "Clip có thoại: Omni nói để khớp miệng; dựng xong cho lời từng nhân vật qua ElevenLabs Voice Changer (giữ nhịp, khớp miệng). "
        "S55, S91, hook E-1 dựng UI ở CapCut; hook D-1 dùng lại T_S79.")
settings = dict(parallel=False, quantity=1, delay_between_nodes=20, timeout_per_node=300, retry_on_error=1, stop_on_error=False)
wf = {"version": "1.0", "type": "workflow", "exported_at": "2026-10-21T14:00:00.000Z",
      "workflow": {"name": WF_NAME, "description": desc, "settings": settings, "nodes": nodes, "edges": edges}}
json.dump(wf, open(f'{OUT}/workflow_S14c_Black.json', 'w'), ensure_ascii=False, indent=1)

# MCP create_workflow payload (edges in UI form, refs by node_name)
name_of = {n['node_id']: n['node_name'] for n in nodes}
mcp = dict(name=WF_NAME, description=desc, settings_json=settings,
           nodes=[{**{k: v for k, v in n.items() if k not in ('node_id', 'pos_x', 'pos_y', 'node_type')}, 'ref': n['node_name'], 'type': n['node_type'],
                   **({'frame_1_source': name_of[n['frame_1_source']]} if n.get('frame_1_source') else {}),
                   **({'frame_2_source': name_of[n['frame_2_source']]} if n.get('frame_2_source') else {})} for n in nodes],
           edges=[dict(**{'from': name_of[e['source_node_id']], 'to': name_of[e['target_node_id']]}, port=e['target_port'], source_port=e['source_port'],
                       source_handle=e['source_handle'], target_port=e['target_port'], target_handle=e['target_handle'], data_type=e['data_type']) for e in edges])
json.dump(mcp, open(f'{OUT}/mcp_create_workflow_S14c_Black.json', 'w'), ensure_ascii=False, indent=1)

json.dump(dict(rows=rows, sheets=[s[0] for s in sheet_specs], bgs=list(BG), imgs=IMGS, n_nodes=len(nodes), n_edges=len(edges)),
          open(f'{OUT}/_rows.json', 'w'), ensure_ascii=False, indent=1)

# ---------- prompt pack ----------
with open(f'{OUT}/S14c_Black_prompt_pack.txt', 'w') as f:
    f.write(f"S14c We Talked About This - ban da den - prompt pack TobyFlow ({len(nodes)} node, {len(edges)} edge)\n")
    f.write("Model anh: Nano Banana Pro 9:16 (sheet 16:9). Video: Omni 1.1 Flash, Frames, 720p, tai 1080p.\n\n")
    f.write("=== CHARACTER SHEET + PROP ===\n")
    for name, pr, refs in sheet_specs:
        f.write(f"\n## {name}  (anh dinh: {', '.join(refs) or 'khong'})\n{pr}\n")
    f.write("\n=== ANH NEN ===\n")
    for k, pr in BG.items():
        f.write(f"\n## BG_{k}\n{idx['P_BG_'+k]['prompt']}\n")
    f.write("\n=== SHOT ===\n")
    for sid, clip, fp, vp, refs, dur in pack:
        f.write(f"\n## {sid}  ->  {clip}  ({dur} s)\nAnh dinh theo thu tu Image 1..n: {', '.join(refs)}\n")
        if fp: f.write(f"[KHUNG DAU]\n{fp}\n")
        f.write(f"[VIDEO]\n{vp}\n")

# ---------- SRT (6 versions) ----------
def ts(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s_ = t % 60
    return f"{h:02d}:{m:02d}:{int(s_):02d},{int(round((s_ - int(s_)) * 1000)):03d}"
body = []
for sid, sh in src.items():
    if not sid.startswith('S'): continue
    m = re.match(r'(\d+):(\d+),(\d)\n(\d+),(\d) s', sh['time'])
    st = int(m.group(1)) * 60 + int(m.group(2)) + int(m.group(3)) / 10; ln = float(m.group(4) + '.' + m.group(5))
    spk, txt = line_of(sid)
    if txt: body.append((sid, st, st + ln, txt))
HOOKS = {'H1': (3.5, []), 'A': (4.2, [('A-1', 0, 4.2)]), 'B': (4.5, [('B-1', 0, 4.5)]),
         'C': (4.9, [('C-1', 0, 2.6), ('C-2', 2.6, 4.9)]), 'E': (5.1, [('E-2', 2.6, 5.1)]), 'D': (4.4, [('D-1', 0, 1.8)])}
for hk, (hl, lines) in HOOKS.items():
    items = []
    for hid, a, b in lines:
        items.append((a, b, line_of(hid)[1]))
    shift = 0 if hk == 'H1' else (hl if hk == 'D' else hl - 3.5)
    for sid, a, b, txt in body:
        if sid == 'S01' and hk not in ('H1', 'D'): continue
        items.append((a + shift, b + shift, txt))
    items.sort()
    items = [(a, min(b, items[i + 1][0]) if i + 1 < len(items) else b, t_) for i, (a, b, t_) in enumerate(items)]
    with open(f'{OUT}/S14c_Black_{hk}.srt', 'w') as f:
        for i, (a, b, t_) in enumerate(items, 1):
            f.write(f"{i}\n{ts(a)} --> {ts(b)}\n{t_.upper()}\n\n")
print('nodes', len(nodes), 'edges', len(edges), 'clips', len(rows))
