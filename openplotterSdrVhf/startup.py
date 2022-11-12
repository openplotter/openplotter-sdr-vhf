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
		
		self.initialMessage = _('Checking SDR processes conflicts...')

	def check(self):
		green = ''
		black = ''
		red = ''

		worksAis = False
		worksAdsb = False
		indexAdsb = ''
		indexAis = self.conf.get('SDR-VHF', 'sdraisdeviceindex')
		try:
			with open('/etc/default/dump1090-fa', 'r') as f:
				for line in f:
					if 'RECEIVER_OPTIONS=' in line:
						line = line.replace('\n', '')
						line = line.strip()
						items = line.split('=')
						item1 = items[1].replace('"', '')
						item1 = item1.strip()
						options = item1.split(' ')
						#--device-index 1 --gain -10 --ppm 0
						indexAdsb = options[1]
		except Exception as e: print(str(e))
		if indexAis == indexAdsb:
			try:
				subprocess.check_output(['systemctl', 'is-enabled', 'openplotter-rtl_ais']).decode(sys.stdin.encoding)
				worksAis = True
			except: worksAis = False
			try:
				subprocess.check_output(['systemctl', 'is-enabled', 'dump1090-fa']).decode(sys.stdin.encoding)
				worksAdsb = True
			except: worksAdsb = False
			if worksAis and worksAdsb:
				red = _('AIS and ADS-B processes are trying to read the same SDR device.')
			else:
				green = _('no conflicts')
		else:
			green = _('no conflicts')

		return {'green': green,'black': black,'red': red}
