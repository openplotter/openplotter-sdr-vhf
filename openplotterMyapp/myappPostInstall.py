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

import os, sys, subprocess
from openplotterSettings import conf
from openplotterSettings import language
from openplotterSettings import platform
from .version import version

def main():
	conf2 = conf.Conf()
	currentdir = os.path.dirname(os.path.abspath(__file__))
	currentLanguage = conf2.get('GENERAL', 'lang')
	package = 'openplotter-myapp' ### replace by the name of your package
	language.Language(currentdir, package, currentLanguage)
	platform2 = platform.Platform()

	app = {
	'name': 'My app', ### replace My app by your app name
	'platform': 'both', ### rpi, debian or both
	'package': package,
	'preUninstall': platform2.admin+' '+'myappPreUninstall', ### replace myappPreUninstall by your pre uninstall entry point (see setup.py file).
	'uninstall': package,
	'sources': ['https://dl.cloudsmith.io/public/openplotter/openplotter-external/deb/debian buster'], ### replace by your repositories URLs separated by commas.
	'dev': 'no', ### set to "yes" if you do not want your app to be updated from repositories yet.
	'entryPoint': 'openplotter-myapp', ### replace by your app GUI entry point (see setup.py file).
	'postInstall': platform2.admin+' '+'myappPostInstall', ### replace myappPostInstall by your post install entry point (see setup.py file).
	'reboot': 'no', ### set to "yes" if you want to shown a message "Reboot to apply changes" after updating from openplotter-settings.
	'module': 'openplotterMyapp' ### replace by your python module name (see setup.py file).
	}
	gpgKey = currentdir+'/data/myapp.gpg.key' ### replace by the path to your gpg key file. Replace contents of this file by your key.
	sourceList = currentdir+'/data/myapp.list' ### replace by the path to your sources list file. Replace contents of this file by your packages sources.

	print(_('Adding app to OpenPlotter...'))
	try:
		externalApps1 = []
		try:
			externalApps0 = eval(conf2.get('APPS', 'external_apps'))
		except: externalApps0 = []
		for i in externalApps0:
			if i['package'] != package: externalApps1.append(i)
		externalApps1.append(app)
		conf2.set('APPS', 'external_apps', str(externalApps1))
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))

	print(_('Checking sources...'))
	try:
		sources = subprocess.check_output('apt-cache policy', shell=True).decode(sys.stdin.encoding)
		exists = True
		for i in app['sources']:
			if not i in sources: exists = False
		if not exists:
			os.system('cp '+sourceList+' /etc/apt/sources.list.d')
			os.system('apt-key add - < '+gpgKey)
			os.system('apt update')
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))

	###
	### Do here whatever you need after package installation. This file will be executed as sudo. 
	###
	
	print(_('Setting version...'))
	try:
		conf2.set('APPS', 'myapp', version) ### replace myapp by the name of your app, use the same name in openplotterMyapp.py and myappPreUninstall.py scripts.
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))

if __name__ == '__main__':
	main()