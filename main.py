import wx
import controller

app = wx.App(False)

frame = controller.MyGui(parent=None)
frame.Show()
app.MainLoop()
