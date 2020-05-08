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

def main():
	conf2 = conf.Conf()
	currentdir = os.path.dirname(os.path.abspath(__file__))
	currentLanguage = conf2.get('GENERAL', 'lang')
	language.Language(currentdir,'openplotter-sdr-vhf',currentLanguage)

	print(_('Installing GQRX...'))
	try:
		subprocess.call(('apt install -y gqrx-sdr').split())
		if not os.path.isdir(conf2.home+'/.config/gqrx'):
			subprocess.call(('mkdir ' + conf2.home+'/.config/gqrx').split())
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))

	print(_('Configuring GQRX...'))
	try:
		file = conf2.home+'/.config/gqrx/bookmarks.csv'
		if not os.path.isfile(file):	
			subprocess.call((' cp ' + currentdir + '/data/bookmarks.csv ' + conf2.home + '/.config/gqrx/').split())
		file = conf2.home+'/.config/gqrx/default.conf'
		if not os.path.isfile(file):	
			subprocess.call((' cp ' + currentdir + '/data/default.conf ' + conf2.home + '/.config/gqrx/').split())
		subprocess.call(['chown', '-R', conf2.user, conf2.home+'/.config/gqrx'])
		subprocess.call(('rm -f /usr/share/applications/gnuradio-grc.desktop').split())
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))

if __name__ == '__main__':
	main()
