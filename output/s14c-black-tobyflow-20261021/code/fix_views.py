# 0E2 (Nam 23/10): in the chosen room views, some small framed photos show children (and one face reads light-skinned); every photo in this
# house shows the Black family, adults only. One edit of each chosen view changes only the people inside the frames.
import json, random, string, contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    import build14 as b
random.seed(2310)
def nid(): return 'node_' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
TAIL = ("Looking like an ordinary frame from a real camera with a normal lens, not a render; true-to-life gentle colors; no over-sharpening, no HDR, no CGI look. "
        "No people in the room. No subtitles, no captions, no on-screen text, no logos.")
FIX = {
 'WEST': ("Edit Image 1, a photo of the empty dining room facing the wall with the framed family photos. Keep everything exactly as in Image 1: the camera position "
          "and framing, the walls, the tall china hutch, the low cabinet, the chandelier and its warm light, the table with the lace tablecloth, the chairs, the carpet, "
          "the edge of the archway, and every picture frame in the same place, size and color. Change only two things. 1) Remove the flower centerpiece from the table; "
          "the lace tablecloth stays bare and flat there, nothing tall on the table. 2) The people inside the framed photos: "
          "every person in every photo is a Black American adult, with no children: the two framed photos on top of the tall china hutch each show a group of four or "
          "five Black adults; the church photo shows Black adults in their church clothes in front of the altar cross; the small portrait in pink shows a young Black "
          "woman in her twenties; the wedding photo and the graduation portraits stay as they are. The photos stay small and a little soft, with no lettering. " + TAIL +
          " Final check: the same room and the same frames as in Image 1; no flower centerpiece on the table; only the people inside the photos changed, all Black adults."),
 'SOUTH': ("Edit Image 1, a photo of the empty dining room seen from the head of the table toward the opening to the living room. Keep everything exactly as in Image 1: "
           "the camera position and framing, the walls, the window with its curtains, the peace lily, the opening, the sofa and the floor lamp, the china hutch, the "
           "chandelier and its warm light, the table with the lace tablecloth, the chairs, the flower centerpiece, the carpet, and every picture frame in the same place, "
           "size and color. Change only the people inside the framed photos on the wall at screen-right and on top of the china hutch: every person in every photo is a "
           "Black American adult with brown skin, with no children: the portrait of the older woman with short hair shows an older Black woman with deep brown skin; the "
           "group photo shows a group of Black adults; the wedding portrait and the graduation portrait stay as they are. The photos stay small and a little soft, with "
           "no lettering. " + TAIL + " Final check: the same room and the same frames as in Image 1; only the people inside the photos changed, all Black adults."),
}
nodes, edges = [], []
for r, k in enumerate(('WEST', 'SOUTH')):
    up = dict(node_id=nid(), node_type='image', node_name=f'IMG_BG_A_{k}_CU', pos_x=0, pos_y=r * 400, enabled=True, slug=f'img_bg_a_{k.lower()}_cu', slug_auto=False, ref_images=[])
    pr = dict(node_id=nid(), node_type='prompt', node_name=f'P_BG_A_{k}_FIX', pos_x=400, pos_y=r * 400, enabled=True, slug=f'p_bg_a_{k.lower()}_fix', slug_auto=False,
              prompt=FIX[k], prompt_mode='all', ref_mode='all', use_ai=False, ai_fallback=True, ai_delete_after_run=True, timeout_sec=60)
    im = dict(node_id=nid(), node_type='generate', node_name=f'BG_A_{k}_FIX', pos_x=800, pos_y=r * 400, enabled=True, slug=f'bg_a_{k.lower()}_fix', slug_auto=False,
              media_type='Image', prompt_source='upstream_node', multi_prompt=False, model='Nano Banana Pro', ratio='9:16', quantity=4, download_resolution='2k')
    base = len(nodes); nodes += [up, pr, im]
    edges.append(dict(edge_id=f'edge_{base + 1}_output_1_{base + 3}_input_1', source_node_id=up['node_id'], source_handle='output_1', source_port='media',
                      target_node_id=im['node_id'], target_handle='input_1', target_port='image_ref', data_type='image'))
    edges.append(dict(edge_id=f'edge_{base + 2}_output_1_{base + 3}_input_2', source_node_id=pr['node_id'], source_handle='output_1', source_port='text',
                      target_node_id=im['node_id'], target_handle='input_2', target_port='text', data_type='text'))
wf = {"version": "1.0", "type": "workflow", "exported_at": "2026-10-23T12:00:00.000Z",
      "workflow": {"name": "S14c_0E2 Sua anh treo tuong", "description": ("Sửa 2 ảnh hướng đã chọn ở 0E: ảnh treo có trẻ em thành người lớn da đen; ảnh tường ảnh bỏ thêm lọ hoa giữa bàn (che miệng người nói ở F1b, F5b). "
                   "Tải BG_A_WEST đã chọn vào IMG_BG_A_WEST_CU, BG_A_SOUTH đã chọn vào IMG_BG_A_SOUTH_CU, chạy, chọn 1 ảnh mỗi node; ảnh đó thay cho BG_A_WEST, BG_A_SOUTH."),
                   "settings": {"parallel": False, "quantity": 1, "delay_between_nodes": 20, "timeout_per_node": 300, "retry_on_error": 1, "stop_on_error": False},
                   "nodes": nodes, "edges": edges}}
json.dump(wf, open('out/fix/workflow_S14c_0E2_SuaAnhTreo.json', 'w'), ensure_ascii=False, separators=(',', ':'))
low = ' '.join(FIX.values()).lower()
assert not any(w in ' ' + low + ' ' for w in (' dark ', 'glasses', 'smooth', 'perfect', 'cinematic'))
print('ok', [len(v.split()) for v in FIX.values()])
