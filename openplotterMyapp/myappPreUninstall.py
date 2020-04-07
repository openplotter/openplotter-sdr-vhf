#!/usr/bin/env python3

# This file is part of Openplotter.
# Copyright (C) 2020 by Sailoog <https://github.com/openplotter/openplotter-myapp>
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

import os
from openplotterSettings import conf
from openplotterSettings import language

def main():
	conf2 = conf.Conf()
	currentdir = os.path.dirname(os.path.abspath(__file__))
	currentLanguage = conf2.get('GENERAL', 'lang')
	package = 'openplotter-myapp' ### replace openplotter-myapp by the name of your package
	language.Language(currentdir, package, currentLanguage)

	print(_('Removing app from OpenPlotter...'))
	try:
		externalApps0 = eval(conf2.get('APPS', 'external_apps'))
		externalApps1 = []
		for i in externalApps0:
			if i['package'] != package: externalApps1.append(i)
		conf2.set('APPS', 'external_apps', str(externalApps1))
		os.system('rm -f /etc/apt/sources.list.d/myapp.list') ### replace myapp.list by the name of your sources file (see myappPostInstall.py script).
		os.system('apt update')
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))

	###
	### Do here whatever you need to remove files and programs before app uninstallation. This file will be executed as sudo. 
	###

	print(_('Removing version...'))
	try:
		conf2.set('APPS', 'myapp', '') ### replace myapp by the name of your app, use the same name in openplotterMyapp.py and myappPostInstall.py scripts.
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))

if __name__ == '__main__':
	main()