#!/bin/bash

feh --bg-scale $HOME/Pictures/Wallpapers/1.jpg & # Background
nm-applet & # Network manager applet
ibus-daemon -drx --panel /usr/lib/ibus/ibus-ui-gtk3 & #ibus applet
compton --config $HOME/.config/picom.conf & # Compositor
clipmenud & # Clipboard manager
light-locker &
