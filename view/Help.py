import wx
from wx.core import NotifyEvent
from view.GuiInterface import Help

class classHelp(Help):
    def __init__(self, parent):
        Help.__init__(self, parent=None)