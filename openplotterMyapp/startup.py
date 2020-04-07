#!/usr/bin/env python3

# This file is part of Openplotter.
# Copyright (C) 2020 by Sailoog <https://github.com/openplotter/openplotter-myapp>
#                     
# Openplotter is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# any later version.
# Openplotter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Openplotter. If not, see <http://www.gnu.org/licenses/>.

import time, os, subprocess, sys
from openplotterSettings import language

class Start(): ### This class will be always called at startup. You should start here only GUI programs. Non GUI progrmas should be started as a services.
	def __init__(self, conf, currentLanguage):
		self.conf = conf
		currentdir = os.path.dirname(os.path.abspath(__file__))
		language.Language(currentdir,'openplotter-myapp',currentLanguage)
		
		self.initialMessage = _('Opening "My app"...') ### "self.initialMessage" will be printed at startup if it has content. If not, the function "start" will not be called. Use trasnlatable text: _('Starting My App...')

	def start(self): ### this funtion will be called only if "self.initialMessage" has content.
		green = '' ### green messages will be printed in green after the "self.initialMessage"
		black = '' ### black messages will be printed in black after the green message
		red = '' ### red messages will be printed in red in a new line

		### start here any GUI program that needs to be started at startup and set the messages.
		green = _('This message should be green')
		black = _('This message should be black')
		red = _('"My app" should open. Uninstall "My app" to remove this.')
		subprocess.Popen('openplotter-myapp')

		time.sleep(1) ### "check" function is always called after "start" function, so if we start any program here we should wait some seconds before checking it. 
		return {'green': green,'black': black,'red': red}

class Check(): ### This class is always called after "start" function and when the user checks the system.
	def __init__(self, conf, currentLanguage):
		self.conf = conf
		currentdir = os.path.dirname(os.path.abspath(__file__))
		language.Language(currentdir,'openplotter-myapp',currentLanguage)
		
		self.initialMessage = _('Checking "My app"...') ### "self.initialMessage" will be printed when checking the system. If it is empty the function check will not be called. Use trasnlatable text: _('Checking My App...')

	def check(self): ### this funtion will be called only if "self.initialMessage" has content.
		green = '' ### green messages will be printed in green after the "self.initialMessage"
		black = '' ### black messages will be printed in black after the green message
		red = '' ### red messages will be printed in red in a new line

		### check here any feature and set the messages
		green = _('"My app" is installed')
		test = subprocess.check_output(['ps','aux']).decode(sys.stdin.encoding)
		if 'openplotter-myapp' in test: black = _('"My app" is running')
		else: black = _('"My app" is not running')
		red = _('Warning example. Uninstall "My app" to remove this.')

		return {'green': green,'black': black,'red': red}

