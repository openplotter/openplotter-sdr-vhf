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

import wx, os, webbrowser, subprocess, time
from openplotterSettings import conf
from openplotterSettings import language
from openplotterSettings import platform
from .version import version

class MyFrame(wx.Frame):
	def __init__(self):
		self.conf = conf.Conf()
		self.conf_folder = self.conf.conf_folder
		self.platform = platform.Platform()
		self.currentdir = os.path.dirname(os.path.abspath(__file__))
		self.currentLanguage = self.conf.get('GENERAL', 'lang')
		self.language = language.Language(self.currentdir,'openplotter-myapp',self.currentLanguage) ### replace openplotter-myapp by your package name

		wx.Frame.__init__(self, None, title='My App '+version, size=(800,444))
		self.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
		icon = wx.Icon(self.currentdir+"/data/openplotter-myapp.png", wx.BITMAP_TYPE_PNG)
		self.SetIcon(icon)
		self.CreateStatusBar()
		font_statusBar = self.GetStatusBar().GetFont()
		font_statusBar.SetWeight(wx.BOLD)
		self.GetStatusBar().SetFont(font_statusBar)

		self.toolbar1 = wx.ToolBar(self, style=wx.TB_TEXT)
		toolHelp = self.toolbar1.AddTool(101, _('Help'), wx.Bitmap(self.currentdir+"/data/help.png"))
		self.Bind(wx.EVT_TOOL, self.OnToolHelp, toolHelp)
		if not self.platform.isInstalled('openplotter-doc'): self.toolbar1.EnableTool(101,False)
		toolSettings = self.toolbar1.AddTool(102, _('Settings'), wx.Bitmap(self.currentdir+"/data/settings.png"))
		self.Bind(wx.EVT_TOOL, self.OnToolSettings, toolSettings)
		self.toolbar1.AddSeparator()

		self.notebook = wx.Notebook(self)
		self.notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.onTabChange)
		self.myapp = wx.Panel(self.notebook)
		self.connections = wx.Panel(self.notebook)
		self.output = wx.Panel(self.notebook)
		self.notebook.AddPage(self.myapp, 'My App')
		self.il = wx.ImageList(24, 24)
		img0 = self.il.Add(wx.Bitmap(self.currentdir+"/data/openplotter-24.png", wx.BITMAP_TYPE_PNG))
		self.notebook.AssignImageList(self.il)
		self.notebook.SetPageImage(0, img0)

		vbox = wx.BoxSizer(wx.VERTICAL)
		vbox.Add(self.toolbar1, 0, wx.EXPAND)
		vbox.Add(self.notebook, 1, wx.EXPAND)
		self.SetSizer(vbox)

		self.pageMyapp()

		maxi = self.conf.get('GENERAL', 'maximize')
		if maxi == '1': self.Maximize()

		self.Centre()

		self.ShowStatusBarGREEN(_('Click on "Help" to learn how to get started'))

	def ShowStatusBar(self, w_msg, colour):
		self.GetStatusBar().SetForegroundColour(colour)
		self.SetStatusText(w_msg)

	### red for error or cancellation messages
	def ShowStatusBarRED(self, w_msg):
		self.ShowStatusBar(w_msg, (130,0,0))

	### green for succesful messages
	def ShowStatusBarGREEN(self, w_msg):
		self.ShowStatusBar(w_msg, (0,130,0))

	### black for informative messages
	def ShowStatusBarBLACK(self, w_msg):
		self.ShowStatusBar(w_msg, wx.BLACK) 

	### yellow for attention or prcessing messages
	def ShowStatusBarYELLOW(self, w_msg):
		self.ShowStatusBar(w_msg,(255,140,0)) 

	def onTabChange(self, event):
		try:
			self.SetStatusText('')
		except:pass

	### replace url by your manuals
	def OnToolHelp(self, event): 
		url = "/usr/share/openplotter-doc/external/myapp_app.html"
		webbrowser.open(url, new=2)

	def OnToolSettings(self, event=0): 
		subprocess.call(['pkill', '-f', 'openplotter-settings'])
		subprocess.Popen('openplotter-settings')

	def pageMyapp(self):
		text1 = wx.StaticText(self.myapp, label=_('This app does nothing.'))
		text2 = wx.StaticText(self.myapp, label=_('This is a template to start writing your own OpenPlotter app.'))

		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		hbox1.AddStretchSpacer(1)
		hbox1.Add(text1, 0, wx.ALL | wx.EXPAND, 5)
		hbox1.AddStretchSpacer(1)

		hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		hbox2.AddStretchSpacer(1)
		hbox2.Add(text2, 0, wx.ALL | wx.EXPAND, 5)
		hbox2.AddStretchSpacer(1)

		vbox = wx.BoxSizer(wx.VERTICAL)
		vbox.AddStretchSpacer(1)
		vbox.Add(hbox1, 0, wx.ALL | wx.EXPAND, 5)
		vbox.Add(hbox2, 0, wx.ALL | wx.EXPAND, 5)
		vbox.AddStretchSpacer(1)
		self.myapp.SetSizer(vbox)

################################################################################

def main():
	try:
		platform2 = platform.Platform()
		if not platform2.postInstall(version,'myapp'): ### replace myapp by the name of your app, use the same name in myappPostInstall and myappPreUninstall scripts.
			subprocess.Popen(['openplotterPostInstall', platform2.admin+' myappPostInstall']) ### replace myappPostInstall by your post install entry point (see setup.py file).
			return
	except: pass

	app = wx.App()
	MyFrame().Show()
	time.sleep(1)
	app.MainLoop()

if __name__ == '__main__':
	main()
