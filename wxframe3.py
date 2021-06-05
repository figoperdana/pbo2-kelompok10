import wx
import GUI
from models import stok
from models import dbsqlite
from wxframe3create import wxframe3create

# Implementing mainFrame
class wxframe3( GUI.Stock ):
	def __init__( self, parent ):
		GUI.Stock.__init__( self, parent )
		self.stockModel = stok.stock()
		self.columns = ['ID', 'Nama Barang', 'Jenis Barang', 'Harga Barang', 'Jumlah Barang', 'Added']
		self.selectedstock = None
		self.initColumns()
		self.editItemBtn.Disable()
		self.deleteItemBtn.Disable()
		self.Bind(wx.EVT_SIZING, self.onResize)
		self.limitData.SetValue(10)

	def clearListStocks(self):
		self.listCtrlStok.ClearAll()
		self.initColumns()

	def initColumns(self):
		for index, col in enumerate(self.columns):
			self.listCtrlStok.InsertColumn(index, col)

	# Handlers for mainFrame events.
	def refreshItemClick( self, event ):
		self.clearListStocks()
		Stocks = self.stockModel.get(orderByColumn='id_barang', orderByDirection='DESC', limit=self.limitData.GetValue())
		for rowIndex, row in enumerate(Stocks):
			self.listCtrlStok.InsertItem(rowIndex, row[0])
			for columnIndex, col in enumerate(self.columns):
				self.listCtrlStok.SetItem(rowIndex, columnIndex, str(row[columnIndex]))

	def handleSelectedItem(self, event):
		selectedId = event.GetItem().GetText()
		if not selectedId: return

		self.selectedstock = selectedId
		self.editItemBtn.Enable()
		self.deleteItemBtn.Enable()

	def deleteItemClick(self, event):
		if self.selectedstock == None: return

		r = wx.MessageDialog(None, 'This data will be deleted permanently.', 'Are you sure', style=wx.ICON_WARNING | wx.YES_NO | wx.NO_DEFAULT).ShowModal()

		if r == wx.ID_YES:
			self.stockModel.delete(self.selectedstock)
			wx.MessageDialog(None, 'Stock has been deleted.', 'Delete Success', style=wx.OK | wx.ICON_INFORMATION).ShowModal()

	def editItemClick(self, event):
		if self.selectedstock == None: return

		stocks = self.stockModel.find(self.selectedstock)
		frame = wxframe3create()
		frame.setNamaBarang(stocks[1])
		frame.setJenisBarang(stocks[2])
		frame.setHarga(stocks[3])
		frame.setJumlahBarang(stocks[4])
		frame.setId(self.selectedstock)
		frame.Show()

	def addItemClick(self, event):
		frame = wxframe3create()
		frame.Show()

	def onResize(self, event):
		parentSize = self.GetSize()
		self.listCtrlStok.SetMinSize(wx.Size(parentSize.GetWidth() - 38, parentSize.GetHeight() * 0.8))
