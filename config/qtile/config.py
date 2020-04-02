# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

""" 
dotslashluis' Qtile configuration
Programs used:
dmenu
xscreensaver
fcitx
pamixer
nm-applet
picom
clipmenu
shotgun
"""
## Initial imports
from libqtile.config import Key, Screen, Group, Drag, Click, Match
from libqtile.command import lazy
from libqtile import layout, bar, widget, extension
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

## Set home directory variable for easier reading
HOME = os.path.expanduser("~")

## Applications
term = "alacritty"
screenshot="shotgun"


## Colors
# Colorscheme used: Atelier heath dark by Bram de Haan
# Check him out! (http://atelierbramdehaan.nl)
# He also has a github (https://github.com/atelierbram/)
"""
b16 = [ 
    "#1b181b",
    "#ca402b",
    "#379a37",
    "#bb8a35",
    "#516aec",
    "#7b59c0",
    "#159393",
    "#ab9bab",
    "#776977",
    "#ca402b",
    "#379a37",
    "#bb8a35",
    "#516aec",
    "#7b59c0",
    "#159393",
    "#f7f3f7"
]
"""
b16 = [
    "#111219",
    "#db5966",
    "#7cbe8c",
    "#9b956b",
    "#2994c6",
    "#6c75cb",
    "#73c1a9",
    "#9ea3c0",
    "#545c8c",
    "#c173c1",
    "#7cbe8c",
    "#b5ae7d",
    "#31a9e5",
    "#929be5",
    "#2aacbd",
    "#9ea3c0",
]

bg = b16[0]
fg = b16[7]

## Common commands
# Volume control 
vol_step = 5
vol_up = f"pamixer -i {vol_step}"
vol_down = f"pamixer -d {vol_step}"
vol_mute = "pamixer -t"

# Screen lock FIX: Doesn't work
lock = "xcreensaver-command -lock"

## Autostart hook
@hook.subscribe.startup_once
def autostart():
    subprocess.call(f"{HOME}/.config/qtile/autostart.sh")

## Groups
# FIX!! Only brave works with the match (????????)
groups = [
        Group("web", 
            matches=[
                Match(wm_class="brave-browser"),
                Match(wm_class="firefox"),
                Match(wm_class="Opera")
            ]
        ),
        Group("steam",
            matches=[
                Match(wm_class="Steam")
            ]    
        ),
        Group("code",
            matches=[
                Match(wm_class="code-oss")
            ]
        ),
        Group("chat",
            matches=[
                Match(wm_class="discord")
            ]
        ),
        Group("etc"),
        Group("term",
            matches=[
                Match(wm_class="Alacritty")
            ]
        ),
]

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

    # Open the preferred terminal emulator
    Key([mod], "t", lazy.spawn(term)),
    
    # Close focused window
    Key([mod], "w", lazy.window.kill()),

    # Restart Qtile
    Key([mod, "control"], "r", lazy.restart()),

    # Close Qtile completely
    Key([mod, "control"], "q", lazy.shutdown()),

    # Command promt.  Dmenu replaces it
    #Key([mod], "r", lazy.spawncmd()),
    
    # Dmenu
    Key([mod], "d", lazy.run_extension(extension.DmenuRun(
            dmenu_prompt=">",
            dmenu_bottom=True,
            dmenu_font="Noto Sans"
            )
        )
    ),
    
    # Clipboard manager
    Key([mod], "c", lazy.spawn("clipmenu")),

    # Screenshot
    Key([], "Print", lazy.spawn(screenshot)),

    # Toggle floating
    Key([mod], SPACE, lazy.window.toggle_floating()),

    ##Group handling
    # Switch between groups
    Key([mod], "1", lazy.group["web"].toscreen()),
    Key([mod], "2", lazy.group["steam"].toscreen()),
    Key([mod], "3", lazy.group["code"].toscreen()),
    Key([mod], "4", lazy.group["chat"].toscreen()),
    Key([mod], "5", lazy.group["term"].toscreen()),
    Key([mod], "6", lazy.group["etc"].toscreen()),
    
    # Move window to group
    Key([mod, SHIFT], "1", lazy.window.togroup("web")),
    Key([mod, SHIFT], "2", lazy.window.togroup("steam")),
    Key([mod, SHIFT], "3", lazy.window.togroup("code")),
    Key([mod, SHIFT], "4", lazy.window.togroup("chat")),
    Key([mod, SHIFT], "5", lazy.window.togroup("term")),
    Key([mod, SHIFT], "6", lazy.window.togroup("etc")),

    ## Function keys

    # Volume control
    Key([], "XF86AudioRaiseVolume", lazy.spawn(vol_up)),
    Key([], "XF86AudioLowerVolume", lazy.spawn(vol_down)),
    Key([], "XF86AudioMute", lazy.spawn(vol_mute)),
    Key([mod], "v", lazy.spawn("pavucontrol")),
    # Brightness keys
    Key([], "XF86MonBrightnessUp", lazy.spawn(f"{HOME}/.config/qtile/brightness.sh -i")),
    Key([], "XF86MonBrightnessDown", lazy.spawn(f"{HOME}/.config/qtile/brightness.sh -d")),
        
    # Lock key
    Key([mod], "l", lazy.spawn(lock)),
    # Note: Lock key works without mod.  This locks the screen
    # with mod + l
]

layouts = [
    # BSP layout (i3 like)
    layout.Bsp(
        border_focus  = fg,
        border_normal = bg,
        border_width  = 2,
        margin        = 10
    ),
    layout.Floating(
        border_focus = fg,
        border_normal = bg,
    )
]


widget_defaults = dict(
    font= "Inconsolata",
    fontsize= 14,
    padding= 10,
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
                widget.GroupBox(
                    fontsize=10,
                    foreground=fg,
                    background=bg,
                    hide_unused=True,
                    highlight_method="text",
                    center_aligned=False,
                    spacing=4,
                ), #Group list
                widget.Spacer(5),
                widget.Prompt(),
                widget.WindowName(),
                widget.Systray(),
                widget.TextBox("Hello"),
                widget.Battery(
                    format="{char} {percent:2.0%}",
                    low_foreground=b16[1],
                    low_percentage=0.25,
                ),
                widget.Clock(format='%d-%m-%Y %a %H:%M'),
            ],
            # Bar size
            32,
            # Background color
            background=bg,
            # Opacity
            opacity=0.9

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
    {'wmclass': 'pavucontrol'},
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
