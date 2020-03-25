## Initial imports
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget
from typing import List  # noqa: F401

# Autostart applications imports'
from libqtile import hook
import os
import subprocess

## Rename the keys for easier reading
WIN = "mod4"
ALT = "mod1"
TAB = "Tab"
CTRL = "control"
SHIFT = "shift"
RETURN = "Return"
SPACE = "space"
mod = WIN

## Set terminal to alacritty
term = "alacritty"

## Color for borders
color_focus = "8fa1b3"
color_idle  = "000000"

## Common commands
# Volume control 
vol_step = 5
vol_up = f"pamixer -i {vol_step}"
vol_down = f"pamixer -d {vol_step}"
vol_mute = "pamixer -t"

# Screen lock
lock = "xcreensaver-command --lock"

## Autostart hook
@hook.subscribe.startup_once
def autostart():
    subprocess.call("/home/lc/.config/qtile/autostart.sh")

# Keybindings
keys = [
    # Change window focus
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),

    # Moves windows
    Key([mod, SHIFT], "Down", lazy.layout.shuffle_down()),
    Key([mod, SHIFT], "Up", lazy.layout.shuffle_up()),
    Key([mod, SHIFT], "Left", lazy.layout.shuffle_left()),
    Key([mod, SHIFT], "Right", lazy.layout.shuffle_right()),

    # Increase the size of the window
    Key([mod, CTRL], "Down", lazy.layout.grow_down()),
    Key([mod, CTRL], "Up", lazy.layout.grow_up()),
    Key([mod, CTRL], "Left", lazy.layout.grow_left()),
    Key([mod, CTRL], "Right", lazy.layout.grow_right()),
    
    # Fullscreen toggle
    Key([mod], "m", lazy.window.toggle_fullscreen()),

    # Reset the size of the windows
    Key([mod, SHIFT], "n", lazy.layout.normalize()),
    Key([mod], RETURN, lazy.layout.toggle_split()),

    # Open the terminal
    Key([mod], "t", lazy.spawn(term)),
    
    # Close the window
    Key([mod], "w", lazy.window.kill()),

    # Restart Qtile
    Key([mod, "control"], "r", lazy.restart()),

    # Close Qtile completely
    Key([mod, "control"], "q", lazy.shutdown()),

    # Dmenu-like command prompt
    Key([mod], "r", lazy.spawncmd()),

    # Volume keys
    Key([mod], "XF86AudioRaiseVolume", lazy.spawn(vol_up)),
    Key([mod], "XF86AudioLowerVolume", lazy.spawn(vol_down)),
    Key([mod], "XF86AudioMute", lazy.spawn(vol_mute)),


]

groups = [Group(i) for i in "1234"]

for i in groups:
    # mod + number to switch to the group
    keys.append(
            Key([mod], i.name, lazy.group[i.name].toscreen())
    )
    # mod + shift + number to move focused window to group
    keys.append(
            Key([mod, SHIFT], i.name, lazy.window.togroup(i.name))
    )


layouts = [
    # BSP layout (i3 like)
    layout.Bsp(
        border_focus  = color_focus,
        border_normal = color_idle,
        border_width  = 2,
        margin        = 10
    )
]


widget_defaults = dict(
    font=     "Cantarell",
    fontsize= 12,
    padding=  3,
)

extension_defaults = widget_defaults.copy()

# Physical screens
screens = [
        
    # Main screen
    Screen(
        
        #Create a bar at the top of the screen
        top=bar.Bar(
            # Widgets
            [
                widget.GroupBox(), #Group list
                widget.Prompt(),
                widget.WindowName(),
                widget.Systray(),
                #Volume widget
                widget.Volume(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
            ],
            # Bar size
            36,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
