import wx
from wx.core import Frame
from view.GuiInterface import HomePemilik

class classHomePemilik(HomePemilik):
    def __init__(self, parent):
        HomePemilik.__init__(self,parent)