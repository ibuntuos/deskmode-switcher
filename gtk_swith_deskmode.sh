#!/bin/bash
#####################################################
# (c) 2020 by iBuntu OS
# 
# Script for Changing Desktopmode in iBuntu
# 
#V 1.0   09.01.2020 (Th)
#V 1.1   04.07.2020 (Sa)
#V 1.2   08.08.2020 (Sa)
#####################################################

#get actual chosen theme and set values for zenity checkbox to FALSE
mode=`gsettings get org.gnome.shell.extensions.user-theme name`
light="FALSE"
dark="FALSE"

#check if Light-Mode is enabled
if  [ "$mode" = "'Os-Catalina-gtk'" ] ||  [ "$mode" = "'WhiteSur-light'" ]; then

	light="TRUE"
	dark="FALSE"
elif  [ "$mode" = "'Mc-OS-CTLina-Gnome-Dark-1.1'" ] || [  "$mode" = "'WhiteSur-dark'" ]; then

	light="FALSE"
	dark="TRUE"
else
	zenity --info --text "No Deafault Screen Mode was selected!" --width=400
fi

#zenity GUI for choosing Screenmode
change=`zenity --list --radiolist --title="Switch Screenmode" --column "" --column "Mode"  $light 'Bright Mode'  $dark  'Dark Mode'`


if  [ "$change" = "Bright Mode" ]; then

gsettings set org.gnome.shell.extensions.user-theme name "Os-Catalina-gtk"
gsettings set org.gnome.desktop.interface gtk-theme "Os-Catalina-gtk"
gsettings set net.launchpad.plank.dock.settings:/net/launchpad/plank/docks/dock1/ theme "macOS Catalina Day Default"
gsettings set org.gnome.desktop.background  picture-uri "file:///usr/share/backgrounds/Catalina-13.jpg"


elif  [ "$change" = "Dark Mode" ]; then

gsettings set org.gnome.shell.extensions.user-theme name "Mc-OS-CTLina-Gnome-Dark-1.1"
gsettings set org.gnome.desktop.interface gtk-theme "Mc-OS-CTLina-Gnome-Dark-1.1"
gsettings set net.launchpad.plank.dock.settings:/net/launchpad/plank/docks/dock1/ theme "macOS Catalina Night Default"
gsettings set org.gnome.desktop.background  picture-uri "file:///usr/share/backgrounds/Catalina-15.jpg"


else
exit 0
fi

