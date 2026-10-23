import json,re,collections
from build14 import FORBID, HOLD_POSE, FOOD_ACA, SKIN_TONE, SKIN_TONE_FRAME, CH, PEOPLE_LOCK  # rebuild deterministic
wf=json.load(open('out/workflow_S14c_Black.json'))['workflow']
N=wf['nodes'];E=wf['edges'];byid={n['node_id']:n for n in N}
err=[]
# ids/slug
c=collections.Counter(n['slug'] for n in N); err+=[f'dup slug {k}' for k,v in c.items() if v>1]
c=collections.Counter(n['node_id'] for n in N); err+=[f'dup id {k}' for k,v in c.items() if v>1]
for e in E:
    if len(e)!=8: err.append('edge fields '+e['edge_id'])
    if e['source_node_id'] not in byid or e['target_node_id'] not in byid: err.append('dangling '+e['edge_id'])
inc=collections.defaultdict(list)
for e in E: inc[e['target_node_id']].append(e)
for n in N:
    if n.get('media_type')=='Image' and n.get('quantity')!=4: err.append('qty x4 '+n['node_name'])
    if n.get('media_type')=='Video' and n.get('quantity')!=2: err.append('qty x2 '+n['node_name'])
    if n.get('media_type')=='Video':
        f1=[e for e in inc[n['node_id']] if e['target_port']=='frame_1']
        if len(f1)!=1 or f1[0]['source_node_id']!=n['frame_1_source']: err.append('frame1 '+n['node_name'])
        t=[e for e in inc[n['node_id']] if e['target_port']=='text']
        if len(t)!=1: err.append('vtext '+n['node_name'])
        p=byid[t[0]['source_node_id']]['prompt']
        if not p.startswith(re.match(r'^[^,]+',p).group(0)) or f", {n['video_duration'].rstrip('s')} seconds," not in p or not re.fullmatch(r'(4|6|8|10)s', n['video_duration']) or n.get('download_resolution')!='1080p' : err.append('dur text '+n['node_name'])
        for k in ('Action:','Physics:','Living layer','Object lock'):
            if k not in p: err.append(f'{k} missing '+n['node_name'])
        if n['video_download_resolution']!='1080p': err.append('1080 '+n['node_name'])
        f2=[e for e in inc[n['node_id']] if e['target_port']=='frame_2']
        talk=n['node_name'].startswith('S14c_T_'); sid=[r['id'] for r in json.load(open('out/_rows.json'))['rows'] if r['clip']==n['node_name']][0]
        want=talk and sid in HOLD_POSE
        if want!=bool(n.get('frame_2_source')) or len(f2)!=int(want): err.append('frame2 '+n['node_name'])
        if f2 and (f2[0]['source_node_id']!=n['frame_2_source'] or n['frame_2_source']!=n['frame_1_source'] or f2[0]['target_handle']!='input_4'): err.append('frame2 src '+n['node_name'])
        if 'Living layer (only what is already in the frame moves, nothing is added)' not in p: err.append('living form '+n['node_name'])
        if 'nothing moves on its own' not in p: err.append('phys logic '+n['node_name'])
        if 'the main action starts within the first second' not in p: err.append('first second '+n['node_name'])
        if talk and ('lips close and stay closed, no sound' not in p or 'Face and body:' not in p or 'never over-acted' not in p): err.append('talk blocks '+n['node_name'])
        if re.search(r'\bwag|neck roll|rolls? (her|his) eyes|hands? on (her|his) hips?|sassy|snaps? (her|his) fingers', p): err.append('stereotype gesture '+n['node_name'])
        act = re.search(r'Action: (.*?) Living layer', p).group(1)
        if talk and (re.search(r'(stays|keeps) (\w+ )?still', act) or 'same grip, length and angle' in p): err.append('hold-pose wording '+n['node_name'])
    if n.get('media_type')=='Image':
        t=[e for e in inc[n['node_id']] if e['target_port']=='text']
        if len(t)!=1: err.append('itext '+n['node_name'])
        p=byid[t[0]['source_node_id']]['prompt']
        refs=[e for e in inc[n['node_id']] if e['target_port']=='image_ref']
        mx=max([int(x) for x in re.findall(r'Image (\d+)',p)] or [0])
        if mx!=len(refs): err.append(f'ref count {n["node_name"]} prompt {mx} edges {len(refs)}')
        if 'IMG_ACA' in ' '.join(byid[e['source_node_id']]['node_name'] for e in refs) and n['node_name'].startswith('S14c_F') and 'Lighting match' not in p: err.append('lightmatch '+n['node_name'])
    if n['node_type']=='download':
        s=[e for e in inc[n['node_id']]]
        if len(s)!=1 or s[0]['target_port']!='media_in' or s[0]['data_type']!='video': err.append('tai '+n['node_name'])
for n in N:
    if n['node_type']=='prompt':
        low=' '+n['prompt'].lower().replace('over-sharpening','')+' '
        for w in FORBID:
            if w in low: err.append(f'forbid "{w}" in {n["node_name"]}')
        if 'WRENFIELD' in n['prompt'] or 'HAPPY 71ST' in n['prompt']:
            if 'no on-screen text' in n['prompt'] or 'no logos' in n['prompt'].replace('No other text, no logos','') : err.append('text kill '+n['node_name'])
# timing + lines
rows=json.load(open('out/_rows.json'))['rows']
src={s['id']:s for s in json.load(open('shots.json'))}
for r in rows:
    if r['kind']=='T':
        if r['end']+0.6>r['dur']: err.append('timing '+r['id'])
        if r['dur']>10: err.append('long '+r['id'])
# all lines covered
spoken={r['txt'] for r in rows if r['txt']}
for sid,s in src.items():
    m=re.match(r'^([A-Z]+)(?: \([^)]*\))?: (.*)$',s['line'])
    if m and m.group(2) not in spoken and sid not in ('D-1',): err.append('line missing '+sid)
# srt == lines
srt=open('out/S14c_Black_H1.srt').read()
for sid,s in src.items():
    if sid.startswith('S'):
        m=re.match(r'^([A-Z]+)(?: \([^)]*\))?: (.*)$',s['line'])
        if m and m.group(2).upper() not in srt: err.append('srt '+sid)
# policy / realism / food rules learned from Nam's chats
POLICY=['from behind','back to the','missing finger','extra finger','extra hand','third hand','woman shopper','not horror','toxic','poison']
REAL=['8k','ultra detailed','hyperrealistic','masterpiece','pristine','flawless','beautiful','perfect','smooth']
FOODW=r'potato|salad|tast|serv|spoonful|\bpot\b'
for n in N:
    if n['node_type']!='prompt': continue
    low=n['prompt'].lower()
    for w in POLICY:
        if w in low: err.append(f'policy "{w}" in {n["node_name"]}')
    for w in REAL:
        if w in low: err.append(f'realism "{w}" in {n["node_name"]}')
    if FOOD_ACA in n['prompt'] and re.search(r'crumb|burnt|spill|splatter|dirty',low): err.append('food-aca dirty '+n['node_name'])
    if ('acacia' in low or 'wooden serving spoon' in low or 'wooden spoon' in low) and re.search(FOODW,low) and n['node_name'].startswith(('P_F_','P_V_')):
        sid=n['node_name'][4:]
        from data14 import SH
        sh=[x for x in SH if x['id']==sid]
        if sh and 'aca' in sh[0]['props'] and re.search(FOODW,sh[0]['frame']+' '+sh[0]['action']) and FOOD_ACA not in n['prompt']: err.append('food-aca missing '+n['node_name'])
# characters: identity in every sheet, no glasses leaking onto people who wear none, brown-skin block, People lock
from data14 import SH as _SH
_sh={x['id']:x for x in _SH}
byname={n['node_name']:n for n in N}
for k,c in CH.items():
    if k=='B': continue
    pn=byname['P_'+c['sheet']]['prompt']
    if 'Black American' not in pn or SKIN_TONE not in pn: err.append('sheet identity '+c['sheet'])
    if c['full'] not in pn: err.append('sheet full text '+c['sheet'])
    if k[0] in 'TJW' or k=='FD':
        if 'glasses' in pn.lower(): err.append('glasses leak '+c['sheet'])
for sid,x in _sh.items():
    pf=byname.get('P_F_'+sid)
    if not pf: continue
    pl=pf['prompt'].lower(); who=set(c[0] for c in x['chars'])
    if re.search(r'(?<!drinking )\bglasses\b', pl) and not (who & {'G','D'}): err.append('glasses leak frame '+sid)
    if (x['chars'] and SKIN_TONE_FRAME not in pf['prompt']) or (x['hands_of'] and 'palms lighter than the backs of the hands' not in pf['prompt']): err.append('skin block '+sid)
    pv=byname['P_V_'+sid]['prompt']
    if x['chars'] and PEOPLE_LOCK not in pv: err.append('people lock '+sid)
from build14 import BOTTLE
if 'church hat' not in byname['P_CS_DOROTHY']['prompt']: err.append('dorothy hat sheet')
for sid,x in _sh.items():
    pf=byname.get('P_F_'+sid)
    if not pf: continue
    hasD='D' in x['chars']
    if hasD != ('church hat' in pf['prompt']): err.append('hat '+sid)
    if ('bottle' in x['props']) != (BOTTLE in pf['prompt']) or ('bottle' not in x['props'] and 'tumbler' in pf['prompt']): err.append('bottle '+sid)
# rooms and photos: every photo shows this Black family; room states are edits of one base image; no unnamed people at the table
from build14 import BG_EDIT, WALL_PHOTOS, FRIDGE_PHOTOS, CHURCH_FAN, TABLE_FOOD
for n in N:
    if n['node_type']!='prompt': continue
    pl=n['prompt']
    if re.search(r'family and graduation photos|family photos on the fridge', pl): err.append('generic photos '+n['node_name'])

if WALL_PHOTOS not in byname['P_BG_A_BDAY']['prompt']: err.append('wall photos')
for k in ('B_MORNING',):
    if FRIDGE_PHOTOS not in byname['P_BG_'+k]['prompt'] or CHURCH_FAN not in byname['P_BG_'+k]['prompt']: err.append('kitchen decor '+k)
from build14 import SEATS, GUESTS, PART_VIEW, GIFTS, GIFTS_MASTER, FRI_SIDEBOARD, FRI_SIDEBOARD_SOFT, NO_CAKE, OFF_SIDEBOARD, WIFE_WEAR, MASTER_PROMPT, aunt, uncle
from build14 import HALLWAY
def is_dinner(x): return x['bg'] in ('A_BDAY','A_FRI') and bool(x['chars']) and x['id'] not in HALLWAY
for sid,x in _sh.items():
    pf=byname.get('P_F_'+sid)
    if not pf: continue
    p=pf['prompt']
    if is_dinner(x):
        f=byname['S14c_F_'+sid]
        srcs=[byid[e['source_node_id']]['node_name'] for e in inc[f['node_id']] if e['target_port']=='image_ref']
        if {'A_BDAY':'MASTER_A_BDAY','A_FRI':'MASTER_A_FRI'}[x['bg']] not in srcs: err.append('dinner ref '+sid)
        wide=x['shot']=='Wide shot'
        if wide and not all(b in p for b in (SEATS, GUESTS, aunt(x['bg']), uncle(x['bg']))): err.append('seat plan '+sid)
        if not wide and PART_VIEW not in p: err.append('part view '+sid)
        if wide and f"framing as Image {srcs.index({'A_BDAY':'MASTER_A_BDAY','A_FRI':'MASTER_A_FRI'}[x['bg']])+1}" not in p: err.append('main camera '+sid)
        if 'W' in x['chars'] and WIFE_WEAR[x['bg']] not in p: err.append('wife outfit '+sid)
        if x['bg']=='A_BDAY' and 'table' in x['frame'] and NO_CAKE not in p: err.append('no cake '+sid)
        side=bool(re.search(r'gift|sideboard', x['frame'])) and OFF_SIDEBOARD not in x['frame']
        if x['bg']=='A_FRI' and (wide or side) and (FRI_SIDEBOARD if 'aca' in x['props'] else FRI_SIDEBOARD_SOFT) not in p: err.append('friday sideboard '+sid)
        if 'wooden utensils' in p and 'aca' not in x['props'] and 'soft and out of focus' not in p: err.append('wood without product ref '+sid)
        if OFF_SIDEBOARD in x['frame'] and (GIFTS in p or FRI_SIDEBOARD in p or FRI_SIDEBOARD_SOFT in p): err.append('sideboard block off-frame '+sid)
        if re.search(r'behind (him|her), soft, the (gold 71 balloons|corner of the sideboard)', x['frame']): err.append('head of room behind speaker '+sid)
    elif re.search(r'\b(family|whole (birthday )?table|everyone at|relatives|guests)\b', x['frame']) and 'Black American' not in x['frame']: err.append('unnamed people '+sid)
    want_g = x['gifts'] if x['gifts'] is not None else bool(re.search(r'gift|sideboard', x['frame']) and OFF_SIDEBOARD not in x['frame'])
    if x['bg']=='A_BDAY' and (want_g or x['shot']=='Wide shot') != (GIFTS in p): err.append('gifts '+sid)
    if 'D' in x['chars'] and 'tote bag on the swing' in x['frame'] and 'on her shoulder' in p: err.append('two tote bags '+sid)
    if x['bg'] not in ('A_BDAY','A_FRI') and re.search(r'wall with the archway|fork and spoon on the wall', x['frame']): err.append('room side mixed up '+sid)
    if x['bg'] in ('A_BDAY','A_FRI') and re.search(r'in front of the sideboard|behind it the grandmother|across the table toward (her|his) (mother|grandmother)|sideboard behind', x['frame']+' '+x['action']+' '+p): err.append('sideboard / head position '+sid)
    if x['chars'] and f"Expressions true to this moment: {x['face']};" not in p: err.append('face line '+sid)
    if re.search(r'nobody smiles|no smile', x['face']) and re.search(r'\bsmil|\bgrin|laugh', x['frame'] + ' ' + x['action']) and not re.search(r'smile (fades|freezes|falter)|smile still|still smiling|hostess smile', x['frame'] + ' ' + x['action']): err.append('smile in a no-smile beat '+sid)
    if re.search(r'angr|rage|furious|disgust', x['face']) and not re.search(r'not (angry|raging)|never disgusted|not angry', x['face']): err.append('face tone '+sid)
    if 'full set in the round holder' in x['action'] and 'holding' in x['frame']: err.append('eight pieces '+sid)
    if '{MASTER}' in p or 'framing as :' in p or ('main camera' in x['frame'] and not re.search(r'framing as Image \d', p)) or re.search(r'\bcake\b', p.replace(NO_CAKE, '')): err.append('master/cake text '+sid)
    if x['bg'] in ('A_BDAY','A_FRI') and x['chars'] and not is_dinner(x) and 'hallway' not in x['frame']: err.append('dinner flag '+sid)
    if ('bro' in x['props']) != (sid in ('B-1','S04','S05','S07','S08','S16','D-2','S78')): err.append('brochure place '+sid)
for b in (SEATS, GUESTS, GIFTS_MASTER, NO_CAKE, aunt('A_BDAY'), uncle('A_BDAY')):
    if b not in MASTER_PROMPT: err.append('master block')
m=byname['MASTER_A_BDAY']
if [byid[e['source_node_id']]['node_name'] for e in inc[m['node_id']] if e['target_port']=='image_ref']!=['BG_A_BDAY','CS_GLORIA_1','CS_TERRANCE_1','CS_JADA_1','CS_WIFE']: err.append('master refs')
if 'no brochure in this frame' not in _sh['S06']['frame']: err.append('S06 brochure')
for k,(base,_,_,_) in BG_EDIT.items():
    im=byname['BG_'+k]
    srcs=[byid[e['source_node_id']]['node_name'] for e in inc[im['node_id']] if e['target_port']=='image_ref']
    if not srcs or srcs[0]!='BG_'+base: err.append('bg edit ref '+k)
for sid,x in _sh.items():
    pf=byname.get('P_F_'+sid)
    if pf and is_dinner(x) and 'table' in x['frame'] and TABLE_FOOD not in pf['prompt']: err.append('table food '+sid)
# physical causes and continuity added in the final review
from build14 import KEEP_DINING, KITCHEN
if 'sideboard' not in KEEP_DINING or 'trash can' not in KITCHEN: err.append('room keep list')
for sid,x in _sh.items():
    t=x['frame']+' '+x['action']
    if re.search(r'\blid\b', t) and 'pedal' not in t: err.append('lid without cause '+sid)
    if re.search(r'steam|simmer|sizzl', t) and not re.search(r'lit burner|boiling|just-boiled|hot|warm', t): err.append('steam without heat '+sid)
    pf=byname.get('P_F_'+sid)
    if pf and x['bg_ref'] and x['bg_ref'].split('{n}')[0] not in pf['prompt']: err.append('bg_ref '+sid)
for n in N:
    if n['node_type']=='prompt' and re.search(r'moving box', n['prompt']) and 'unprinted and unlabeled, with no brand marks' not in n['prompt'] and 'no boxes' not in n['prompt']: err.append('box logos '+n['node_name'])
# light (Nam 23/10, "quá tối"): kitchen frames state the brightness and the faces; the 0B kitchen edits name their new light, the night one never pitch black
from build14 import FRAME_LIGHT
for sid,x in _sh.items():
    pf=byname.get('P_F_'+sid)
    if pf and x['bg'] in FRAME_LIGHT and FRAME_LIGHT[x['bg']] not in pf['prompt']: err.append('frame light '+sid)
for k,w in (('B_NIGHT','never pitch black'),('B_BOXES','bright, plain daytime light'),('B_CLEAR','bright, warm, even daylight')):
    if w not in byname['P_BG_'+k]['prompt'].split('Change only:')[1].split(' Look:')[0]: err.append('room light '+k)
# Nam 23/10 (F1 still mixed up): every dining-room frame is an edit of that day's chosen master photo (Image 1), from the same camera;
# the Friday master is an edit of the birthday master; a talking frame never covers the lips
from build14 import EDIT_KEEP, MASTER_OF
fm=byname['MASTER_A_FRI']
if [byid[e['source_node_id']]['node_name'] for e in inc[fm['node_id']] if e['target_port']=='image_ref']!=['MASTER_A_BDAY','CS_GLORIA_3','CS_TERRANCE_3','CS_JADA_2','CS_WIFE','IMG_ACA_SET']: err.append('friday master refs')
for sid,x in _sh.items():
    pf=byname.get('P_F_'+sid)
    if not pf: continue
    if x['bg'] in MASTER_OF and sid not in HALLWAY:
        fr=byname['S14c_F_'+sid]
        first=[byid[e['source_node_id']]['node_name'] for e in inc[fr['node_id']] if e['target_port']=='image_ref'][:1]
        if first!=[MASTER_OF[x['bg']]] or EDIT_KEEP not in pf['prompt'] or not x['frame'].startswith('the same '): err.append('master edit '+sid)
    if 'from across the' in pf['prompt']: err.append('old camera text '+sid)
    if x.get('kind')=='T' and re.search(r'hand[^;]*(beside|over|to|behind) her mouth', x['frame']) and 'lips in view' not in x['frame']: err.append('lips hidden '+sid)
# straight-on variants (F1b / F5b): Image 1 is the photo-wall plate, the day's master tells who sits where, the seat order and what is behind each person
from build14 import FRAME_H2, ACROSS_SEATS, SIDE_REF
for sid in FRAME_H2:
    x=_sh[sid]; pf=byname.get('P_F_'+sid+'_H2'); fr=byname.get('S14c_F_'+sid+'_H2')
    if not pf or not fr: err.append('alt missing '+sid); continue
    srcs=[byid[e['source_node_id']]['node_name'] for e in inc[fr['node_id']] if e['target_port']=='image_ref']
    if srcs[:1]!=['BG_A_WEST'] or {'A_BDAY':'MASTER_A_BDAY','A_FRI':'MASTER_A_FRI'}[x['bg']] not in srcs: err.append('alt refs '+sid)
    p=pf['prompt']
    if ACROSS_SEATS not in p or PART_VIEW not in p or f"Expressions true to this moment: {x['face']};" not in p or 'as in Image 1.' not in p: err.append('alt text '+sid)
    if re.search(r'balloons|banner|gift bag|archway', FRAME_H2[sid]): err.append('alt decor '+sid)
# Nam 23/10 (S05 came out with strangers at the table): anyone named as visible in a dinner frame has a sheet in that frame (chars or extra);
# a person only looked at or whose chair is mentioned is said to be out of the frame
from build14 import FRAME_H2 as _FH2
_WHO = {'T': r"\b(her|the) son\b(?!'s wife)|\bher father\b|\bhis father\b", 'J': r"\bthe granddaughter\b|\bhis daughter\b|\bher granddaughter\b",
        'W': r"\bthe son's wife\b|\bhis wife\b|wife's chair", 'G': r"\bthe grandmother\b|\bhis mother\b|\bher grandmother\b"}
for sid,x in _sh.items():
    if x['bg'] not in ('A_BDAY','A_FRI') or sid in HALLWAY: continue
    have={c[0] for c in x['chars']+x['extra']+x['edge']}
    for alt,txt in (('',x['frame']),('_H2',_FH2.get(sid))):
        if not txt: continue
        for clause in re.split(r';|\. ', txt):
            for k,rx in _WHO.items():
                if re.search(rx,clause) and not re.search(r"out of the frame|not in the room|empty|hidden|sleeve",clause) and k not in have: err.append(f'unsheeted {k} in '+sid+alt)
    for c in x['extra']:
        for nm in ('S14c_F_'+sid, 'S14c_F_'+sid+'_H2'):
            if nm in byname and CH[c]['sheet'] not in [byid[e['source_node_id']]['node_name'] for e in inc[byname[nm]['node_id']] if e['target_port']=='image_ref']: err.append('extra sheet '+nm)
# the standard room (0E, Nam 23/10): three empty views, each an edit of the 0A dining plate, with no people and no decorations
for v in ('BG_A_WEST','BG_A_EAST','BG_A_SOUTH'):
    im=byname[v]
    if [byid[e['source_node_id']]['node_name'] for e in inc[im['node_id']] if e['target_port']=='image_ref']!=['BG_A_BDAY']: err.append('view ref '+v)
    p=byname['P_'+v]['prompt']
    if 'No people' not in p or 'no birthday decorations in view' not in p: err.append('view text '+v)
# ---- pre-flight review 23/10 (five reviewers): one automatic check per failure class they found, so the same slip cannot come back ----
from build14 import (H2_TABLE, H2_END, BANNER_IF, COMP, COMP_TIGHT, ACA_FULL, LIVING_EMPTY, KREV, SIL_REF, VOICE, MASTER_FRI_PROMPT, FRAME_H2 as _H2)
_rows = {r['id']: r for r in json.load(open('out/_rows.json'))['rows']}
def _frame_refs(nm): return [byid[e['source_node_id']]['node_name'] for e in inc[byname[nm]['node_id']] if e['target_port'] == 'image_ref']
def _clauses(txt): return re.split(r';|\. ', txt)
COVER = [r'\bat (her|his) (lips|mouth)\b', r'just below (her|his) nose', r'behind (her|his) (hand|raised glass|glass)\b', r'(hand|fingers?|mug|cup|fork) (over|to) (her|his) mouth']
for sid, x in _sh.items():
    pf = byname.get('P_F_' + sid); pv = byname['P_V_' + sid]['prompt']
    talk = _rows[sid]['kind'] == 'T'
    texts = [('', x['frame'])] + ([('_H2', _H2[sid])] if sid in _H2 else [])
    # 1 lips: a talking frame or clip never covers the speaker's mouth (S21, S23, S32, S42, S64, A-1, S02_C)
    if talk:
        for alt, txt in texts + [('clip', x['action'])]:
            for cl in _clauses(txt):
                if any(re.search(r_, cl) for r_ in COVER) and not re.search(r'clear of|in view|mouth clear|stays clear', cl): err.append(f'lips covered {sid}{alt}')
    # 2 eyes-only extreme close-up on a talking clip (S17)
    if talk and x['shot'] == 'Extreme close-up' and re.search(r"\beyes\b", x['frame']) and not re.search(r'mouth|lips|chin|nose', x['frame']): err.append('no mouth in talking ECU ' + sid)
    # 3 a talking single in the kitchens and porches says where the listener is and which side (S09-S70)
    if talk and x['cam'] != 'to' and x['bg'] in ('B_NIGHT', 'B_MORNING', 'B_BOXES', 'D') and len(x['chars']) == 1:
        if 'out of the frame' not in x['frame']: err.append('listener not placed ' + sid)
        if x['bg'].startswith('B_') and not re.search(r'screen-(left|right)', x['frame']): err.append('no screen side ' + sid)
    # 4 Acawood count: a piece in a hand or out of the frame changes the count sentence (S86 came out with 8 pieces)
    if 'aca' in x['props'] and pf:
        one = re.search(r'\b(holds?|holding|in (her|his) (own )?hands?)\b[^;]*\bwooden\b|\bwooden (ladle|spoon|serving spoon)\b|mixing spoon from the set|serving spoon from the set', x['frame'])
        if one and not x['aca_count']: err.append('aca count ' + sid)
        if x['aca_count'] and (ACA_FULL in pf['prompt'] or 'shapes, number,' in pf['prompt']): err.append('aca full set text ' + sid)
    # 5 the hallway and the kitchen seen from the other end use the right plate (S78 in the empty dining room; S10 doorway; S85 stove behind her)
    if sid in HALLWAY and 'use it only for' not in (x['bg_ref'] or ''): err.append('hallway plate ' + sid)
    if x['bg'] in ('B_NIGHT', 'B_CLEAR') and re.search(r'doorway|behind her over her shoulder', x['frame']) and not x['plate']: err.append('reverse plate ' + sid)
    if x['plate'] and pf and _frame_refs('S14c_F_' + sid)[0] != x['plate']: err.append('plate ref ' + sid)
    # 6 lettering: the banner line only where the banner can be; the photo wall has none (review A)
    if pf:
        p = pf['prompt']
        if 'the banner lettering in the background stays' in p and not (x['bg'] == 'A_BDAY' and x['shot'] == 'Wide shot'): err.append('banner line ' + sid)
        if x['bg'] == 'A_BDAY' and x['shot'] != 'Wide shot' and not x['end_f'] and BANNER_IF not in p: err.append('banner if ' + sid)
        # 7 headroom under the hook banner (docx part 4)
        if x['chars'] and not (x['comp'] or COMP in p or COMP_TIGHT in p): err.append('composition ' + sid)
        # 8 a no-people frame never invites a person in the clip
        if not (x['chars'] or x['hands_of']) and re.search(r'anyone|breathes', pv.split('Living layer')[1].split('.')[0]): err.append('living invites people ' + sid)
        # 9 the brochure title: drawn and kept (text on object), or turned away / left blank
        if 'bro' in x['props'] and not (x['text_on_object'] or x['bro_ref']): err.append('brochure title ' + sid)
        # 10 the old generic silicone line pulled the muffin pan and a second crock into spatula shots
        if 'sil' in x['props'] and 'use it only for their shape and teal color.' in p: err.append('silicone ref ' + sid)
        # 11 a granddaughter zoom from the foot camera shows the aunt at the edge (strangers in S05)
        if x['bg'] in MASTER_OF and sid not in HALLWAY and re.search(r'zoomed in (close )?on the granddaughter', x['frame']) and 'the aunt' not in x['frame']: err.append('aunt edge ' + sid)
        # 12 hands at the edge: only the ring that person wears
        if x['hands_of'] and 'sleeves and rings' in p: err.append('rings ' + sid)
    if sid in _H2:
        ph = byname['P_F_' + sid + '_H2']['prompt']
        if H2_TABLE not in ph or not ph.endswith(H2_END): err.append('H2 table/banner ' + sid)
    # 13 a talking clip starts its line 1 s after an action that comes first (Nam's timing rule)
    if talk and re.search(r'in the first (half )?second', x['action']) and x['start'] < 1.0: err.append('line during action ' + sid)
    # 14 the steady-breath voice never carries a shaking, whispered or crying line
    if talk and _rows[sid]['spk'] == 'GLORIA' and re.search(r'whisper|shak|trembl|crack|catch|frighten|crying|breath', x['tone']) and not x['voice_free']: err.append('voice block ' + sid)
    # 15 to camera: the frame already looks into the lens; sound effects stay in CapCut
    if x['cam'] == 'to' and re.search(r'turns her head and looks straight into the lens', x['action']): err.append('to-camera turn ' + sid)
    if talk and re.search(r'with a bang', x['action']): err.append('bang on a talking clip ' + sid)
    # 16 old hands holding a utensil in a close-up get blocked: no other person's hand holds a prop at the speaker's face
    if x['hands_of'] and x['hands_of'][0] in 'GD' and x['shot'] in ('Close-up', 'Extreme close-up', 'Medium close-up'): err.append('old hand close-up ' + sid)
# 17 setup: the Friday master keeps no centerpiece and gets the real product photo; the kitchen plates seen from the sink end exist
if 'the flower centerpiece and the chairs' in MASTER_FRI_PROMPT or 'no flower centerpiece' not in MASTER_FRI_PROMPT: err.append('friday master centerpiece')
for k, (state, _, _) in KREV.items():
    if 'BG_' + k not in byname or _frame_refs('BG_' + k) != ['BG_B_MORNING', 'BG_' + state]: err.append('reverse plate node ' + k)
if 'no teal spatula' not in byname['P_BG_B_BOXES']['prompt']: err.append('boxes crock spatula')
# ---- Nam's chosen plates, 23/10 (18-22.jpg): the relit kitchen lost its range, the other states had no trash can, the porch table stood in front ----
from build14 import KITCHEN_FIXED
_a2 = [n['prompt'] for n in json.load(open('out/fix/workflow_S14c_0A2_SuaBepSang.json'))['workflow']['nodes'] if n['node_type'] == 'prompt'][0]
if not ('is not removed, moved, covered or replaced' in _a2 and 'near the fridge' in _a2 and 'foot pedal clearly visible' in _a2): err.append('0A2 range / trash can')
for k in ('B_NIGHT', 'B_BOXES', 'B_CLEAR'):
    if KITCHEN_FIXED not in byname['P_BG_' + k]['prompt']: err.append('kitchen state keeps range and can ' + k)
for sid, x in _sh.items():
    if x['bg'] == 'D' and byname.get('S14c_F_' + sid) and _frame_refs('S14c_F_' + sid)[0] != 'BG_D_FIX': err.append('porch plate ' + sid)
_e2 = {n['node_name']: n.get('prompt', '') for n in json.load(open('out/fix/workflow_S14c_0E2_SuaAnhTreo.json'))['workflow']['nodes']}
if 'Remove the flower centerpiece' not in _e2['P_BG_A_WEST_FIX']: err.append('0E2 centerpiece')
import collections as _c; print('ERRORS',len(err)); print(_c.Counter(e.split(' S14c')[0].split(' P_')[0] for e in err)); print('\n'.join(err[:40]))
lens=[len(byid[e['source_node_id']]['prompt'].split()) for n in N if n.get('media_type')=='Video' for e in inc[n['node_id']] if e['target_port']=='text']
print('video prompt words min/max',min(lens),max(lens))
if max(lens)>600: err.append('clip prompt over 600 words'); print('ERROR clip prompt over 600 words')
tl=[(len(byid[e['source_node_id']]['prompt'].split()),n['node_name']) for n in N if n.get('media_type')=='Video' for e in inc[n['node_id']] if e['target_port']=='text']
print('T >370 words:',[x for x in tl if x[1].startswith('S14c_T_') and x[0]>370]); print('V >320 words:',[x for x in tl if x[1].startswith('S14c_V_') and x[0]>320])
print('frame_2 clips:',sum(1 for n in N if n.get('frame_2_source')),'| x4 images:',sum(1 for n in N if n.get('media_type')=='Image' and n.get('quantity')==4),'| x2 videos:',sum(1 for n in N if n.get('media_type')=='Video' and n.get('quantity')==2))
print(collections.Counter(r['dur'] for r in rows), collections.Counter(r['kind'] for r in rows))
