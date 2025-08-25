#!/bin/bash

wallDIR="$HOME/Wallpapers"

# 1️⃣ Wallpaper listesini al ve rastgele seç
mapfile -t ALL_PICS < <(
  find -L "$wallDIR" -maxdepth 1 -mindepth 1 \
       -type f \( -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.png' \)
)
(( ${#ALL_PICS[@]} )) || exit 1

# 2️⃣ Rastgele bir wallpaper seç
selected_path="${ALL_PICS[RANDOM % ${#ALL_PICS[@]}]}"

# 3️⃣ swww ile efektli wallpaper değişimi
if ! pgrep -x "swww-daemon" >/dev/null; then
    swww-daemon &
    sleep 1
fi

swww img "$selected_path" \
  --transition-type grow \
  --transition-pos top-left \
  --transition-fps 60 \
  --transition-bezier 0.25,0.1,0.25,1

# 4️⃣ Wallust ile sadece Rofi renklerini uygula
wallust -i "$selected_path"