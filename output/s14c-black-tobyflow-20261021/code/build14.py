# Build S14c (Black) TobyFlow workflow: Toby export JSON + MCP payload + prompt pack + SRT
import json, random, re, string, os
from data14 import SH, FRAME_H2

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
DOROTHY_SHORT = ("The friend: a 73-year-old Black American woman with deep brown skin and cool undertones, clearly deeper than the grandmother's, a long oval face, short close-cropped silver natural hair "
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
          "She is just back from church and keeps her church hat on all afternoon: a moss-green church hat with a medium upturned brim, a matching band and a small "
          "fabric flower, worn tilted slightly to one side, her silver hair showing below it; a moss-green dress, a matching cardigan with a small brooch, "
          "a canvas tote bag on her shoulder.", 'CS_DOROTHY',
          "Image {n} is the friend's character sheet: use it only for her face, skin tone, silver hair, round glasses, church hat and clothes.",
          "the friend is the same woman as in her character sheet, with the same skin tone, silver hair, round glasses and moss-green church hat; nobody else wears a hat",
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
# frames: the wife's birthday outfit comes from her sheet (the 0A sheet prompt only says "nice dinner clothes", so text alone drifted shot to shot)
WIFE_WEAR = {'A_BDAY': "She wears the same dinner outfit as in her character sheet.",
             'A_FRI': "She wears a soft rust-orange knit sweater instead of her dinner outfit."}
def wear(c, bg, frame=''):
    if c == 'W': return WIFE_WEAR.get(bg, outfit_of(c, bg))
    if c == 'D' and 'tote bag on the swing' in frame:  # S31-S32: the tote is set down, not on her shoulder (review 23/10)
        return outfit_of(c, bg).replace("a canvas tote bag on her shoulder", "her canvas tote bag set down on the swing beside her")
    return outfit_of(c, bg)
def ref_of(c, bg):
    if c == 'W' and bg == 'A_BDAY':
        return "Image {n} is the son's wife's character sheet: use it only for her face, skin tone, hair and dinner outfit."
    return CH[c]['ref']
LOOKS = {
 'A_BDAY': "warm evening light from a small chandelier, soft shadows, warm family-film color",
 'A_FRI': "warm evening light from a small chandelier, soft shadows, warm family-film color",
 'B_NIGHT': "night, the kitchen lit only by the warm yellow range-hood light, the rest of the room falling into soft shadow, quiet and tense",
 'B_MORNING': "early morning, slanted sunlight through the window over the sink, soft and a little cool",
 'B_BOXES': "plain daylight in a lived-in kitchen, natural color",
 'B_CLEAR': "bright, clean, warm daylight kitchen",
 'C': "night, a yellow porch light against the deep blue night",
 'D': "soft late-afternoon sun, warm and calm",
 'D_FIX': "soft late-afternoon sun, warm and calm",
}
# kitchen frames: the room plate came out dim and grey-green (Nam 23/10, "quá tối"); frames copy the plate's light, so state the brightness and the faces too.
# Night stays lit only by the range hood (docx), but faces and the room must stay readable on brown skin.
FRAME_LIGHT = {
 'B_MORNING': "The kitchen is bright and airy: soft daylight fills the whole room, the white cabinets read clean white, nothing is gloomy, and every visible face is clearly lit.",
 'B_NIGHT': "The range-hood light falls softly on every visible face, enough to read the expression; the cabinets and the fridge stay readable in soft shadow, never pitch black.",
 'B_BOXES': "The kitchen is bright: plain daylight fills the whole room, the white cabinets read clean white, nothing is gloomy, and every visible face is clearly lit, never in shadow against the window.",
 'B_CLEAR': ("The kitchen is bright and airy: soft daylight fills the whole room, the white cabinets read clean white, nothing is gloomy, and every visible face is "
             "clearly lit; her face is lit softly from the front, never backlit against the window."),
 'D': "Soft daylight reaches under the porch roof and under the brim of the friend's hat, so every visible face is clearly lit.",
}
# every photo in the house shows this Black family (adults only), small and a little soft; the church fan has no people and no lettering
FRIDGE_PHOTOS = ("snapshots of this same Black American family held by plain magnets on the fridge door: the grandmother with her church friends, "
    "her son and his wife, her granddaughter in a graduation cap; every person in them is Black American, only adults, the photos small and a little soft, with no lettering")
WALL_PHOTOS = ("framed photos of this Black American family on the wall: an old wedding photo of the grandmother and her late husband as a young Black couple, "
    "her son's college graduation photo in cap and gown, her granddaughter's high-school graduation portrait, and the grandmother with her son and his wife "
    "outside their church; every person in every photo is Black American, only adults, the photos small and a little soft, with no lettering")
CHURCH_FAN = "a paper church hand fan on a wooden stick, its printed side a simple painting of a small white country church with no people and no lettering"
KITCHEN = ("Her own kitchen, lived in for 42 years: painted white cabinets, a laminate counter, a sink under a window, an old white gas range with a range hood "
    "and a seasoned cast-iron skillet on one burner, a white step trash can with a foot pedal and a lid at the end of the counter, "
    + FRIDGE_PHOTOS + "; " + CHURCH_FAN + ", hanging by the old corded wall receiver.")
SIL = "a matching set of new-looking teal silicone kitchen utensils (spatula, ladle, serving spoon) with teal handles, no chips, no damage"
BG = {
 'A_BDAY': ("Photorealistic vertical 9:16 photo of an empty room, no people. The dining room of a well-kept family home in a mid-size American city: "
    "a long deep-brown wooden table with a white lace tablecloth over a solid cloth, eight chairs, a warm chandelier, a china hutch holding the good china, "
    "an artificial flower centerpiece, " + WALL_PHOTOS + ", a large decorative carved wooden fork and spoon hanging on the wall, "
    "an archway on one side leading to the hallway. Birthday decorations: a gold banner reading \"HAPPY 71ST, MAMA\", gold number balloons \"7\" and \"1\", gift bags tied with bows on the sideboard."),
 'B_MORNING': "Photorealistic vertical 9:16 photo of an empty kitchen, no people. " + KITCHEN + " A white ceramic crock of " + SIL + " stands beside the stove. Morning.",
 'C': "Photorealistic vertical 9:16 photo, no people, seen from inside the house through the screen door. The front porch of her house at night: a screen door, a yellow porch light, two porch chairs, a potted fern, a quiet residential street beyond.",
 'D': "Photorealistic vertical 9:16 photo, no people. The friend's front porch on the same street, Sunday afternoon after church: a white porch swing, hanging Boston ferns, a small side table with a coffee mug, a short driveway.",
}
# other states of the same two rooms: edits of the base image, so walls, photos and furniture stay identical (base image comes from 0A)
# moving boxes get brand logos unless told otherwise (seen on a run, 22/10)
PLAIN_BOXES = "plain brown cardboard moving boxes, unprinted and unlabeled, with no brand marks"
KEEP_DINING = ("the same table, lace tablecloth, chairs, chandelier, china hutch, sideboard, flower centerpiece, framed family photos, carved wooden fork and spoon, "
    "walls and archway")
KEEP_KITCHEN = ("the same cabinets, counter, sink and window, white gas range, range hood, cast-iron skillet, step trash can, fridge with the family snapshots, "
    "church fan, wall receiver and floor")
KITCHEN_FIXED = ("The old white gas range with the cast-iron skillet stays in the lower screen-right and the white step trash can with its foot pedal stays on the "
    "floor by the fridge, exactly as in Image 1.")
BG_EDIT = {
 'A_FRI': ('A_BDAY', 'the empty birthday dining room', KEEP_DINING,
           "remove the birthday banner, the gold number balloons and the gift bags; through the archway, " + PLAIN_BOXES + " now stand stacked in the hallway; a Friday night."),
 'B_NIGHT': ('B_MORNING', 'the empty kitchen in the morning', KEEP_KITCHEN + ", the white crock of teal silicone utensils",
           "the time of day: night outside the window; the kitchen is now lit only by the warm yellow light under the range hood, falling across the stove "
           "and the counter, and the rest of the room falls into soft shadow where the cabinets, the fridge, the trash can and the floor stay readable, never "
           "pitch black. " + KITCHEN_FIXED),
 'B_BOXES': ('B_MORNING', 'the empty kitchen in the morning', KEEP_KITCHEN + ", the white crock of teal silicone utensils",
           "the kitchen is half-packed for a move: " + PLAIN_BOXES + ", a few on the counter near the fridge end and a few on the floor along the cabinets, "
           "crumpled newspaper with soft, unreadable small print and no headlines, and clear packing tape on the counter; the sink, the counter beside the range, the range and the trash can stay clear of boxes; the white "
           "crock now holds only a teal ladle and a teal serving spoon, no teal spatula; bright, plain daytime light fills the whole room and the white cabinets "
           "read clean white. " + KITCHEN_FIXED),
 'D_FIX': ('D', "the friend's empty front porch", ("the same porch ceiling, white porch post, white porch swing and its chains, hanging Boston ferns, potted fern, "
           "grey floor boards, brick walkway, the street and the houses beyond, and the same soft late-afternoon light"),
           "the camera stands a little further back, so the whole porch swing with both of its ends is in the frame; the small wooden side table now stands at the "
           "screen-left end of the swing, right beside its armrest, with the same coffee mug on it; no newspaper and no other paper anywhere."),
 'B_CLEAR': ('B_MORNING', 'the empty kitchen in the morning', KEEP_KITCHEN,
           "weeks later: no boxes, the counter clean; the white crock and the teal silicone utensils are gone; a round acacia wood utensil holder with the wooden "
           "utensil set now stands on the counter by the stove; bright, warm, even daylight now fills the whole kitchen and the white cabinets look clean and bright. "
           + KITCHEN_FIXED + " "
           "Image 2 is the real product photo of the holder with the set: use it only for the holder and "
           "utensils' shapes, number, grain and color; ignore its lighting and background."),
}
BG_DESC = {'A_BDAY':'the empty birthday dining room','A_FRI':'the empty dining room on Friday night','B_NIGHT':'the empty kitchen at night',
 'B_MORNING':'the empty kitchen in the morning','B_BOXES':'the empty half-packed kitchen','B_CLEAR':'the empty clean kitchen weeks later',
 'C':'the empty front porch at night seen through the screen door','D':"the friend's empty front porch",
 'D_FIX':"the friend's empty front porch",
 'B_NIGHT_REV':'the empty kitchen at night, seen from the sink end toward the range and the kitchen doorway',
 'B_CLEAR_REV':'the empty clean kitchen weeks later, seen from the sink end toward the range'}
PORCHES = ('C', 'D', 'D_FIX')  # outdoor plates: "on exactly this porch", not "this room"

CAMERA_LOOK = ("looking like an ordinary frame from a real camera with a normal lens, not a render; true-to-life gentle colors and soft natural contrast; "
    "fine natural grain; the far background a touch softer than the foreground. No over-sharpening, no HDR, no CGI look.")
SKIN = ("Skin as a real camera sees it from a couple of meters away: natural, with subtle texture and slight unevenness, not retouched, not over-detailed; "
    "no airbrushed, waxy or plastic skin.")
ACA_LOOK = ("ACAWOOD SET: solid deep-brown acacia wood utensils with visible natural grain, each carved from a single piece, matte oiled finish (not glossy, not varnished), "
    "a small hanging hole near the end of each handle.")
ACA_FULL = ("Exactly seven utensils in the full set: a ladle, a wok spatula, a slotted spoon, a turner, a serving spoon, "
    "a mixing spoon and a small spoon.")
ACA_SHAPE = "The utensils keep the exact shape of the real product photo."
ACA = ' '.join([ACA_LOOK, ACA_FULL, ACA_SHAPE])
TOWEL = "one red-and-white checkered cotton kitchen towel (the same towel in every shot)"
BRO = "a glossy senior-living brochure whose cover photo shows smiling seniors at a communal dining table"
# the prop sheet fixes the cover photo: a mixed, mostly white group like a real US senior-living ad, so Wrenfield reads as a world away from her own table
BRO_SHEET = ("One glossy senior-living brochure, letter size, shown closed twice: from the front and at an angle. "
    "The cover reads \"WRENFIELD · SENIOR LIVING\" in clean simple print at the top. Below the title, the cover photo shows six smiling seniors "
    "in their seventies and eighties sharing a meal at a long communal dining table in a bright senior-living dining room: a mixed group, mostly white, "
    "with one Black couple among them, all neatly dressed and cheerful, like an ordinary stock marketing photo; only residents in the photo.")
DISH = "a large glass bowl of homemade potato salad (potatoes, chopped egg, celery, relish, a light dusting of paprika on top)"
DISHPOT = "a large mixing bowl of warm, just-boiled potatoes and chopped egg with mayonnaise"
BOTTLE = "a large light-pink insulated tumbler with a handle, a lid and a straw, plain, with no logo or lettering"
# dinner frames edit the master, which has the tumbler at her place (13.jpg), so it stays there in every frame that shows her place (review A)
BOTTLE_AT = {'A_BDAY': 'at her place, as in Image 1', 'A_FRI': 'at her place, as in Image 1',
             'B_MORNING': 'on the counter beside her'}
BOTTLE_AT_SIDE = 'on the table just beyond her plate, on the side away from her father'
BOTTLE_IF = "If the granddaughter's place at the table shows in the frame, her own water bottle stands there exactly as in Image 1, and nobody touches it."
TABLE_FOOD = "Other dishes on the table, soft: collard greens, candied sweet potatoes and cornbread."
# Birthday and Friday dinner: one seat plan (docx: Gloria at the head, Terrance on her right, Jada right next to him, his wife and the boy across;
# Friday: "the same people as at the birthday, in the same seats"). Nam 23/10, F1 run: seats, gift bags and the brochure moved shot to shot and
# strangers sat at the table, so every dinner frame gets the seat plan or a part-view line, the guest list and the 0C table reference MASTER_A_BDAY
AUNT_LOOK = "a Black American woman with medium-brown skin, a round face and shoulder-length silver-grey natural hair in soft twists"
UNCLE_LOOK = "a Black American man with deep brown skin, a bald head and a short white beard"
KIN_WEAR = {'A_BDAY': ("she wears a plum-colored dress.", "he wears a grey sport coat over a light-blue shirt."),
            'A_FRI': ("she wears a navy cardigan over a cream blouse.", "he wears a brown V-neck sweater over a collared shirt.")}
def aunt(bg): return f"The aunt, the grandmother's younger sister, about 66: {AUNT_LOOK}; {KIN_WEAR[bg][0]}"
def uncle(bg): return f"The uncle, the aunt's husband, about 70: {UNCLE_LOOK}; {KIN_WEAR[bg][1]}"
SEATS = ("The seats never change at this table: the grandmother's own chair stands at the head of the table, against the far wall with the archway "
    "and the carved wooden fork and spoon, the sideboard in the corner beside it on the son's wife's side; along the side wall with the framed family photos and the china hutch "
    "sit, from the head: her son, then the granddaughter, then the aunt; "
    "on the other side, facing them, sit from the head: the son's wife, then the boy, then the uncle; the chair at the foot of the table stays empty.")
GUESTS = ("Only these seven people are at this dinner: the grandmother, her son, his wife, the granddaughter, the boy, the aunt and the uncle; "
    "no other guests, no other children, nobody else in the room.")
PART_VIEW = "This shot shows only part of the dinner: everyone not described here is out of the frame, and nobody else is in the room."
GIFTS_MASTER = ("The birthday gifts stand only on the sideboard: the same three gift bags with tissue paper as in Image 1 (a gold one with pink tissue, "
    "a light-blue one and a pink patterned one) and a small crystal dish; there are no gifts on the table.")
# frames edit the chosen master (13.jpg): what is really on the sideboard there (review A)
GIFTS = "The birthday gifts stay only on the sideboard, exactly as in Image 1; there are no gifts on the table."
FRI_SIDEBOARD = ("On the sideboard, where the gift bags stood at the birthday, lies the red-and-white checkered towel with a few pieces of the wooden set on it, "
    "never more than six, and nothing else.")
FRI_SIDEBOARD_SOFT = "On the sideboard, soft and out of focus, lies the red-and-white checkered towel with a few wooden utensils on it, and nothing else."
OFF_SIDEBOARD = 'the sideboard is out of the frame'  # frames that keep the head of the room to one side get no sideboard blocks"
NO_CAKE = "No birthday cake on the table yet."
HALLWAY = {'D-2', 'S78'}  # Friday shots in the hallway, not at the table"
# the boy sits between his mother and the uncle; from the main camera he is hidden behind the uncle (0C image 1, 23/10)
BOY_EDGE = {'A_BDAY': "only the boy's small hand and striped polo sleeve show; the rest of him is hidden behind the uncle",
            'A_FRI': "only the boy's small hands and blue hoodie sleeves show; the rest of him is hidden behind the uncle"}
# Nam 23/10, F1 run: with the master only as a seating reference, almost every dinner frame still put people in the wrong places
# (Jada at the head, Terrance across from her, the sideboard on another wall). Every frame in the dining room is now an edit of that
# day's chosen master photo (0C birthday, 0D Friday), from the same camera: it only zooms in and changes the moment, actions and faces.
MASTER_EDIT = {
 'A_BDAY': "Image {n} is the chosen photo of this birthday dinner from the main camera at the foot of the table, everyone in their own chair: edit this photo.",
 'A_FRI': "Image {n} is the chosen photo of this Friday dinner from the main camera at the foot of the table, everyone in their own chair: edit this photo.",
}
MASTER_OF = {'A_BDAY': 'MASTER_A_BDAY', 'A_FRI': 'MASTER_A_FRI'}
EDIT_KEEP = ("Keep exactly as in Image 1: the room, the camera position and its direction, the light, the table setting, and every person's face, hair and clothes; "
             "everyone who sits stays in their own chair, and nobody new appears. Change only the framing, the moment, the actions and the expressions described here.")
EDIT_ZOOM = "The camera stays put and zooms in, much tighter than Image 1."
# straight-on variants (F1b / F5b): Image 1 is Nam's chosen 0E plate of the wall with the framed photos; the day's master only tells who sits where
SIDE_REF = ("Image {n} is the dining room seen from across the table, looking straight at the wall with the framed family photos and the china hutch: "
            "the shot takes place in exactly this room, same furniture, same light; keep the background exactly as in Image {n}.")
MASTER_REF_SIDE = {
 'A_BDAY': ("Image {n} shows this birthday dinner from the main camera at the foot of the table: use it only to know who sits in which chair "
            "and how the aunt and the uncle look and dress; this shot looks from the other side of the table, as in Image 1."),
 'A_FRI': ("Image {n} shows this Friday dinner from the main camera at the foot of the table: use it only to know who sits in which chair, "
           "how the aunt and the uncle look and what everyone wears tonight; this shot looks from the other side of the table, as in Image 1."),
}
ACROSS_SEATS = ("From this side of the table the head of the table is at screen-right: along the wall, from screen-right to screen-left, stand the chairs of "
                "her son (in front of the low wooden cabinet with the crystal jar and the cluster of framed photos above it), the granddaughter (in front of the "
                "framed graduation portrait of a young man in cap and gown) and the aunt (in front of the tall glass-door china hutch); only the people described "
                "above are in the frame.")
H2_TABLE = ("The only change on the table: the flower centerpiece of Image 1 is gone; only the low dinner dishes are on the table, and nothing on the table "
            "rises between the camera and anyone's face or hands. The camera is just above the near edge of the table; the near-side chairs and the people in "
            "them are behind the camera, not in the frame; the near edge of the table, with a plate of food and cutlery at each place, runs along the bottom "
            "of the frame.")
H2_END = "No subtitles, no captions, no lettering anywhere in the frame; no banner and no balloons on this wall."
BANNER_IF = "banner letters inside this framing stay exactly as in Image 1; no other lettering."
# the hook banner sits at y 290-525 on top of the whole video; faces go below y 560 (docx part 4), so frames keep the top third for background (review A, D)
COMP = "Composition: the top third of the frame holds only background; every face sits below it."
COMP_TIGHT = ("Composition: the eyes sit just above the middle of the frame and the mouth below it; the top third of the frame shows only the forehead, hair "
              "and soft background.")
SIL_REF = ("Image {n} shows the teal silicone utensils: use it only for the shape and color of the teal pieces this shot describes; add nothing else "
           "from it, no muffin pan and no second crock.")
# hands at the edge of the frame: only the rings that person wears (Dorothy wears none; review C1, D)
HANDS_REF = {'T': "use it only for the skin tone of his hands, his sleeves or shirt cuffs and his single gold wedding band",
             'G': "use it only for the skin tone of her hands, her sleeves and her thin gold wedding band",
             'D': "use it only for the skin tone of her hands and her sleeves; she wears no rings"}
FOOD_ACA = "Food with the wooden utensils: fresh, bright and appetizing, neatly served; the bowl, plates, pot, counter and table are clean and tidy."
# Nam 23/10: the expression of every visible person fits the story beat (data14 FACE); image models default to smiles
def face_line(s):
    return f"Expressions true to this moment: {s['face']}; natural and believable, never exaggerated or posed." if s.get('face') else ''
def food_aca(s):
    return 'aca' in s['props'] and bool(re.search(r'potato|salad|tast|serv|spoonful|\bpot\b', s['frame'] + ' ' + s['action']))

def lighting_match(n, number=True, holder=False):
    use = 'the shapes, number, grain and color of the wood' if number else 'the shapes, grain and color of the wood' + (' and for the holder' if holder else '')
    return ("Lighting match: the wooden utensils are lit by exactly the same light as the rest of the scene: the same direction, color temperature, softness and exposure, "
        "with soft highlights on the side facing the main light and matching shade on the far side, a soft contact shadow where they touch the counter, towel or a hand. "
        f"The same grain, softness and color grade as the rest of the photo, the same perspective, and a realistic size (the ladle about 33 cm long). Use Image {n} only for {use}; "
        "ignore its lighting, background and shadows. It must look photographed together in one shot, never pasted in or cut out.")

VOICE = {
 'GLORIA': "the voice of a Black American woman in her early seventies with soft Southern roots: a warm, rich alto with a gentle Southern lilt in her vowels, strong and steady breath, no tremor; natural film-dialogue delivery, not an announcer, not salesy",
 'GLORIA_FREE': "the voice of a Black American woman in her early seventies with soft Southern roots: a warm, rich alto with a gentle Southern lilt in her vowels, a healthy voice, never frail; natural film-dialogue delivery, not an announcer, not salesy",
 'TERRANCE': "the voice of a Black American man in his mid-forties, a professional: a mellow, even baritone, tired and controlled; natural film-dialogue delivery, not an announcer, not salesy",
 'JADA': "the voice of a nineteen-year-old Black American college student: bright, casual, honest and direct, warm with her grandmother; natural, not an announcer, not salesy",
 'DOROTHY': "the voice of a Black American woman in her early seventies with Southern roots: a low, warm, unhurried alto with the calm authority of an elder and a dry wit; natural, not an announcer, not salesy",
}
SPK_WHO = {'GLORIA':'the grandmother','TERRANCE':'her son','JADA':'the granddaughter','DOROTHY':'the friend'}
AMB = {'A_BDAY':'a family dining room, faint cutlery','A_FRI':'a quiet family dining room, a wall clock ticking',
 'B_NIGHT':'a quiet kitchen at night, the range hood humming softly','B_MORNING':'a morning kitchen, birds outside the window',
 'B_BOXES':'a quiet daytime kitchen','B_CLEAR':'a quiet bright kitchen','C':'crickets outside','D':'birds and a quiet street'}
LIVING = {'A_BDAY':'anyone in the soft background breathes and shifts a little; if a balloon ribbon is already in the frame, it sways slightly; nothing else is added',
 'A_FRI':'anyone in the soft background breathes and shifts a little; the chandelier light stays steady',
 'B_NIGHT':'the range-hood light glows steady; nothing else in the room moves',
 'B_MORNING':'the morning light stays steady',
 'B_BOXES':'the daylight stays steady',
 'B_CLEAR':'daylight stays steady on the counter',
 'C':'the porch light glows steady; nothing else moves',
 'D':'the afternoon light stays steady; if a hanging fern is already in the frame, it stirs slightly in the breeze'}
LIVING_EMPTY = 'nothing in the frame moves; no person and no hand appears'
LIVING_PHOTO = 'nothing in the picture moves; the light stays steady'
OBJECT_LOCK = ("Object lock: every utensil, bowl, plate, glass, brochure and prop in the picture is a rigid solid object that keeps exactly the same shape, size, length, color "
    "and number of pieces from the first frame to the last; nothing bends, stretches, melts, warps, splits, merges, multiplies, morphs or turns into something else; "
    "nothing appears, disappears or swaps places.")
PEOPLE_LOCK = ("People: everyone in the start frame keeps the same face, age, skin tone, hair and clothes; nobody is added or replaced; "
    "bodies move with real weight, feet on the floor.")
HOLD_LOCK = ("Whatever anyone holds stays firmly in their grip and moves only together with their hand; it keeps its exact shape and length "
             "and never slides through or passes through their fingers.")
PICTURE = "Keep the look, lighting and natural skin of the start frame to the last second."
# talking clips locked to their start image (frame_2 = frame_1). Nam 22/10: none; talking clips act freely like a film scene
HOLD_POSE = set()
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
        end = max(s['start'] + words(txt) / 2.5, s.get('end') or 0)
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
    # fields and value types as in Nam's Toby files that import (Script 11 04b / 05): duration "6s", download "1080p";
    # frame_1 (+ frame_2 when same_end: talking clip locked to its start image) as in the Script 11 fix
    return add(name, 'generate', x, y, enabled=enabled, prompt_mode='all', ref_mode='all', media_type='Video', video_input_type='Frames',
               video_duration=f'{dur}s', model='Omni 1.1 Flash', quantity=2, ratio='9:16', download_resolution='1080p',
               prompt_source='upstream_node', multi_prompt=False, video_download_resolution='1080p',
               frame_ref_mode='upstream_node', frame_1_source=frame_src,
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
sheet_specs.append(('PROP_BROCHURE', ("Photorealistic product reference sheet, 16:9, " + CAMERA_LOOK + " Plain light-grey background, soft even daylight. " + BRO_SHEET +
    " No other text, no logos, no address. The lettering on the cover stays exactly \"WRENFIELD · SENIOR LIVING\"."), []))
for i, (name, pr, refs) in enumerate(sheet_specs):
    y = 400 + i * 400
    p = prompt_node('P_' + name, 400, y, pr)
    im = image_node(name, 800, y, ratio='16:9')
    for r in refs: link(idx[r], im, 'image_ref')
    link(p, im, 'text')

# --- backgrounds ---
base_y = 400 + len(sheet_specs) * 400
for i, k in enumerate(list(BG) + list(BG_EDIT)):
    y = base_y + i * 400
    look = ' Look: ' + LOOKS[k] + '. ' + CAMERA_LOOK
    tail = (' No people. No subtitles, no captions, no text overlays; the lettering on the banner and the gold number balloons stays.' if k == 'A_BDAY'
            else ' No people. No subtitles, no captions, no on-screen text, no logos.')
    if k in BG_EDIT:
        base, desc, keep, change = BG_EDIT[k]
        place = 'porch' if k == 'D_FIX' else 'room'
        cam_keep = 'the same lens and camera height' if k == 'D_FIX' else 'the same camera position and lens'  # the porch fix steps the camera back
        pr = (f"Edit Image 1, a photo of {desc}. Keep the same {place} exactly: {keep}, {cam_keep}. Change only: {change}"
              + (' ' + lighting_match(2) if k == 'B_CLEAR' else ''))
        tail += f' Final check: the same {place} as in Image 1, only the listed changes.'
    else:
        pr = BG[k]
    p = prompt_node(f'P_BG_{k}', 400, y, pr + look + tail)
    im = image_node(f'BG_{k}', 800, y)
    if k in BG_EDIT: link(idx['BG_' + BG_EDIT[k][0]], im, 'image_ref')
    if k == 'B_CLEAR': link(idx['IMG_ACA_HOLDER'], im, 'image_ref')
    link(p, im, 'text')

# --- dinner table reference (0C): the birthday room plate from 0A with everyone in their seats, same camera ---
MASTER_PEOPLE = ['G1', 'T1', 'J1', 'W']
master_y = base_y + (len(BG) + len(BG_EDIT)) * 400
m_refs = [('BG_A_BDAY', "Image 1 is the empty birthday dining room.")] + [(CH[c]['sheet'], ref_of(c, 'A_BDAY')) for c in MASTER_PEOPLE]
MASTER_PROMPT = ' '.join([
    ' '.join(d.format(n=i + 1) for i, (_, d) in enumerate(m_refs)),
    "Edit Image 1 into the same room during the birthday dinner, seen from exactly the same camera. Keep the room exactly as in Image 1: the same camera position, "
    "lens and framing, walls, archway, carved wooden fork and spoon, framed family photos, china hutch, chandelier, table, lace tablecloth, flower centerpiece, "
    "the HAPPY 71ST, MAMA banner, the gold 7 and 1 balloons, the sideboard with the same gift bags, and the same warm light.",
    "Add the dinner: at every place a plate of food, cutlery and a drinking glass; bowls of collard greens and candied sweet potatoes and a basket of cornbread on the table. " + NO_CAKE,
    SEATS,
    GLORIA_SHORT, outfit_of('G1'), f"She stands at the head of the table beside her own chair, pulled out a little, the sideboard in the corner beside her, smiling, holding {DISH} with a teal silicone serving spoon in it.",
    TERR_SHORT, outfit_of('T1'), "He sits in his chair beside the head of the table.",
    JADA_SHORT, outfit_of('J1'), f"She sits right next to her father; her own water bottle stands {BOTTLE_AT_SIDE}: {BOTTLE}.",
    WIFE_SHORT, WIFE_WEAR['A_BDAY'], "She sits on the other side, opposite her husband, next to the head of the table.",
    aunt('A_BDAY'), uncle('A_BDAY'),
    "Between the son's wife and the uncle, " + BOY_EDGE['A_BDAY'] + ".",
    GIFTS_MASTER, GUESTS,
    "Everyone is relaxed in the middle of the meal, with calm, pleasant faces; the grandmother smiles as the proud hostess; everyone's eyes stay off-lens.",
    "Every hand has five fingers in natural proportion and a natural grip; each person has exactly two arms and two hands; nothing floats.",
    'Look: ' + LOOKS['A_BDAY'] + '.', SKIN, SKIN_TONE_FRAME, CAMERA_LOOK,
    "No subtitles, no captions, no text overlays; the banner lettering stays.",
    "Final check: the same room and camera as in Image 1; " + '; '.join(CH[c]['final'] for c in MASTER_PEOPLE) + "; seven people at the dinner, each in the chair listed."])
pm = prompt_node('P_MASTER_A_BDAY', 400, master_y, MASTER_PROMPT)
mm = image_node('MASTER_A_BDAY', 800, master_y)
for nm, _ in m_refs: link(idx[nm], mm, 'image_ref')
link(pm, mm, 'text')

# --- the Friday dinner master (0D): the birthday master edited to Friday night, same camera and chairs; every Friday table frame edits it ---
FRI_PEOPLE = ['G3', 'T3', 'J2', 'W']
f_refs = [('MASTER_A_BDAY', "Image 1 is the chosen photo of the birthday dinner, taken from the main camera at the foot of the table with everyone in their own chair.")] + \
         [(CH[c]['sheet'], ref_of(c, 'A_FRI')) for c in FRI_PEOPLE] + \
         [('IMG_ACA_SET', "Image 6 is the real product photo: the wooden serving spoon and the pieces on the towel are these utensils, matte deep-brown acacia "
                          "with a small hanging hole near the end of each handle; a few of them lie on the towel, never more than six.")]
MASTER_FRI_PROMPT = ' '.join([
    ' '.join(d.format(n=i + 1) for i, (_, d) in enumerate(f_refs)),
    "Edit Image 1 into the same table on a Friday night two weeks later, seen from exactly the same camera. Keep exactly as in Image 1: the camera position, lens and framing, "
    "the walls, the archway, the carved wooden fork and spoon, the framed family photos, the china hutch, the chandelier and its warm light, the table with the lace tablecloth "
    "and the chairs, and every person in the same chair; there is no flower centerpiece on the table, as in Image 1.",
    "Change only: the birthday banner, the gold 7 and 1 balloons, the gift bags and the crystal dish are gone; through the archway, " + PLAIN_BOXES +
    " stand stacked in the hallway. " + FRI_SIDEBOARD,
    "On the table: a plate of food, cutlery and a drinking glass at every place; bowls of collard greens and candied sweet potatoes and a basket of cornbread; no potato salad on the table yet.",
    GLORIA_SHORT, outfit_of('G3'), f"She stands at the head of the table beside her own chair, holding {DISH} with the wooden serving spoon of the set in it.",
    TERR_SHORT, outfit_of('T3'), "He sits in his chair beside the head of the table.",
    JADA_SHORT, outfit_of('J2'), f"She sits right next to her father; her own water bottle stands {BOTTLE_AT_SIDE}: {BOTTLE}.",
    WIFE_SHORT, WIFE_WEAR['A_FRI'], "She sits on the other side, opposite her husband, next to the head of the table.",
    aunt('A_FRI'), uncle('A_FRI'),
    "Between the son's wife and the uncle, " + BOY_EDGE['A_FRI'] + ".",
    GUESTS,
    "Everyone is quiet and a little uneasy, waiting; nobody smiles; everyone's eyes stay off-lens.",
    "Every hand has five fingers in natural proportion and a natural grip; each person has exactly two arms and two hands; nothing floats.",
    'Look: ' + LOOKS['A_FRI'] + '.', SKIN, SKIN_TONE_FRAME, CAMERA_LOOK,
    "No subtitles, no captions, no on-screen text, no logos.",
    "Final check: the same room, camera and seats as in Image 1, with no birthday decorations; " + '; '.join(CH[c]['final'] for c in FRI_PEOPLE) +
    "; seven people at the dinner, each in the chair listed."])
# --- the standard dining room (Nam 23/10: "dựng 1 căn phòng chuẩn để không bị tù về góc quay"): what stands behind every chair, one empty plate per
# camera direction (0E), each an edit of the 0A plate. No birthday decorations in these views, so both dinners use them. The boy's chair is never
# framed from the east or south view (no child faces).
ROOM = {
 # the wall as in Nam's chosen BG_A_WEST (23/10): a rerun gives the same wall; it also matches the 0C photo (graduation portrait and wedding photo near the head end)
 'W': ("on the wall, from screen-right to screen-left: near the head of the table, a low wooden cabinet with glass doors holding china, a crystal jar and small "
       "framed photos on top, and above it a cluster of framed photos: the old wedding photo of the grandmother and her late husband as a young Black couple, two "
       "graduation portraits of young women in cap and gown and a church photo of the family in their church clothes; behind the middle chair, her son's framed "
       "college graduation portrait in cap and gown; near the foot of the table, a tall wooden china hutch with glass doors full of the good china, two framed "
       "family photos on top; every person in every photo is Black American, only adults, the photos small and a little soft, with no lettering"),
 'E': ("on the wall, from screen-left to screen-right: behind the first chair, nearest the head of the table, a framed painting of a quiet country landscape with a white "
       "farmhouse, with no people and no lettering; behind the middle chair, a window with sheer white curtains, night outside; behind the third chair, nearest the "
       "foot of the table, a tall potted peace lily standing on the carpet in the corner"),
 'S': ("in the far wall, a wide cased opening into the living room: beyond it, soft, a beige sofa with a crocheted throw and a lit floor lamp; along the screen-right side, "
       "the wall with the framed family photos and, near the foot, the china hutch; along the screen-left side, the wall with the window with sheer white curtains and, "
       "near the foot, the tall potted peace lily in the corner"),
}
VIEW_CAM = {
 'W': ("the camera stands on the far side of the table from the framed family photos, at seated eye level, and looks straight across the table at the side wall with the "
       "framed family photos and the china hutch. In the frame: the long side of the deep-brown wooden table with the white lace tablecloth over a solid cloth runs across "
       "the lower part of the frame; on its far side three empty slat-back wooden chairs stand in a row against that wall; ", 
       "The head of the table is just out of the frame at screen-right and the foot just out of the frame at screen-left; no archway, banner, balloons, gift bags or sideboard in this view."),
 'E': ("the camera stands on the side of the table with the framed family photos, at seated eye level, and looks straight across the table at the opposite side wall. "
       "In the frame: the long side of the deep-brown wooden table with the white lace tablecloth over a solid cloth runs across the lower part of the frame; on its far side "
       "three empty slat-back wooden chairs stand in a row against that wall; ",
       "The head of the table is just out of the frame at screen-left and the foot just out of the frame at screen-right; no sideboard, banner, balloons or gift bags in this view."),
 'S': ("the camera stands at the head of the table, at seated eye level, and looks down the length of the table toward its foot. In the frame: the long deep-brown wooden "
       "table with the white lace tablecloth over a solid cloth runs from the lower part of the frame toward the foot, three empty slat-back wooden chairs on each side and "
       "the empty chair at the foot; ",
       "The birthday decorations and the sideboard are on the wall behind the camera, so none of them is in this view."),
}
VIEW_NAME = {'W': 'the side wall with the framed family photos', 'E': 'the side wall with the window', 'S': 'the foot of the table and the opening to the living room'}
def view_prompt(k):
    cam, end = VIEW_CAM[k]
    return ' '.join([
        "Image 1 is the empty birthday dining room, photographed from the foot of the table toward its head.",
        "Make a new photo of this same empty room from another camera position: " + cam + ROOM[k] + "; the flower centerpiece on the table and the chandelier above it.",
        end,
        "Keep everything that belongs to the room exactly as in Image 1: the same cream wall color, table, lace tablecloth, chairs, carpet, "
        + ('' if k == 'E' else 'china hutch, ') + "flower centerpiece and the warm light of the chandelier.",
        'Look: ' + LOOKS['A_BDAY'] + '. ' + CAMERA_LOOK,
        "No people. No subtitles, no captions, no on-screen text, no logos.",
        "Final check: the same room as in Image 1, now facing " + VIEW_NAME[k] + "; every chair empty; nobody in the room; no birthday decorations in view."])
for i, k in enumerate(('W', 'E', 'S')):
    pv_ = prompt_node(f'P_BG_A_{ {"W": "WEST", "E": "EAST", "S": "SOUTH"}[k] }', 1200 + i * 800, master_y + 400, view_prompt(k))
    iv_ = image_node(f'BG_A_{ {"W": "WEST", "E": "EAST", "S": "SOUTH"}[k] }', 1600 + i * 800, master_y + 400)
    link(idx['BG_A_BDAY'], iv_, 'image_ref'); link(pv_, iv_, 'text')

# --- the kitchen seen from the other end (0F, review 23/10): the kitchen photo looks from the range end toward the fridge and has no doorway, so the
# shots toward the range end (the son in the doorway and the over-the-shoulder shot at night, the son tasting at the stove behind her in the Close) get
# their own empty plate, made from the base morning kitchen like the dining room views (0E); Image 2 gives only that day's light and counter
REV_CAM = ("the camera now stands in the aisle at the sink end of the kitchen, at standing eye level, and looks back toward the range end. In the frame: along the "
    "screen-left side, the laminate counter with the white cabinets above and below it, the wall receiver and the paper church fan on the wall, and the old white "
    "gas range with its range hood and the cast-iron skillet at the far end of the counter; at the end of the kitchen, just past the range, an open doorway with a "
    "plain white door frame leading into the hallway; at screen-right, the plain cream wall across the aisle; the fridge and the white step trash can beside it are "
    "behind the camera, out of the frame")
KREV = {
 'B_NIGHT_REV': ('B_NIGHT', 'the same kitchen at night',
    "the white crock of teal silicone utensils stands on the counter beside the range; night outside the window; the kitchen is lit only by the warm yellow "
    "light under the range hood, falling across the stove and the counter, and the rest of the room falls into soft shadow where the cabinets and the floor "
    "stay readable, never pitch black; the hallway beyond the doorway is dim"),
 'B_CLEAR_REV': ('B_CLEAR', 'the same kitchen weeks later',
    "no boxes, the counter clean; no white crock and no teal utensils anywhere; the round acacia wood utensil holder with the wooden utensil set stands on the "
    "counter beside the range; bright, warm, even daylight fills the whole kitchen and the hallway beyond the doorway, and the white cabinets look clean and bright"),
}
def rev_prompt(k):
    state, desc2, now = KREV[k]
    return ' '.join([
        "Image 1 is the empty kitchen in the morning, photographed from the range end along the counter toward the fridge.",
        f"Image 2 is {desc2}, from the same camera: use it only for the time of day, the light and what stands on the counter.",
        "Make a new photo of this same empty kitchen from the other end: " + REV_CAM + ".",
        "Keep everything that belongs to the room exactly as in Image 1: the same white cabinets and their handles, laminate counter, white gas range, range hood, "
        "cast-iron skillet, wall receiver, church fan, walls and floor.",
        "The room now: " + now + ".",
        'Look: ' + LOOKS[state] + '. ' + CAMERA_LOOK[0].upper() + CAMERA_LOOK[1:],
        "No people. No subtitles, no captions, no on-screen text, no logos.",
        "Final check: the same kitchen as in Image 1, now seen from the sink end toward the range and the open doorway; nobody in the room."])
for i, k in enumerate(KREV):
    pr_ = prompt_node(f'P_BG_{k}', 3600 + i * 800, master_y + 400, rev_prompt(k))
    ir_ = image_node(f'BG_{k}', 4000 + i * 800, master_y + 400)
    link(idx['BG_B_MORNING'], ir_, 'image_ref'); link(idx['BG_' + KREV[k][0]], ir_, 'image_ref'); link(pr_, ir_, 'text')

pf_ = prompt_node('P_MASTER_A_FRI', 400, master_y + 400, MASTER_FRI_PROMPT)
mf_ = image_node('MASTER_A_FRI', 800, master_y + 400)
for nm, _ in f_refs: link(idx[nm], mf_, 'image_ref')
link(pf_, mf_, 'text')

# --- shots ---
shot_y = base_y + (len(BG) + len(BG_EDIT)) * 400 + 800
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
        for alt in ((False, True) if s['id'] in FRAME_H2 else (False,)):
            fr_ = FRAME_H2[s['id']] if alt else s['frame']
            medit = not alt and s['bg'] in MASTER_OF and s['id'] not in HALLWAY  # dining-room frame: an edit of that day's master photo
            plate = s['plate'] or ('BG_D_FIX' if s['bg'] == 'D' else 'BG_' + s['bg'])
            refs = ([('BG_A_WEST', SIDE_REF)] if alt else [(MASTER_OF[s['bg']], MASTER_EDIT[s['bg']])] if medit else
                    [(plate, s['bg_ref'] or f"Image {{n}} is {BG_DESC[plate[3:]]}: the shot takes place {'on exactly this porch' if plate[3:] in PORCHES else 'in exactly this room'}, same furniture, same light; keep the background exactly as in Image {{n}}.")])
            for c in s['chars'] + s['extra']:
                refs.append((CH[c]['sheet'], ref_of(c, s['bg'])))
            for c in s['edge']:  # only a shoulder or the hair shows at the edge: the sheet keeps them the right person, no description block
                pr_, pos_ = CH[c]['pr'], ('his' if CH[c]['pr'] == 'he' else 'her')
                refs.append((CH[c]['sheet'], f"Image {{n}} is {CH[c]['who']}'s character sheet: {pr_} shows only in part, at the edge of this frame; use it only for {pos_} skin tone, hair and clothes."))
            if s['hands_of']:
                refs.append((CH[s['hands_of']]['sheet'], f"Image {{n}} is {CH[s['hands_of']]['who']}'s character sheet: {HANDS_REF[s['hands_of'][0]]}."))
            if 'sil' in s['props']: refs.append(('PROP_SILICONE', s['sil_ref'] or SIL_REF))
            if 'bro' in s['props']: refs.append(('PROP_BROCHURE', s['bro_ref'] or "Image {n} shows the brochure: use it only for its size and cover."))
            if 'aca' in s['props']: refs.append(('IMG_ACA_HOLDER' if 'hold' in s['props'] else 'IMG_ACA_SET', "Image {n} is the real product photo of the wooden utensils."))
            if 'water' in s['props']: refs.append(('IMG_WATERTEST', "Image {n} is a frame from the real hot-water test: match its container, water and light."))
            for xn, xt in s['xrefs']: refs.append((xn, xt))
            if alt: refs.append((MASTER_OF[s['bg']], MASTER_REF_SIDE[s['bg']]))
            dinner = (medit or alt) and bool(s['chars'])
            wide = dinner and s['shot'] == 'Wide shot'
            frame_txt = fr_
            img_lines = [d.format(n=i + 1) for i, (_, d) in enumerate(refs)]
            blocks = [CH[c]['short'] + ' ' + wear(c, s['bg'], fr_) for c in s['chars'] + s['extra']]
            prop_txt = []
            if 'dish' in s['props']: prop_txt.append('The bowl is ' + DISH + '.')
            if 'dishpot' in s['props']: prop_txt.append('The bowl is ' + DISHPOT + '.')
            if 'towel' in s['props']: prop_txt.append('The towel is ' + TOWEL + '.')
            if 'bro' in s['props']: prop_txt.append('The brochure is ' + BRO + '.')
            if dinner:
                if wide: prop_txt += [SEATS, aunt(s['bg']), uncle(s['bg']), GUESTS]
                else:
                    if alt: prop_txt.append(ACROSS_SEATS)
                    if 'the aunt' in fr_ and not re.search(r"the aunt[^;]*out of the frame", fr_): prop_txt.append(aunt(s['bg']))
                    if 'the uncle' in fr_: prop_txt.append(uncle(s['bg']))
                    prop_txt.append(PART_VIEW)
                if 'table' in fr_: prop_txt.append(TABLE_FOOD + (' ' + NO_CAKE if s['bg'] == 'A_BDAY' else ''))
            side = s['gifts'] if s['gifts'] is not None else bool(re.search(r'gift|sideboard', fr_) and OFF_SIDEBOARD not in fr_)
            if s['bg'] == 'A_BDAY' and (wide or side): prop_txt.append(GIFTS)
            if s['bg'] == 'A_FRI' and dinner and (wide or side):
                prop_txt.append(FRI_SIDEBOARD if 'aca' in s['props'] else FRI_SIDEBOARD_SOFT)
            # the half-packed kitchen and the Friday hallway are full of boxes even when the frame does not name them (review C1, D)
            if (re.search(r'\bbox(es)?\b', fr_) or s['bg'] in ('B_BOXES', 'A_FRI')) and 'no boxes' not in fr_:
                prop_txt.append("Every moving box is plain brown cardboard, unprinted and unlabeled, with no brand marks.")
            if 'bottle' in s['props']:
                prop_txt.append(f"The granddaughter's own water bottle stands {BOTTLE_AT_SIDE if alt else BOTTLE_AT[s['bg']]}, clear of her hands, and nobody touches it: {BOTTLE}.")
            elif medit and not wide and [c for c in s['chars'] + s['extra'] + s['edge'] if c[0] == 'J']: prop_txt.append(BOTTLE_IF)
            if 'aca' in s['props']:
                n_aca = [i for i, (nm, _) in enumerate(refs) if nm.startswith('IMG_ACA')][0] + 1
                prop_txt.append(' '.join([ACA_LOOK, s['aca_count'] or ACA_FULL, ACA_SHAPE]))
                prop_txt.append(lighting_match(n_aca, number=not s['aca_count'], holder='hold' in s['props']))
                if food_aca(s): prop_txt.append(FOOD_ACA)
            people = bool(s['chars'] or s['hands_of'])
            hands = ("Every hand has five fingers in natural proportion and a natural grip; each person has exactly two arms and two hands; nothing floats."
                     if people else '')
            eyes = ("She looks straight into the lens, as if talking to a friend across the counter." if s['cam'] == 'to'
                    else ("Everyone's eyes stay off-lens; nobody looks into the camera." if s['chars'] else ''))
            final = ''
            if [c for c in s['chars'] + s['extra'] if c != 'B']:
                final = 'Final check: ' + '; '.join(CH[c]['final'] for c in s['chars'] + s['extra'] if c != 'B') + '.'
            # lettering: the banner only where the framing holds it (the photo wall in the straight-on views has none); text on an object stays
            keep_obj = (s['text_on_object'] + " stays; ") if s['text_on_object'] else ''
            if s['end_f']: end_txt = s['end_f']
            elif alt: end_txt = H2_END
            elif s['bg'] == 'A_BDAY' and s['shot'] == 'Wide shot': end_txt = "No subtitles, no captions, no text overlays; " + keep_obj + "the banner lettering in the background stays."
            elif s['bg'] == 'A_BDAY': end_txt = "No subtitles, no captions, no text overlays; " + keep_obj + BANNER_IF
            elif s['text_on_object']: end_txt = "No subtitles, no captions, no text overlays; " + s['text_on_object'] + " stays."
            else: end_txt = "No subtitles, no captions, no on-screen text."
            comp = s['comp'] or ((COMP_TIGHT if s['shot'] in ('Extreme close-up', 'Very tight close-up') else COMP) if s['chars'] else '')
            fprompt = ' '.join(x for x in [
                "Photorealistic vertical 9:16 photo, the first frame of a video shot, " + CAMERA_LOOK,
                ' '.join(img_lines),
                H2_TABLE if alt else '',
                (EDIT_KEEP + ('' if s['shot'] == 'Wide shot' else ' ' + EDIT_ZOOM)) if medit else '',
                f"{s['shot']}. The photo shows {frame_txt}.", comp,
                ' '.join(blocks), ' '.join(prop_txt), face_line(s), hands, eyes,
                ("Look: " + (s['look'] or LOOKS[s['bg']]) + '.') if s['bg'] else '', FRAME_LIGHT.get(s['bg'], ''), (SKIN + ' ' + (SKIN_TONE_FRAME if s['chars'] else SKIN_TONE_HANDS)) if people else '', final, end_txt] if x)
            sfx = '_H2' if alt else ''
            pfx = prompt_node(f'P_F_{s["id"]}{sfx}', 1200 if alt else 400, y, fprompt)
            frx = image_node(f'{SCRIPT}_F_{s["id"]}{sfx}', 1600 if alt else 800, y)
            for nm, _ in refs: link(idx[nm], frx, 'image_ref')
            link(pfx, frx, 'text')
            if not alt: pf, frame, main = pfx, frx, (refs, fprompt)
        refs, fprompt = main  # the rows, QA table and prompt pack describe the main frame, not the straight-on variant
    # ----- video -----
    cam = {'locked': 'Camera: standing on a tripod, locked off, no movement.',
           'push': 'Camera: glides a few centimeters closer over the whole shot, nothing else.',
           'pullback': 'Camera: eases back a few centimeters in the first second, then holds still.',
           'to': 'Camera: standing on the counter at chest height, locked off.'}[s['cam']]
    phys = ["Physics: real weight and balance; nothing moves on its own: whatever moves is moved by a visible hand or by the action.", OBJECT_LOCK + (' ' + s['lock_extra'] if s['lock_extra'] else '')]
    if s['chars']: phys += [HOLD_LOCK, PEOPLE_LOCK]
    if 'aca' in s['props']: phys.append("The wooden pieces keep the scene's light and real shadows; exactly the same number of wooden pieces as in the start frame.")
    if 'water' in s['props']: phys.append("The water itself stays completely clear and colorless the whole time.")
    if food_aca(s): phys.append(FOOD_ACA)
    live_ = s['living'] or (LIVING_PHOTO if s['src'] else LIVING_EMPTY if not (s['chars'] or s['hands_of']) and s['bg'] in MASTER_OF else LIVING.get(s['bg'] or 'B_BOXES', ''))
    living = 'Living layer (only what is already in the frame moves, nothing is added): ' + ('the people breathe and blink naturally; ' if s['chars'] else '') + live_ + '.'
    amb = s['amb'] or AMB.get(s['bg'] or 'B_BOXES')
    if s['kind'] == 'T':
        who = SPK_WHO[spk]
        pr, pos = ('he', 'his') if spk == 'TERRANCE' else ('she', 'her')
        free = s['voice_free'] and spk == 'GLORIA'
        speech = (f"Speech: {who} speaks with clear lip-sync in {VOICE['GLORIA_FREE' if free else spk]}. This is the one voice used for {who} in every clip of this video: "
                  + ("keep exactly this voice, accent, age and pitch; the delivery follows 'This time'. " if free else "keep exactly this voice, accent, age, pitch and pace. ")
                  + f"This time: {s['tone']}. Exactly these words, word for word, nothing added or repeated: \"{txt}\" " + (s['say'] + ' ' if s['say'] else '') +
                  f"{who[0].upper() + who[1:]} starts speaking at about {s['start']} seconds and has finished the whole line by about {end} seconds at the latest; "
                  f"after the last word {pr} keeps the same feeling in {pos} face, lips close and stay closed, no sound. Everyone else stays silent and reacts only with their face and body. "
                  f"Face and body: fully alive and in the moment, like a real person in this family scene; the feeling shows clearly in the eyes, brows, mouth and posture "
                  f"and changes with the meaning of each phrase, each new expression starting a split second before the words that carry it; natural gestures and "
                  f"small movements of the head, shoulders and hands while talking; never frozen, never a fixed smile, never over-acted.")
        audio = f"Audio: only {who}'s voice and quiet room tone of {amb}; no music."
    else:
        speech = "Nobody speaks; mouths stay closed or only show expressions."
        audio = f"Audio: no voice, no speech, no singing, no humming, no music; only quiet natural room sound: {amb}."
    eyes_v = ("She looks straight into the lens, as if talking to a friend across the counter." if s['cam'] == 'to'
              else ("Everyone's eyes stay off-lens; nobody looks into the camera." if s['chars'] else ''))
    end_v = s['end_v'] or ("No subtitles, no captions, no text overlays; " + s['text_on_object'] + " stays and never changes." if s['text_on_object']
             else "No subtitles, no captions, no on-screen text.")
    face_ = s['face_v'] or s['face']
    clip_face = f"Expressions: {face_}." if face_ and (s['kind'] == 'V' or len(s['chars']) > 1) else ''  # speakers also get their tone in Speech
    vprompt = ' '.join(x for x in [
        f"{s['shot']}, {dur} seconds, one continuous shot, no cuts. The image is the start frame; the shot begins exactly on it.",
        cam, ' '.join(phys), f"Action: {s['action']}", living, clip_face, speech, eyes_v, "Real-time pace, nothing slow-motion; the main action starts within the first second.", PICTURE, audio, end_v] if x)
    pv = prompt_node(f'P_V_{s["id"]}', 1200, y, vprompt)
    same_end = s['kind'] == 'T' and s['id'] in HOLD_POSE
    v = video_node(f'{SCRIPT}_{clip}', 1600, y, dur, frame['node_id'], enabled=s['enabled'], same_end=same_end)
    link(frame, v, 'frame_1')
    if same_end: link(frame, v, 'frame_2')
    link(pv, v, 'text')
    t = tai_node(clip, 2000, y, enabled=s['enabled'])
    link(v, t, 'image_ref')  # placeholder, fixed below
    edges[-1].update(target_handle='input_1', target_port='media_in', data_type='video')
    rows.append(dict(id=s['id'], clip=f'{SCRIPT}_{clip}', kind=s['kind'], dur=dur, end=end, spk=spk, txt=txt, src=s['src'], f2=same_end, face=s.get('face', ''),
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
        "Ảnh x4, clip x2. Clip nói chỉ có khung đầu (frame_1): nhân vật diễn và có động tác như phim (Nam 22/10). "
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

json.dump(dict(rows=rows, sheets=[s[0] for s in sheet_specs], bgs=list(BG) + list(BG_EDIT), imgs=IMGS, n_nodes=len(nodes), n_edges=len(edges)),
          open(f'{OUT}/_rows.json', 'w'), ensure_ascii=False, indent=1)

# ---------- prompt pack ----------
with open(f'{OUT}/S14c_Black_prompt_pack.txt', 'w') as f:
    f.write(f"S14c We Talked About This - ban da den - prompt pack TobyFlow ({len(nodes)} node, {len(edges)} edge)\n")
    f.write("Model anh: Nano Banana Pro 9:16 (sheet 16:9). Video: Omni 1.1 Flash, Frames, 720p, tai 1080p.\n\n")
    f.write("=== CHARACTER SHEET + PROP ===\n")
    for name, pr, refs in sheet_specs:
        f.write(f"\n## {name}  (anh dinh: {', '.join(refs) or 'khong'})\n{pr}\n")
    f.write("\n=== ANH NEN ===\n")
    for k in list(BG) + list(BG_EDIT):
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
