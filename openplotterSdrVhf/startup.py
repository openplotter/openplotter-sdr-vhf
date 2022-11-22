#!/usr/bin/env python3

# This file is part of OpenPlotter.
# Copyright (C) 2022 by Sailoog <https://github.com/openplotter/openplotter-sdr-vhf>
# Copyright (C) 2020 by e-sailing <https://github.com/e-sailing/openplotter-sdr-vhf>
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

import os, sys, subprocess
from openplotterSettings import language

class Start(): 
	def __init__(self, conf, currentLanguage):
		self.conf = conf
		currentdir = os.path.dirname(os.path.abspath(__file__))
		language.Language(currentdir,'openplotter-sdr-vhf',currentLanguage)
		
		self.initialMessage = ''

	def start(self):
		green = ''
		black = ''
		red = ''

		return {'green': green,'black': black,'red': red}

class Check(): 
	def __init__(self, conf, currentLanguage):
		self.conf = conf
		currentdir = os.path.dirname(os.path.abspath(__file__))
		language.Language(currentdir,'openplotter-sdr-vhf',currentLanguage)
		
		self.initialMessage = _('Checking SDR processes...')

	def check(self):
		green = ''
		black = ''
		red = ''

		try:
			subprocess.check_output(['systemctl', 'is-active', 'openplotter-rtl_ais']).decode(sys.stdin.encoding)
			green = _('SDR AIS is running')
		except:
			black = _('SDR AIS is not running')

		return {'green': green,'black': black,'red': red}
