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

from setuptools import setup
from openplotterSdrVhf import version

setup (
	name = 'openplotterSdrVhf',
	version = version.version,
	description = 'Suite of applications for SDR reception in VHF range',
	license = 'GPLv3',
	author="Sailoog/e-sailing",
	author_email='info@sailoog.com',
	url='https://github.com/openplotter/openplotter-sdr-vhf',
	packages=['openplotterSdrVhf'],
	classifiers = ['Natural Language :: English',
	'Operating System :: POSIX :: Linux',
	'Programming Language :: Python :: 3'],
	include_package_data=True,
	entry_points={'console_scripts': ['openplotter-sdr-vhf=openplotterSdrVhf.openplotterSdrVhf:main','sdrVhfPostInstall=openplotterSdrVhf.sdrVhfPostInstall:main','sdrVhfPreUninstall=openplotterSdrVhf.sdrVhfPreUninstall:main']},
	data_files=[('share/applications', ['openplotterSdrVhf/data/openplotter-sdr-vhf.desktop']),('share/pixmaps', ['openplotterSdrVhf/data/openplotter-sdr-vhf.png']),],
	)
