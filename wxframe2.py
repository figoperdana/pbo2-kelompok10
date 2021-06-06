import wx
import GUI
from models import transaksi
from models import dbsqlite
from wxframe2create import wxframe2create

# Implementing mainFrame
class wxframe2( GUI.Transaction ):
	def __init__( self, parent ):
		GUI.Transaction.__init__( self, parent )
		self.transactionModel = transaksi.transaction()
		self.columns = ['ID Transaksi', 'ID Barang', 'Nama Barang', 'Harga Barang', 'Jumlah Beli', 'Total']
		self.selectedtransaction = None
		self.initColumns()
		self.deleteDataBtn.Disable()
		self.Bind(wx.EVT_SIZING, self.onResize)
		self.tanggalTransaksiBtn

	def clearListTransaction(self):
		self.listCtrlTransaction.ClearAll()
		self.initColumns()

	def initColumns(self):
		for index, col in enumerate(self.columns):
			self.listCtrlTransaction.InsertColumn(index, col)

	# Handlers for mainFrame events.
	def handleSelectedTranc(self, event):
		selectedId = event.GetItem().GetText()
		if not selectedId: return

		self.selectedtransaction = selectedId
		self.deleteDataBtn.Enable()

	def deleteDataClick(self, event):
		if self.selectedtransaction == None: return

		r = wx.MessageDialog(None, 'This Data will be deleted', 'Are you sure', style=wx.ICON_WARNING | wx.YES_NO | wx.NO_DEFAULT).ShowModal()

		if r == wx.ID_YES:
			self.transactionModel.delete(self.selectedtransaction)
			wx.MessageDialog(None, 'Data has been deleted.', 'Delete Success', style=wx.OK | wx.ICON_INFORMATION).ShowModal()

	def inputDataClick(self, event):
		frame = wxframe2create()
		frame.Show()

	def onResize(self, event):
		parentSize = self.GetSize()
		self.listCtrlTransaction.SetMinSize(wx.Size(parentSize.GetWidth() - 38, parentSize.GetHeight() * 0.8))
