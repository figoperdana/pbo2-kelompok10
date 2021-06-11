import wx
from wx.core import NotifyEvent
from view.GuiInterface import Add_employee

class classAddEmployee(Add_employee):
    def __init__(self, parent):
        Add_employee.__init__(self, parent=None)

    def setEmployeeName(self, EmployeeName):
        self.namaPegawai.SetValue(EmployeeName)

    def setEmployeeAddress(self, EmployeeAddress):
        self.alamatPegawai.SetValue(str(EmployeeAddress))

    def setEmployeePhoneNumber(self, EmployeePhoneNumber):
        self.telpPegawai.SetValue(str(EmployeePhoneNumber))

    def setEmployeeUsername(self, EmployeeUsername):
        self.usernameEmp.SetValue(str(EmployeeUsername))

    def setEmployeePassword(self, EmployeePassword):
        self.passwordEmp.SetValue(str(EmployeePassword))