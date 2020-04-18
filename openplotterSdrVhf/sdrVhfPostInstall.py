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

import os, subprocess
from openplotterSettings import conf
from openplotterSettings import language
from openplotterSettings import platform
from .version import version

def main():
	conf2 = conf.Conf()
	platform2 = platform.Platform()
	currentdir = os.path.dirname(os.path.abspath(__file__))
	currentLanguage = conf2.get('GENERAL', 'lang')
	package = 'openplotter-sdr-vhf'
	language.Language(currentdir, package, currentLanguage)

	print(_('Installing python packages...'))
	try:
		subprocess.call(['pip3', 'install', 'pyrtlsdr'])
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))

	print(_('Adding rtl_ais service...'))
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
		'EnvironmentFile='+conf2.home+'/.openplotter/openplotter.conf\n'+
		'ExecStart=rtl_ais -d $sdraisdeviceindex -p $sdraisppm -P $sdraisport\n'+
		'Restart=always\n'+
		'RestartSec=30\n'+
		'KillMode=process\n\n'+
		'[Install]\n'+
		'WantedBy=multi-user.target\n'
		)
		fo.close()
		subprocess.call((' systemctl daemon-reload').split())
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))

	print(_('Setting version...'))
	try:
		conf2.set('APPS', 'sdr_vhf', version)
	except Exception as e: print(_('FAILED: ')+str(e))

if __name__ == '__main__':
	main()