# Pre-flight review brief: S14c "We Talked About This" (Black family, Acawood ad)

You are reviewing prompts BEFORE they are run, so the producer (Nam) does not have to redo work. Every frame he runs costs his time; every
video clip costs credits. Your job: find every place where the image model (Nano Banana Pro) or the video model (Omni, start frame +
lip-sync) will most likely produce something wrong, and say exactly how to fix the prompt text. Be adversarial and concrete. Do not report
style preferences or rewrites that only "sound better".

## How the pipeline works

- Frame node `P_F_<shot>` (image prompt) + reference images "Image 1..n" (listed in order in the packet) -> `S14c_F_<shot>`, 4 variants, Nam picks 1.
- Clip node `P_V_<shot>` (video prompt) starts from the chosen frame (frame_1 only) and acts the line with lip-sync. Video costs credits.
- Dining-room frames (birthday `A_BDAY`, Friday `A_FRI`) are EDITS of the chosen master photo (Image 1 = the whole dinner seen from the main
  camera at the foot of the table); a frame only "zooms in" from that same camera and changes actions/expressions. `_H2` variants are the same
  shots seen straight on from across the table, with Image 1 = an empty plate of the wall with the framed family photos.
- Every other frame uses an empty room plate as Image 1 with "keep the background exactly as in Image 1".
- Character sheets (Image 2..n) are only for faces, skin, hair, clothes.

## Reference files (read what you need)

- Script (Vietnamese + English, the source of truth for story, lines, props): `/tmp/claude-0/-home-user-xxx/e5c1abfe-6111-5fb9-a4c0-c254e1c997e7/scratchpad/review/script_docx.txt`
- Characters, outfits per day: `/home/user/xxx/output/s14c-black-tobyflow-20261021/S14c_Black_NhanVat.md`
- Producer guide (scene list, seat chart, decisions): `/home/user/xxx/output/s14c-black-tobyflow-20261021/S14c_Black_TobyFlow.md`
- Producer's rules learned the hard way: `/home/user/xxx/references/toby-flow-rules-nam.md`
- Seat chart image: `/home/user/xxx/output/s14c-black-tobyflow-20261021/S14c_SoDoChoNgoi.png`; dining room, 4 walls and what is behind every chair:
  `/home/user/xxx/output/s14c-black-tobyflow-20261021/S14c_PhongAn_4Huong.png`
- The chosen images (look at them): master birthday dinner `/tmp/claude-0/-home-user-xxx/e5c1abfe-6111-5fb9-a4c0-c254e1c997e7/images/13.jpg`;
  empty dining room from the foot `.../images/14.jpg`; window wall `.../images/15.jpg`; view from the head toward the living room `.../images/16.jpg`;
  photo wall (the `_H2` plate) `.../images/17.jpg`; morning kitchen plate before its relight edit
  `/tmp/claude-0/-home-user-xxx/e5c1abfe-6111-5fb9-a4c0-c254e1c997e7/scratchpad/bgimgs/bg5.jpeg` (the other kitchen states are edits of it).
- Room and setup prompts: `/tmp/claude-0/-home-user-xxx/e5c1abfe-6111-5fb9-a4c0-c254e1c997e7/scratchpad/s14/review_pk/setup_prompts.md`

Dining room facts (from the chosen images): main camera at the foot of the table looks at the head wall. Head wall, left to right: archway to the
hallway, small framed picture, carved wooden fork and spoon, Gloria's chair centred, sideboard on the right with the gift bags, banner above it, gold
71 balloons. Seats: photo-wall side (screen-left from the main camera): Terrance next to the head, then Jada, then the aunt nearest the foot; other
side: Terrance's wife next to the head, then the boy (only his hand and striped sleeve may show, never his face), then the uncle; foot chair empty.
Exactly seven people at both dinners. Birthday gifts only on the sideboard; no cake yet.

## Failure classes already seen in this project (look for every instance)

1. A person visible in the frame (even soft, at an edge, in the foreground) without a character sheet and description -> drawn as a stranger
   (S05 came out with strangers at the table).
2. The described camera direction differs from Image 1 while the prompt says "keep the background exactly as in Image 1" -> the model keeps
   Image 1's wall (close-ups "from across the table" came out with the banner wall behind Jada, as if she sat at the head).
3. A location given by a person or their chair ("beyond his wife's chair") pulls that person into the frame.
4. A person who is only looked at or spoken to must be stated as "just out of the frame", or the model adds them somewhere.
5. Talking clip whose speaker's lips are covered (hand, fork, cup, bowl) or whose speaker faces away / is out of frame in the start frame.
6. Seat or side mistakes: beside vs across, screen-left vs screen-right, the order Terrance-Jada-aunt.
7. Prop continuity across shots: brochure route (under the gold gift bag B-1/S04, in Gloria's hands S05/S07/S08, on the night counter S16,
   hallway on Friday D-2/S78); gift bags only on the sideboard; potato salad bowl route; Jada's pink tumbler only where listed; the red-white towel;
   exactly 7 wooden utensils in the set; teal silicone utensils in their white crock until replaced; the step trash can; new soap and sponge.
8. Outfits wrong for the day/scene (sheet numbers per scene in the character file).
9. Child faces (never), photos on walls/fridge must be this Black family, adults only; "glasses" only for Gloria and Dorothy; no stereotype gestures.
10. Unintended lettering, logos, subtitles; brand marks on boxes.
11. Clip vs frame: the clip's first second does not start from what the frame shows; the clip needs an object/person that is not in the frame;
    someone enters from nowhere; objects move on their own; the line is spoken by someone not visible.
12. Physics: impossible holds, steam without heat, a lid open without the pedal, a hand count, a held object changing.
13. Light and time of day: night vs morning vs daylight must match the scene; night kitchen lit only by the range hood but faces readable.

Also flag anything the script requires that the prompts miss or contradict (wrong line, wrong emotion, wrong action, wrong order).

## Output

Write your findings to the file named in your task, as a markdown table:
`| node | severity | what will go wrong | evidence (quote the prompt) | exact fix (text to add/replace) |`
Severity: **blocker** (very likely wrong frame/clip: stranger, wrong wall/room, wrong person, covered lips on a talking clip, story contradiction),
**likely** (real risk worth fixing now), **minor** (cheap polish). Only include issues you checked against the prompt text and the references.
Then reply with a short summary: counts by severity and the 5 most important findings. Do not edit any project files.
