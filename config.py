import os
import subprocess
from libqtile import layout, hook
from libqtile.config import Key, Group
from libqtile.lazy import lazy

mod = "mod1"
terminal = "konsole"

keys = [
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "d", lazy.spawn("rofi -show drun")),
    Key([mod, "shift"], "d", lazy.spawn("thunar")),
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),
    Key([mod], "j", lazy.layout.left()),
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "l", lazy.layout.up()),
    Key([mod], "semicolon", lazy.layout.right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "semicolon", lazy.layout.shuffle_right()),
    Key([mod], "e", lazy.next_layout()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "shift"], "e", lazy.spawn("~/maria/Launchers/rofi/powermenu/powermenu")),
]

groups = [Group(str(i)) for i in range(1, 11)]
for g in groups:
    keys.extend([
        Key([mod], g.name, lazy.group[g.name].toscreen()),
        Key([mod, "shift"], g.name, lazy.window.togroup(g.name)),
    ])

layouts = [
    layout.MonadTall(border_focus="#d8a657", border_width=2, margin=5),
    layout.Max(),
    layout.Stack(num_stacks=2),
    layout.Floating(),
]

screens = []

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~")
    subprocess.Popen(["feh", "--bg-scale", f"{home}/walls/Anime/blue.jpg"])
    subprocess.Popen(["dex", "--autostart", "--environment", "i3"])
    subprocess.Popen(["xss-lock", "--transfer-sleep-lock", "--", "i3lock", "--nofork"])
    subprocess.Popen(["nm-applet"])
    subprocess.Popen(["polybar", "main"])