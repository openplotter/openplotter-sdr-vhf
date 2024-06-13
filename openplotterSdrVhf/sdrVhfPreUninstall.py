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

def main():
	conf2 = conf.Conf()
	currentdir = os.path.dirname(os.path.abspath(__file__))
	currentLanguage = conf2.get('GENERAL', 'lang')
	package = 'openplotter-sdr-vhf'
	language.Language(currentdir, package, currentLanguage)

	print(_('Removing python packages...'))
	try:
		subprocess.call(['pip3', 'uninstall', '-y', 'pyrtlsdr', '--break-system-packages'])
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))

	subprocess.call(('python3 '+currentdir+'/unInstallGqrx.py').split())
	subprocess.call(('python3 '+currentdir+'/unInstallDvbt.py').split())
	subprocess.call(('apt autoremove -y welle.io').split())

	print(_('Removing version...'))
	try:
		conf2.set('APPS', 'sdr_vhf', '')
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))

if __name__ == '__main__':
	main()