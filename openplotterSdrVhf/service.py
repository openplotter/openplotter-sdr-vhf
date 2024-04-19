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

import sys, subprocess, os
from openplotterSettings import conf

conf2 = conf.Conf()

if sys.argv[1]=='stopProcesses':
	subprocess.call(['pkill', '-15', 'rtl_test'])
	subprocess.call(['pkill', '-15', 'kal'])
	subprocess.call(['pkill', '-15', 'rtl_eeprom'])
	subprocess.call(['pkill', '-15', 'gqrx'])
	subprocess.call(['pkill', '-15', 'welle-io'])
	subprocess.call(['pkill', '-15', 'w_scan'])
	subprocess.call(['pkill', '-15', 'vlc'])
	subprocess.call(['systemctl', 'stop', 'ais-catcher'])

if sys.argv[1]=='startProcesses':
	try:
		subprocess.check_output(['systemctl', 'is-enabled', 'ais-catcher']).decode(sys.stdin.encoding)
		subprocess.call(['systemctl', 'restart', 'ais-catcher'])
	except: subprocess.call(['systemctl', 'stop', 'ais-catcher'])
	try:
		subprocess.call(['systemctl', 'stop', 'signalk.service'])
		subprocess.call(['systemctl', 'stop', 'signalk.socket'])
		subprocess.call(['systemctl', 'start', 'signalk.socket'])
		subprocess.call(['systemctl', 'start', 'signalk.service'])
	except: pass

if sys.argv[1]=='editSdrAis':
	gain = sys.argv[2]
	if not gain: gain = 'auto'
	sdraisppm = sys.argv[3]
	if not sdraisppm: sdraisppm = '0'
	sdraisdeviceindex = sys.argv[4]
	if not sdraisdeviceindex: sdraisdeviceindex = '0'
	sdraisport = sys.argv[5]
	if not sdraisport: sdraisport = '10110'
	enable = sys.argv[6]
	if not enable: enable = '0'
	share = sys.argv[7]
	if share == '1': share = ' -X'
	else: share = ''

	try:
		fo = open('/etc/default/ais-catcher', "w")
		fo.write('OPTS=" -gr RTLAGC on TUNER '+gain+' -a 192K -p '+sdraisppm+' -d:'+sdraisdeviceindex+' -q -u 127.0.0.1 '+sdraisport+' -N 8100 CDN /usr/share/ais-catcher-webassets'+share+'"')
		fo.close()
		if enable == '1': subprocess.call(['systemctl', 'enable', 'ais-catcher'])
		else: subprocess.call(['systemctl', 'disable', 'ais-catcher'])
	except Exception as e: print(str(e))
