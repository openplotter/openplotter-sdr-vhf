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
import sys, subprocess, os
from openplotterSettings import conf

def onKillProcesses():
	subprocess.call(['pkill', '-15', 'rtl_test'])
	subprocess.call(['pkill', '-15', 'kal'])
	subprocess.call(['pkill', '-15', 'rtl_eeprom'])
	subprocess.call(['pkill', '-15', 'gqrx'])
	subprocess.call(['pkill', '-15', 'welle-io'])
	subprocess.call(['pkill', '-15', 'w_scan'])
	subprocess.call(['pkill', '-15', 'vlc'])

conf2 = conf.Conf()

if sys.argv[1]=='stopProcesses':
	onKillProcesses()
	subprocess.call(['systemctl', 'stop', 'openplotter-rtl_ais'])
	subprocess.call(['systemctl', 'stop', 'dump1090-fa'])
	subprocess.call(['systemctl', 'stop', 'piaware'])

if sys.argv[1]=='restartProcesses':
	onKillProcesses()
	try:
		subprocess.check_output(['systemctl', 'is-enabled', 'openplotter-rtl_ais']).decode(sys.stdin.encoding)
		subprocess.call(['systemctl', 'restart', 'openplotter-rtl_ais'])
	except: pass
	try:
		subprocess.check_output(['systemctl', 'is-enabled', 'dump1090-fa']).decode(sys.stdin.encoding)
		subprocess.call(['systemctl', 'restart', 'dump1090-fa'])
	except: pass
	try:
		subprocess.check_output(['systemctl', 'is-enabled', 'piaware']).decode(sys.stdin.encoding)
		subprocess.call(['systemctl', 'restart', 'piaware'])
	except: pass
	try:
		subprocess.call(['systemctl', 'stop', 'signalk.service'])
		subprocess.call(['systemctl', 'stop', 'signalk.socket'])
		subprocess.call(['systemctl', 'start', 'signalk.socket'])
		subprocess.call(['systemctl', 'start', 'signalk.service'])
	except: pass
	subprocess.call(['service', 'lighttpd', 'restart'])

if sys.argv[1]=='editAdsb':
	index = sys.argv[2]
	gain = sys.argv[3]
	ppm = sys.argv[4]
	port = sys.argv[5]
	settings = 'RECEIVER_OPTIONS="--device-index '+index+' --gain '+gain+' --ppm '+ppm+'"'
	settingsPort = '$SERVER["socket"] == ":'+port+'" {'

	file = open('/etc/default/dump1090-fa', 'r')
	file1 = open('dump1090-fa', 'w')
	while True:
		line = file.readline()
		if not line: break
		if 'RECEIVER_OPTIONS' in line: 
			file1.write(settings+'\n')
		else: file1.write(line)
	file.close()
	file1.close()

	file = open('/etc/lighttpd/conf-available/89-dump1090-fa.conf', 'r')
	file1 = open('89-dump1090-fa.conf', 'w')
	while True:
		line = file.readline()
		if not line: break
		if '$SERVER["socket"]' in line: 
			file1.write(settingsPort+'\n')
		else: file1.write(line)
	file.close()
	file1.close()

	if os.system('diff dump1090-fa /etc/default/dump1090-fa > /dev/null'):
		os.system('mv dump1090-fa /etc/default')
	else: os.system('rm -f dump1090-fa')

	if os.system('diff 89-dump1090-fa.conf /etc/lighttpd/conf-available/89-dump1090-fa.conf > /dev/null'):
		os.system('mv 89-dump1090-fa.conf /etc/lighttpd/conf-available')
	else: os.system('rm -f 89-dump1090-fa.conf')

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
