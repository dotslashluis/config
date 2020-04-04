#!/bin/bash

feh --bg-scale $HOME/Wallpapers/1.jpg & # Background
nm-applet & # Network manager applet
compton --config $HOME/.config/picom.conf & # Compositor
ibus-daemon -drx --panel /usr/lib/ibus/ibus-ui-gtk3 & # iBus applet
clipmenud & # Clipboard manager
light-locker &
