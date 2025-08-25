if [ -f "$HOME/.config/.current_wallpaper" ]; then
    swww img "$(cat $HOME/.config/.current_wallpaper)" \
        --transition-type grow \
        --transition-pos top-left \
        --transition-fps 60 \
        --transition-bezier 0.25,0.1,0.25,1
    wallust -i "$(cat $HOME/.config/.current_wallpaper)"
fi