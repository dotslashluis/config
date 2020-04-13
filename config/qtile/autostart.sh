#!/bin/bash

feh --bg-scale $HOME/Pictures/Wallpapers/1.jpg & # Background
nm-applet & # Network manager applet
compton --config $HOME/.config/picom.conf & # Compositor
clipmenud & # Clipboard manager
light-locker &
