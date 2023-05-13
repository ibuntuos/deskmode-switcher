#!/usr/bin/env python3
#	(c) 2020 by iBuntu OS
# 	08/08/2020
#	Recoding of Deskmode-Switcher for Version 1.3 Catalinux
#       02/04/2023 adjustment for Version 3.0 Monterix

import PySimpleGUI as sg
import subprocess
from gi.repository import Gio
import os
import sys


light=False
dark=False
sur=False
mont=False
ventu=False
theme='LightGrey'


#Get current Theme
settings = Gio.Settings.new("org.gnome.shell.extensions.user-theme")
iconsettings = Gio.Settings.new("org.gnome.desktop.interface")
mode=settings.get_string("name")
icons=iconsettings.get_string("icon-theme")
print(mode)
print(icons)

if mode == "Colloid-Light" or mode == "WhiteSur-Light":
	light=True
	dark=False

if mode == "Colloid-Dark" or mode == "WhiteSur-Dark":
	light=False
	dark=True
	theme='DarkGrey5'

#Which Skin is activated
if mode == "WhiteSur-Light" or mode == "WhiteSur-Dark":
	#Now we know it's not Monterey or Ventura so it only can be Big Sur
	sur = True
	
#The Icon Theme will tell us if it's Monterey or Ventura
if icons == "Ventura-Icons":
	ventu=True
else:
	mont=True


if light == False and dark == False:
	[[sg.popup_error('No Default Screen Mode was selected!')]]


#Define GUI
sg.theme(theme)
winicon='/etc/deskmode-switch/switch_icon.png'
frame_layout = [
	[sg.T('    '), sg.T('Mode'),sg.T('			')],
	[sg.Radio('Bright Mode', "RADIO1", default=light, enable_events=True, key='Bright')],
	[sg.Radio('Dark Mode', "RADIO1", default=dark, enable_events=True, key='Dark')]]

frame_layout2 = [
	[sg.T('    '), sg.T('Skin'),sg.T('			')],
	[sg.Radio('Big Sur', "RADIO2", default=sur, enable_events=True, key='BigSur')],
	[sg.Radio('Monterey', "RADIO2", default=mont, enable_events=True, key='Monterey')],
	[sg.Radio('Ventura', "RADIO2", default=ventu, enable_events=True, key='Ventura')]]
		
colClose= [[sg.Button('Cancel'), sg.Button('OK')]]

layout = [
	  [sg.T('Select Screenmode from the list below')],
          [sg.Frame('', frame_layout, font='Any 9', title_color='blue')],
          [sg.Frame('', frame_layout2, font='Any 9', title_color='blue')],
          [sg.Column(colClose)]
         ]



#Initialize Gui
window = sg.Window('Switch Screenmode', layout, font=("Helvetica", 12), icon=winicon, size=(300, 300), finalize=True)


#Logic
while True:
	event, values = window.read()
	print(values)

	if event == sg.WIN_CLOSED or 'Cancel' in event:
		break

	if event == 'OK':
		if values['Bright'] == True:
			if values['BigSur'] == True:
				os.system('gsettings set org.gnome.shell.extensions.user-theme name "WhiteSur-Light"')
				os.system('gsettings set org.gnome.desktop.interface gtk-theme "WhiteSur-Light"')
				os.system('gsettings set org.gnome.desktop.interface icon-theme "Colloid"')
#				os.system('gsettings set net.launchpad.plank.dock.settings:/net/launchpad/plank/docks/dock1/ theme "mcOS-BS-White"')
				os.system('gsettings set org.gnome.desktop.background  picture-uri "file:///usr/share/backgrounds/WhiteSur-light.png"')
#				os.system('gsettings set org.gnome.desktop.screensaver picture-uri "file:///usr/share/backgrounds/BigLock.png"')
				break

			if values['Monterey'] == True:
				os.system('gsettings set org.gnome.shell.extensions.user-theme name "Colloid-Light"')
				os.system('gsettings set org.gnome.desktop.interface gtk-theme "Colloid-Light"')
				os.system('gsettings set org.gnome.desktop.interface icon-theme "Colloid"')
#				os.system('gsettings set net.launchpad.plank.dock.settings:/net/launchpad/plank/docks/dock1/ theme "macOS Catalina Day Default"')
				os.system('gsettings set org.gnome.desktop.background  picture-uri "file:///usr/share/backgrounds/Monterey-light.png"')
#				os.system('gsettings set org.gnome.desktop.screensaver picture-uri "file:///usr/share/backgrounds/Catalina-13.jpg"')
				break

			if values['Ventura'] == True:
				os.system('gsettings set org.gnome.shell.extensions.user-theme name "Colloid-Light"')
				os.system('gsettings set org.gnome.desktop.interface gtk-theme "Colloid-Light"')
				os.system('gsettings set org.gnome.desktop.interface icon-theme "Ventura-Icons"')
#				os.system('gsettings set net.launchpad.plank.dock.settings:/net/launchpad/plank/docks/dock1/ theme "macOS Catalina Day Default"')
				os.system('gsettings set org.gnome.desktop.background  picture-uri "file:///usr/share/backgrounds/macos_ventura_bright.jpg"')
#				os.system('gsettings set org.gnome.desktop.screensaver picture-uri "file:///usr/share/backgrounds/macos_ventura_bright.jpg"')
				break
		if values['Dark'] == True:

			if values['BigSur'] == True:
				os.system('gsettings set org.gnome.shell.extensions.user-theme name "WhiteSur-Dark"')
				os.system('gsettings set org.gnome.desktop.interface gtk-theme "WhiteSur-Dark"')
				os.system('gsettings set org.gnome.desktop.interface icon-theme "Colloid"')
#				os.system('gsettings set net.launchpad.plank.dock.settings:/net/launchpad/plank/docks/dock1/ theme "mcOS-BS-Bluish-NS"')
				os.system('gsettings set org.gnome.desktop.background  picture-uri "file:///usr/share/backgrounds/WhiteSur-dark.png"')
#				os.system('gsettings set org.gnome.desktop.screensaver picture-uri "file:///usr/share/backgrounds/BigLock.png"')
				break

			if values['Monterey'] == True:
				os.system('gsettings set org.gnome.shell.extensions.user-theme name "Colloid-Dark"')
				os.system('gsettings set org.gnome.desktop.interface gtk-theme "Colloid-Dark"')
				os.system('gsettings set org.gnome.desktop.interface icon-theme "Colloid"')
	#			os.system('gsettings set net.launchpad.plank.dock.settings:/net/launchpad/plank/docks/dock1/ theme "macOS Catalina Night Default"')
				os.system('gsettings set org.gnome.desktop.background  picture-uri "file:///usr/share/backgrounds/Monterey-dark.png"')
	#			os.system('gsettings set org.gnome.desktop.screensaver picture-uri "file:///usr/share/backgrounds/Catalina-13.jpg"')
				break

			if values['Ventura'] == True:
				os.system('gsettings set org.gnome.shell.extensions.user-theme name "Colloid-Dark"')
				os.system('gsettings set org.gnome.desktop.interface gtk-theme "Colloid-Dark"')
				os.system('gsettings set org.gnome.desktop.interface icon-theme "Ventura-Icons"')
#				os.system('gsettings set net.launchpad.plank.dock.settings:/net/launchpad/plank/docks/dock1/ theme "macOS Catalina Day Default"')
				os.system('gsettings set org.gnome.desktop.background  picture-uri "file:///usr/share/backgrounds/macos_ventura_dark.jpg"')
#				os.system('gsettings set org.gnome.desktop.screensaver picture-uri "file:///usr/share/backgrounds/macos_ventura_bright.jpg"')
				break

