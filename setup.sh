#!/bin/bash

# This script is made for installing the required dependencies for this setup.  Run as sudo otherwise it won't work

mkdir $HOME/.config

REPO_DIR=$( pwd )


sudo pacman -S qtile xscreensaver fcitx alacritty picom network-manager-applet feh clipmenu curl vim xf86-video-amdgpu

# Now copy the files
cp -r config/* $HOME/.config
cp -r home $HOME 
sudo cp xorg.conf.d/* /etc/X11/xorg.conf.d/



