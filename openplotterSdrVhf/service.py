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
import sys, subprocess

if sys.argv[1]=='start':
	subprocess.call(['systemctl', 'start', 'signalk.socket'])
	subprocess.call(['systemctl', 'start', 'signalk.service'])
if sys.argv[1]=='stop':
	subprocess.call(['systemctl', 'stop', 'signalk.service'])
	subprocess.call(['systemctl', 'stop', 'signalk.socket'])
if sys.argv[1]=='restart':
	subprocess.call(['systemctl', 'stop', 'signalk.service'])
	subprocess.call(['systemctl', 'stop', 'signalk.socket'])
	subprocess.call(['systemctl', 'start', 'signalk.socket'])
	subprocess.call(['systemctl', 'start', 'signalk.service'])