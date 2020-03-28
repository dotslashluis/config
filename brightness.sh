#!/bin/bash

# Current brightness
oldb=$(cat /sys/class/backlight/amdgpu_bl0/brightness)

# Max brightness
maxb=$(cat /sys/class/backlight/amdgpu_bl0/max_brightness)

# Brightness step
step=30

# Calculate the new brightness
if [[ "$1" == "-d" ]]; then
    newb=$((oldb-step))
elif [[ "$1" == "-i" ]]; then
    newb=$((oldb+step))
fi

# Conditional so that brightness doesn't go above the max or below 0
if [[ $newb  -le $maxb ]] && [[ $newb -gt $step ]]; then
    echo $newb > /sys/class/backlight/amdgpu_bl0/brightness
fi
