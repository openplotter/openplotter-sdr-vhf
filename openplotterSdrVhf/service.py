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
	subprocess.call(['systemctl', 'stop', 'openplotter-rtl_ais'])

if sys.argv[1]=='startProcesses':
	try:
		subprocess.check_output(['systemctl', 'is-enabled', 'openplotter-rtl_ais']).decode(sys.stdin.encoding)
		subprocess.call(['systemctl', 'restart', 'openplotter-rtl_ais'])
	except: pass

	try:
		subprocess.call(['systemctl', 'stop', 'signalk.service'])
		subprocess.call(['systemctl', 'stop', 'signalk.socket'])
		subprocess.call(['systemctl', 'start', 'signalk.socket'])
		subprocess.call(['systemctl', 'start', 'signalk.service'])
	except: pass

if sys.argv[1]=='editSdrAis':
	home = sys.argv[2]
	gain = sys.argv[3]
	if gain == 'auto': 
		execStart = 'ExecStart=/usr/bin/rtl_ais -d $sdraisdeviceindex -p $sdraisppm -P $sdraisport\n'
	else: 
		execStart = 'ExecStart=/usr/bin/rtl_ais -d $sdraisdeviceindex -p $sdraisppm -g $sdraisgain -P $sdraisport\n'
	try:
		fo = open('/etc/systemd/system/openplotter-rtl_ais.service', "w")
		fo.write(
		'[Unit]\n'+
		'Description = Decode AIS received by rtl-sdr and send as NMEA 0183 to UDP port\n'+
		'After=syslog.target network.target audit.service\n'+
		'StartLimitInterval=200\n'+
		'StartLimitBurst=5\n'+
		'[Service]\n'+
		'Type=simple\n'+
		'User=root\n'+
		'EnvironmentFile='+home+'/.openplotter/openplotter.conf\n'+
		execStart+
		'Restart=always\n'+
		'RestartSec=30\n'+
		'KillMode=process\n\n'+
		'[Install]\n'+
		'WantedBy=multi-user.target\n'
		)
		fo.close()
		subprocess.call((' systemctl daemon-reload').split())
	except Exception as e: print(str(e))
