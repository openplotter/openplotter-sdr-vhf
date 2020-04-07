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

from setuptools import setup
from openplotterMyapp import version ### replace openplotterMyapp by your python module name, See below.

setup (
	name = 'openplotterMyapp', ### replace by the python module name of your app. This must be lowerCamelCase and must match the name of the folder openplotterMyapp.
	version = version.version,
	description = 'This is a template to help create apps for OpenPlotter', ### replace by your description.
	license = 'GPLv3',
	author="xxxx", ### replace by your name.
	author_email='xxxx@xxxx.com', ### replace by your email.
	url='https://github.com/openplotter/openplotter-myapp', ### replace by your project in github.
	packages=['openplotterMyapp'], ### this must match the name of the folder openplotterMyapp.
	classifiers = ['Natural Language :: English',
	'Operating System :: POSIX :: Linux',
	'Programming Language :: Python :: 3'],
	include_package_data=True,
	entry_points={'console_scripts': ['openplotter-myapp=openplotterMyapp.openplotterMyapp:main','myappPostInstall=openplotterMyapp.myappPostInstall:main','myappPreUninstall=openplotterMyapp.myappPreUninstall:main']},
	### entry_points: creating entry points you will be able to run these python scripts from everywhere.
		### openplotter-myapp = This is the GUI of your app
		### myappPostInstall = This file must be executed after the package installation and it should contain any extra task like installing pip packages, creating services... 
		### myappPreUninstall = This file must be executed before the package uninstallation. Here you should revert all changes in myappPostInstall.
	data_files=[('share/applications', ['openplotterMyapp/data/openplotter-myapp.desktop']),('share/pixmaps', ['openplotterMyapp/data/openplotter-myapp.png']),],
	### data_files = Add files to the host system. This will work only when installed as debian package, not as python module.
	)

	### MORE REQUIRED CHANGES

	### replace openplotterMyapp in MANIFEST.in file by your python module name.

	### replace the file name openplotterMyapp/locale/en/LC_MESSAGES/openplotter-myapp.po by your package name.
	### use Poedit program to update the translations sources in openplotterMyapp/locale/en/LC_MESSAGES/openplotter-myapp.po

	### replace openplotter-myapp by your package name in file openplotterMyapp/data/openplotter-myapp.desktop

	### replace openplotter-myapp by your package name in debian/rules file content
	### replace openplotter-myapp by your package name in debian/openplotter-myapp-docs.docs file name
	### change Upstream-Name, Source and Copyright values in debian/copyright file content
	### change Source, Maintainer, Homepage, Package and Description values in debian/control file content
	### replace openplotter-myapp by your package name and Sailoog <info@sailoog.com> by your name and email in debian/changelog file content
