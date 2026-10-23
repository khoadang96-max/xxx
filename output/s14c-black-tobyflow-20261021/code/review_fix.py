# Pre-flight review fixes (Nam 23/10: "kiểm tra thật kỹ các lỗi vặt"), applied on top of data14.SH.
# Five independent reviewers read every frame and clip prompt against the script, the chosen images (13.jpg master, 17.jpg photo wall,
# bg5 kitchen) and the 13 failure classes seen so far (review_pk/findings_*.md); each fix below was checked against the prompt text and the
# images. Keys replace whole fields of a shot. New fields read by build14:
#   edge      people only partly in the frame (a shoulder, braids): their sheet as a reference, no description block, no final check
#   plate     another empty-room plate as Image 1 (the kitchen seen from the sink end, 0F)
#   aca_count replaces the "Exactly seven utensils in the full set" sentence when a piece is in a hand or out of the frame
#   sil_ref / bro_ref  the reference line for the silicone / brochure sheet; xrefs: extra (node, line) references
#   living / look / comp / end_f / end_v / face_v / end / say / gifts / voice_free: per-shot overrides of the generated lines
#
# Staging (one sight line per scene, the other person always "just out of the frame"). The kitchen photo looks from the range end along the
# counter: range and crock at screen-right, sink and window in the middle, fridge at screen-left.
#   night (S09-S17): the grandmother on the sink side looks toward screen-right; her son, at the range end, toward screen-left
#   morning (S20-S26): the grandmother at the range looks toward screen-left; the granddaughter, at the sink counter, toward screen-right
#   half-packed kitchen (S36-S70): the grandmother among the boxes near the sink at screen-left looks toward screen-right; the visitor
#   (her friend on Sunday, her son on Thursday) by the stove and the crock at screen-right looks toward screen-left
#   the friend's porch (S31-S35, fixed porch plate BG_D_FIX: the side table at the screen-left end of the swing): the friend sits at the screen-left
#   end next to the table and looks toward screen-right; the grandmother sits at the screen-right end and looks toward screen-left
G_LEFT = ("she stands at screen-left among the moving boxes near the sink, turned toward screen-right, where her {who} stands just out of the frame; "
          "only she is in the picture")
D_RIGHT = ("she stands at screen-right by the stove and the white crock, turned toward screen-left, where her friend stands just out of the frame; "
           "only she is in the picture")
T_RIGHT = ("he stands at screen-right in the aisle by the stove, turned toward screen-left, where his mother stands just out of the frame; "
           "only he is in the picture")
DISH = "the empty clear-glass rectangular baking dish"
PORCH_ONLY = "only the {who} is in the frame"
# people at the edge of a dinner zoom (13.jpg: the aunt's twists are the nearest head on the photo-wall side, the son's shoulder touches the
# granddaughter's, her braids sit just left of him)
AUNT_EDGE = {'A_BDAY': "nearest the camera at the lower screen-left edge, soft and cut by the frame, only the aunt's shoulder and silver-grey twists",
             'A_FRI': "nearest the camera at the lower screen-left edge, soft and cut by the frame, only the aunt's shoulder and silver-grey twists"}
DAD_EDGE = "at the screen-right edge, soft and cut by the frame, only her father's shoulder in his plaid button-down shirt"
JADA_EDGE = "at the screen-left edge, soft and out of focus, only the granddaughter's braids and the shoulder of her green knit sweater"
BOWL_FRI = "the large glass bowl of potato salad stands on the table between the granddaughter and her father, the wooden serving spoon resting in it"
# the brochure is held with its cover toward her (the title is added in CapCut where it shows)
BRO_BACK = "Image {n} shows the brochure: use it only for its size and look; here its cover faces her and its plain back faces the camera."
TEAR = ("it is a thin brochure of only a few pages; both hands grip it near the top, close together at the middle, thumbs side by side on the front cover "
        "just under the title, ready to tear it straight down the middle; the whole title \"WRENFIELD · SENIOR LIVING\" is readable above his thumbs")
TEAR_LOCK = ("The brochure is the only thing that changes: it tears once, straight down from the top edge between his thumbs, into two halves; "
             "the hands keep exactly five fingers each; nothing else changes.")
TEAR_END = "No subtitles, no captions, no text overlays; each half of the brochure keeps its part of the cover lettering, clean and unchanged."
HALL_LOOK = "warm evening light from the hallway ceiling light, soft shadows, warm family-film color"
NEW_SOAP = ("on the counter right beside the white crock stand a new, full bottle of green dish soap with a plain white label without any lettering and a "
            "new yellow sponge still in a plain clear wrapper with no print; the old soap bottle and sponge by the faucet stay as in Image 1")
SIL_ONE = "Image {n} shows the teal silicone utensils: use it only for the {what}'s shape and teal color; do not add any other piece from it."
ONE = "Only one utensil of the set is in the picture: the {piece} in {pos} hand; the rest of the set is out of the frame; no other wooden utensils anywhere."
EYES_ONLY = "Composition: the eyes sit across the middle of the frame; the top third shows only the forehead and soft background."
VOICE_FREE = {'S07', 'S11', 'S14', 'S17', 'S24', 'S34', 'S40', 'S79'}

FIX = {
 # ---------- A: the birthday dinner (master edits of 13.jpg; _H2 straight-on variants in FIX_H2) ----------
 'A-1': dict(frame=("the same dinner from the same camera, zoomed in on the granddaughter and her father on the side with the framed family photos: the "
                    "granddaughter leans toward her father in the next chair, nearer the head of the table, and raises the hand nearer her father beside the "
                    "far side of her mouth, away from the camera, as if to whisper, her fingers clear of her lips and her whole mouth in view; her father, "
                    "partly in frame and soft, turns his head toward her; beyond them, soft in the background, the grandmother still stands at the head of the "
                    "table beside her own chair, holding the potato salad bowl with the teal serving spoon in it; " + AUNT_EDGE['A_BDAY']),
             action=("She whispers toward her father, her raised hand beside the far side of her mouth, away from the camera, her fingers clear of her lips; her "
                     "lips stay in full view for the whole line, loud enough for the whole table to hear. Halfway through, the focus shifts gently to the "
                     "grandmother at the head of the table, who holds the bowl and hears every word; her smile fades."),
             props=['dish', 'bottle'],
             face_v=("the granddaughter embarrassed and uneasy, wincing a little as she whispers, not mean; her father tense; the grandmother in the background "
                     "smiling at first, her smile fading as she hears the words")),
 'B-1': dict(frame=("the same dining room from the same camera, zoomed in on the head end of the room: the grandmother is not in the room yet and her own chair "
                    "at the head of the table stands empty; the son has left his chair and stands at the end of the sideboard nearest the head of the table, by "
                    "the gold gift bag with pink tissue paper, in profile: one hand holds the brochure tilted up toward the camera just above the "
                    "sideboard, about to slide it under that gold gift bag, its cover and title readable in clean print, and his other hand tips the gold bag up "
                    "a little at its base; his daughter has followed him and stands a step behind him at screen-left of him, nearer the table, her face fully "
                    "clear of his shoulder, turned three-quarters toward the camera, her lips in view, stunned, looking at what he is doing; the son's wife sits "
                    "in her chair at the lower right edge of the frame, out of focus, looking at the table"),
             action=("In the first second he lays the brochure flat and slides it under the tipped gold gift bag, then sets the bag down on it; he turns his "
                     "head toward his daughter; the camera eases back a few centimeters as she speaks, her lips in view the whole time.")),
 'S02_B': dict(frame=("the same dining room from the same camera, zoomed in close on the son standing at the end of the sideboard nearest the head of the "
                      "table, the gift bags beside him: he turns his head toward his daughter, who stands at screen-left of him, a step nearer the table; his "
                      "face in three-quarter view to the camera, his mouth in view; the son's wife sits in her chair at the lower right edge of the frame, out "
                      "of focus, looking at the table; the grandmother is not in the room yet")),
 'C-1': dict(action=("He lifts his glass a little higher toward his mother, off-frame at the head of the table, as he starts the toast, his free hand pressed "
                     "to his chest for a moment; on 'still cooking' a proud grin breaks across his face and he tips the glass toward her. The aunt, on the "
                     "other side of his daughter from him, lifts her glass a little higher; his daughter keeps chewing.")),
 'C-2': dict(frame=("the same dinner from the same camera, zoomed in close on the granddaughter in her chair: mid-chew, fork just lowered, eyes starting to "
                    "water; her standing father's arm in its navy quarter-zip sleeve, his deep-brown hand with a gold wedding band holding his drinking glass, "
                    "soft at the screen-right edge of the frame; the aunt, in the next chair nearer the camera, is just out of the frame at screen-left"),
             hands_of='T1', props=['bottle'], start=1.0),
 'E-2': dict(frame=("the same dinner from the same camera, zoomed in close on the granddaughter in her chair, from her head down to the table edge: she looks "
                    "down at a slim modern handset with a black glass touchscreen, the size of her palm, held low in front of her with its screen tilted away "
                    "from the camera, her plate of food on the table in front of her, barely touched; her father, in the next chair at screen-right, and the "
                    "aunt, in the next chair at screen-left, are both just out of the frame"),
             action=("She looks up from the handset, pushes her plate a few centimeters toward the middle of the table, clear of her tumbler, in the first "
                     "second, turns her head toward her father, just out of the frame at screen-right, and says it out loud to him."),
             props=['bottle'], start=1.0),
 # S01: the grandmother has come around to the corner beside her son's chair, so the granddaughter speaks toward screen-right with her face in
 # view (behind her chair she would turn away from the camera); S03 picks her up there, mid-step
 'S01': dict(frame=("the same dinner from the same camera, zoomed in on the granddaughter and her father: the granddaughter has just pushed her plate away "
                    "and grimaces, mouth open to speak, her face turned up toward her grandmother at screen-right, in three-quarter view to the camera; her "
                    "father beside her, nearer the head of the table, soft; the grandmother has come around the head of the table and stands at the corner of "
                    "the table beside her son's chair, the potato salad bowl in one arm and the teal silicone serving spoon in her other hand, just done "
                    "serving her son; " + AUNT_EDGE['A_BDAY']),
             action=("The granddaughter looks up at her grandmother at screen-right and says the line to her, her face in three-quarter view and her lips in "
                     "view the whole time; her grandmother stops beside her son's chair with the bowl and her proud smile freezes, and as it freezes she lowers "
                     "the teal serving spoon back into the bowl; her father closes his eyes for a moment."),
             face_v=("the granddaughter's face an apologetic, pained grimace, honest, never disgusted or mocking; her father already tense, bracing himself; "
                     "the grandmother smiling proudly at first, her smile freezing as the words land")),
 'S02': dict(frame=("the same dinner from the same camera, zoomed in close on the son in his chair: he turns his head toward his daughter beside him at "
                    "screen-left, jaw tight; behind him, soft, the archway; his mother stands just out of the frame at screen-right, beside his chair; the "
                    "sideboard is out of the frame at screen-right")),
 'S02_C': dict(frame=("the same dinner from the same camera, zoomed in close on the son, still standing at his chair, his drinking glass still raised at "
                      "shoulder height, off to the side and clear of his face, his mouth in full view, turning his head toward his daughter beside him at "
                      "screen-left; behind him, soft, the archway; his mother is just out of the frame at screen-right, at the head of the table; the "
                      "sideboard is out of the frame at screen-right"),
               action=("Still holding his glass at shoulder height, clear of his face, he speaks to his daughter through his teeth; on the last word his eyes "
                       "flick toward the gift bags on the sideboard at the head of the room.")),
 # S03 shows only her (script CU); her son is out of the frame, so it cuts after S02, S02_C (son standing) and S02 of every hook
 'S03': dict(frame=("the same dinner from the same camera, zoomed in close on the grandmother at the head of the table, the frame tight on her from her "
                    "head to her waist: mid-step at the head end of the table, she holds the potato salad bowl with the teal serving spoon resting in it, still "
                    "smiling, her eyes turning toward the sideboard at screen-right; behind her, soft, the carved wooden fork and spoon; her son is just out of "
                    "the frame at screen-left")),
 'S03_B': dict(frame=("the same dining room from the same camera, zoomed in on the archway, the frame tight on the grandmother from her head to her waist, "
                      "so the table and the chairs are below the frame: she stands in the archway, just coming in from the hallway with the potato salad bowl "
                      "in her hands, the teal serving spoon in it, still smiling, looking across the room toward the sideboard, out of the frame at "
                      "screen-right, where her son stands; behind her, soft, the dim hallway; nobody else is in the frame"),
               action=("Her eyes follow her son, out of the frame at screen-right, as he walks back from the sideboard toward the table; he never enters the "
                       "frame and nobody moves into it; her smile fades as she asks."),
               props=['dish', 'sil'], sil_ref=SIL_ONE.format(n='{n}', what='serving spoon'), gifts=False),
 'S04': dict(frame=("the same dining room from the same camera, an extreme close-up of the sideboard at the head end of the room: under the gold gift bag "
                    "with pink tissue paper, the top part of a glossy brochure sticks out toward the camera; its cover photo of smiling seniors at a communal "
                    "dining table is clearly visible, and a plain pale band along its top edge is left empty for the title added later; no letters anywhere "
                    "in the frame; the other gift bags soft beside it; no people in the frame"),
             action="Nothing moves.", cam='locked',
             bro_ref="Image {n} shows the brochure: use it only for its size and its cover photo, never its title.",
             living="nothing in the frame moves; no person and no hand appears",
             end_f="No subtitles, no captions, no lettering anywhere in the frame.", end_v="No subtitles, no captions, no lettering anywhere in the frame."),
 'S05': dict(frame=("the same dinner from the same camera, zoomed in on the head end of the room: the grandmother has walked to the end of the sideboard "
                    "nearest her own chair, near the gold gift bag, and stands there between her empty chair and the son's wife, in full view from head to "
                    "waist, nobody in front of her, turned toward the table, holding the brochure in both hands and looking at its cover; the potato salad "
                    "bowl, the teal serving spoon in it, now sits on the sideboard beside the gift bags, the gold gift bag pushed aside; her own chair at the "
                    "head of the table stands empty; in the mid-ground, soft, her son and the granddaughter sit frozen in their chairs at screen-left and the "
                    "son's wife at screen-right, all turned toward her; nearest the camera, soft and cut by the frame: at the lower-left corner the aunt's "
                    "shoulder and silver-grey twists; at the lower-right corner the uncle's bald head and grey sport coat shoulder; between the son's wife "
                    "and the uncle only the boy's small hand and striped sleeve show, his face hidden behind the uncle; no child's face in the frame"),
             bro_ref=BRO_BACK, start=1.0),
 'S06': dict(frame=("the same dinner from the same camera, zoomed in on the son: he rises halfway from his chair, turned toward the head of the room, one "
                    "open hand reaching out toward his mother, who stands just out of the frame at the sideboard at screen-right; her own chair at the head "
                    "of the table, at the screen-right edge, stands empty; the granddaughter beside him at screen-left, soft; " + AUNT_EDGE['A_BDAY'] +
                    "; no brochure in this frame"),
             gifts=False),
 'S07': dict(frame=("the same dinner from the same camera, zoomed in close on the grandmother standing at the end of the sideboard nearest her own chair: "
                    "her eyes red and wet, the brochure held at chest height in trembling hands, its cover toward her and its plain back toward the camera; "
                    "the son's wife sits in her chair at the lower right edge of the frame, out of focus, turned toward her; on the sideboard beside the "
                    "grandmother, soft, the potato salad bowl with the teal serving spoon in it next to the gift bags"),
             bro_ref=BRO_BACK, tone="hurt and betrayed; one small crack on 'BIRTHDAY', the only break in her steady voice"),
 'S08': dict(frame=("the same dinner from the same camera, with the same framing as Image 1: the whole birthday table frozen. Along the side wall with the "
                    "family photos her son stares at his plate, the granddaughter covers her mouth with her hand and the aunt looks down; on the other side "
                    "the son's wife stares down at her plate and the uncle looks down, and between them only the boy's small hand and striped sleeve show, "
                    "the rest of him hidden behind the uncle. Her own chair at the head of the table stands empty; at the end of the sideboard nearest her "
                    "empty chair, between that chair and the son's wife, the grandmother stands alone holding the brochure, soft, in full view from head to "
                    "waist, the potato salad bowl with the teal serving spoon in it beside the gift bags, the gold 71 balloons and the banner above her; "
                    "nobody at the table looks at her"),
             bro_ref=BRO_BACK),

 # ---------- B: the night kitchen, the porch, the next morning (S09-S26) ----------
 # S09 opens on the LATER THAT NIGHT card: the plate's own framing holds the trash can and the crock wherever they stand, so nothing is moved or doubled
 'S09': dict(shot='Wide shot',
             frame=("at night in her kitchen, with the same camera and framing as Image 1: the grandmother stands at the white step trash can, exactly where "
                    "it stands in Image 1, her foot on its pedal holding the lid open, a plate and fork in her hands, her face turned enough toward the camera "
                    "that her lips are in view; the white ceramic crock of teal silicone utensils stands on the counter beside the old white gas range, where "
                    "it stands in Image 1; there is only one trash can and one crock in the kitchen; her son is just out of the frame at screen-right"),
             action=("She scrapes the plate hard into the trash can with the fork, twice, her foot staying on the pedal the whole time so the lid stays open, "
                     "then says it with her eyes still on the plate, her head lifted just enough that her lips stay in view.")),
 'S10': dict(plate='BG_B_NIGHT_REV',
             frame=("her son leaning in the open kitchen doorway at the far end of the kitchen, beside the old white gas range, with his arms crossed, tired, "
                    "looking off screen-left toward his mother, who is just out of the frame; nobody else is in the frame"),
             action=("He pushes off the door frame and uncrosses his arms in the first second, taking one step into the kitchen toward his mother, just out "
                     "of the frame at screen-left; he opens one hand toward her on 'every dinner since Christmas' and rubs the back of his neck on 'we've all "
                     "noticed', tired, loving but helpless; after the line his hand drops and he holds her gaze."),
             start=1.0),
 'S11': dict(frame=("the grandmother at night, holding the scraped plate still, the fork resting on it, her face turning toward screen-right, where her son "
                    "stands just out of the frame"),
             action="She stops, the plate still in her hand, and asks quietly, looking at her son just out of the frame at screen-right.",
             tone='quiet, small and wounded'),
 'S12': dict(plate='BG_B_NIGHT_REV',
             frame=("an over-the-shoulder shot: the grandmother's silver hair and cream cardigan shoulder soft in the foreground at the screen-left edge; her "
                    "son stands beyond her, a step in from the kitchen doorway by the old white gas range, facing her and looking screen-left at her")),
 'S13': dict(frame=("her son in the night kitchen, a step from the old white gas range, which stands at the screen-right edge of the frame, the white crock "
                    "of teal utensils on the counter behind him; he looks off screen-left toward his mother, who is just out of the frame"),
             action=("He steps over to the old gas range in the first second and rests his fingertips on the counter beside it; on 'smell gas' he glances "
                     "down at the burners, then looks back up at his mother, just out of the frame at screen-left, his brow knotted with worry; the burners "
                     "stay off and unlit; after the line he waits for her answer."),
             start=1.0),
 'S14': dict(frame=("the grandmother at night, chin trembling, lowering the plate, the fork resting on it, toward the counter, her eyes on her son, who is "
                    "just out of the frame at screen-right"),
             tone="proud, her voice catching and shaking on 'forty-two years', holding back tears", start=1.0),
 'S15': dict(frame=("her son in the night kitchen, his eyes red; he looks off screen-left toward his mother, who is just out of the frame; the wall receiver "
                    "and the church fan soft behind him"),
             action=("He nods once on 'I know', then leans a little closer to his mother, just out of the frame at screen-left, and says the rest quietly, "
                     "his wet eyes steady on her and his jaw working to hold it together; after the line he presses his lips together and looks down for a "
                     "moment.")),
 'S16': dict(frame=("her son at the kitchen counter at night, beside the white crock, one hand flat on the brochure lying on the counter; exactly one "
                    "brochure, lying face up, its cover lettering exactly \"WRENFIELD · SENIOR LIVING\" as on the brochure sheet, partly under his hand, and no "
                    "other text; his mother is just out of the frame at screen-left"),
             action=("He slides the brochure a short way along the counter toward screen-left, toward his mother, in the first second, lets go, and says "
                     "it."),
             text_on_object='the brochure cover lettering "WRENFIELD · SENIOR LIVING"'),
 'S17': dict(frame=("an extreme close-up of the grandmother's face at night from her brows to her chin, her eyes and her mouth both in the frame, her eyes "
                    "looking off screen-right toward her son, who is just out of the frame, tears welling"),
             tone='barely above a whisper, breathy with disbelief'),
 'S18': dict(frame=("seen from inside the house through a screen door (the mesh soft in the foreground): her son stands at the far end of the front porch "
                    "at screen-right, under the yellow porch light, turned toward the street, a small black mobile handset to his ear, its screen off; the "
                    "mesh and the distance keep his face hidden"),
             action=("He stays turned toward the street, shifts his weight and lowers his head, the handset at his ear; his face stays hidden the whole "
                     "time.")),
 'S19': dict(frame=("the grandmother just inside the screen door at night, the yellow porch light on her face through the mesh, her eyes toward "
                    "screen-left, where her son stands out of the frame at the end of the porch"),
             look="night: the yellow porch light falls through the mesh on her face; behind her the front hallway is dim"),
 'S20': dict(frame=("next morning in slanted sun, the grandmother stands at the screen-left front corner of the range, beside the white crock of teal "
                    "utensils, turned toward the cast-iron skillet that sits on the back burner as in Image 1, her face in three-quarter view; she stirs "
                    "scrambled eggs in that skillet with a teal silicone spatula, her other hand on the skillet handle, a low blue flame on the lit burner under it; nothing "
                    "stands between the range and the wall; " + NEW_SOAP)),
 'S21': dict(frame=("the granddaughter in her grey hoodie in the morning kitchen, standing at the counter in front of the sink, a step to the screen-left "
                    "of the range, turned toward screen-right; car keys on a plain black fob with no logo in one hand; in the other hand a fork with a bite "
                    "of scrambled eggs from the skillet, held just below her lips, the tines clear of her mouth and her lips in view; her grandmother is just "
                    "out of the frame at screen-right, at the range; nobody else is in the frame"),
             action=("In the first second she takes the bite and lowers the fork to chest height; she chews once and swallows, winces apologetically, then "
                     "says it to her grandmother just out of the frame at screen-right, her lips clear and in view; the fork stays below her chin while she "
                     "speaks."),
             start=1.4),
 'S22': dict(shot='Medium close-up',
             frame=("the grandmother framed from the waist up, the counter edge along the bottom of the frame, in the morning kitchen at the counter beside "
                    "the white crock, pointing down at the new green dish soap bottle that stands on the counter in front of her at the bottom of the frame, "
                    "the teal silicone spatula in her other hand; she looks off screen-left toward her granddaughter, who is just out of the frame; "
                    + NEW_SOAP),
             action=("She jabs her finger toward the new green dish soap bottle on 'THREE times', then taps the counter beside it on 'new soap, new sponge', "
                     "frustrated and insistent, looking at her granddaughter just out of the frame at screen-left; the teal spatula in her other hand moves "
                     "only with that hand; after the line she throws up her free hand a little and shakes her head.")),
 'S23': dict(frame=("the grandmother in the morning kitchen holding a fork with a bite of the same scrambled eggs just below her lips, the tines clear of "
                    "her mouth and her lips in view; she has put the teal spatula down, her other hand empty; her eyes toward screen-left, where her "
                    "granddaughter stands just out of the frame"),
             action=("In the first second she takes the bite and lowers the fork to chest height; she chews twice, taking her time, finds nothing wrong, "
                     "swallows and says it, puzzled; the fork stays low, away from her lips."),
             start=1.6),
 'S24': dict(frame=("an extreme close-up of the grandmother's face from her brows to her chin in the morning light, her eyes looking off screen-left toward "
                    "her granddaughter, who is just out of the frame; nobody else is in the frame"),
             action=("Her eyes fill as she asks it in a small, frightened voice; her brows lift and draw together and her lips tremble on 'losing it'; for a "
                     "moment her gaze drops away from her granddaughter, then comes back up, searching the face of her granddaughter, just out of the frame "
                     "at screen-left."),
             tone="small and frightened, her voice thin and trembling on 'losing it'"),
 'S25': dict(frame=("the granddaughter at screen-left in three-quarter profile facing screen-right, toward her grandmother at screen-right, who faces her in "
                    "the morning kitchen; the granddaughter's lips parted as if about to answer, her car keys in her hand at her side; nobody holds a fork or "
                    "a spatula"),
             action=("In the first second she stops herself and steps in to hug her grandmother tight, both arms around her grandmother's shoulders, the "
                     "grandmother's hands on her back; exactly four arms between them; their faces stay separate, cheek beside cheek; they hold the hug.")),
 'S26': dict(frame=("over the granddaughter's shoulder at the screen-left edge (her braids and grey hood soft in the foreground): the grandmother's face at "
                    "screen-right of centre inside the hug, staring into the distance; the granddaughter's arms around her grandmother's shoulders, the "
                    "grandmother's hands on her back; exactly four arms between them; their faces stay separate, cheek beside cheek")),

 # ---------- C1: half-packed kitchen, the friend's porch (S27-S48) ----------
 'S27': dict(frame=("a few days later, the grandmother at the counter wrapping a white ceramic mixing bowl in plain newsprint whose small print is soft and unreadable, "
                    "with no headlines and no photos; the open moving box stands on the counter in the lower foreground, one plain unmarked side facing the camera "
                    "squarely, nothing in front of it and no newspaper over that side; she stands just beyond it, her face in three-quarter view; flattened boxes and "
                    "tape on the counter"),
             action="She lowers the wrapped bowl into the box in the first second and lets go; the box itself does not move.",
             amb='the soft rustle of newspaper'),
 'S28': dict(frame=("Sunday afternoon, seen from the sidewalk: the friend's daughter in her car, parked nose-in at the house end of the short driveway at screen-left, "
                    "waving through the window, a foil-covered plate on the passenger seat; the friend waves from her porch; the grandmother stands on the sidewalk at "
                    f"screen-right, a few steps clear of the driveway, holding {DISH} in both hands; only these three women are in the picture; nobody else on the "
                    "street, the sidewalk or in the yards; no other moving cars"),
             bg_ref=("Image {n} is the friend's front porch: this is the same house seen from the sidewalk: keep the porch, the white swing, the hanging ferns and the "
                     "side table exactly as in Image {n}, now in the background, with the short driveway at screen-left and the sidewalk and a quiet street in the foreground."),
             action=("The daughter backs the car out of the driveway at walking pace, well clear of the grandmother, and drives off out of the frame at screen-left; "
                     "the friend and her daughter keep waving; the grandmother only watches, the glass dish in both hands."),
             lock_extra="The car is the only exception: it drives out of the frame."),
 'S29': dict(frame=(f"the grandmother on the porch steps, holding {DISH} in both hands, her body turned three-quarters toward the camera and her face in three-quarter "
                    "view as she glances down the street toward screen-left, her mouth clearly visible; the car is already out of sight; her friend is up on the "
                    "porch just out of the frame; nobody else is in the frame"),
             action="She climbs the last step and says it, glancing down the street, her face staying turned three-quarters toward the camera."),
 'S30': dict(frame=("the friend on her porch, one hand raised waving down the street, her raised hand beside her shoulder, clear of her face, her lips in view, smiling; "
                    "her friend is on the porch steps just out of the frame; " + PORCH_ONLY.format(who='friend')),
             action=("She gives one last wave down the street, lowers her hand and turns her head back to her friend, just out of the frame, in the first second, then "
                     "says it with a dry, knowing smile and a lift of her eyebrows; after the line her smile widens a little; her church hat stays in place."),
             start=1.2),
 'S31': dict(frame=("the two women seated side by side on the white porch swing: the friend at the screen-left end next to the small side table with her coffee "
                    f"mug on it, her canvas tote bag on the swing beside her; the grandmother at the screen-right end with {DISH} on her lap"),
             action=("The grandmother, the woman without a hat, in the lavender cardigan with the glass dish on her lap, turns to her friend in the moss-green church "
                     "hat and asks; only the grandmother's lips move; the friend's lips stay closed.")),
 'S32': dict(frame=("the friend on the porch swing at the end next to the small side table, her coffee mug held in one hand at chest height, just lowered from a sip, "
                    "the mug well below her chin and her lips fully in view, her canvas tote bag on the swing beside her, her eyes on her friend, who sits at the other "
                    "end of the swing, just out of the frame at screen-right; " + PORCH_ONLY.format(who='friend')),
             action="She lowers the mug to her lap in the first second and says it like it's nothing, the mug staying below her chin."),
 'S33': dict(frame=(f"the grandmother on the porch swing, framed from her face down to her lap, both hands resting on {DISH} on her lap, the dish and her hands in "
                    "the frame, her eyes on her friend, who sits at the other end of the swing, just out of the frame at screen-left; " + PORCH_ONLY.format(who='grandmother')),
             action=("She freezes, staring at her friend; her hands go slack on the dish, it slides a few centimeters toward her knees, and she catches it with both hands.")),
 'S34': dict(frame=("the grandmother on the porch swing, looking toward screen-left at her friend, who sits at the other end of the swing just out of the frame; "
                    f"{DISH} still on her lap, below the frame; " + PORCH_ONLY.format(who='grandmother')),
             start=2.0),
 'S35': dict(frame=("the friend rising from her end of the swing next to the small side table, the canvas tote bag already on her shoulder, the coffee mug set down on "
                    "the side table, looking down toward screen-right at her friend, who is still seated at the other end of the swing just out of the frame; the frame shows only the "
                    "friend's end of the swing; nobody else is in the frame"),
             start=2.0),
 'S36': dict(frame=("the half-packed kitchen cluttered with moving boxes: the friend, in her moss-green dress, stands at screen-right by the stove holding a teal "
                    "silicone spatula by its handle, just pulled from the white crock, and looks at it; the white crock with the rest of the teal utensils stands on "
                    "the counter beside her, in the frame; her friend, the grandmother, stands just out of the frame at screen-left; only the friend is in the frame"),
             action="She turns her eyes from the spatula to her friend, just out of the frame at screen-left, and asks.",
             sil_ref="Image {n} shows the teal silicone utensils: use it only for the shape and teal color of the spatula and the utensils in the crock; no muffin pan and no second crock."),
 'S37': dict(frame=("the grandmother with a roll of packing tape in her hand; " + G_LEFT.format(who='friend')), start=1.0),
 'S38': dict(frame=("the friend at screen-right in the kitchen, looking straight toward screen-left at her friend, who stands just out of the frame, one eyebrow "
                    "raised; the teal spatula from the crock still in her hand, held low at her waist; only the friend is in the frame"),
             action=("She keeps her eyes on her friend just out of the frame and asks it quietly, her eyebrow still raised, patient and knowing; after the line she "
                     "simply waits, the spatula still at her waist; her church hat stays in place."),
             props=['sil'], sil_ref=SIL_ONE.format(n='{n}', what='spatula')),
 'S39': dict(frame=("an extreme close-up of the grandmother's eyes, looking off toward screen-left, away from her friend and away from the lens; her reading glasses "
                    "hang on their chain at her chest, below the frame; no glasses on her face"),
             comp=EYES_ONLY),
 'S40': dict(frame="the grandmother's face as something dawns on her; " + G_LEFT.format(who='friend'),
             tone='realization, quiet, unhurried, with a small catch of breath before the word', end=2.0),
 'S41': dict(frame=("the friend at screen-right holding the teal silicone spatula by its handle, her fingers wrapped around the handle, its head up close to the nose "
                    "of the grandmother at screen-left; the two women face each other in three-quarter view"),
             action=("She holds the teal spatula steady under her friend's nose and says it, firm and simple; only the woman in the moss-green church hat speaks; "
                     "the grandmother, without a hat, keeps her lips closed; she hesitates, glances from the spatula to her friend and back, and leans in a few "
                     "centimeters toward it, wary."),
             sil_ref=SIL_ONE.format(n='{n}', what='spatula')),
 'S42': dict(frame=("an extreme close-up of the grandmother, the teal silicone spatula head held a hand's width in front of her face at nose height, a little to the "
                    "screen-right side of her nose, her mouth and lips fully in view, nothing in front of them; the spatula's handle runs out of the frame at the "
                    "screen-right edge; no hand in the frame; her reading glasses hang on their chain at her chest, below the frame; no glasses on her face"),
             hands_of=None, tone='shocked, disbelieving, the truth landing', sil_ref=SIL_ONE.format(n='{n}', what='spatula')),
 'S43': dict(frame=("the friend from the brim of her hat down to her chest, holding the teal silicone spatula by its handle low at chest height, only its head and "
                    "the top of her hand at the bottom edge of the frame; " + D_RIGHT),
             action=("She lifts the teal spatula a little between them and looks from it to her friend, just out of the frame, as she says it, calm, like someone who "
                     "has been through it, with a small nod on 'whatever soap you use'; the spatula moves only with her hand; her church hat stays in place."),
             sil_ref=SIL_ONE.format(n='{n}', what='spatula')),
 'S44': dict(frame=("an insert close-up from about 40 cm, looking down at a slight angle: a large mixing bowl of warm, just-boiled potatoes and chopped egg with "
                    "mayonnaise fills most of the frame, a teal silicone spatula resting in it, a faint wisp of steam; the bowl stands on the counter beside the "
                    "stove, away from the sink; behind it only a soft, out-of-focus strip of the same counter and the corner of a plain brown box from Image 1; "
                    "no dish-soap bottle and no sponge in the frame"),
             sil_ref=SIL_ONE.format(n='{n}', what='spatula')),
 'S45': dict(frame="the grandmother, troubled; " + G_LEFT.format(who='friend'),
             action=("She shakes her head as she says it, troubled, and spreads one hand a little, palm up, still defending herself, her eyes searching the face of "
                     "her friend, just out of the frame at screen-right; after the line her hand drops and she looks down.")),
 'S46': dict(frame="the friend with a sad, knowing smile; " + D_RIGHT,
             action=("She gives a small shrug and a sad, knowing smile on 'neither could I', then tips her head toward her friend, just out of the frame, and says "
                     "the rest gently, her eyes kind; after the line she gives one small nod; her church hat stays in place.")),
 'S47': dict(frame=("the friend standing beside an open upper cabinet at screen-right, already turned away from it toward screen-left, where her friend stands just "
                    "out of the frame, her face in three-quarter view and fully visible, holding a teal silicone muffin pan in both hands at chest height; the "
                    "spatula is no longer in her hands; inside the open cabinet only plain white bowls and plates, no packages, no labels"),
             action=("She lifts her eyes from the pan to her friend just out of the frame in the first second, holding the teal silicone muffin pan out a little in "
                     "both hands, and says it serious and plain, not preachy, lifting the pan a few centimeters on 'baking pans' and lowering it on 'chemicals "
                     "leached out'."),
             sil_ref="Image {n} shows the teal silicone set, including the muffin pan: use it only for the muffin pan's shape and teal color.", start=1.0),
 # the line is the friend's, off screen (V clip): the grandmother stares at the pan her friend has set down; no hands (old hands holding things get blocked)
 'S48': dict(frame=("the grandmother at screen-left staring down toward screen-right at the teal silicone muffin pan that her friend has just set on the counter at "
                    "the bottom edge of the frame; no hands in the picture; her friend is just out of the frame"),
             hands_of=None, props=['sil'],
             sil_ref="Image {n} shows the teal silicone set, including the muffin pan: use it only for the muffin pan's shape and teal color.",
             action="She keeps staring at the pan; her eyes widen a little, her lips part, she swallows; her skin tone stays exactly as in the start frame."),
 # ---------- C2: the wooden set, the son's visit (S49-S70) ----------
 'S49': dict(amb='a quiet daytime kitchen',
             action=("The seven wooden utensils lie still on the red-and-white checkered towel; only the daylight shifts a little across them. No hand, arm or person "
                     "enters the frame.")),
 'S50': dict(frame=("the friend at the counter, one hand resting on a corner of the red-and-white checkered towel; the seven wooden utensils lie in a row on the "
                    "towel; " + D_RIGHT),
             xrefs=[('IMG_ACA_TOWEL', "Image {n} is the real photo of the same seven utensils on the same towel: copy the towel's check size, red and white "
                                      "colors and hem, and the order of the utensils in the row from Image {n}; ignore its lighting, background and camera angle.")]),
 'S51': dict(frame=("the grandmother holding one wooden spoon at chest height, a little to one side, looking down at it and frowning, her mouth clear and in view; "
                    + G_LEFT.format(who='friend')),
             action=("She tilts the wooden spoon toward the light on 'Wood?' with a skeptical frown, keeping it at chest height and to one side, never in front of "
                     "her mouth, then looks up at her friend, just out of the frame at screen-right, to say the rest, one eyebrow raised, like a cook who has seen "
                     "it all; the spoon moves only with her hand and keeps its exact shape."),
             aca_count=ONE.format(piece='wooden spoon', pos='her')),
 'S52': dict(frame="the friend in the kitchen, shaking her head a little; " + D_RIGHT),
 'S53': dict(action="Nothing in the picture moves; the camera glides a few centimeters closer along the grain over the whole shot."),
 'S54': dict(frame=("the friend holding her own small handset at chest height, its screen turned toward her and away from the camera, her thumb on the screen; the "
                    "back of the handset is plain black with no logo, marks or lettering; her mouth is clear and in view; a second small handset lies face up on "
                    "the counter in front of her, its screen off; the towel with the wooden utensils is out of the frame; " + D_RIGHT),
             start=1.0, say="She says Acawood as AH-kah-wood."),
 'S56': dict(frame=("the friend at the counter, one hand on a rolled-up red-and-white checkered towel; all seven wooden utensils are rolled up inside the towel, only "
                    "their handle ends showing at one end; no utensils lie loose on the counter; " + D_RIGHT),
             action=("She slides the rolled towel a short way across the counter toward screen-left, toward her friend just out of the frame, in the first second, "
                     "lets go and says it; no other hand enters the frame."),
             xrefs=[('IMG_ACA_TOWEL', "Image {n} shows the same towel: copy only its check size, colors and hem.")]),
 'S57': dict(frame=("her son in a grey fleece vest standing in the aisle in front of the counter, a stack of flattened moving boxes in one arm, a roll of clear "
                    "packing tape in his other hand; " + T_RIGHT)),
 'S58': dict(frame=("the grandmother holding the teal silicone spatula out at chest height toward her son, who is just out of the frame at screen-right; no other "
                    "person, hand or arm reaches into the frame; " + G_LEFT.format(who='son')),
             action=("She leans toward her son, just out of the frame at screen-right, in the first second and holds the teal spatula out to him, head up, and says "
                     "it calm and firm; after the line she keeps it held out, eyebrows raised, waiting."),
             sil_ref=SIL_ONE.format(n='{n}', what='spatula'), start=1.0),
 'S59': dict(frame="her son in the kitchen, exhaling, worn out; " + T_RIGHT),
 'S60': dict(frame="the grandmother in the kitchen, face set; her hand holding the teal spatula out toward him is below the frame; " + G_LEFT.format(who='son'),
             action=("She leans a little toward her son, just out of the frame at screen-right, in the first second, her face staying in the middle of the frame, "
                     "and says it, her voice hardening, her chin lifting on 'Terrance', her eyes never leaving his; she does not back down."),
             start=1.0),
 # S61: he holds it himself (an old hand holding a utensil in a close-up gets blocked, and S62 has it in his hand); his mother is out of the frame
 'S61': dict(frame=("an extreme close-up of her son holding the teal silicone spatula head just below his nose in his own hand (deep brown skin, a gold wedding "
                    "band, the cuff of his button-down shirt); his mother is just out of the frame at screen-left; nobody else is in the picture"),
             hands_of=None, sil_ref=SIL_ONE.format(n='{n}', what='spatula')),
 'S62': dict(frame=("her son holding the teal silicone spatula at chest height in his own hand, staring down at it, his mouth clear and in view; " + T_RIGHT),
             action=("He stares down at the teal spatula at chest height as if seeing it for the first time, then says it, stunned and quiet, his eyes lifting "
                     "toward screen-left to his mother, just out of the frame, on 'dish soap'; the spatula stays below his chin and moves only with his hand."),
             start=2.0, sil_ref=SIL_ONE.format(n='{n}', what='spatula')),
 'S63': dict(frame=("the grandmother holding out one wooden ladle at chest height toward her son, who is just out of the frame at screen-right; no other person, "
                    "hand or arm reaches into the frame; " + G_LEFT.format(who='son')),
             aca_count=ONE.format(piece='wooden ladle', pos='her')),
 'S64': dict(frame=("her son holding the wooden ladle in his own hand, its bowl up by his nose and tilted to one side so his mouth stays clear and in view; "
                    + T_RIGHT),
             action=("He sniffs the wooden ladle once in the first second, frowns, lowers it to chest height so his mouth is fully clear, shakes his head once and "
                     "says it, reluctant but honest; after the line he glances at his mother, just out of the frame at screen-left, a little embarrassed."),
             start=1.8, end=2.4, aca_count=ONE.format(piece='wooden ladle', pos='his')),
 'S65': dict(frame="the grandmother in the kitchen, chin up; " + G_LEFT.format(who='son'),
             action=("She raises one finger at shoulder height, clear of her mouth, on 'one sniff', then lowers her hand and says 'my nose is FINE' with her chin up, "
                     "dry and proud; after the line a small, satisfied smile.")),
 'S66': dict(shot='Medium-wide shot',
             frame=("framed from the knees up: the grandmother stands right beside the white step trash can with a foot pedal, exactly where it stands in Image 1, "
                    "holding the teal silicone spatula over its open lid, her foot, just below the frame, holding the pedal down so the lid stays open; her son "
                    "stands beside her on the other side of the can, looking at it; both are turned three-quarters toward the camera, her face and lips in view"),
             action=("She lets the spatula drop into the trash can in the first second, then lifts her foot off the pedal below the frame and the lid falls shut; "
                     "she says it to her son, who looks at the closed lid, caught out."),
             sil_ref=SIL_ONE.format(n='{n}', what='spatula')),
 'S67': dict(frame=("her son in the kitchen, looking down and toward screen-right, away from his mother, who is just out of the frame at screen-left; only he is in "
                    "the picture")),
 'S68': dict(frame="the grandmother in the kitchen, very composed; " + G_LEFT.format(who='son'),
             tone='measured and firm, each phrase laid down deliberately at a steady, normal speaking pace', start=1.0),
 'S69': dict(shot='Very tight close-up',
             frame=("the grandmother's face filling the frame from her eyebrows to her chin, her eyes unblinking, looking toward screen-right at her son, who is "
                    "just out of the frame; her lips in view"),
             living='she breathes naturally and does not blink'),
 'S70': dict(frame=("her son in the kitchen, looking toward screen-left, meeting the gaze of his mother, who is just out of the frame; " + T_RIGHT)),

 # ---------- D: Friday dinner (master edits of the 0D photo), the hallway, the Close (S71-S90) ----------
 # the hallway is not in any plate: the Friday room plate gives only the light and the boxes, the camera looks along the hallway
 'D-2': dict(bg_ref=("Image {n} is the dining room on Friday night: use it only for the warm light and the look of the plain moving boxes seen through the "
                     "archway. The camera is in the hallway beyond the archway, close to his hands; behind the hands, soft and out of focus, only the stacked plain "
                     "moving boxes and the hallway wall; no table, no chairs, nobody else."),
             frame=("her son's two hands (deep brown skin, lighter palms, a gold wedding band, the cuffs of his plaid button-down shirt) hold the glossy "
                    "senior-living brochure, cover facing the camera, in the hallway stacked with plain moving boxes; " + TEAR + "; his face is out of the frame"),
             lock_extra=TEAR_LOCK, end_v=TEAR_END, look=HALL_LOOK,
             living="only his hands and the brochure move; nobody else is in the hallway and nobody appears; the light stays steady",
             amb='a quiet hallway and the sound of the paper tearing'),
 'S71': dict(frame=("the same Friday dinner from the same camera, with the same framing as Image 1: the same people in the same chairs. The grandmother has come "
                    "around the head of the table and stands behind the gap between her son's chair and the granddaughter's chair, setting the potato salad bowl "
                    "down on the table between the granddaughter and her father, the wooden serving spoon from the set in her other hand; her own chair at the "
                    "head of the table waits for her; plain moving boxes stand stacked in the hallway beyond the archway; on the sideboard lies the "
                    "red-and-white checkered towel with a few of the other wooden pieces of the set on it"),
             action=("She sets the bowl down in the first second; everyone at the table watches her in tense silence. The boy stays hidden behind the uncle "
                     "the whole time; only his hands and blue sleeves show; his face never appears."),
             aca_count=("Exactly seven utensils in the full set: the serving spoon is the one in her hand; a few of the other pieces lie on the towel on the "
                        "sideboard, never more than six, and no serving spoon among them.")),
 'S72': dict(frame=("the same Friday dinner from the same camera, zoomed in on the grandmother serving her granddaughter: the grandmother stands behind the gap "
                    "between her son's chair and her granddaughter's chair, leaning over the potato salad bowl on the table between them, serving a spoonful of "
                    "potato salad onto her granddaughter's plate with the wooden serving spoon, her face turned toward her granddaughter and fully visible to "
                    "the camera, her lips in view; the granddaughter looks up at her; her father beside her, nearer the head of the table, soft; "
                    + AUNT_EDGE['A_FRI']),
             action=("She finishes setting the spoonful on the plate in the first second, looks her granddaughter straight in the eye and says it; after the "
                     "line she rests the wooden serving spoon in the bowl and steps back toward her place at the head of the table."),
             aca_count=("Only the wooden serving spoon from the set is in this shot; the rest of the set lies on the towel on the sideboard, out of the "
                        "frame.")),
 'S73': dict(frame=("the same Friday dinner from the same camera, zoomed in close on the granddaughter in her chair with a forkful of potato salad at her lips; "
                    "her father beside her, nearer the head of the table, soft, holding his breath; " + BOWL_FRI + "; " + AUNT_EDGE['A_FRI'])),
 'S74': dict(frame=("the same Friday dinner from the same camera, zoomed in close on the granddaughter in her chair, mid-chew, eyes going wide, her fork resting "
                    "on her plate, both hands away from her face, her lips in view; " + DAD_EDGE + "; " + AUNT_EDGE['A_FRI'] + "; her grandmother at the head "
                    "of the table is just out of the frame at screen-right"),
             action="She stops chewing in the first second, swallows, eyes wide, and says it.", start=1.0, edge=['T3']),
 'S75': dict(frame=("the same Friday dinner from the same camera, zoomed in close on the granddaughter in her chair breaking into a laugh, eyes wet, one hand "
                    "pressed to her chest, the other on the table, her fingers clear of her lips and her lips in view; " + DAD_EDGE + "; " + AUNT_EDGE['A_FRI'] +
                    "; her grandmother at the head of the table is just out of the frame at screen-right"),
             action=("She breaks into a laugh, eyes wet, one hand pressed to her chest, and says it bursting with relief and joy, her shoulders shaking; on "
                     "'NONE' she opens her hand toward her grandmother, just out of the frame at screen-right."),
             edge=['T3']),
 'S76': dict(frame=("the same Friday dinner from the same camera, zoomed in close on the son in his chair with a forkful of potato salad at his mouth; behind "
                    "him, soft, the archway with plain moving boxes in the hallway beyond; " + JADA_EDGE + "; his mother at the head of the table is just out "
                    "of the frame at screen-right; the sideboard is out of the frame"),
             edge=['J2']),
 'S77': dict(frame=("the same Friday dinner from the same camera, zoomed in close on the son in his chair, eyes red, looking toward his mother at the head of "
                    "the table, just out of the frame at screen-right, his hands on the table, away from his face, his lips in view; behind him, soft, the "
                    "archway; " + JADA_EDGE + "; the sideboard is out of the frame, on the side he looks toward"),
             edge=['J2']),
 'S78': dict(bg_ref=("Image {n} is the dining room on Friday night: use it only for the cream wall color, the warm light and the look of the plain moving "
                     "boxes seen through the archway. The camera stands inside the hallway, a few steps beyond the archway, and looks along the hallway away "
                     "from the dining room; the dining table, its chairs and the family are behind the camera and not in the frame; nobody else is in the "
                     "hallway."),
             frame=("her son from the waist up, standing in the hallway beside a stack of plain moving boxes, his face softly and clearly lit by a warm "
                    "hallway ceiling light, holding the brochure upright in front of his chest; " + TEAR),
             text_on_object='the brochure cover lettering "WRENFIELD · SENIOR LIVING"', lock_extra=TEAR_LOCK, end_v=TEAR_END, look=HALL_LOOK,
             living="nobody else is in the hallway and nobody appears; the light stays steady",
             amb='a quiet hallway and the sound of the paper tearing'),
 'S79': dict(frame=("the same Friday dinner from the same camera, zoomed in close on the grandmother, now sitting in her own chair at the head of the table, "
                    "half laughing, half crying, her hands resting on the table, her fingers clear of her lips and her lips in view; behind her, soft, the "
                    "carved wooden fork and spoon; the sideboard is out of the frame; her son is just out of the frame at screen-left, and the son's wife is "
                    "just out of the frame at screen-right"),
             action=("Half laughing, half crying, she gives the order with a wet smile, her open hand gesturing toward her son, just out of the frame at "
                     "screen-left, on 'Terrance'; after the line she wipes under one eye with her fingertip and lets out a small laugh, still smiling.")),
 'S80': dict(frame=("the same Friday dinner from the same camera, zoomed in on the granddaughter: she holds her empty plate out toward her grandmother at the "
                    "head of the table, just out of the frame at screen-right, mouth closed, grinning; her father beside her, nearer the head of the table, "
                    "soft; " + BOWL_FRI + "; " + AUNT_EDGE['A_FRI'])),
 'S81': dict(frame=("the same Friday dinner from the same camera, with the same framing as Image 1: the same people in the same chairs, laughing. The "
                    "grandmother sits in her own chair at the head of the table; along the side wall with the family photos her son holds the wooden serving "
                    "spoon over his daughter's plate, the potato salad bowl on the table between them, the aunt laughing beside the granddaughter; on the "
                    "other side the son's wife and the uncle laugh, and between them only the boy's small hands and blue hoodie sleeves show, the rest of him "
                    "hidden behind the uncle; on the sideboard lies the red-and-white checkered towel with a few of the other wooden pieces of the set on it, "
                    "where the gift bags stood at the birthday"),
             action=("The son serves his daughter seconds in the first second; the table keeps laughing. The boy stays hidden behind the uncle the whole "
                     "time; only his hands and blue sleeves show; his face never appears."),
             amb='soft laughter without words, cutlery',
             aca_count=("Exactly seven utensils in the full set: the serving spoon is the one in her son's hand; a few of the other pieces lie on the towel "
                        "on the sideboard, never more than six, and no serving spoon among them.")),
 'S82': dict(frame=("weeks later in the clean kitchen, no boxes, the round wooden utensil holder with all seven wooden utensils of the set on the counter; the "
                    "grandmother in a soft blue cardigan holds the leftover teal silicone ladle upright at chest height beside her, clear of her face and lips; "
                    "the leftover teal ladle in her hand is the only teal silicone item in the kitchen; no white crock, no other teal utensils"),
             action=("From the first frame she already looks straight into the lens and starts right away, as if letting the viewer in on a secret, with a "
                     "dry, mischievous smile; she lifts the ladle a little as she speaks, keeping it below her chin and clear of her lips; on 'over THIS' "
                     "she raises her eyebrows at the ladle. The ladle moves only with her hand; the wooden set in the holder stays exactly in place."),
             sil_ref=SIL_ONE.format(n='{n}', what='ladle')),
 'S84': dict(shot='Medium-wide shot',
             frame=("framed from the knees up: the grandmother beside the white step trash can on the floor, exactly where it stands in Image 1, its lid held "
                    "open by her foot on the pedal, holding the teal silicone ladle over the opening at hip height, looking into the lens; the leftover teal "
                    "ladle is the only teal silicone item in the kitchen; no white crock, no other teal utensils"),
             action=("She lets the ladle drop into the trash can in the first second, then lifts her foot off the pedal and the lid falls shut; she says it "
                     "to the viewer."),
             sil_ref=SIL_ONE.format(n='{n}', what='ladle')),
 # S85: her son tastes at the stove behind her, so the camera looks toward the range end (0F plate seen from the sink end)
 'S85': dict(plate='BG_B_CLEAR_REV',
             frame=("the grandmother in the clean kitchen looking into the lens; behind her over her shoulder, soft, her son in a navy sweater stands at the old "
                    "white gas range, tasting from the pot on its lit front burner with the mixing spoon from the set"),
             action=("She glances over her shoulder at her son, who nods while tasting, then looks back into the lens before the first word and says it; one "
                     "eyebrow lifts on 'smell HERS' and she gives a small, warm nod on 'before you blame her', smiling."),
             start=1.2,
             aca_count=("Exactly seven utensils in the full set: her son holds the mixing spoon, and the round holder beside the range holds only the other "
                        "six; no second mixing spoon.")),
 'S86': dict(frame=("the grandmother standing beside the round wooden utensil holder on the counter, holding the wooden ladle upright at chest height beside her, "
                    "clear of her face and lips, looking into the lens"),
             action=("She lifts the wooden ladle a little, keeping it below her chin and clear of her lips, with a proud smile on 'Mine are Acawood now', then "
                     "opens her free hand toward the rest of the set in the round holder on 'seven pieces' and says the rest, proud and clear. The ladle moves "
                     "only with her hand; every wooden piece in the holder stays exactly in place."),
             say="She says Acawood as AH-kah-wood.",
             aca_count=("Exactly seven utensils in the full set: the ladle is in her hand, and the round holder holds only the other six (a wok spatula, a "
                        "slotted spoon, a turner, a serving spoon, a mixing spoon and a small spoon); the ladle's place in the holder is empty and there is no "
                        "second ladle anywhere.")),
 'S87': dict(amb='a quiet kitchen room tone',
             aca_count="Only the ladle is in this shot; the rest of the set is out of the frame."),
 'S88': dict(action=("She finishes drying the ladle and stands it in the round holder in the first two seconds, then lets go; now all seven pieces stand in "
                     "the holder."),
             amb='wood touching the holder',
             aca_count=("Exactly seven utensils in the full set: the ladle is in her hands, and the round holder beside her holds only the other six; the "
                        "ladle's place in the holder is empty.")),
 'S83': dict(start=1.0),
 'S89': dict(end=6.8, start=1.0),
}
# straight-on variants (F1b / F5b) whose text changes with the fixes above
_T_BACK = "the low wooden cabinet with the crystal jar and the cluster of framed photos on the wall above it"
_J_BACK = "the framed graduation portrait of a young man in cap and gown"
FIX_H2 = {
 'C-2': (f"a close-up from across the birthday table: the granddaughter mid-chew in her chair, fork just lowered, eyes starting to water; behind her, soft, "
         f"{_J_BACK}; her standing father's arm in its navy quarter-zip sleeve, his deep-brown hand with a gold wedding band holding his drinking glass, soft "
         "at the screen-right edge of the frame, on the side toward the head of the table"),
 'S02_C': (f"a close-up from across the birthday table: her son still standing at his chair, his drinking glass still raised at shoulder height, off to the "
           f"side and clear of his face, his mouth in full view, turning his head toward his daughter beside him at screen-left; behind him, soft, {_T_BACK}; "
           "the sideboard is out of the frame, on the side he looks toward at the end of the line"),
 'E-2': (f"a close-up from across the birthday table: the granddaughter in her chair looking down at a slim modern handset with a black glass touchscreen, the "
         f"size of her palm, held low in front of her with its screen tilted away from the camera, her plate of food in front of her, barely touched; behind "
         f"her, soft, {_J_BACK}; her father, in the next chair at screen-right, and the aunt, in the next chair at screen-left, are both just out of the frame"),
 'S01': (f"a medium shot from across the birthday table: the granddaughter in her chair has just pushed her plate away and grimaces, mouth open to speak, her "
         f"face turned up toward her grandmother at screen-right, in three-quarter view to the camera; her father sits beside her on the side nearer the head of "
         f"the table, at screen-right, soft; the grandmother has come around the head of the table and stands at the corner of the table beside her son's chair, "
         f"the potato salad bowl in one arm and the teal silicone serving spoon in her other hand; behind them, soft, {_J_BACK} and, toward screen-right, {_T_BACK}"),
 'S03': (f"a close-up from across the birthday table: the grandmother at the head end of the table, mid-step, holding the potato salad "
         f"bowl with the teal serving spoon resting in it, still smiling, her eyes turning toward the head of the room at screen-right; behind her, soft, "
         f"{_T_BACK}; her son is just out of the frame at screen-left; the sideboard is out of the frame, on the side she looks toward"),
 'S06': (f"a medium shot from across the birthday table: her son half risen from his chair, turned toward the head of the room at screen-right, one open hand "
         f"reaching out toward his mother, who stands just out of the frame at the sideboard; behind him, soft, {_T_BACK}; the sideboard is out of the frame, "
         f"on the side he reaches toward; beside him at screen-left, soft, his daughter frozen in her chair; no brochure in this frame"),
 'S72': (f"a medium shot from across the Friday dinner table: the grandmother stands behind the gap between her granddaughter's chair and her son's chair, "
         f"between the chairs and the wall, leaning over the potato salad bowl on the table between them, serving a spoonful onto her granddaughter's plate "
         f"with the wooden serving spoon, her face turned toward her granddaughter, in three-quarter view to the camera, her lips in view; the granddaughter "
         f"looks up at her; her father sits beside her on the side nearer the head of the table, at screen-right, soft; behind them, soft, {_J_BACK} and, "
         f"toward screen-right, {_T_BACK}"),
 'S74': (f"a close-up from across the Friday dinner table: the granddaughter in her chair, mid-chew, eyes going wide, her fork resting on her plate, both "
         f"hands away from her face, her lips in view; behind her, soft, {_J_BACK}; her eyes are on her grandmother, who is just out of the frame at "
         f"screen-right; nobody looks into the lens"),
 'S75': (f"a close-up from across the Friday dinner table: the granddaughter in her chair breaking into a laugh, eyes wet, one hand pressed to her chest, the "
         f"other on the table, her fingers clear of her lips and her lips in view; behind her, soft, {_J_BACK}; her eyes are on her grandmother, who is just "
         f"out of the frame at screen-right; nobody looks into the lens"),
 'S77': (f"a close-up from across the Friday dinner table: her son in his chair, eyes red, looking toward his mother at the head of the table, just out of the "
         f"frame at screen-right, his hands on the table, away from his face, his lips in view; behind him, soft, {_T_BACK}; the sideboard is out of the "
         f"frame, on the side he looks toward"),
 'S80': (f"a medium shot from across the Friday dinner table: the granddaughter in her chair holding her empty plate out toward her grandmother at the head of "
         f"the table, just out of the frame at screen-right, mouth closed, grinning; her father beside her at screen-right, soft; the large glass bowl of "
         f"potato salad stands on the table between them, the wooden serving spoon resting in it; behind them, soft, {_J_BACK} and, toward screen-right, "
         f"{_T_BACK}"),
}
# who else is visible (sheet + description): S03 now shows only her; the boy's sleeves in S05
EXTRA = {'S05': ['T1', 'J1', 'W', 'B'], 'S06': ['J1'], 'B-1': ['W'], 'S02_B': ['W'], 'S07': ['W']}
# face lines that would turn brown skin grey, or show a smile the beat does not have
FACE_FIX = {
 'S02_C': "the son embarrassed and alarmed, his glass still raised, jaw tight, keeping his voice down, not angry; his daughter guilty but stubborn; nobody smiles",
 'S48': "the grandmother alarmed: eyes wide and fixed on the pan, lips slightly parted, jaw tight; her skin keeps exactly its warm medium-deep brown tone; no smile",
 'S61': "the son reluctant, eyes narrowed as he sniffs; no smile",
 'S64': "the son reluctant, searching hard for something wrong; no smile",
}
