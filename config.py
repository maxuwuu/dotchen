import os
from libqtile import layout, hook
from libqtile.config import Key, Group
from libqtile.lazy import lazy

# -----------------------------
# Mod ve terminal
# -----------------------------
mod = "mod1"           # Alt tuşu
terminal = "konsole"

# -----------------------------
# Keybinds
# -----------------------------
keys = [
    # Terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Rofi launcher
    Key([mod], "d", lazy.spawn("rofi -show drun"), desc="Run Rofi"),

    # File manager
    Key([mod, "shift"], "d", lazy.spawn("thunar"), desc="Open Thunar"),

    # Close window
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),

    # Fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),

    # Floating toggle
    Key([mod, "shift"], "space", lazy.window.toggle_floating(), desc="Toggle floating"),

    # Focus windows (hjkl)
    Key([mod], "j", lazy.layout.left(), desc="Focus left"),
    Key([mod], "k", lazy.layout.down(), desc="Focus down"),
    Key([mod], "l", lazy.layout.up(), desc="Focus up"),
    Key([mod], "semicolon", lazy.layout.right(), desc="Focus right"),

    # Move windows
    Key([mod, "shift"], "j", lazy.layout.shuffle_left(), desc="Move left"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(), desc="Move down"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_up(), desc="Move up"),
    Key([mod, "shift"], "semicolon", lazy.layout.shuffle_right(), desc="Move right"),

    # Layout switching
    Key([mod], "s", lazy.group.setlayout("stack"), desc="Stack layout"),
    Key([mod], "w", lazy.group.setlayout("monadtall"), desc="Monadtall layout"),
    Key([mod], "e", lazy.next_layout(), desc="Toggle layout"),

    # Restart / Exit
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "shift"], "e", lazy.spawn("~/maria/Launchers/rofi/powermenu/powermenu"), desc="Exit powermenu"),
]

# -----------------------------
# Workspaces / Groups
# -----------------------------
groups = [Group(str(i)) for i in range(1, 11)]

for g in groups:
    keys.extend([
        # Switch to workspace
        Key([mod], g.name, lazy.group[g.name].toscreen(), desc="Switch to group"),
        # Move focused window to workspace
        Key([mod, "shift"], g.name, lazy.window.togroup(g.name), desc="Move window to group"),
    ])

# -----------------------------
# Layouts
# -----------------------------
layouts = [
    layout.MonadTall(border_focus="#d8a657", border_width=2, margin=5),
    layout.Max(),
    layout.Stack(num_stacks=2),
    layout.Floating(),
]

# -----------------------------
# Screens (Qtile bar kapalı)
# -----------------------------
screens = []  # Qtile bar’ı devre dışı

# -----------------------------
# Autostart (Polybar + diğer uygulamalar)
# -----------------------------
@hook.subscribe.startup_once
def autostart():
    os.system("feh --bg-scale ~/walls/Anime/blue.jpg &")
    os.system("dex --autostart --environment i3 &")
    os.system("xss-lock --transfer-sleep-lock -- i3lock --nofork &")
    os.system("nm-applet &")
    os.system("polybar main &")  # Polybar başlatılıyor