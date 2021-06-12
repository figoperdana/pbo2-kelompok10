import wx
from wx.core import NotifyEvent
from view.GuiInterface import Add_item

class classAddItem(Add_item):
    def __init__(self, parent):
        Add_item.__init__(self, parent=None)

    def setProductName(self, productName):
        self.namaBarang.SetValue(productName)

    def setCategory(self, category):
        self.jenisBarang.SetValue(str(category))

    def setUnitPrice(self, unitPrice):
        self.hargaBarang.SetValue(str(unitPrice))

    def setUnitQuantity(self, UnitQuantity):
        self.jumlahBarang.SetValue(str(UnitQuantity))



