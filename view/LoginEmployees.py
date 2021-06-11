import wx
from wx.core import Frame
from view.GuiInterface import LoginPegawai

class classLoginPegawaiFrame(LoginPegawai):
    def __init__(self, parent):
        LoginPegawai.__init__(self,parent)