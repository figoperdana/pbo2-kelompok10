import wx
from wx.core import NotifyEvent
from view.GuiInterface import About

class classAbout(About):
    def __init__(self, parent):
        About.__init__(self, parent=None)