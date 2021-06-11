import wx
from controller.Controller import Controller
class MainApp(wx.App):
    def OnInit(self):
        self.frame = Controller()
        self.frame.main()
        return True

if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()