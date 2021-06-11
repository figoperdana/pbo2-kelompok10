import wx
from view.GuiInterface import Transaction
from models import stok
from models import database

class classTransaction(Transaction):
    def __init__(self, parent):
        Transaction.__init__(self,parent=None)
        self.ItemModel=stok.stock()
        self.columns = ['ID','Nama Barang','Harga', 'Jumlah']
        self.selectedItem = None
        self.initColom()
        self.initData()

    def initColom(self):
        for index, col in enumerate(self.columns):
            self.listCtrlTransaction.InsertColumn(index, col)

    def initData(self):
            transaksi = self.ItemModel.get(columns="nama_barang, nama_barang, harga_barang",orderByColumn='id_barang', orderByDirection='DESC', limit=100)
            n = 1
            for rowIndex, row in enumerate(transaksi):
                self.listCtrlTransaction.InsertItem(rowIndex, row[0])
                for columnIndex, col in enumerate(self.columns):
                    if columnIndex == 0:
                        self.listCtrlTransaction.SetItem(rowIndex, columnIndex, str(n))
                    elif columnIndex == 3:
                        self.listCtrlTransaction.SetItem(rowIndex, columnIndex, "0")
                    else:
                        self.listCtrlTransaction.SetItem(rowIndex, columnIndex, str(row[columnIndex]))
                n += 1
