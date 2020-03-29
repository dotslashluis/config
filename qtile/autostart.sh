#!/bin/bash

feh --bg-scale $HOME/Pictures/Backgrounds/wallpaper.png &
nm-applet &
xscreensaver -no-splash &
compton --config $HOME/.config/picom.conf &
ibus-daemon -drx --panel /usr/lib/ibus/ibus-ui-gtk3 &
clipmenud &

