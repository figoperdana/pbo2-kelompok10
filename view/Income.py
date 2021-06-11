import wx
from view.GuiInterface import Income
from models import stok
from models import income
from models import database

class classIncome(Income):
    def __init__(self, parent):
        Income.__init__(self,parent=None)
        self.incomeModel = income.Nota()
        self.columns = ['No.','Nama Barang','Harga Barang','Jumlah Beli','Tanggal Transaksi']
        self.selectedProduct = None
        self.initColom()
        self.initData()

    def initColom(self):
        for index, col in enumerate(self.columns):
            self.listCtrlTranc.InsertColumn(index, col)

    def initData(self):
            income = self.incomeModel.get(columns="*",orderByColumn='id_transaksi', orderByDirection='DESC', limit=self.limitData.GetValue())
            for rowIndex, row in enumerate(income):
                self.listCtrlTranc.InsertItem(rowIndex, row[0])
                for columnIndex, col in enumerate(self.columns):
                    self.listCtrlTranc.SetItem(rowIndex, columnIndex, str(row[columnIndex]))