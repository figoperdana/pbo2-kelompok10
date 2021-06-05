# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import wx.grid

###########################################################################
## Class Login
###########################################################################

class Login ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Login", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		gSizer2 = wx.GridSizer( 1, 1, 0, 0 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Welcome back to Firo Smart Seller !", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		gSizer2.Add( self.m_staticText10, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer10.Add( gSizer2, 1, wx.ALL|wx.EXPAND, 5 )

		gSizer3 = wx.GridSizer( 4, 1, 0, 0 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		gSizer3.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.username = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.username, 0, wx.ALL|wx.EXPAND|wx.LEFT, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		gSizer3.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gSizer3.Add( self.password, 0, wx.ALL|wx.EXPAND|wx.LEFT, 5 )


		bSizer10.Add( gSizer3, 1, wx.ALL|wx.EXPAND, 5 )

		gSizer4 = wx.GridSizer( 0, 1, 0, 0 )

		self.loginBtn = wx.Button( self, wx.ID_ANY, u"Sign In", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.loginBtn, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizer10.Add( gSizer4, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer10 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.loginBtn.Bind( wx.EVT_BUTTON, self.loginClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def loginClick( self, event ):
		event.Skip()


###########################################################################
## Class HomePemilik
###########################################################################

class HomePemilik ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Home", pos = wx.DefaultPosition, size = wx.Size( 300,250 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Help", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem2 )

		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )

		self.m_menuItem11 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Logout", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem11 )

		self.m_menubar1.Append( self.m_menu1, u"Menu" )

		self.SetMenuBar( self.m_menubar1 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Welcom to Firo Smart Seller !", wx.DefaultPosition, wx.Size( 1000,20 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText1.Wrap( -1 )

		wSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )


		bSizer1.Add( wSizer1, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer10 = wx.GridSizer( 2, 2, 0, 0 )

		self.stock = wx.Button( self, wx.ID_ANY, u"Stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.stock, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.transaction = wx.Button( self, wx.ID_ANY, u"Transaction", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.transaction, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.employee = wx.Button( self, wx.ID_ANY, u"Employee", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.employee, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.income = wx.Button( self, wx.ID_ANY, u"Income", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.income, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer1.Add( gSizer10, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.HelpMenu, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.AboutMenu, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.LogoutMenu, id = self.m_menuItem11.GetId() )
		self.stock.Bind( wx.EVT_BUTTON, self.stockClick )
		self.transaction.Bind( wx.EVT_BUTTON, self.transactionClick )
		self.employee.Bind( wx.EVT_BUTTON, self.employeeClick )
		self.income.Bind( wx.EVT_BUTTON, self.incomeClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def HelpMenu( self, event ):
		event.Skip()

	def AboutMenu( self, event ):
		event.Skip()

	def LogoutMenu( self, event ):
		event.Skip()

	def stockClick( self, event ):
		event.Skip()

	def transactionClick( self, event ):
		event.Skip()

	def employeeClick( self, event ):
		event.Skip()

	def incomeClick( self, event ):
		event.Skip()


###########################################################################
## Class HomePegawai
###########################################################################

class HomePegawai ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Home", pos = wx.DefaultPosition, size = wx.Size( 300,250 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )

		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Help", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem2 )

		self.m_menuItem11 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Logout", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem11 )

		self.m_menubar1.Append( self.m_menu1, u"Menu" )

		self.SetMenuBar( self.m_menubar1 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Welcom to Firo Smart Seller !", wx.DefaultPosition, wx.Size( 1000,20 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText1.Wrap( -1 )

		wSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )


		bSizer1.Add( wSizer1, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer10 = wx.GridSizer( 2, 1, 0, 0 )

		self.stock = wx.Button( self, wx.ID_ANY, u"Stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.stock, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.transaction = wx.Button( self, wx.ID_ANY, u"Transaction", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.transaction, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer1.Add( gSizer10, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.HelpMenu, id = self.m_menuItem1.GetId() )
		self.stock.Bind( wx.EVT_BUTTON, self.stockClick )
		self.transaction.Bind( wx.EVT_BUTTON, self.transactionClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def HelpMenu( self, event ):
		event.Skip()

	def stockClick( self, event ):
		event.Skip()

	def transactionClick( self, event ):
		event.Skip()


###########################################################################
## Class Stock
###########################################################################

class Stock ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Stock", pos = wx.DefaultPosition, size = wx.Size( 800,537 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu7 = wx.Menu()
		self.m_menuItem12 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"Home", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu7.Append( self.m_menuItem12 )

		self.m_menuItem13 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu7.Append( self.m_menuItem13 )

		self.m_menuItem14 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"Help", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu7.Append( self.m_menuItem14 )

		self.m_menuItem15 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"Logout", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu7.Append( self.m_menuItem15 )

		self.m_menubar2.Append( self.m_menu7, u"Menu" )

		self.SetMenuBar( self.m_menubar2 )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.mainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.limitData = wx.SpinCtrl( self.mainPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS|wx.SP_WRAP, 0, 100000, 10 )
		self.limitData.SetMinSize( wx.Size( 70,-1 ) )

		bSizer4.Add( self.limitData, 0, wx.ALL, 5 )

		self.addItemBtn = wx.Button( self.mainPanel, wx.ID_ANY, u"Add Item", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.addItemBtn, 0, wx.ALL, 5 )

		self.refreshItemBtn = wx.Button( self.mainPanel, wx.ID_ANY, u"Refresh Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.refreshItemBtn, 0, wx.ALL, 5 )

		self.editItemBtn = wx.Button( self.mainPanel, wx.ID_ANY, u"Edit Item", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.editItemBtn, 0, wx.ALL, 5 )

		self.deleteItemBtn = wx.Button( self.mainPanel, wx.ID_ANY, u"Delete Item", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.deleteItemBtn, 0, wx.ALL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer3.Add( bSizer4, 0, wx.ALL|wx.EXPAND, 5 )

		fgSizer3 = wx.FlexGridSizer( 0, 2, 1, 5 )
		fgSizer3.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

		self.listCtrlStok = wx.ListCtrl( self.mainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		self.listCtrlStok.SetMinSize( wx.Size( 840,480 ) )

		fgSizer3.Add( self.listCtrlStok, 0, wx.ALL, 5 )


		bSizer3.Add( fgSizer3, 0, wx.EXPAND, 5 )


		self.mainPanel.SetSizer( bSizer3 )
		self.mainPanel.Layout()
		bSizer3.Fit( self.mainPanel )
		bSizer20.Add( self.mainPanel, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer20 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.HomeMenuBtnClick, id = self.m_menuItem12.GetId() )
		self.Bind( wx.EVT_MENU, self.AboutMenu2, id = self.m_menuItem13.GetId() )
		self.Bind( wx.EVT_MENU, self.HelpMenu2, id = self.m_menuItem14.GetId() )
		self.Bind( wx.EVT_MENU, self.LogoutMenu, id = self.m_menuItem15.GetId() )
		self.addItemBtn.Bind( wx.EVT_BUTTON, self.addItemClick )
		self.refreshItemBtn.Bind( wx.EVT_BUTTON, self.refreshItemClick )
		self.editItemBtn.Bind( wx.EVT_BUTTON, self.editItemClick )
		self.deleteItemBtn.Bind( wx.EVT_BUTTON, self.deleteItemClick )
		self.listCtrlStok.Bind( wx.EVT_LIST_ITEM_SELECTED, self.handleSelectedItem )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def HomeMenuBtnClick( self, event ):
		event.Skip()

	def AboutMenu2( self, event ):
		event.Skip()

	def HelpMenu2( self, event ):
		event.Skip()

	def LogoutMenu( self, event ):
		event.Skip()

	def addItemClick( self, event ):
		event.Skip()

	def refreshItemClick( self, event ):
		event.Skip()

	def editItemClick( self, event ):
		event.Skip()

	def deleteItemClick( self, event ):
		event.Skip()

	def handleSelectedItem( self, event ):
		event.Skip()


###########################################################################
## Class Add_item
###########################################################################

class Add_item ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add Item", pos = wx.DefaultPosition, size = wx.Size( 380,424 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		gSizer11 = wx.GridSizer( 8, 1, 0, 0 )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Nama Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		gSizer11.Add( self.m_staticText19, 0, wx.ALL, 5 )

		self.namaBarang = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.namaBarang, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Jenis Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		gSizer11.Add( self.m_staticText20, 0, wx.ALL, 5 )

		jenisBarangChoices = [ u"Alat Tulis", u"Produk Kertas", u"Perlengkapan Kantor" ]
		self.jenisBarang = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, jenisBarangChoices, 0 )
		gSizer11.Add( self.jenisBarang, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		gSizer11.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.hargaBarang = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.hargaBarang, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Jumlah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		gSizer11.Add( self.m_staticText22, 0, wx.ALL, 5 )

		self.jumlahBarang = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		gSizer11.Add( self.jumlahBarang, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer11.Add( gSizer11, 1, wx.ALL|wx.EXPAND, 5 )

		gSizer12 = wx.GridSizer( 1, 1, 0, 0 )

		self.saveItemBtn = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.saveItemBtn, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizer11.Add( gSizer12, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.saveItemBtn.Bind( wx.EVT_BUTTON, self.saveItemClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def saveItemClick( self, event ):
		event.Skip()


###########################################################################
## Class Edit_item
###########################################################################

class Edit_item ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Edit Item", pos = wx.DefaultPosition, size = wx.Size( 380,290 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		gSizer11 = wx.GridSizer( 6, 1, 0, 0 )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Nama Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		gSizer11.Add( self.m_staticText19, 0, wx.ALL, 5 )

		self.namaBarang = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.namaBarang, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Jenis Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		gSizer11.Add( self.m_staticText20, 0, wx.ALL, 5 )

		jenisBarangChoices = [ u"Alat Tulis", u"Produk Kertas", u"Perlengkapan Kantor" ]
		self.jenisBarang = wx.ComboBox( self, wx.ID_ANY, u"Pilih Jenis Barang", wx.DefaultPosition, wx.DefaultSize, jenisBarangChoices, 0 )
		gSizer11.Add( self.jenisBarang, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		gSizer11.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.hargaBarang = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.hargaBarang, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer11.Add( gSizer11, 1, wx.ALL|wx.EXPAND, 5 )

		gSizer12 = wx.GridSizer( 1, 1, 0, 0 )

		self.saveItemBtn = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.saveItemBtn, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizer11.Add( gSizer12, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.saveItemBtn.Bind( wx.EVT_BUTTON, self.saveItemClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def saveItemClick( self, event ):
		event.Skip()


###########################################################################
## Class Employee
###########################################################################

class Employee ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Employee", pos = wx.DefaultPosition, size = wx.Size( 793,513 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu7 = wx.Menu()
		self.m_menuItem12 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"Home", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu7.Append( self.m_menuItem12 )

		self.m_menuItem13 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu7.Append( self.m_menuItem13 )

		self.m_menuItem14 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"Help", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu7.Append( self.m_menuItem14 )

		self.m_menuItem15 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"Logout", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu7.Append( self.m_menuItem15 )

		self.m_menubar2.Append( self.m_menu7, u"Menu" )

		self.SetMenuBar( self.m_menubar2 )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.mainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.limitData = wx.SpinCtrl( self.mainPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS|wx.SP_WRAP, 0, 100000, 10 )
		self.limitData.SetMinSize( wx.Size( 70,-1 ) )

		bSizer4.Add( self.limitData, 0, wx.ALL, 5 )

		self.addEmpBtn = wx.Button( self.mainPanel, wx.ID_ANY, u"Add Employee", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.addEmpBtn, 0, wx.ALL, 5 )

		self.refreshEmpBtn = wx.Button( self.mainPanel, wx.ID_ANY, u"Refresh Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.refreshEmpBtn, 0, wx.ALL, 5 )

		self.editEmpBtn = wx.Button( self.mainPanel, wx.ID_ANY, u"Edit Employee", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.editEmpBtn, 0, wx.ALL, 5 )

		self.deleteEmpBtn = wx.Button( self.mainPanel, wx.ID_ANY, u"Delete Employee", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.deleteEmpBtn, 0, wx.ALL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer3.Add( bSizer4, 0, wx.ALL|wx.EXPAND, 5 )

		fgSizer3 = wx.FlexGridSizer( 0, 2, 1, 5 )
		fgSizer3.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

		self.listCtrlPegawai = wx.ListCtrl( self.mainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		self.listCtrlPegawai.SetMinSize( wx.Size( 840,480 ) )

		fgSizer3.Add( self.listCtrlPegawai, 0, wx.ALL, 5 )


		bSizer3.Add( fgSizer3, 0, wx.EXPAND, 5 )


		self.mainPanel.SetSizer( bSizer3 )
		self.mainPanel.Layout()
		bSizer3.Fit( self.mainPanel )
		bSizer20.Add( self.mainPanel, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer20 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.HomeMenuBtnClick, id = self.m_menuItem12.GetId() )
		self.Bind( wx.EVT_MENU, self.AboutMenu2, id = self.m_menuItem13.GetId() )
		self.Bind( wx.EVT_MENU, self.HelpMenu2, id = self.m_menuItem14.GetId() )
		self.Bind( wx.EVT_MENU, self.LogoutMenu, id = self.m_menuItem15.GetId() )
		self.addEmpBtn.Bind( wx.EVT_BUTTON, self.addEmpClick )
		self.refreshEmpBtn.Bind( wx.EVT_BUTTON, self.refreshEmpClick )
		self.editEmpBtn.Bind( wx.EVT_BUTTON, self.editEmpClick )
		self.deleteEmpBtn.Bind( wx.EVT_BUTTON, self.deleteEmpClick )
		self.listCtrlPegawai.Bind( wx.EVT_LIST_ITEM_SELECTED, self.handleSelectedEmp )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def HomeMenuBtnClick( self, event ):
		event.Skip()

	def AboutMenu2( self, event ):
		event.Skip()

	def HelpMenu2( self, event ):
		event.Skip()

	def LogoutMenu( self, event ):
		event.Skip()

	def addEmpClick( self, event ):
		event.Skip()

	def refreshEmpClick( self, event ):
		event.Skip()

	def editEmpClick( self, event ):
		event.Skip()

	def deleteEmpClick( self, event ):
		event.Skip()

	def handleSelectedEmp( self, event ):
		event.Skip()


###########################################################################
## Class Add_employee
###########################################################################

class Add_employee ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add Employee", pos = wx.DefaultPosition, size = wx.Size( 380,479 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		gSizer11 = wx.GridSizer( 10, 1, 0, 0 )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Nama Pegawai", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		gSizer11.Add( self.m_staticText19, 0, wx.ALL, 5 )

		self.namaPegawai = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.namaPegawai, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Alamat Pegawai", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		gSizer11.Add( self.m_staticText20, 0, wx.ALL, 5 )

		self.alamatPegawai = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.alamatPegawai, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"No Telp", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		gSizer11.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.telpPegawai = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.telpPegawai, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		gSizer11.Add( self.m_staticText22, 0, wx.ALL, 5 )

		self.usernameEmp = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.usernameEmp, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText57 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText57.Wrap( -1 )

		gSizer11.Add( self.m_staticText57, 0, wx.ALL, 5 )

		self.passwordEmp = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.passwordEmp, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer11.Add( gSizer11, 1, wx.ALL|wx.EXPAND, 5 )

		gSizer12 = wx.GridSizer( 1, 1, 0, 0 )

		self.saveEmpBtn = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.saveEmpBtn, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizer11.Add( gSizer12, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.saveEmpBtn.Bind( wx.EVT_BUTTON, self.saveEmpClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def saveEmpClick( self, event ):
		event.Skip()


###########################################################################
## Class Edit_employee
###########################################################################

class Edit_employee ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Edit Employee", pos = wx.DefaultPosition, size = wx.Size( 380,420 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		gSizer11 = wx.GridSizer( 8, 1, 0, 0 )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Nama Pegawai", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		gSizer11.Add( self.m_staticText19, 0, wx.ALL, 5 )

		self.namaPegawai = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.namaPegawai, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Alamat Pegawai", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		gSizer11.Add( self.m_staticText20, 0, wx.ALL, 5 )

		self.alamatPegawai = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.alamatPegawai, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"No Telp", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		gSizer11.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.telpPegawai = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.telpPegawai, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		gSizer11.Add( self.m_staticText22, 0, wx.ALL, 5 )

		self.usernameEmp = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.usernameEmp, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText57 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText57.Wrap( -1 )

		gSizer11.Add( self.m_staticText57, 0, wx.ALL, 5 )

		self.passwordEmp = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gSizer11.Add( self.passwordEmp, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer11.Add( gSizer11, 1, wx.ALL|wx.EXPAND, 5 )

		gSizer12 = wx.GridSizer( 1, 1, 0, 0 )

		self.saveEmpBtn = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.saveEmpBtn, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizer11.Add( gSizer12, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.saveEmpBtn.Bind( wx.EVT_BUTTON, self.saveEmpClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def saveEmpClick( self, event ):
		event.Skip()


###########################################################################
## Class About
###########################################################################

class About ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"About", pos = wx.DefaultPosition, size = wx.Size( 300,220 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		gSizer17 = wx.GridSizer( 2, 1, 0, 0 )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Alamat Toko Offline Firo :\n\nJl. Raya Yos Sudarso BA-9 Sidopekso\nKraksaan, Kabupaten Probolinggo\nKode Pos 67282, Provinsi Jawa Timur, Indonesia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		gSizer17.Add( self.m_staticText31, 0, wx.ALL, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Jam Operasional :\n\nBuka Senin - Minggu\nPukul 07.00 - 21.00 WIB", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		gSizer17.Add( self.m_staticText33, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer20.Add( gSizer17, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer20 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class Help
###########################################################################

class Help ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Help", pos = wx.DefaultPosition, size = wx.Size( 300,150 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		gSizer17 = wx.GridSizer( 2, 1, 0, 0 )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Memiliki Pertanyaan atau Kendala ?\nKami akan selalu siap sedia untuk membantu !\n\nHubungi kami pada 081216195308 atau\nKirim email pada ffitridwia@gmail.com", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		gSizer17.Add( self.m_staticText31, 0, wx.ALL, 5 )


		bSizer20.Add( gSizer17, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer20 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class Transaction
###########################################################################

class Transaction ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Transaction", pos = wx.DefaultPosition, size = wx.Size( 630,598 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu7 = wx.Menu()
		self.m_menuItem12 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"Home", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu7.Append( self.m_menuItem12 )

		self.m_menuItem13 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu7.Append( self.m_menuItem13 )

		self.m_menuItem14 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"Help", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu7.Append( self.m_menuItem14 )

		self.m_menuItem15 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"Logout", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu7.Append( self.m_menuItem15 )

		self.m_menubar2.Append( self.m_menu7, u"Menu" )

		self.SetMenuBar( self.m_menubar2 )

		bSizer32 = wx.BoxSizer( wx.VERTICAL )

		gSizer41 = wx.GridSizer( 1, 6, 0, 0 )

		self.inputDataBtn = wx.Button( self, wx.ID_ANY, u"Input Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer41.Add( self.inputDataBtn, 0, wx.ALL, 5 )

		self.deleteDataBtn = wx.Button( self, wx.ID_ANY, u"Delete Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer41.Add( self.deleteDataBtn, 0, wx.ALL, 5 )


		gSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText69 = wx.StaticText( self, wx.ID_ANY, u"Tanggal Transaksi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69.Wrap( -1 )

		gSizer41.Add( self.m_staticText69, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.tanggalTransaksiBtn = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gSizer41.Add( self.tanggalTransaksiBtn, 0, wx.ALL, 5 )


		bSizer32.Add( gSizer41, 1, wx.ALL|wx.EXPAND, 5 )

		gSizer42 = wx.GridSizer( 0, 6, 0, 0 )

		self.tableTransaction = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tableTransaction.CreateGrid( 10, 6 )
		self.tableTransaction.EnableEditing( True )
		self.tableTransaction.EnableGridLines( True )
		self.tableTransaction.EnableDragGridSize( False )
		self.tableTransaction.SetMargins( 0, 0 )

		# Columns
		self.tableTransaction.AutoSizeColumns()
		self.tableTransaction.EnableDragColMove( False )
		self.tableTransaction.EnableDragColSize( True )
		self.tableTransaction.SetColLabelSize( 30 )
		self.tableTransaction.SetColLabelValue( 0, u"id_transaksi" )
		self.tableTransaction.SetColLabelValue( 1, u"id_barang" )
		self.tableTransaction.SetColLabelValue( 2, u"nama_barang" )
		self.tableTransaction.SetColLabelValue( 3, u"harga_barang" )
		self.tableTransaction.SetColLabelValue( 4, u"jumlah_beli" )
		self.tableTransaction.SetColLabelValue( 5, u"total" )
		self.tableTransaction.SetColLabelValue( 6, wx.EmptyString )
		self.tableTransaction.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tableTransaction.AutoSizeRows()
		self.tableTransaction.EnableDragRowSize( True )
		self.tableTransaction.SetRowLabelSize( 50 )
		self.tableTransaction.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tableTransaction.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		gSizer42.Add( self.tableTransaction, 0, wx.ALL, 5 )


		bSizer32.Add( gSizer42, 1, wx.ALL|wx.EXPAND, 5 )

		gSizer47 = wx.GridSizer( 1, 5, 0, 0 )

		self.m_staticText78 = wx.StaticText( self, wx.ID_ANY, u"Total Bayar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText78.Wrap( -1 )

		gSizer47.Add( self.m_staticText78, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.totalBayarBtn = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer47.Add( self.totalBayarBtn, 0, wx.ALL, 5 )


		gSizer47.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer47.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer47.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer32.Add( gSizer47, 1, wx.ALL, 5 )

		gSizer471 = wx.GridSizer( 1, 5, 0, 0 )

		self.m_staticText781 = wx.StaticText( self, wx.ID_ANY, u"Uang Bayar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText781.Wrap( -1 )

		gSizer471.Add( self.m_staticText781, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.uangBayarBtn = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer471.Add( self.uangBayarBtn, 0, wx.ALL, 5 )


		gSizer471.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer471.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer471.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer32.Add( gSizer471, 1, wx.ALL|wx.EXPAND, 5 )

		gSizer472 = wx.GridSizer( 1, 5, 0, 0 )

		self.m_staticText83 = wx.StaticText( self, wx.ID_ANY, u"Uang Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83.Wrap( -1 )

		gSizer472.Add( self.m_staticText83, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.uangKembaliBtn = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer472.Add( self.uangKembaliBtn, 0, wx.ALL, 5 )


		gSizer472.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer472.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.okBtn = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer472.Add( self.okBtn, 0, wx.ALL, 5 )


		bSizer32.Add( gSizer472, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer32 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.HomeMenuBtnClick, id = self.m_menuItem12.GetId() )
		self.Bind( wx.EVT_MENU, self.AboutMenu2, id = self.m_menuItem13.GetId() )
		self.Bind( wx.EVT_MENU, self.HelpMenu2, id = self.m_menuItem14.GetId() )
		self.Bind( wx.EVT_MENU, self.LogoutMenu, id = self.m_menuItem15.GetId() )
		self.inputDataBtn.Bind( wx.EVT_BUTTON, self.inputDataClick )
		self.deleteDataBtn.Bind( wx.EVT_BUTTON, self.deleteDataClick )
		self.okBtn.Bind( wx.EVT_BUTTON, self.okClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def HomeMenuBtnClick( self, event ):
		event.Skip()

	def AboutMenu2( self, event ):
		event.Skip()

	def HelpMenu2( self, event ):
		event.Skip()

	def LogoutMenu( self, event ):
		event.Skip()

	def inputDataClick( self, event ):
		event.Skip()

	def deleteDataClick( self, event ):
		event.Skip()

	def okClick( self, event ):
		event.Skip()


###########################################################################
## Class Input_data
###########################################################################

class Input_data ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Input Data", pos = wx.DefaultPosition, size = wx.Size( 380,220 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		gSizer11 = wx.GridSizer( 4, 1, 0, 0 )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"ID Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		gSizer11.Add( self.m_staticText19, 0, wx.ALL, 5 )

		self.inputIdBarangBtn = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.inputIdBarangBtn, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Jumlah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		gSizer11.Add( self.m_staticText22, 0, wx.ALL, 5 )

		self.inputJumlahBarangBtn = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		gSizer11.Add( self.inputJumlahBarangBtn, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer11.Add( gSizer11, 1, wx.ALL|wx.EXPAND, 5 )

		gSizer12 = wx.GridSizer( 1, 1, 0, 0 )

		self.saveInputBtn = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.saveInputBtn, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizer11.Add( gSizer12, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.saveInputBtn.Bind( wx.EVT_BUTTON, self.saveInputClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def saveInputClick( self, event ):
		event.Skip()


###########################################################################
## Class Income
###########################################################################

class Income ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Income", pos = wx.DefaultPosition, size = wx.Size( 473,355 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu7 = wx.Menu()
		self.m_menuItem12 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"Home", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu7.Append( self.m_menuItem12 )

		self.m_menuItem13 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu7.Append( self.m_menuItem13 )

		self.m_menuItem14 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"Help", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu7.Append( self.m_menuItem14 )

		self.m_menuItem15 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"Logout", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu7.Append( self.m_menuItem15 )

		self.m_menubar2.Append( self.m_menu7, u"Menu" )

		self.SetMenuBar( self.m_menubar2 )

		bSizer32 = wx.BoxSizer( wx.VERTICAL )

		gSizer68 = wx.GridSizer( 1, 4, 0, 0 )


		gSizer68.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_spinCtrl19 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 10 )
		gSizer68.Add( self.m_spinCtrl19, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.refreshIncomeBtn = wx.Button( self, wx.ID_ANY, u"Refresh Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer68.Add( self.refreshIncomeBtn, 0, wx.ALL, 5 )


		gSizer68.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer32.Add( gSizer68, 1, wx.ALL, 5 )

		gSizer42 = wx.GridSizer( 0, 6, 0, 0 )

		self.tableIncome = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tableIncome.CreateGrid( 10, 4 )
		self.tableIncome.EnableEditing( True )
		self.tableIncome.EnableGridLines( True )
		self.tableIncome.EnableDragGridSize( False )
		self.tableIncome.SetMargins( 0, 0 )

		# Columns
		self.tableIncome.AutoSizeColumns()
		self.tableIncome.EnableDragColMove( False )
		self.tableIncome.EnableDragColSize( True )
		self.tableIncome.SetColLabelSize( 30 )
		self.tableIncome.SetColLabelValue( 0, u"id_pemasukan" )
		self.tableIncome.SetColLabelValue( 1, u"id_transaksi" )
		self.tableIncome.SetColLabelValue( 2, u"tanggal_transaksi" )
		self.tableIncome.SetColLabelValue( 3, u"total_bayar" )
		self.tableIncome.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tableIncome.AutoSizeRows()
		self.tableIncome.EnableDragRowSize( True )
		self.tableIncome.SetRowLabelSize( 50 )
		self.tableIncome.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tableIncome.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		gSizer42.Add( self.tableIncome, 0, wx.ALL, 5 )


		bSizer32.Add( gSizer42, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer32 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.HomeMenuBtnClick, id = self.m_menuItem12.GetId() )
		self.Bind( wx.EVT_MENU, self.AboutMenu2, id = self.m_menuItem13.GetId() )
		self.Bind( wx.EVT_MENU, self.HelpMenu2, id = self.m_menuItem14.GetId() )
		self.Bind( wx.EVT_MENU, self.LogoutMenu, id = self.m_menuItem15.GetId() )
		self.refreshIncomeBtn.Bind( wx.EVT_BUTTON, self.refreshIncomeClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def HomeMenuBtnClick( self, event ):
		event.Skip()

	def AboutMenu2( self, event ):
		event.Skip()

	def HelpMenu2( self, event ):
		event.Skip()

	def LogoutMenu( self, event ):
		event.Skip()

	def refreshIncomeClick( self, event ):
		event.Skip()


