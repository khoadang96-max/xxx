#!/usr/bin/env bash
# RD HOME - "Mot vong can ho"
# Dung video Ken Burns cham tu 5 anh tinh. Yeu cau: ffmpeg (libx264, zoompan, xfade, drawtext, geq).
#   ./render.sh                  -> renders/rd-home-9x16.mp4
#   ./render.sh --ratio 16:9
#   ./render.sh --audio nhac.mp3
#   ./render.sh --no-text
#   ./render.sh --draft          -> render nhanh de duyet
set -euo pipefail
cd "$(dirname "$0")"

RATIO=9:16 ; AUDIO="" ; TEXT=1 ; QUALITY=high ; SRC=assets ; OUT=""
while [ $# -gt 0 ]; do
  case "$1" in
    --ratio)   RATIO="$2"; shift 2 ;;
    --audio)   AUDIO="$2"; shift 2 ;;
    --src)     SRC="$2";   shift 2 ;;
    --out)     OUT="$2";   shift 2 ;;
    --no-text) TEXT=0;     shift ;;
    --draft)   QUALITY=draft; shift ;;
    *) echo "Tham so la: $1" >&2; exit 2 ;;
  esac
done

case "$RATIO" in
  9:16) W=1080; H=1920 ;;
  16:9) W=1920; H=1080 ;;
  4:5)  W=1080; H=1350 ;;
  1:1)  W=1080; H=1080 ;;
  *) echo "Ty le khong ho tro: $RATIO (chon 9:16 | 16:9 | 4:5 | 1:1)" >&2; exit 2 ;;
esac

FPS=30 ; DUR=7.0 ; XF=1.2 ; ENDCARD=4.0
PUSH=0.16            # bien do zoom push-in / pull-out
DRIFT=1.18           # muc zoom co dinh cua pan / tilt -> bien do troi 18%
SCRIM=0.62           # do dam lop phu chan khung; anh sang can lop nay de doc chu
CREAM=0xF3EDE4 ; INK=0x3A332C
FONT=/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf
FONTB=/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf
BRAND="RD HOME"

# file | huong may | dong 1 | dong 2
SHOTS=(
  "01-loi-vao.jpg|tilt-down|Lối vào|nơi bắt đầu một ngày"
  "02-bep.jpg|pan-right|Bếp|ấm sáng sau lớp kính mờ"
  "03-khoang-tho.jpg|push-in|Khoảng thở|nắng lọc qua rèm"
  "04-toan-canh.jpg|push-in|Liền mạch|bếp — khách — ngủ trong một nhịp"
  "05-nhin-lai.jpg|pull-out|Về nhà|"
)

command -v ffmpeg >/dev/null || { echo "Chua co ffmpeg. macOS: brew install ffmpeg | Ubuntu: sudo apt install ffmpeg"; exit 1; }

missing=0
for s in "${SHOTS[@]}"; do
  f="$SRC/${s%%|*}"
  [ -f "$f" ] || { echo "Thieu anh: $f"; missing=1; }
done
if [ "$missing" = 1 ]; then
  echo; echo "Dat 5 anh vao '$SRC/' dung ten tren (thu tu ten = thu tu xuat hien)."; exit 1
fi

N=${#SHOTS[@]}
IDX_END=$N ; IDX_SCRIM=$((N+1)) ; IDX_AUDIO=$((N+2))
SW=$((W*2)) ; SH=$((H*2))                      # upscale 2x -> khong rung vien khi zoompan
SCH=$((H*45/100))                              # chieu cao lop scrim
D=$(awk -v d="$DUR" -v f="$FPS" 'BEGIN{printf "%d", d*f}')
FADE=0.9 ; HOLD=$(awk -v d="$DUR" 'BEGIN{printf "%.2f", d-1.6}')

P="(on/($((D-1))))" ; E="($P*$P*(3-2*$P))"     # smoothstep: vao cham, ra cham
CX="iw/2-(iw/zoom/2)" ; CY="ih/2-(ih/zoom/2)"

esc() { printf '%s' "$1" | sed "s/'/\\\\'/g; s/:/\\\\:/g; s/%/\\\\%/g"; }

TMP=$(mktemp -d) ; trap 'rm -rf "$TMP"' EXIT
ffmpeg -y -v error -f lavfi -i "color=c=black:s=${W}x${SCH}" \
  -vf "format=rgba,geq=r=0:g=0:b=0:a='255*${SCRIM}*pow(Y/(H-1)\,1.8)'" \
  -frames:v 1 "$TMP/scrim.png"

inputs=() ; fc="" ; i=0 ; tn=0
for s in "${SHOTS[@]}"; do
  IFS='|' read -r file move l1 l2 <<< "$s"
  inputs+=(-i "$SRC/$file")

  case "$move" in
    push-in)   Z="1+$PUSH*$E"       ; X="$CX" ; Y="$CY" ;;
    pull-out)  Z="1+$PUSH-$PUSH*$E" ; X="$CX" ; Y="$CY" ;;
    pan-right) Z="$DRIFT" ; X="(iw-iw/zoom)*$E"     ; Y="$CY" ;;
    pan-left)  Z="$DRIFT" ; X="(iw-iw/zoom)*(1-$E)" ; Y="$CY" ;;
    tilt-down) Z="$DRIFT" ; X="$CX" ; Y="(ih-ih/zoom)*$E" ;;
    tilt-up)   Z="$DRIFT" ; X="$CX" ; Y="(ih-ih/zoom)*(1-$E)" ;;
    *) echo "Huong may khong hop le: $move" >&2; exit 2 ;;
  esac

  seg="[$i:v]scale=$SW:$SH:force_original_aspect_ratio=increase,crop=$SW:$SH,"
  seg+="zoompan=z='$Z':x='$X':y='$Y':d=$D:s=${W}x${H}:fps=$FPS,setsar=1"

  if [ "$TEXT" = 1 ] && [ -n "$l1" ]; then
    fc+="$seg[b$i];"
    seg="[b$i][sc$tn]overlay=0:$((H-SCH))"
    tn=$((tn+1))
    A="if(lt(t,0.6),0,if(lt(t,0.6+$FADE),(t-0.6)/$FADE,if(lt(t,$HOLD),1,if(lt(t,$HOLD+$FADE),1-(t-$HOLD)/$FADE,0))))"
    MX=$((W/12)) ; BY=$((H*74/100)) ; S1=$((W*62/1000)) ; S2=$((W*36/1000))
    seg+=",drawtext=fontfile=$FONTB:text='$(esc "$l1")':fontcolor=white@0.97:fontsize=$S1"
    seg+=":x=$MX:y=$BY:shadowcolor=black@0.30:shadowx=0:shadowy=3:alpha='$A'"
    [ -n "$l2" ] && seg+=",drawtext=fontfile=$FONT:text='$(esc "$l2")':fontcolor=white@0.86:fontsize=$S2:x=$MX:y=$((BY+S1+22)):shadowcolor=black@0.30:shadowx=0:shadowy=2:alpha='$A'"
  fi
  fc+="$seg,format=yuv420p[v$i];"
  i=$((i+1))
done

inputs+=(-f lavfi -t "$ENDCARD" -i "color=c=$CREAM:s=${W}x${H}:r=$FPS")
inputs+=(-i "$TMP/scrim.png")

if [ "$tn" -gt 0 ]; then
  sp="[$IDX_SCRIM:v]scale=$W:$SCH,format=rgba"
  [ "$tn" -gt 1 ] && sp+=",split=$tn"
  for ((k=0;k<tn;k++)); do sp+="[sc$k]"; done
  fc="$sp;$fc"
fi

AE="if(lt(t,0.5),0,if(lt(t,1.4),(t-0.5)/0.9,1))" ; BS=$((W*84/1000))
fc+="[$IDX_END:v]setsar=1,format=yuv420p,"
fc+="drawtext=fontfile=$FONTB:text='$(esc "$BRAND")':fontcolor=$INK:fontsize=$BS"
fc+=":x=(w-tw)/2:y=(h-th)/2:alpha='$AE'[v$IDX_END];"

prev="[v0]" ; off=0
for ((k=1; k<=N; k++)); do
  off=$(awk -v o="$off" -v d="$DUR" -v x="$XF" 'BEGIN{printf "%.3f", o+d-x}')
  lbl="[x$k]" ; [ "$k" -eq "$N" ] && lbl="[vout]"
  fc+="${prev}[v$k]xfade=transition=fade:duration=$XF:offset=$off$lbl;"
  prev="$lbl"
done
fc="${fc%;}"

TOTAL=$(awk -v n="$N" -v d="$DUR" -v e="$ENDCARD" -v x="$XF" 'BEGIN{printf "%.2f", n*d+e-n*x}')
if [ "$QUALITY" = draft ]; then CRF=28; PRESET=veryfast; else CRF=17; PRESET=slow; fi
[ -n "$OUT" ] || OUT="renders/rd-home-${RATIO/:/x}.mp4"
mkdir -p "$(dirname "$OUT")"

args=(-y "${inputs[@]}")
if [ -n "$AUDIO" ]; then
  args+=(-i "$AUDIO")
  fc+=";[$IDX_AUDIO:a]afade=t=in:st=0:d=2,afade=t=out:st=$(awk -v t="$TOTAL" 'BEGIN{printf "%.2f", t-2.5}'):d=2.5,volume=0.85[aout]"
  args+=(-filter_complex "$fc" -map "[vout]" -map "[aout]" -c:a aac -b:a 192k -shortest)
else
  args+=(-filter_complex "$fc" -map "[vout]" -an)
fi
args+=(-t "$TOTAL" -c:v libx264 -preset "$PRESET" -crf "$CRF" -pix_fmt yuv420p -movflags +faststart -r "$FPS" "$OUT")

echo "Render ${W}x${H} · ${TOTAL}s · $QUALITY -> $OUT"
ffmpeg -hide_banner -loglevel error -stats "${args[@]}"
echo "Xong: $OUT"
