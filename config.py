# qtile 0.33 minimal config - Polybar destekli

from libqtile import layout, hook
from libqtile.config import Key, Group, Match, Screen
from libqtile.lazy import lazy

mod = "mod1"  # Alt tuşu
terminal = "konsole"

# -----------------------------
# Keybindings
# -----------------------------
keys = [
    # Terminal aç
    Key([mod], "Return", lazy.spawn(terminal)),
    
    # Çıkış
    Key([mod, "control"], "q", lazy.shutdown()),
    
    # Pencereyi kapat
    Key([mod], "w", lazy.window.kill()),
    
    # Pencereler arasında geçiş
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),

    # Layout değiştirme
    Key([mod], "space", lazy.next_layout()),
]

# -----------------------------
# Gruplar
# -----------------------------
groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

# -----------------------------
# Layouts
# -----------------------------
layouts = [
    layout.MonadTall(border_focus="#ff0000", border_width=2, margin=8),
    layout.Max(),
]

# -----------------------------
# Window rules
# -----------------------------
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(title="Confirmation"),
        Match(title="Qalculate!"),
    ]
)

# -----------------------------
# Screens (Bar yok, Polybar kullanılacak)
# -----------------------------
screens = [
    Screen()
]

# -----------------------------
# Autostart
# -----------------------------
@hook.subscribe.startup_once
def autostart():
    import os
    home = os.path.expanduser("~")
    # Wallpaper örneği
    os.system(f"feh --bg-scale {home}/walls/Anime/blue.jpg &")
    # Polybar başlat
    os.system("polybar example &")