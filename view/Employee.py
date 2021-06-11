import wx
from view.GuiInterface import Employee
from models import pegawai
from models import database

class classEmployee(Employee):
    def __init__(self, parent):
        Employee.__init__(self,parent=None)
        self.EmployeeModel=pegawai.Employee()
        self.columns = ['ID','Nama Pegawai','Alamat Pegawai','No. Telp Pegawai', 'Username', 'Password']
        self.selectedEmp = None
        self.initColom()
        self.initData()

    def initColom(self):
        for index, col in enumerate(self.columns):
            self.listCtrlPegawai.InsertColumn(index, col)

    def initData(self):
            employee = self.EmployeeModel.get(columns="*",orderByColumn='id_pegawai', orderByDirection='DESC', limit=self.limitData.GetValue())
            for rowIndex, row in enumerate(employee):
                self.listCtrlPegawai.InsertItem(rowIndex, row[0])
                for columnIndex, col in enumerate(self.columns):
                    self.listCtrlPegawai.SetItem(rowIndex, columnIndex, str(row[columnIndex]))