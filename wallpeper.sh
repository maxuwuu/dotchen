#!/bin/bash

wallDIR="$HOME/Wallpapers"
rofiThemeDIR="$HOME/.config/WallpaperSelector/wallpaper-selector.rasi"

mapfile -d '' ALL_PICS < <(
  find -L "$wallDIR" -maxdepth 1 -mindepth 1 \
       -type f \( -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.png' \) \
       -print0
)
(( ${#ALL_PICS[@]} )) || exit 1

mapfile -t SHUFFLED_PICS < <(printf '%s\n' "${ALL_PICS[@]}" | shuf)

declare -A lookup
entries=()
for pic in "${SHUFFLED_PICS[@]}"; do
  name=$(basename "$pic")
  lookup["$name"]="$pic"
  entries+=("$name" "$pic")
done

selected_name=$(printf '%s\x00icon\x1f%s\n' "${entries[@]}" \
  | rofi -dmenu -i -theme "$rofiThemeDIR" -p "Select Wallpaper:" -format 's')
[[ -n "$selected_name" ]] || exit 0
selected_path="${lookup["$selected_name"]}"

if [ -n "$selected_path" ]; then
  if ! pgrep -x "swww-daemon" >/dev/null; then
    swww-daemon &
    sleep 1
  fi

  # swww ile efektli wallpaper değişimi
  swww img "$selected_path" \
    --transition-type grow \
    --transition-pos top-left \
    --transition-fps 60 \
    --transition-bezier 0.25,0.1,0.25,1

  # Wallust ile sadece Rofi renklerini uygula
  wallust -i "$selected_path"
fi