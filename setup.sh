#!/bin/bash

# Create the .config, alacritty and qtile directories
mkdir -p $HOME/.config/qtile $HOME/.config/alacritty

# Now copy the repo to the .config directory so the configuration looks cleaner
[ "$( pwd )" == "$HOME/.config/dotfiles" ] && mkdir -p $HOME/.config/dotfile && cp -r ./* .config/dotfiles/
cd $HOME/.config/dotfiles

## Link the fuck out of everything
# HOME DOTFILES
ln home/bashrc $HOME/.bashrc || echo "ERROR - Couldn't link bashrc"
ln home/Xresources $HOME/.Xresources || "ERROR - Couldn't link Xresources"
ln home/pam_profile $HOME/.pam_profile || "ERROR - Couldn't link pam_profile"
ln home/bash_profile $HOME/.bash_profile || "ERROR - Couldn't link bash_profile"
ln home/vimrc $HOME/.vimrc || "ERROR - Couldn't link vimrc"

# QTILE
ln config/qtile/config.py $HOME/config/qtile/config.py
ln config/qtile/autostart.sh $HOME/config/qtile/autostart.sh
ln config/qtile/brightness.sh $HOME/config/qtile/brightness.sh

# ALACRITTY
ln config/alacritty/alacritty.yml $HOME/.config/alacritty/alacritty.yml
