# S14c We Talked About This (Black) - shot data for TobyFlow
# frame = what the start frame shows; action = what happens in the clip
# chars: G1-4 Gloria outfits, T1-4 Terrance, J1-2 Jada, D Dorothy, W wife, B grandson, FD friend's daughter
# props: sil (teal silicone), bro (brochure), aca (Acawood set), hold (holder), towel, water (real test clip)

SH = []
def S(id, bg, chars, shot, frame, action, props=(), tone='', start=0.4, cam='locked', src=None,
      text_on_object=None, living='', amb=None, lock_extra='', enabled=True, line_from=None, hands_of=None, bg_ref=None):
    # hands_of: hands-only shot; the character whose skin tone, ring and sleeves the hands must match
    SH.append(dict(id=id, bg=bg, chars=list(chars), shot=shot, frame=frame, action=action,
                   props=list(props), tone=tone, start=start, cam=cam, src=src,
                   text_on_object=text_on_object, living=living, amb=amb,
                   lock_extra=lock_extra, enabled=enabled, line_from=line_from or id, hands_of=hands_of, bg_ref=bg_ref))

# ---------------- HOOKS ----------------
S('A-1','A_BDAY',['J1','T1','G1'],'Close-up',
  "the granddaughter, seated right next to her father at the birthday table, leans toward him with one hand raised beside her mouth as if to whisper; her father is partly in frame, soft; the grandmother stands at the head of the table in the soft background holding the potato salad bowl",
  "She whispers to her father behind her hand, loud enough for the whole table to hear. Halfway through, the focus shifts gently to the grandmother at the head of the table, who holds the bowl and hears every word.",
  props=['dish'], tone='a loud whisper that she thinks is quiet, embarrassed, not mean')
S('B-1','A_BDAY',['T1','J1'],'Medium shot',
  "at the sideboard, his hand is sliding the senior-living brochure under a gift bag tied with a bow; the cover is readable; his daughter stands right behind him, stunned",
  "His hand finishes pushing the brochure under the gift bag in the first second; he turns his head; the camera eases back a few centimeters to show his daughter behind him, who speaks.",
  props=['bro'], tone='shocked, hushed, protective of her grandmother', cam='pullback',
  text_on_object='the brochure cover lettering "WRENFIELD · SENIOR LIVING"')
S('C-1','A_BDAY',['T1','J1'],'Medium shot',
  "he stands at the birthday table raising his glass toward his mother, who is off-frame at the head of the table; around the table, soft, his wife, his daughter and two older relatives, all Black American adults, lift their drinking glasses",
  "He lifts his glass a little higher toward his mother, off-frame at the head of the table, as he starts the toast, his free hand pressed to his chest for a moment; on 'still cooking' a proud grin breaks across his face and he tips the glass toward her. Around the table the family smile and lift their drinking glasses a little higher; his daughter grins toward the head of the table.",
  tone='warm, proud, a little formal')
S('C-2','A_BDAY',['J1'],'Close-up',
  "the granddaughter mid-chew at the birthday table, fork just lowered, eyes starting to water",
  "She stops chewing, sets her fork down on the plate in the first second, and says it with an apologetic wince.",
  tone='apologetic, uncomfortable, honest')
S('D-2','A_FRI',[],'Extreme close-up',
  "her son's two hands (deep brown skin, lighter palms, a gold wedding band, the cuffs of his plaid button-down shirt) hold the glossy senior-living brochure, cover facing camera and readable, in a hallway stacked with cardboard moving boxes; his face is out of the frame",
  "In the first second the hands tear the brochure in half in one motion, then hold the two halves still.",
  props=['bro'], start=0, text_on_object='the brochure cover lettering "WRENFIELD · SENIOR LIVING"', hands_of='T3',
  lock_extra="The brochure is the only thing that changes: it tears once into two halves along one clean line; the hands keep exactly five fingers each; nothing else changes.")
S('E-2','A_BDAY',['J1'],'Close-up',
  "the granddaughter at the birthday table looking down at a small handset held in her lap with its screen tilted away from the camera, her plate in front of her",
  "She looks up from the handset, pushes her plate a few centimeters away in the first second and says it out loud to her father.",
  tone='done pretending, blunt but not cruel', start=0.8)

# ---------------- BODY ----------------
S('S01','A_BDAY',['G1','J1','T1'],'Medium shot',
  "the grandmother walks around her birthday table carrying the potato salad bowl, a teal silicone serving spoon in her other hand; the granddaughter, seated right next to her father, has just pushed her plate away and grimaces, mouth open to speak; the rest of the Black American family, adults only, soft in the background",
  "The granddaughter says the line straight to her grandmother; the grandmother stops beside her with the bowl.",
  props=['dish','sil','bottle'], tone='blunt, honest, not mean')
S('S02','A_BDAY',['T1','J1'],'Close-up',
  "her son at the birthday table turning his head toward his daughter beside him, jaw tight",
  "He speaks to his daughter through his teeth; on the last word his eyes flick toward the gift bags on the sideboard.",
  tone='a low hiss through his teeth, embarrassed')
S('S02_B','A_BDAY',['T1','J1'],'Close-up',
  "her son standing at the sideboard by the gift bags, turning his head toward his daughter who stands right behind him",
  "He speaks to his daughter through his teeth; on the last word his eyes flick down to the gift bags beside his hand.",
  tone='a low hiss through his teeth, embarrassed', line_from='S02', enabled=True)
S('S02_C','A_BDAY',['T1','J1'],'Close-up',
  "her son still standing at the birthday table with his raised glass in hand, turning his head toward his daughter beside him",
  "Still holding his glass, he speaks to his daughter through his teeth; on the last word his eyes flick toward the gift bags on the sideboard.",
  tone='a low hiss through his teeth, embarrassed', line_from='S02')
S('S03','A_BDAY',['G1'],'Close-up',
  "the grandmother standing still mid-step holding the potato salad bowl, still smiling, her eyes turning toward the sideboard",
  "She follows her son's glance toward the sideboard and her smile fades as she asks.",
  props=['dish'], tone='light at first, then uncertain')
S('S03_B','A_BDAY',['G1'],'Close-up',
  "the grandmother standing still holding the potato salad bowl, still smiling, looking across the room toward her son at the sideboard",
  "She looks at her son standing by the sideboard and her smile fades as she asks.",
  props=['dish'], tone='light at first, then uncertain', line_from='S03')
S('S04','A_BDAY',[],'Insert, extreme close-up',
  "on the sideboard, under a gift bag tied with a bow, the corner of a glossy brochure sticks out; its cover photo shows smiling seniors at a communal dining table; no lettering visible",
  "Nothing moves; the camera glides a few centimeters closer to the brochure corner.",
  props=['bro'], start=0, cam='push')
S('S05','A_BDAY',['G1'],'Medium shot',
  "the grandmother at the sideboard holding the brochure in both hands, the bowl set down beside her; behind her, soft, the Black American family at the table is frozen, only adults in view",
  "She looks at the cover, then turns her head to her son and says it.",
  props=['bro','dish'], tone='stunned, hurt, rising')
S('S06','A_BDAY',['T1'],'Medium shot',
  "her son half risen from his chair at the birthday table, one hand reaching out toward the brochure",
  "Half risen from his chair, he keeps his open hand out toward his mother off-frame as he starts pleading, then lets it drop onto the table edge on 'after cake' and shakes his head a little at himself; after the line he sinks back down into his chair, cornered, his eyes still on her.",
  tone='pleading, cornered, soft')
S('S07','A_BDAY',['G1'],'Close-up',
  "the grandmother's face, eyes red and wet, the brochure held at chest height in trembling hands",
  "Her hands tremble on the brochure and she lowers it a few centimeters as she says it with a broken breath; her chin quivers and her eyes go from her son to the rest of the table, off-frame, and back; after the line she presses her lips together hard and shakes her head once, blinking back tears.",
  props=['bro'], tone='hurt, betrayed, a crack in the voice')
S('S08','A_BDAY',['W','J1','B'],'Wide shot',
  "the whole birthday table frozen: the son's wife stares at her plate, the granddaughter covers her mouth with her hand, at the right edge of the frame the boy's small hand and striped sleeve rest on the table, his face out of the frame; two older Black American relatives sit frozen, soft at the far end; gold balloons float behind them",
  "Nobody moves except for breathing and one small swallow; the balloons sway slightly.", start=0,
  props=['bottle'])
S('S09','B_NIGHT',['G1'],'Medium shot',
  "at night in her kitchen the grandmother stands at the step trash can, her foot on its pedal holding the lid open, a plate and fork in her hands, the white ceramic crock of teal silicone utensils on the counter beside the old white gas range",
  "She scrapes the plate hard into the trash can with the fork, twice, then says it without looking up.",
  props=['sil'], tone='stung, offended, hiding hurt', start=1.0)
S('S10','B_NIGHT',['T1'],'Medium shot',
  "her son leaning in the kitchen doorway at night with his arms crossed, tired",
  "He pushes off the door frame and uncrosses his arms in the first second, taking one step into the kitchen toward his mother off-frame; he opens one hand toward her on 'every dinner since Christmas' and rubs the back of his neck on 'we've all noticed', tired, loving but helpless; after the line his hand drops and he holds her gaze.",
  tone='tired, loving but helpless')
S('S11','B_NIGHT',['G1'],'Close-up',
  "the grandmother at night, holding the scraped plate still, her face turning toward the doorway",
  "She stops, the plate still in her hand, and asks quietly.",
  tone='small, wounded')
S('S12','B_NIGHT',['T1','G1'],'Over-the-shoulder shot',
  "an over-the-shoulder shot: the grandmother's silver hair and cardigan shoulder soft in the foreground at the frame edge; her son faces her in the night kitchen",
  "He tilts his head and gives her a small, sympathetic smile, the way you talk to a child, and lifts one hand a little toward her as he says it; in the soft foreground the grandmother's shoulder stiffens and she draws back a few centimeters, away from his hand.",
  tone='gentle, patronizing without meaning to be')
S('S13','B_NIGHT',['T1'],'Medium shot',
  "her son in the night kitchen, the old white gas range at the edge of frame",
  "He steps over to the old gas range in the first second and rests his fingertips on the counter beside it; on 'smell gas' he glances down at the burners, then looks back up at his mother off-frame, his brow knotted with worry; the burners stay off and unlit; after the line he waits for her answer.",
  tone='worried, careful')
S('S14','B_NIGHT',['G1'],'Close-up',
  "the grandmother at night, chin trembling, lowering the plate toward the counter",
  "She sets the plate down on the counter in the first second and says it, proud and shaking.",
  tone='proud, shaking, holding back tears')
S('S15','B_NIGHT',['T1'],'Close-up',
  "her son in the night kitchen, his eyes red",
  "He nods once on 'I know', then leans a little closer to his mother off-frame and says the rest quietly, his wet eyes steady on her and his jaw working to hold it together; after the line he presses his lips together and looks down for a moment.",
  tone='honest, scared for her')
S('S16','B_NIGHT',['T1'],'Medium shot',
  "her son at the kitchen counter at night, one hand flat on the brochure lying on the counter",
  "He slides the brochure a short way across the counter toward his mother in the first second, lets go, and says it.",
  props=['bro'], tone='controlled, rehearsed, guilty', start=1.0)
S('S17','B_NIGHT',['G1'],'Extreme close-up',
  "an extreme close-up of the grandmother's eyes at night, looking off to one side, tears welling",
  "A tear spills as she says it; she holds still for half a second after the line.",
  tone='disbelief, barely a whisper')
S('S18','C',['T1'],'Medium shot',
  "seen from inside the house through a screen door (the mesh soft in the foreground): her son stands at the far end of the front porch under the yellow porch light, turned toward the street, a handset to his ear; the mesh and the distance keep his face hidden",
  "He stays turned toward the street, shifts his weight and lowers his head as he talks on the handset; his face stays hidden the whole time.",
  start=0, amb='crickets outside, a distant car')
S('S19','C',['G1'],'Close-up',
  "the grandmother just inside the screen door at night, the yellow porch light on her face through the mesh",
  "In the first second she presses her hand over her mouth and closes her eyes, then holds still.",
  start=0, amb='crickets outside',
  bg_ref="Image {n} shows the same front porch seen from inside the house; this shot is the reverse angle, from the porch looking in through the screen door at the dim front hallway: use Image {n} only for the screen door, the yellow porch light and the colors.")
S('S20','B_MORNING',['G2'],'Medium shot',
  "next morning in slanted sun, the grandmother stands at the stove scrambling eggs in a skillet on a lit burner with a teal silicone spatula; a new bottle of dish soap and a new sponge with plain unbranded labels sit on the counter",
  "She stirs the eggs with the spatula; a little steam rises from the skillet.",
  props=['sil'], start=0, amb='eggs sizzling softly in the skillet')
S('S21','B_MORNING',['J1'],'Medium shot',
  "the granddaughter in her grey hoodie in the morning kitchen, car keys in one hand, a forkful of scrambled eggs at her mouth",
  "She takes the bite, chews once, winces apologetically and says it.",
  tone='apologetic, gentle', start=1.0,
  props=['bottle'])
S('S22','B_MORNING',['G2'],'Close-up',
  "the grandmother in the morning kitchen, one finger pointing at the new dish soap bottle on the counter, the teal silicone spatula in her other hand",
  "She jabs her finger toward the new dish soap bottle on 'THREE times', then taps the counter beside it on 'new soap, new sponge', frustrated and insistent, looking back at her granddaughter off-frame; the teal spatula in her other hand moves only with that hand; after the line she throws up her free hand a little and shakes her head.",
  props=['sil'], tone='frustrated, insistent')
S('S23','B_MORNING',['G2'],'Close-up',
  "the grandmother in the morning kitchen with a fork of the same eggs at her lips",
  "She takes the bite and chews, taking her time; she finds nothing wrong and says it, puzzled.",
  tone='puzzled, quietly scared', start=1.0)
S('S24','B_MORNING',['G2'],'Extreme close-up',
  "an extreme close-up of the grandmother's face in the morning light, eyes looking off to one side toward her granddaughter",
  "Her eyes fill as she asks it in a small, frightened voice; her brows lift and draw together and her lips tremble on 'losing it'; for a moment her gaze drops away from her granddaughter, then comes back up, searching her face.",
  tone='small, frightened')
S('S25','B_MORNING',['J1','G2'],'Close-up',
  "the granddaughter facing her grandmother in the morning kitchen, lips parted as if about to answer",
  "In the first second she stops herself and steps in to hug her grandmother tight; they hold the hug.", start=0)
S('S26','B_MORNING',['J1','G2'],'Over-the-shoulder shot',
  "over the granddaughter's shoulder (her braids and grey hood soft in the foreground): the grandmother's face inside the hug, staring into the distance",
  "They hold the hug; the grandmother blinks once and keeps staring into the distance.", start=0)
S('S27','B_BOXES',['G2'],'Medium shot',
  "a few days later, the grandmother at the counter wrapping a mixing bowl in newspaper above an open cardboard moving box; flattened boxes and tape on the counter",
  "She lowers the wrapped bowl into the box in the first second and lets go.", start=0, amb='a strip of packing tape being pulled')
S('S28','D',['D','FD','G2'],'Wide shot',
  "Sunday afternoon on the street: the friend's daughter in her car in the driveway, waving through the window, a foil-covered plate on the passenger seat; the friend waves from her porch; the grandmother stands on the sidewalk holding an empty glass baking dish",
  "The car rolls out of the driveway at walking pace and away; both women keep waving; the grandmother watches.", start=0,
  amb='a car driving off, birds')
S('S29','D',['G2'],'Medium shot',
  "the grandmother on the friend's porch steps holding the empty baking dish, looking down the street after the car",
  "She climbs the last step and says it, still looking after the car.",
  tone='surprised, curious, a little pointed', start=1.0)
S('S30','D',['D'],'Close-up',
  "the friend on her porch, one hand raised waving down the street, smiling",
  "She gives one last wave down the street, lowers her hand and turns her head back to her friend off-frame in the first second, then says it with a dry, knowing smile and a lift of her eyebrows; after the line her smile widens a little; her church hat stays in place.",
  tone='dry, amused')
S('S31','D',['G2','D'],'Medium shot',
  "the two women seated side by side on the white porch swing, the empty baking dish on the grandmother's lap, a coffee mug on the side table",
  "The grandmother turns to her friend and asks.",
  tone='genuinely curious')
S('S32','D',['D'],'Close-up',
  "the friend on the porch swing with a coffee mug at her lips",
  "She takes a sip, lowers the mug and says it like it's nothing.",
  tone='matter-of-fact, calm', start=1.0)
S('S33','D',['G2'],'Close-up',
  "the grandmother on the porch swing, the baking dish on her lap",
  "She goes completely still; the dish slips a few centimeters on her lap and she catches it.", start=0)
S('S34','D',['G2'],'Close-up',
  "the grandmother on the porch swing, looking at her friend",
  "She shifts her weight and the porch swing rocks a little under her; she lowers her eyes, then lifts them back to her friend and says it almost in a whisper, with a small nod of recognition; after the line she keeps looking at her friend, her lips pressed together.",
  tone='a near whisper, recognition')
S('S35','D',['D'],'Medium shot',
  "the friend standing up from the porch swing, canvas tote bag already on her shoulder, the coffee mug set on the side table",
  "She straightens up and says it, decided.",
  tone='calm, decisive')
S('S36','B_BOXES',['D'],'Medium shot',
  "in the grandmother's kitchen cluttered with moving boxes, the friend in her moss-green dress holds a teal silicone spatula she has pulled from the white crock, looking at it",
  "She turns her eyes from the spatula to her friend and asks.",
  props=['sil'], tone='casual but probing')
S('S37','B_BOXES',['G2'],'Close-up',
  "the grandmother among the moving boxes, a roll of packing tape in her hand",
  "She lowers the roll of packing tape to her side in the first second and answers her friend off-frame a little defensively, with a small shrug on 'Terrance sent me' and a quick shake of her head on 'black plastic', as if it was obvious.",
  tone='defensive, explaining')
S('S38','B_BOXES',['D'],'Close-up',
  "the friend in the kitchen, looking straight at her friend, one eyebrow raised",
  "She tilts her head and leans in a little toward her friend as she asks it, her eyebrow still raised and a knowing half-smile at one corner of her mouth; after the line she folds her arms and waits; her church hat stays in place.",
  tone='knowing, leading')
S('S39','B_BOXES',['G2'],'Extreme close-up',
  "an extreme close-up of the grandmother's eyes, looking off to one side",
  "Her eyes move a little as she counts back the weeks in her head.", start=0)
S('S40','B_BOXES',['G2'],'Close-up',
  "the grandmother's face as something dawns on her",
  "It dawns on her in the first second: her eyes widen and her gaze drifts away from her friend into the middle distance; she says the one word quietly and her hand rises to her chest; after the word she presses her lips together, shaken.",
  tone='realization, quiet', start=1.0)
S('S41','B_BOXES',['D','G2'],'Medium shot',
  "the friend holds the head of the teal silicone spatula up close to the grandmother's nose",
  "She holds the teal spatula steady under her friend's nose and says it, firm and simple; the grandmother hesitates, glances from the spatula to her friend and back, and leans in a few centimeters toward it, wary.",
  props=['sil'], tone='firm, simple')
S('S42','B_BOXES',['G2'],'Extreme close-up',
  "an extreme close-up of the grandmother with the teal silicone spatula head just below her nose, held there by the friend's hand coming in from the edge of the frame (deep brown skin, a moss-green cardigan sleeve)",
  "She sniffs once, flinches back and wrinkles her nose, then says it.",
  props=['sil'], tone='shocked, indignant', start=1.0, hands_of='D')
S('S43','B_BOXES',['D'],'Close-up',
  "the friend holding the teal silicone spatula loosely in her fingers",
  "She lifts the teal spatula a little between them and looks from it to her friend as she says it, calm, like someone who has been through it, with a small nod on 'whatever soap you use'; the spatula moves only with her hand; her church hat stays in place.",
  props=['sil'], tone='calm, like someone who has been through it')
S('S44','B_BOXES',[],'Insert close-up',
  "a large mixing bowl of warm, just-boiled potatoes and chopped egg with mayonnaise on the counter, a teal silicone spatula resting in it; a faint wisp of steam",
  "The spatula rests in the warm potatoes and does not move; a faint wisp of real steam rises from the hot potatoes; the camera glides a few centimeters closer to the spatula. No effects, no bubbles on the spatula.",
  props=['sil','dishpot'], start=0, cam='push', amb='a quiet daytime kitchen')
S('S45','B_BOXES',['G2'],'Close-up',
  "the grandmother among the moving boxes, troubled",
  "She shakes her head as she says it, troubled, and spreads one hand a little, palm up, still defending herself, her eyes searching her friend's face off-frame; after the line her hand drops and she looks down.",
  tone='troubled, still defending herself')
S('S46','B_BOXES',['D'],'Close-up',
  "the friend with a sad, knowing smile",
  "She gives a small shrug and a sad, knowing smile on 'neither could I', then tips her head toward her friend and says the rest gently, her eyes kind; after the line she gives one small nod; her church hat stays in place.",
  tone='gentle, knowing')
S('S47','B_BOXES',['D'],'Medium shot',
  "the friend at an open cabinet holding a teal silicone muffin pan in both hands",
  "She turns from the open cabinet toward her friend off-frame in the first second, holding the teal silicone muffin pan out a little in both hands, and says it serious and plain, not preachy, lifting the pan a few centimeters on 'baking pans' and lowering it on 'chemicals leached out'.",
  props=['sil'], tone='serious, plain, not preachy')
S('S48','B_BOXES',['G2'],'Close-up',
  "the grandmother staring at a teal silicone muffin pan held in the friend's hands at the edge of the frame (deep brown skin, moss-green cardigan sleeves)",
  "She keeps staring at the pan; the color drains from her face a little; she swallows.", start=0, hands_of='D')
S('S49',None,[],'Top shot',
  "REAL PRODUCT PHOTO",
  "The seven wooden utensils lie still on the red-and-white checkered towel; only the daylight shifts a little across them.",
  props=['aca','towel'], start=0, src='IMG_ACA_TOWEL', amb='two wooden pieces touching softly')
S('S50','B_BOXES',['D'],'Medium shot',
  "the friend at the counter, one hand resting on a red-and-white checkered towel beside a row of the seven wooden utensils",
  "She makes a small tossing-away motion with her free hand on 'threw all mine out', then opens that hand toward the row of wooden utensils on 'got these', with a confident little smile at her friend off-frame; her other hand stays resting on the towel and every wooden piece stays exactly where it is.",
  props=['aca','towel'], tone='plain, confident')
S('S51','B_BOXES',['G2'],'Close-up',
  "the grandmother holding one of the wooden spoons in front of her, looking at it, frowning",
  "She raises the wooden spoon a little closer to her eyes on 'Wood?' with a skeptical frown, then lowers it and looks up at her friend off-frame to say the rest, one eyebrow raised, like a cook who has seen it all; the spoon moves only with her hand and keeps its exact shape.",
  props=['aca'], tone='doubtful, experienced cook')
S('S52','B_BOXES',['D'],'Close-up',
  "the friend in the kitchen, shaking her head a little",
  "She shakes her head once on 'that's the finish' and says the rest plainly, certain, holding her friend's gaze; after the line she gives a small, sure nod; her church hat stays in place.",
  tone='certain, brief')
S('S53',None,[],'Macro',
  "REAL PRODUCT MACRO",
  "Nothing moves; the light glides along the grain; the camera glides a few millimeters along the handle.",
  props=['aca'], start=0, src='IMG_ACA_MACRO', cam='push')
S('S54','B_BOXES',['D'],'Medium shot',
  "the friend holding up a small handset with its screen turned away from camera, thumb over it; on the counter another handset lies face up, screen off",
  "She taps once with her thumb; the screen of the handset on the counter lights up with a plain bright glow, nothing readable; she says it.",
  tone='pleased, practical')
S('S56','B_BOXES',['D'],'Medium shot',
  "the friend at the counter, one hand on a rolled-up red-and-white checkered towel with wooden utensil handles showing at one end",
  "She slides the rolled towel a short way across the counter toward her friend in the first second, lets go and says it.",
  props=['aca','towel'], tone='kind, matter-of-fact', start=1.0)
S('S57','B_BOXES',['T2'],'Medium shot',
  "her son in a grey fleece vest just inside the kitchen, a stack of flattened moving boxes in one arm, a roll of tape in his hand",
  "He drops the stack of flattened boxes on the floor in the first second and says it.",
  tone='businesslike, tired', start=1.0)
S('S58','B_BOXES',['G2'],'Medium shot',
  "the grandmother holding the teal silicone spatula out toward her son",
  "She steps toward her son off-frame in the first second and holds the teal spatula out to him, head up, and says it calm and firm; after the line she keeps it held out, eyebrows raised, waiting.",
  props=['sil'], tone='calm, firm')
S('S59','B_BOXES',['T2'],'Close-up',
  "her son in the kitchen, exhaling, worn out",
  "He drops his head for a moment in the first second, then lifts it and says it to his mother off-frame, worn out and exasperated, gesturing with an open hand toward the spatula off-frame on 'SPATULA'; after the line he shakes his head and looks away.",
  tone='worn out, exasperated', start=1.0)
S('S60','B_BOXES',['G2'],'Close-up',
  "the grandmother in the kitchen, face set",
  "She takes one step closer to her son off-frame in the first second and says it, her voice hardening, her chin lifting on 'Terrance', her eyes never leaving his; she does not back down.",
  tone='hard, using his full name')
S('S61','B_BOXES',['T2'],'Extreme close-up',
  "an extreme close-up of her son with the teal silicone spatula head just below his nose, held there by his mother's hand coming in from the edge of the frame (medium-deep brown skin, a gold wedding band, a lavender cardigan sleeve)",
  "He reluctantly sniffs once; his expression changes.",
  props=['sil'], start=0, hands_of='G2')
S('S62','B_BOXES',['T2'],'Close-up',
  "her son holding the teal silicone spatula, staring at it",
  "He lowers the teal spatula a few centimeters from his nose and stares at it as if seeing it for the first time, then says it, stunned and quiet, his eyes lifting to his mother off-frame on 'dish soap'; the spatula moves only with his hand.",
  props=['sil'], tone='stunned, quiet')
S('S63','B_BOXES',['G2'],'Medium shot',
  "the grandmother holding out one wooden ladle toward her son",
  "She holds the wooden ladle out toward her son off-frame and moves it a few centimeters closer to him on 'now Dorothy's', calm, testing him, a hint of a smile at the corner of her mouth on 'every day'; the ladle moves only with her hand and keeps its exact shape.",
  props=['aca'], tone='calm, testing him')
S('S64','B_BOXES',['T2'],'Close-up',
  "her son holding the wooden ladle in his own hand just below his nose",
  "He sniffs the wooden ladle once, frowns, sniffs again, then lowers it a little, shakes his head once and says it, reluctant but honest; after the line he glances at his mother off-frame, a little embarrassed.",
  props=['aca'], tone='reluctant, honest', start=1.0)
S('S65','B_BOXES',['G2'],'Close-up',
  "the grandmother in the kitchen, chin up",
  "She raises one finger on 'one sniff', then lowers her hand and says 'my nose is FINE' with her chin up, dry and proud; after the line a small, satisfied smile.",
  tone='dry, proud')
S('S66','B_BOXES',['G2','T2'],'Medium shot',
  "the grandmother holding the teal silicone spatula over the open step trash can by her son's feet, her foot on its pedal holding the lid open",
  "She lets the spatula drop into the trash can in the first second, then lifts her foot off the pedal and the lid falls shut with a bang; she says it to her son.",
  props=['sil'], tone='pointed, a little bitter', start=1.0)
S('S67','B_BOXES',['T2'],'Close-up',
  "her son in the kitchen, looking away from his mother",
  "He swallows and shifts his weight, still not meeting her eyes, and says 'smelling's one thing, Mama' defensively; on 'tasting's another' he turns his head back to her and lifts his chin, making his last stand.",
  tone='defensive, last stand', start=0.8)
S('S68','B_BOXES',['G2'],'Close-up',
  "the grandmother in the kitchen, very composed",
  "She folds her arms in the first second and lays out each word to her son off-frame, measured and in charge, with a small nod on 'Friday night' and another on 'everybody comes'.",
  tone='measured, one word at a time')
S('S69','B_BOXES',['G2'],'Extreme close-up',
  "an extreme close-up of the grandmother's eyes, unblinking, looking off to one side at her son",
  "Her eyes stay locked on her son without blinking while she says it; her brows draw down a little on 'never say a word' and the skin around her eyes tightens, steady and absolute.",
  tone='steady, absolute')
S('S70','B_BOXES',['T2'],'Close-up',
  "her son in the kitchen, meeting her gaze",
  "He holds her gaze for a beat in the first second, then gives one firm nod and says it quietly, his jaw set; after the line he glances down at the counter and back up at her.",
  tone='quiet, accepting the bet', start=1.0)
S('S71','A_FRI',['G3','T3','J2','W','B'],'Wide shot',
  "Friday night in the dining room with no balloons, moving boxes stacked in the hallway seen through the archway; the same Black American family in the same seats as at the birthday; the grandmother at the head of the table setting down the potato salad bowl, a wooden serving spoon in her other hand; at the edge of the frame only the boy's small hands and blue hoodie sleeves rest on the table",
  "She sets the bowl down in the first second; everyone at the table watches her.",
  props=['dish','aca','bottle'], start=0, amb='only a wall clock ticking')
S('S72','A_FRI',['G3','J2'],'Medium shot',
  "the grandmother serving a spoonful of potato salad onto her granddaughter's plate with the wooden serving spoon",
  "She finishes setting the spoonful on the plate in the first second, looks her granddaughter straight in the eye and says it.",
  props=['dish','aca'], tone='steady, loving, a challenge', start=1.0)
S('S73','A_FRI',['J2','T3'],'Close-up',
  "the granddaughter in her green sweater with a forkful of potato salad at her lips; her father soft in the background, holding his breath",
  "She takes the bite; she chews; her father in the background doesn't move.", start=0,
  amb='only a wall clock ticking')
S('S74','A_FRI',['J2'],'Close-up',
  "the granddaughter mid-chew, eyes going wide",
  "She stops chewing, eyes wide, and says it.",
  tone='amazed, quiet')
S('S75','A_FRI',['J2'],'Close-up',
  "the granddaughter breaking into a laugh, eyes wet",
  "She breaks into a laugh, eyes wet, one hand pressed to her chest, and says it bursting with relief and joy, her shoulders shaking; on 'NONE' she opens her hand toward her grandmother off-frame.",
  tone='bursting with relief and joy')
S('S76','A_FRI',['T3'],'Close-up',
  "her son in a plaid shirt with a forkful at his mouth",
  "He takes the bite, chews, taking his time, puts his fork down in the second half; his eyes redden.",
  start=0)
S('S77','A_FRI',['T3'],'Close-up',
  "her son at the table, eyes red",
  "He looks up at his mother off-frame, his eyes filling, and reaches one hand across the table toward her as he says 'Mama'; on 'I'm so sorry' his voice breaks and he shakes his head a little, ashamed; after the line he presses his lips together, his eyes still on her.",
  tone='voice breaking, real apology')
S('S78','A_FRI',['T3'],'Medium shot',
  "her son in the hallway by the stacked moving boxes, holding the glossy brochure in both hands",
  "In the first second he tears the brochure in half in one motion, then lowers the halves.",
  props=['bro'], start=0,
  lock_extra="The brochure is the only thing that changes: it tears once into two halves along one clean line; nothing else changes.")
S('S79','A_FRI',['G3'],'Close-up',
  "the grandmother at the head of the table, half laughing, half crying",
  "Half laughing, half crying, she gives the order with a wet smile, pointing at her son off-frame on 'Terrance'; after the line she wipes under one eye with her fingertip and shakes her head at him, still smiling.",
  tone='half laughing, half crying, an order')
S('S80','A_FRI',['J2'],'Medium shot',
  "the granddaughter holding her plate out toward her grandmother, mouth closed, grinning",
  "She holds her plate out toward her grandmother off-frame and gives it a little lift with a big grin and raised eyebrows, saying it playfully; after the line she bounces a little in her chair, grinning.",
  tone='playful, happy')
S('S81','A_FRI',['T3','J2','G3','W','B'],'Wide shot',
  "the Black American family laughing and talking around the table, the grandmother in her place at the head of the table; the son holds the wooden serving spoon over his daughter's plate; on the sideboard sits a red-and-white checkered towel with a few wooden utensils on it; at the edge of the frame only the boy's small hands and blue hoodie sleeves rest on the table",
  "The son serves his daughter seconds in the first second; the table keeps laughing and talking.",
  props=['dish','aca','towel','bottle'], start=0, amb='the family laughing softly, cutlery')
S('S82','B_CLEAR',['G4'],'Medium shot',
  "weeks later in the clean kitchen, no boxes, the round wooden utensil holder with the wooden set on the counter; the grandmother in a soft blue cardigan holds up one leftover teal silicone ladle",
  "For the first time she turns her head and looks straight into the lens in the first second, as if letting the viewer in on a secret, and says it with a dry, mischievous smile; on 'over THIS' she lifts the teal silicone ladle a little higher and raises her eyebrows at it. The ladle moves only with her hand; the wooden set in the holder stays exactly in place.",
  props=['sil','aca','hold'], tone='warm, dry, a little mischievous', cam='to')
S('S83','B_CLEAR',['G4'],'Close-up',
  "the grandmother in the clean kitchen looking straight into the lens",
  "She leans a little closer to the lens in the first second, like sharing advice with a friend across the counter, and says it warm and knowing; after the line she taps the side of her nose once with one finger and gives a small, knowing nod.",
  tone='warm, knowing, like advice to a friend', cam='to')
S('S84','B_CLEAR',['G4'],'Medium shot',
  "the grandmother holding the teal silicone ladle over the open step trash can, her foot on its pedal holding the lid open, looking into the lens",
  "She lets the ladle drop into the trash can in the first second, then lifts her foot off the pedal and the lid falls shut with a bang; she says it to the viewer.",
  props=['sil','aca','hold'], tone='dry humor', cam='to', start=1.0)
S('S85','B_CLEAR',['G4','T4'],'Close-up',
  "the grandmother in the clean kitchen looking into the lens; in the soft background her son in a navy sweater tastes from a pot simmering on a lit burner with a wooden spoon",
  "She glances over her shoulder at her son, who nods while tasting, then looks back into the lens and says it, warm, with a gentle warning: one eyebrow lifts on 'smell HERS' and she raises one finger on 'before you blame her', smiling.",
  props=['aca'], tone='warm, a gentle warning', cam='to', start=0.8)
S('S86','B_CLEAR',['G4'],'Medium shot',
  "the grandmother standing beside the round wooden utensil holder on the counter, holding up the wooden ladle, looking into the lens",
  "She lifts the wooden ladle a little higher toward the lens with a proud smile on 'Mine are Acawood now', then opens her free hand toward the full set in the round holder on 'seven pieces' and says the rest, proud and clear. The ladle moves only with her hand; every wooden piece in the holder stays exactly in place.",
  props=['aca','hold'], tone='proud, clear', cam='to')
S('S87','B_CLEAR',[],'Insert close-up',
  "a wooden ladle standing in a clear glass container of hot, steaming water on the kitchen counter; the water completely clear with no color at all; the container, water and light exactly as in the real test frame",
  "The ladle stands still in the water; steam rises gently; the water stays completely clear, no color at all, the whole time.",
  props=['aca','water'], start=0, amb='hot water softly bubbling')
S('S88','B_CLEAR',['G4'],'Medium shot',
  "the grandmother at the kitchen sink seen from the waist up, drying the wooden ladle with a plain cream kitchen towel, the round wooden holder beside her on the counter",
  "She finishes drying the ladle and stands it in the round holder in the first two seconds, then lets go.",
  props=['aca','hold'], start=0, amb='a short splash of tap water, wood touching the holder')
S('S89','B_CLEAR',['G4'],'Medium shot',
  "the grandmother in the clean kitchen, one hand resting on the round wooden holder full of utensils, looking into the lens",
  "Her hand rests on the holder; she leans in a little toward the lens in the first second and says it plain and friendly, with an easy open-hand gesture of her free hand on 'free shipping in the U.S.' and a warm nod on 'ninety-day returns'. The holder and every wooden piece stay exactly in place.",
  props=['aca','hold'], tone='plain, friendly, no hype', cam='to')
S('S90','B_CLEAR',['G4'],'Close-up',
  "the grandmother in the clean kitchen smiling into the lens",
  "She smiles, points down with one finger, and says it.",
  tone='warm, triumphant', cam='to')
