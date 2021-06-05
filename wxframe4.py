import wx
import GUI
from models import pegawai
from models import dbsqlite
from wxframe4create import wxframe4create

# Implementing mainFrame
class wxframe4( GUI.Employee ):
	def __init__( self, parent ):
		GUI.Employee.__init__( self, parent )
		self.employeeModel = pegawai.Employee()
		self.columns = ['ID', 'Nama Pegawai', 'Alamat Pegawai', 'No. Telp Pegawai', 'Username', 'Password']
		self.selectedemployee = None
		self.initColumns()
		self.editEmpBtn.Disable()
		self.deleteEmpBtn.Disable()
		self.Bind(wx.EVT_SIZING, self.onResize)
		self.limitData.SetValue(10)

	def clearListPegawai(self):
		self.listCtrlPegawai.ClearAll()
		self.initColumns()

	def initColumns(self):
		for index, col in enumerate(self.columns):
			self.listCtrlPegawai.InsertColumn(index, col)

	# Handlers for mainFrame events.
	def refreshEmpClick( self, event ):
		self.clearListPegawai()
		Pegawai = self.employeeModel.get(orderByColumn='id_pegawai', orderByDirection='DESC', limit=self.limitData.GetValue())
		for rowIndex, row in enumerate(Pegawai):
			self.listCtrlPegawai.InsertItem(rowIndex, row[0])
			for columnIndex, col in enumerate(self.columns):
				self.listCtrlPegawai.SetItem(rowIndex, columnIndex, str(row[columnIndex]))

	def handleSelectedEmp(self, event):
		selectedId = event.GetItem().GetText()
		if not selectedId: return

		self.selectedemployee = selectedId
		self.editEmpBtn.Enable()
		self.deleteEmpBtn.Enable()

	def deleteEmpClick(self, event):
		if self.selectedemployee == None: return

		r = wx.MessageDialog(None, 'This User Data will be deleted permanently.', 'Are you sure', style=wx.ICON_WARNING | wx.YES_NO | wx.NO_DEFAULT).ShowModal()

		if r == wx.ID_YES:
			self.employeeModel.delete(self.selectedemployee)
			wx.MessageDialog(None, 'User has been deleted.', 'Delete Success', style=wx.OK | wx.ICON_INFORMATION).ShowModal()

	def editEmpClick(self, event):
		if self.selectedemployee == None: return

		stocks = self.employeeModel.find(self.selectedemployee)
		frame = wxframe4create()
		frame.setNamaPegawai(stocks[1])
		frame.setAlamatPegawai(stocks[2])
		frame.setTelpPegawai(stocks[3])
		frame.setUsername(stocks[4])
		frame.setPassword(stocks[5])
		frame.setId(self.selectedemployee)
		frame.Show()

	def addEmpClick(self, event):
		frame = wxframe4create()
		frame.Show()

	def onResize(self, event):
		parentSize = self.GetSize()
		self.listCtrlPegawai.SetMinSize(wx.Size(parentSize.GetWidth() - 38, parentSize.GetHeight() * 0.8))
