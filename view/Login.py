import wx
from wx.core import Frame
from view.GuiInterface import Login

class classLoginFrame(Login):
    def __init__(self, parent):
        Login.__init__(self,parent)