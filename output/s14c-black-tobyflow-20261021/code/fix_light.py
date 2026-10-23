# 0A2 v2 (Nam 23/10, "quá tối"): the morning kitchen plate came out dim and grey-green, and every kitchen shot copies its light.
# One edit from the ORIGINAL 0A kitchen does the 4 old fixes and brightens the room (Nam's rule: never stack edits on an edited image).
# Also writes the paste-ready txt: 0A2 prompt, the 3 kitchen prompts of 0B, and the 16 kitchen frames of F2/F3.
import json, contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    import build14 as b
RELIGHT = ("5) The light: a bright, fresh early morning. Clear sunlight comes in through the window over the sink and falls across the counter, "
    "and soft daylight bounces around the whole room, so the upper and lower cabinets, the fridge and the floor are clearly lit, "
    "with gentle open shadows and nothing dark or gloomy in the corners. The white cabinets, the range and the fridge look clean, true white, not grey or green; "
    "the walls a soft warm cream; only the shadows keep a slight cool morning freshness. The window is bright but keeps its frame and a soft view outside. "
    "The old kitchen looks well kept and cared for.")
PROMPT = ("Edit Image 1, a photo of an empty kitchen in the morning. Keep the same kitchen exactly: the same white cabinets, counter, double sink under the window, "
    "white gas range, range hood, cast-iron skillet, white crock of teal silicone utensils, paper towel holder, soap bottles, wall phone, fridge, floor, "
    "camera position and framing. Change only these five things: "
    "1) The paper hand fan hanging beside the wall phone: its printed side now shows a simple painting of a small white country church under a blue sky, "
    "with no people and no words, letters or writing anywhere on the fan. "
    "2) The snapshots on the fridge door: replace every photo with snapshots of one Black American family, only adults: an older Black woman with short silver hair "
    "smiling with two church friends, a Black man in his forties with a salt-and-pepper beard beside his wife, and a young Black woman with long braids in a graduation cap; "
    "every person in every photo is Black American; keep the same number of photos, the same sizes, magnets and places, small and a little soft; "
    "the paper notes on the fridge are blank. "
    "3) Remove the cereal boxes and everything else from the top of the fridge. "
    "4) Add a white step trash can with a foot pedal and a lid on the floor at the end of the counter, lit like everything around it, with a soft contact shadow on the floor. "
    + RELIGHT + " "
    "Looking like an ordinary frame from a real camera with a normal lens, not a render; true-to-life gentle colors; no over-sharpening, no HDR, no CGI look. "
    "No people. No subtitles, no captions, no on-screen text, no logos. "
    "Final check: the same kitchen as Image 1; only the fan picture, the fridge photos, the top of the fridge, the new trash can and the brighter light changed.")
# same nodes and ids as the 0A2 file sent on 22/10, so a pasted prompt and a fresh import behave the same
SETTINGS = {"parallel": False, "quantity": 1, "delay_between_nodes": 20, "timeout_per_node": 300, "retry_on_error": 1, "stop_on_error": False}
NODES = [
 {"node_id": "node_jClJpbqh", "node_type": "image", "node_name": "IMG_BEP_SANG_CU", "pos_x": 0, "pos_y": 0, "enabled": True, "slug": "img_bep_sang_cu", "slug_auto": False, "ref_images": []},
 {"node_id": "node_ntN2Bu56", "node_type": "prompt", "node_name": "P_BG_B_MORNING_FIX", "pos_x": 400, "pos_y": 0, "enabled": True, "slug": "p_bg_b_morning_fix", "slug_auto": False,
  "prompt": PROMPT, "prompt_mode": "all", "ref_mode": "all", "use_ai": False, "ai_fallback": True, "ai_delete_after_run": True, "timeout_sec": 60},
 {"node_id": "node_vB8Ylvzb", "node_type": "generate", "node_name": "BG_B_MORNING_FIX", "pos_x": 800, "pos_y": 0, "enabled": True, "slug": "bg_b_morning_fix", "slug_auto": False,
  "media_type": "Image", "prompt_source": "upstream_node", "multi_prompt": False, "model": "Nano Banana Pro", "ratio": "9:16", "quantity": 4, "download_resolution": "2k"}]
EDGES = [
 {"edge_id": "edge_1_output_1_3_input_1", "source_node_id": "node_jClJpbqh", "source_handle": "output_1", "source_port": "media", "target_node_id": "node_vB8Ylvzb", "target_handle": "input_1", "target_port": "image_ref", "data_type": "image"},
 {"edge_id": "edge_2_output_1_3_input_2", "source_node_id": "node_ntN2Bu56", "source_handle": "output_1", "source_port": "text", "target_node_id": "node_vB8Ylvzb", "target_handle": "input_2", "target_port": "text", "data_type": "text"}]
wf = {"version": "1.0", "type": "workflow", "exported_at": "2026-10-23T08:00:00.000Z",
      "workflow": {"name": "S14c_0A2 Sua bep buoi sang",
                   "description": ("Sửa ảnh bếp buổi sáng GỐC chọn ở 0A (ảnh chưa sửa): tải vào IMG_BEP_SANG_CU, chạy BG_B_MORNING_FIX, chọn 1 ảnh làm BG_B_MORNING "
                                   "(dùng ở 0B và các file F có cảnh bếp). Bản 23/10: sửa 4 chỗ như cũ và làm bếp sáng, trắng ra trắng."),
                   "settings": SETTINGS, "nodes": NODES, "edges": EDGES}}
json.dump(wf, open('out/fix/workflow_S14c_0A2_SuaBepSang.json', 'w'), ensure_ascii=False, separators=(',', ':'))
N = {n['node_name']: n for n in json.load(open('out/workflow_S14c_Black.json'))['workflow']['nodes']}
FR = [f'P_F_{s["id"]}' for s in b.SH if s['bg'] in b.FRAME_LIGHT and not s['src']]
L = ["S14c - prompt anh sang moi (23/10): bep sang hon, mat de doc o canh dem",
     "1) File 0A2: dan vao node P_BG_B_MORNING_FIX. Tai anh bep GOC da chon o 0A (anh chua sua) vao IMG_BEP_SANG_CU, chay BG_B_MORNING_FIX (x4), chon 1 anh = BG_B_MORNING moi.",
     "2) File 0B: tai BG_B_MORNING moi vao IMG_BG_B_MORNING, dan 3 prompt P_BG_B_NIGHT, P_BG_B_BOXES, P_BG_B_CLEAR, chay lai 3 node do.",
     "3) File F2 va F3: da import ma chua chay thi xoa, import ban moi. Khong muon import lai thi dan " + str(len(FR)) + " prompt khung o duoi vao node cung ten.",
     "Cac file khac (0A, 0C, F1, F4, F5, F6, V1-V6) khong doi.", ""]
L += ["===== P_BG_B_MORNING_FIX (file 0A2) =====", PROMPT, ""]
for k in ('P_BG_B_NIGHT', 'P_BG_B_BOXES', 'P_BG_B_CLEAR'): L += [f"===== {k} (file 0B) =====", N[k]['prompt'], ""]
for k in FR: L += [f"===== {k} (file {'F2' if k < 'P_F_S20' else 'F3'}) =====", N[k]['prompt'], ""]
open('out/fix/S14c_prompt_anh_sang_20261023.txt', 'w').write('\n'.join(L))
assert 'morning light, colors' not in PROMPT and PROMPT.count(') ') >= 5
print('0A2 words', len(PROMPT.split()), '| frames', len(FR), FR[0], FR[-1])
