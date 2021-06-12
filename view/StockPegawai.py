import wx
from view.GuiInterface import StockPegawai
from models import stok
from models import database
from view.Add_item import Add_item

class classStockPegawai(StockPegawai):
    def __init__(self, parent):
        StockPegawai.__init__(self,parent=None)
        self.ItemModel=stok.stock()
        self.columns = ['ID','Nama Barang','Jenis Barang','Harga Barang', 'Jumlah Stok', 'Added']
        self.selectedItem = None
        self.initColom()
        self.initData()
        self.limitData.SetValue(10)

    def initColom(self):
        for index, col in enumerate(self.columns):
            self.listCtrlStok.InsertColumn(index, col)

    def initData(self):
            Item = self.ItemModel.get(columns="*",orderByColumn='id_barang', orderByDirection='DESC', limit=self.limitData.GetValue())
            for rowIndex, row in enumerate(Item):
                self.listCtrlStok.InsertItem(rowIndex, row[0])
                for columnIndex, col in enumerate(self.columns):
                    self.listCtrlStok.SetItem(rowIndex, columnIndex, str(row[columnIndex]))