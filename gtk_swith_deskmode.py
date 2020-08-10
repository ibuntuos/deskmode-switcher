#!/usr/bin/env python3
#	(c) 2020 by iBuntu OS
# 	08/08/2020
#	Recoding of Deskmode-Switcher for Version 1.3 Catalinux

import PySimpleGUI as sg
import subprocess
from gi.repository import Gio
import os
import sys


light=False
dark=False
sur=False
theme='LightGrey'


#Get current Theme
settings = Gio.Settings.new("org.gnome.shell.extensions.user-theme")
mode=settings.get_string("name")
print(mode)

if mode == "Os-Catalina-gtk" or mode == "WhiteSur-light":
	light=True
	dark=False

if mode == "Mc-OS-CTLina-Gnome-Dark-1.1" or mode == "WhiteSur-dark":
	light=False
	dark=True
	theme='DarkGrey5'

if mode == "WhiteSur-light" or mode == "WhiteSur-dark":
	sur=True

if light == False and dark == False:
	[[sg.popup_error('No Default Screen Mode was selected!')]]


#Define GUI
sg.theme(theme)
winicon='/etc/deskmode-switch/switch_icon.png'
frame_layout = [
	[sg.T('    '), sg.T('Mode'),sg.T('			')],
	[sg.Radio('Bright Mode', "RADIO1", default=light, enable_events=True, key='Bright')],
	[sg.Radio('Dark Mode', "RADIO1", default=dark, enable_events=True, key='Dark')]]


colClose= [[sg.Button('Cancel'), sg.Button('OK')]]

layout = [
	  [sg.T('Select Items from the list below')],
          [sg.Frame('', frame_layout, font='Any 9', title_color='blue')],
	  [sg.Checkbox('Big Sur Design?', default=sur, key="BigSur")],
          [sg.Column(colClose)]
         ]



#Initialize Gui
window = sg.Window('Switch Screenmode', layout, font=("Helvetica", 12), icon=winicon, size=(300, 200), finalize=True)


#Logic
while True:
	event, values = window.read()
	print(values)

	if event == sg.WIN_CLOSED or 'Cancel' in event:
		break

	if event == 'OK':
		if values['Bright'] == True:
			if values['BigSur'] == True:
				os.system('gsettings set org.gnome.shell.extensions.user-theme name "WhiteSur-light"')
				os.system('gsettings set org.gnome.desktop.interface gtk-theme "WhiteSur-light"')
				os.system('gsettings set org.gnome.desktop.interface icon-theme "WhiteSur"')
				os.system('gsettings set net.launchpad.plank.dock.settings:/net/launchpad/plank/docks/dock1/ theme "mcOS-BS-White"')
				os.system('gsettings set org.gnome.desktop.background  picture-uri "file:///usr/share/backgrounds/BigSurBright.png"')
				os.system('gsettings set org.gnome.desktop.screensaver picture-uri "file:///usr/share/backgrounds/BigLock.png"')
				break

			else:
				os.system('gsettings set org.gnome.shell.extensions.user-theme name "Os-Catalina-gtk"')
				os.system('gsettings set org.gnome.desktop.interface gtk-theme "Os-Catalina-gtk"')
				os.system('gsettings set org.gnome.desktop.interface icon-theme "Cupertino-Catalina"')
				os.system('gsettings set net.launchpad.plank.dock.settings:/net/launchpad/plank/docks/dock1/ theme "macOS Catalina Day Default"')
				os.system('gsettings set org.gnome.desktop.background  picture-uri "file:///usr/share/backgrounds/Catalina-13.jpg"')
				os.system('gsettings set org.gnome.desktop.screensaver picture-uri "file:///usr/share/backgrounds/Catalina-13.jpg"')
				break

		if values['Dark'] == True:

			if values['BigSur'] == True:
				os.system('gsettings set org.gnome.shell.extensions.user-theme name "WhiteSur-dark"')
				os.system('gsettings set org.gnome.desktop.interface gtk-theme "WhiteSur-dark"')
				os.system('gsettings set org.gnome.desktop.interface icon-theme "WhiteSur"')
				os.system('gsettings set net.launchpad.plank.dock.settings:/net/launchpad/plank/docks/dock1/ theme "mcOS-BS-Bluish-NS"')
				os.system('gsettings set org.gnome.desktop.background  picture-uri "file:///usr/share/backgrounds/BigSurDark.jpg"')
				os.system('gsettings set org.gnome.desktop.screensaver picture-uri "file:///usr/share/backgrounds/BigLock.png"')
				break

			else:
				os.system('gsettings set org.gnome.shell.extensions.user-theme name "Mc-OS-CTLina-Gnome-Dark-1.1"')
				os.system('gsettings set org.gnome.desktop.interface gtk-theme "Mc-OS-CTLina-Gnome-Dark-1.1"')
				os.system('gsettings set org.gnome.desktop.interface icon-theme "Cupertino-Catalina"')
				os.system('gsettings set net.launchpad.plank.dock.settings:/net/launchpad/plank/docks/dock1/ theme "macOS Catalina Night Default"')
				os.system('gsettings set org.gnome.desktop.background  picture-uri "file:///usr/share/backgrounds/Catalina-15.jpg"')
				os.system('gsettings set org.gnome.desktop.screensaver picture-uri "file:///usr/share/backgrounds/Catalina-13.jpg"')
				break



