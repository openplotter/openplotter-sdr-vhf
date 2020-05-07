#!/usr/bin/env python3

# This file is part of Openplotter.
# Copyright (C) 2020 by Sailoog <https://github.com/openplotter/openplotter-sdr-vhf>
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
import sys, subprocess, time
from openplotterSettings import conf

def onKillProcesses():
	subprocess.call(['pkill', '-15', 'rtl_test'])
	subprocess.call(['pkill', '-15', 'kal'])
	subprocess.call(['pkill', '-15', 'rtl_eeprom'])
	subprocess.call(['pkill', '-15', 'gqrx'])
	subprocess.call(['pkill', '-15', 'welle-io'])
	subprocess.call(['pkill', '-15', 'w_scan'])
	subprocess.call(['pkill', '-15', 'vlc'])
	time.sleep(1)

conf2 = conf.Conf()

if sys.argv[1]=='stopProcesses':
	onKillProcesses()
	subprocess.call(['systemctl', 'stop', 'openplotter-rtl_ais'])

if sys.argv[1]=='restartProcesses':
	onKillProcesses()
	sdraisdeviceindex = conf2.get('SDR-VHF', 'sdraisdeviceindex')
	if sdraisdeviceindex: subprocess.call(['systemctl', 'restart', 'openplotter-rtl_ais'])
	else: subprocess.call(['systemctl', 'stop', 'openplotter-rtl_ais'])
	try:
		subprocess.call(['systemctl', 'stop', 'signalk.service'])
		subprocess.call(['systemctl', 'stop', 'signalk.socket'])
		subprocess.call(['systemctl', 'start', 'signalk.socket'])
		subprocess.call(['systemctl', 'start', 'signalk.service'])
	except: pass