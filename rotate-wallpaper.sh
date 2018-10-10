#!/bin/sh

# A simple script to change wallpapers at a regular interval.
# Designed for/tested on Ubuntu 16.04.

# Add this script to your crontab (with `crontab -e`). To change your desktop
# wallpaper every 10 minutes, you would add the following line to crontab:
#
# */10 * * * * /bin/bash /path/to/this/script.sh

wallpaperDirectory="$HOME/Pictures/Wallpapers/Firewatch" # Edit this. Point it to the directory where your wallpaper images are stored.
randomPicture=$(ls $wallpaperDirectory | shuf -n1) # grabs a random picture from the wallpaper directory.
gsettings set org.gnome.desktop.background picture-uri "file://$wallpaperDirectory/$randomPicture" #update the wallpaper
