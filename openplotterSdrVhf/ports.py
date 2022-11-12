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

import os, subprocess, sys
from openplotterSettings import language

class Ports:
	def __init__(self,conf,currentLanguage):
		self.conf = conf
		currentdir = os.path.dirname(os.path.abspath(__file__))
		language.Language(currentdir,'openplotter-sdr-vhf',currentLanguage)
		self.connections = []

		command = 'systemctl show openplotter-rtl_ais --no-page'
		output = subprocess.check_output(command.split(),universal_newlines=True)
		if 'SubState=running' in output: self.ais= True
		else: self.ais= False

		command = 'systemctl show dump1090-fa --no-page'
		output = subprocess.check_output(command.split(),universal_newlines=True)
		if 'SubState=running' in output: self.adsb= True
		else: self.adsb= False

	def usedPorts(self):
		usedPorts = []
		if self.ais:
			sdrAisPort = self.conf.get('SDR-VHF', 'sdraisport')
			usedPorts.append({'id':'rtl-ais', 'description':_('SDR AIS output'), 'data':'NMEA 0183', 'direction':'2', 'type':'UDP', 'mode':'client', 'address':'localhost', 'port':sdrAisPort, 'editable':'1'})
		if self.adsb:
			try:
				with open('/etc/lighttpd/conf-available/89-dump1090-fa.conf', 'r') as f:
					for line in f:
						#$SERVER["socket"] == ":8081" {
						if '$SERVER["socket"]' in line:
							line = line.replace('\n', '')
							line = line.strip()
							items = line.split('==')
							item1 = items[1].replace('"', '')
							item1 = item1.replace(':', '')
							item1 = item1.replace('{', '')
							sdrAdsbPort = item1.strip()
			except Exception as e: print(str(e))
			usedPorts.append({'id':'adsb1', 'description':_('SDR ADS-B web interface'), 'data':'', 'direction':'3', 'type':'TCP', 'mode':'server', 'address':'localhost', 'port':sdrAdsbPort, 'editable':'1'})
			usedPorts.append({'id':'adsb2', 'description':_('SDR ADS-B decoder'), 'data':'', 'direction':'3', 'type':'TCP', 'mode':'server', 'address':'localhost', 'port':'30002', 'editable':'0'})
			usedPorts.append({'id':'adsb3', 'description':_('SDR ADS-B decoder'), 'data':'', 'direction':'3', 'type':'TCP', 'mode':'server', 'address':'localhost', 'port':'30003', 'editable':'0'})
			usedPorts.append({'id':'adsb4', 'description':_('SDR ADS-B decoder'), 'data':'', 'direction':'3', 'type':'TCP', 'mode':'server', 'address':'localhost', 'port':'30004', 'editable':'0'})
			usedPorts.append({'id':'adsb5', 'description':_('SDR ADS-B decoder'), 'data':'', 'direction':'3', 'type':'TCP', 'mode':'server', 'address':'localhost', 'port':'30005', 'editable':'0'})
			usedPorts.append({'id':'adsb6', 'description':_('SDR ADS-B decoder'), 'data':'', 'direction':'3', 'type':'TCP', 'mode':'server', 'address':'localhost', 'port':'30104', 'editable':'0'})


		return usedPorts
