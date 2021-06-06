import wx
import GUI
from wxframe2 import wxframe2
from wxframe3 import wxframe3
from wxframe4 import wxframe4
import models.dbsqlite as database

wxframe = GUI.Login

class MyGui(wxframe):
    def __init__(self, parent):
        wxframe.__init__(self, parent)
        super().__init__(parent)

    def loginClick(self, event):
        self._connection = database.connection
        userpemilik = self.CtrlUsername.GetValue()
        passwpemilik = self.CtrlPassword.GetValue()
        query = """SELECT * from pemilik where username_pemilik = ? and password_pemilik = ?"""
        cursor = self._connection.cursor()
        cursor.execute(query, (userpemilik, passwpemilik))
        if cursor.fetchall():
            wx.MessageBox("Login Berhasil!", "Login")
            self.Close()
            frame1 = MyGui1(None)
            frame1.Show()
        else :
            wx.MessageBox("Error", "Login Gagal !")


wxframe1 = GUI.HomePemilik

class MyGui1(wxframe1):
    def __init__(self, parent):
        wxframe1.__init__(self, parent)
        super().__init__(parent)

    def transactionClick(self, event):
        self.Close()
        frame2 = wxframetransaction(None)
        frame2.Show()

    def stockClick(self, event):
        self.Close()
        frame3 = wxframestock(None)
        frame3.Show()

    def employeeClick(self, event):
        self.Close()
        frame4 = wxframeemployee(None)
        frame4.Show()

    def incomeClick(self, event):
        self.Close()
        frame5 = MyGui5(None)
        frame5.Show()

    def HelpMenu(self, event):
        frame6 = MyGUIHelp(None)
        frame6.Show()

    def AboutMenu(self, event):
        frame7 = MyGUIAbout(None)
        frame7.Show()


class wxframestock(wxframe3):
    def __init__(self, parent):
        wxframe3.__init__(self, parent)
        self.Show()

    def HomeMenuBtnClick(self, event):
        self.Close()
        frame1 = MyGui1(None)
        frame1.Show()

    def AboutMenu2(self, event):
        frame11 = MyGUIAbout(None)
        frame11.Show()

    def HelpMenu2(self, event):
        frame12 = MyGUIHelp(None)
        frame12.Show()





class wxframetransaction(wxframe2):
    def __init__(self, parent):
        wxframe2.__init__(self, parent)
        super().__init__(parent)

    def HomeMenuBtnClick(self, event):
        self.Close()
        frame1 = MyGui1(None)
        frame1.Show()

    def AboutMenu2(self, event):
        frame11 = MyGUIAbout(None)
        frame11.Show()

    def HelpMenu2(self, event):
        frame12 = MyGUIHelp(None)
        frame12.Show()


wxframe9 = GUI.Help

class MyGUIHelp(wxframe9):
    def __init__(self, parent):
        wxframe9.__init__(self, parent)
        super().__init__(parent)

wxframe5 = GUI.About

class MyGUIAbout (wxframe5):
    def __init__(self, parent):
        wxframe5.__init__(self, parent)
        super().__init__(parent)


class wxframeemployee (wxframe4):
    def __init__(self, parent):
        wxframe4.__init__(self, parent)
        super().__init__(parent)

    def HomeMenuBtnClick(self, event):
        self.Close()
        frame1 = MyGui1(None)
        frame1.Show()

    def AboutMenu2(self, event):
        frame11 = MyGUIAbout(None)
        frame11.Show()

    def HelpMenu2(self, event):
        frame12 = MyGUIHelp(None)
        frame12.Show()

wxframe7 = GUI.Income

class MyGui5 (wxframe7):
    def __init__(self, parent):
        wxframe7.__init__(self, parent)
        super().__init__(parent)

    def HomeMenuBtnClick(self, event):
        self.Close()
        frame1 = MyGui1(None)
        frame1.Show()

    def AboutMenu2(self, event):
        frame11 = MyGUIAbout(None)
        frame11.Show()

    def HelpMenu2(self, event):
        frame12 = MyGUIHelp(None)
        frame12.Show()





