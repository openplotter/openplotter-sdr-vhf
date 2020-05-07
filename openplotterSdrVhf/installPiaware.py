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

import os, subprocess, sys
from openplotterSettings import conf
from openplotterSettings import language

def main():
	conf2 = conf.Conf()
	currentdir = os.path.dirname(os.path.abspath(__file__))
	currentLanguage = conf2.get('GENERAL', 'lang')
	language.Language(currentdir,'openplotter-sdr-vhf',currentLanguage)

	print(_('Checking sources...'))
	try:
		sources = subprocess.check_output('apt-cache policy', shell=True).decode(sys.stdin.encoding)
		source = 'http://flightaware.com/adsb/piaware/files/packages'
		gpgKey = currentdir+'/data/flightaware-archive-keyring.gpg'
		sourceList = currentdir+'/data/piaware-buster.list'
		if not source in sources: 
			os.system('cp '+sourceList+' /etc/apt/sources.list.d')
			os.system('cp '+gpgKey+' /etc/apt/trusted.gpg.d')
			os.system('apt update')
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))

	print(_('Installing piaware and dump1090-fa...'))
	try:
		subprocess.call(('apt install -y piaware dump1090-fa').split())
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))

	print(_('Configuring piaware...'))
	try:
		subprocess.call(('piaware-config allow-auto-updates yes').split())
		subprocess.call(('piaware-config allow-manual-updates yes').split())
		subprocess.call(('cp -f '+currentdir+'/data/adsb.png /usr/share/pixmaps/').split())
		subprocess.call(('cp -f '+currentdir+'/data/adsb.desktop /usr/share/applications/').split())
		subprocess.call(('ln -s /etc/lighttpd/conf-available/89-dump1090-fa.conf /etc/lighttpd/conf-enabled/89-dump1090-fa.conf').split())
		subprocess.call(('ln -s /etc/lighttpd/conf-available/88-dump1090-fa-statcache.conf /etc/lighttpd/conf-enabled/88-dump1090-fa-statcache.conf').split())
		subprocess.call(('service lighttpd restart').split())
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))

if __name__ == '__main__':
	main()
