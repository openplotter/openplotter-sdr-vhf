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

	print(_('Installing rtl-ais...'))
	try:
		os.chdir('/tmp')
		os.system('rm -rf rtl-ais')
		os.system('git clone https://github.com/dgiardini/rtl-ais')
		os.chdir('rtl-ais')
		os.system('make')
		os.system('make install')
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))

	print(_('Installing kalibrate-rtl...'))
	try:
		os.chdir('/tmp')
		os.system('rm -rf kalibrate-rtl')
		os.system('git clone https://github.com/steve-m/kalibrate-rtl')
		os.chdir('kalibrate-rtl')
		os.system("./bootstrap && CXXFLAGS='-W -Wall -O3'")
		os.system('./configure --prefix=/usr')
		os.system('make')
		os.system('make install')
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))

	print(_('Installing python packages...'))
	try:
		subprocess.call(['pip3', 'install', 'pyrtlsdr', '-U', '--break-system-packages'])
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))

	print(_('Copying udev rules...'))
	try:
		subprocess.call(['cp', '-f', currentdir+'/data/rtl-sdr.rules', '/etc/udev/rules.d/'])
		subprocess.call(['udevadm', 'control', '--reload-rules'])
		subprocess.call(['udevadm', 'trigger'])
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))

	print(_('Setting version...'))
	try:
		conf2.set('APPS', 'sdr_vhf', version)
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))

if __name__ == '__main__':
	main()