import view.GuiInterface
from view.GuiInterface import *
from models import stok
from models import income
from view.Login import *
from view.LoginEmployees import *
from view.HomePegawai import *
from view.HomePemilik import *
from view.Stock import *
from view.Employee import *
from view.Transaction import *
from view.Income import *
from view.About import *
from view.Help import *
from view.Add_employee import *
from view.Add_item import *
from view.StockPegawai import *
from view.TransactionPegawai import *
from view import *
import wx



class Controller():
    def __init__(self):
        self.stockModel= stok.stock()
        self.pegawaiModel = pegawai.Employee()
        self.incomeModel = income.Nota()
        self.jumlahBarang = 0
        self.jumlahHarga = 0
        self.id = None
        self.selectedItem = None
        self.selectedEmp = None

        # class login
        self.loginView = classLoginFrame(parent=None)
        self.loginView.loginPegawaiBtn.Bind(wx.EVT_BUTTON, self.loginPegawaiClick)
        self.loginView.loginBtn.Bind(wx.EVT_BUTTON, self.loginClick)

        # class login pegawai
        self.loginPegawaiView = classLoginPegawaiFrame(parent=None)
        self.loginPegawaiView.loginAdminBtn.Bind(wx.EVT_BUTTON, self.loginAdminClick)
        self.loginPegawaiView.loginEmployeeBtn.Bind(wx.EVT_BUTTON, self.loginEmployeeClick)

        # class Home Pemilik
        self.homePemilikView = classHomePemilik(parent=None)
        self.homePemilikView.Bind(wx.EVT_MENU, self.LogoutMenu)
        self.homePemilikView.stock.Bind(wx.EVT_BUTTON, self.stockClick)
        self.homePemilikView.transaction.Bind(wx.EVT_BUTTON, self.transactionClick)
        self.homePemilikView.employee.Bind(wx.EVT_BUTTON, self.employeeClick)
        self.homePemilikView.income.Bind(wx.EVT_BUTTON, self.incomeClick)

        #class Home Pegawai
        self.homePegawaiView = classHomePegawai(parent=None)
        self.homePegawaiView.Bind(wx.EVT_MENU, self.LogoutMenu)
        self.homePegawaiView.stock.Bind(wx.EVT_BUTTON, self.stockPegawaiClick)
        self.homePegawaiView.transaction.Bind(wx.EVT_BUTTON, self.transactionPegawaiClick)

        # class Stock
        self.StockView = classStock(parent=None)
        self.StockViewP = classStockPegawai(parent=None)
        self.StockView.Bind(wx.EVT_MENU, self.HomeMenuBtnClick)
        self.StockView.addItemBtn.Bind(wx.EVT_BUTTON, self.addItemClick)
        self.StockView.refreshItemBtn.Bind(wx.EVT_BUTTON, self.refreshItemClick)
        self.StockView.editItemBtn.Bind(wx.EVT_BUTTON, self.editItemClick)
        self.StockView.deleteItemBtn.Bind(wx.EVT_BUTTON, self.deleteItemClick)
        self.StockView.listCtrlStok.Bind(wx.EVT_LIST_ITEM_SELECTED, self.handleSelectedItem)
        self.StockView.selectedItem = None

        # class Add Item
        self.AddItemView = classAddItem(parent=None)
        self.AddItemView.saveItemBtn.Bind(wx.EVT_BUTTON, self.saveItemClick)


        # class Employee
        self.EmployeeView = classEmployee(parent=None)
        self.EmployeeView.Bind(wx.EVT_MENU, self.HomeMenuBtnClick)
        self.EmployeeView.addEmpBtn.Bind(wx.EVT_BUTTON, self.addEmpClick)
        self.EmployeeView.refreshEmpBtn.Bind(wx.EVT_BUTTON, self.refreshEmpClick)
        self.EmployeeView.editEmpBtn.Bind(wx.EVT_BUTTON, self.editEmpClick)
        self.EmployeeView.deleteEmpBtn.Bind(wx.EVT_BUTTON, self.deleteEmpClick)
        self.EmployeeView.listCtrlPegawai.Bind(wx.EVT_LIST_ITEM_SELECTED, self.handleSelectedEmp)
        self.EmployeeView.selectedEmp = None

        #class add employee
        self.AddEmployeeView = classAddEmployee(parent=None)
        self.AddEmployeeView.saveEmpBtn.Bind(wx.EVT_BUTTON, self.saveEmpClick)

        #class Aboout
        self.AboutView = classAbout(parent=None)

        # class Help
        self.HelpView = classHelp(parent=None)

        #class Transaction
        self.TransactionView = classTransaction(parent=None)
        self.TransactionView = classTransactionPegawai(parent=None)
        self.TransactionView.Bind(wx.EVT_MENU, self.HomeMenuBtnClick)
        self.TransactionView.listCtrlTransaction.Bind(wx.EVT_LIST_ITEM_SELECTED, self.handleSelectedTranc)
        self.TransactionView.inputDataBtn.Bind(wx.EVT_BUTTON, self.inputDataClick)
        self.TransactionView.deleteDataBtn.Bind(wx.EVT_BUTTON, self.deleteDataClick)
        self.TransactionView.kembalianDataBtn.Bind(wx.EVT_BUTTON, self.kembalianDataClick)
        self.TransactionView.checkDataBtn.Bind(wx.EVT_BUTTON, self.checkDataClick)
        self.TransactionView.okBtn.Bind(wx.EVT_BUTTON, self.okClick)
        self.TransactionView.selectedItem = None

        #class Income
        self.IncomeView = classIncome(parent=None)
        self.IncomeView.Bind(wx.EVT_MENU, self.HomeMenuBtnClick)
        self.IncomeView.refreshIncomeBtn.Bind(wx.EVT_BUTTON, self.refreshIncomeClick)
        self.IncomeView.listCtrlTranc.Bind(wx.EVT_LIST_ITEM_SELECTED, self.handleSelectedTranc)



    #login
    def loginClick(self, event):
        self._connection = database.connection
        userpemilik = self.loginView.CtrlUsername.GetValue()
        passwpemilik = self.loginView.CtrlPassword.GetValue()
        query = """SELECT * from pemilik where username_pemilik = ? and password_pemilik = ?"""
        cursor = self._connection.cursor()
        cursor.execute(query, (userpemilik, passwpemilik))
        if cursor.fetchall():
            wx.MessageBox("Login Berhasil!", "Login")
            self.loginView.Hide()
            self.loginPegawaiView.Hide()
            self.homePemilikView.Show()
        else :
            wx.MessageBox("Error", "Login Gagal !")

    def loginPegawaiClick(self, event):
        self.loginPegawaiView.Show()

    def loginEmployeeClick(self, event):
        self._connection = database.connection
        userpegawai = self.loginPegawaiView.CtrlUsername.GetValue()
        passwpegawai = self.loginPegawaiView.CtrlPassword.GetValue()
        query = """SELECT * from user_pegawai where username = ? and password = ?"""
        cursor = self._connection.cursor()
        cursor.execute(query, (userpegawai, passwpegawai))
        if cursor.fetchall():
            wx.MessageBox("Login Pegawai Berhasil!", "Login")
            self.loginView.Hide()
            self.loginPegawaiView.Hide()
            self.homePegawaiView.Show()
        else :
            wx.MessageBox("Error", "Login Gagal !")

    def loginAdminClick(self, event):
        self.loginPegawaiView.Hide()

    def stockClick(self, event):
        self.StockView.Show()
        self.homePemilikView.Hide()
        self.homePegawaiView.Hide()

    def transactionClick(self, event):
        self.TransactionView.Show()
        self.homePemilikView.Hide()
        self.homePegawaiView.Hide()

    def employeeClick(self, event):
        self.EmployeeView.Show()
        self.homePemilikView.Hide()
        self.homePegawaiView.Hide()

    def incomeClick(self, event):
        self.IncomeView.Show()
        self.homePemilikView.Hide()
        self.homePegawaiView.Hide()

    def stockPegawaiClick(self, event):
        self.StockViewP.Show()
        self.homePegawaiView.Hide()

    def transactionPegawaiClick(self, event):
        self.TransactionViewP.Show()
        self.homePegawaiView.Hide()


    #Transaction Controller

    def inputDataClick( self, event ):
        if self.TransactionView.selectedItem == None : return
        ambil = self.TransactionView.selectedItem
        hasil = self.TransactionView.listCtrlTransaction.GetItemText(item=int(ambil)-1, col=3)
        tambah = int(hasil) + 1
        self.TransactionView.listCtrlTransaction.SetItem(int(ambil)-1, 3, str(tambah))
        self.TransactionView.okBtn.Disable()

    def deleteDataClick( self, event ):
        if self.TransactionView.selectedItem == None : return
        ambil = self.TransactionView.selectedItem
        hasil = self.TransactionView.listCtrlTransaction.GetItemText(item=int(ambil)-1, col=3)
        tambah = int(hasil) - 1
        if hasil == "0"  :
            self.TransactionView.listCtrlTransaction.SetItem(int(ambil)-1, 3, "0")
        else:
            self.TransactionView.listCtrlTransaction.SetItem(int(ambil)-1, 3, str(tambah))
        self.TransactionView.okBtn.Disable()

    def handleSelectedTranc( self, event ):
        selectedId = event.GetItem().GetText()
        if not selectedId: return
        self.TransactionView.selectedItem = selectedId


    def checkDataClick(self, event):
        self.jumlahBarang = 0
        self.jumlahHarga = 0
        for row in range(self.TransactionView.listCtrlTransaction.GetItemCount()):
            item = self.TransactionView.listCtrlTransaction.GetItemText(item=row, col=3)
            self.jumlahBarang += int(item)
        for row in range(self.TransactionView.listCtrlTransaction.GetItemCount()):
            item = self.TransactionView.listCtrlTransaction.GetItemText(item=row, col=3)
            harga = self.TransactionView.listCtrlTransaction.GetItemText(item=row, col=2)
            self.jumlahHarga += (int(item) * int(harga))
            self.TransactionView.totalBayarBtn.SetValue(str(self.jumlahHarga))
        self.TransactionView.okBtn.Enable()

    def kembalianDataClick(self, event):
        a = int(self.TransactionView.totalBayarBtn.GetValue())
        b = int(self.TransactionView.uangBayarBtn.GetValue())
        result = b - a
        self.TransactionView.uangKembaliBtn.SetValue(str(result))


    def okClick(self, event):
        date_income = self.TransactionView.tanggalTransaksiBtn.GetValue()
        for row in range(self.TransactionView.listCtrlTransaction.GetItemCount()):
            item = self.TransactionView.listCtrlTransaction.GetItemText(item=row, col=3)
            if item != "0":
                namaBarang = self.TransactionView.listCtrlTransaction.GetItemText(item=row, col=1)
                hargaProduk = self.TransactionView.listCtrlTransaction.GetItemText(item=row, col=2)
                jumlahProduk = self.TransactionView.listCtrlTransaction.GetItemText(item=row, col=3)
        try:
            if self.id == None:
                result = self.incomeModel.insert(
                    values=[namaBarang, int(hargaProduk), int(jumlahProduk), date_income],
                    columns=['nama_barang', 'harga_barang', 'jumlah_beli','tanggal_transaksi'])
            else:
                result = self.incomeModel.update(
                    colValues={'nama_barang': namaBarang, 'harga_barang': hargaProduk, 'jumlah_beli': jumlahProduk, 'tanggal_transaksi': date_income},
                    identifierValue=self.id, identifierColumn='id_transaksi')

        except Exception as err:
            wx.MessageDialog(None, str(err), 'An error occured.', style=wx.OK | wx.ICON_ERROR).ShowModal()

        finally:
            if self.id == None:
                wx.MessageDialog(None, 'New Data successfully added.', 'Success',
                                 style=wx.OK | wx.ICON_INFORMATION).ShowModal()

            else:
                wx.MessageDialog(None, 'Data has been updated.', 'Update Success',
                                 style=wx.OK | wx.ICON_INFORMATION).ShowModal()




    #Stock Controller

    def addItemClick(self, event):
        self.AddItemView.Show()

    def editItemClick(self, event):
        if self.selectedItem == None: return

        prod = self.stockModel.find(self.selectedItem, column='id_barang')
        self.AddItemView.setProductName(prod[1])
        self.AddItemView.setCategory(prod[2])
        self.AddItemView.setUnitPrice(prod[3])
        self.AddItemView.setUnitQuantity(prod[4])
        self.id = self.selectedItem
        self.AddItemView.Show()

    def deleteItemClick(self, event):
        if self.selectedItem == None: return
        r = wx.MessageDialog(None, 'This data will be deleted permanently.', 'Are you sure',
                             style=wx.ICON_WARNING | wx.YES_NO | wx.NO_DEFAULT).ShowModal()

        if r == wx.ID_YES:
            self.stockModel.delete(value=self.selectedItem, column='id_barang')
            wx.MessageDialog(None, 'Author has been deleted.', 'Delete Success',
                             style=wx.OK | wx.ICON_INFORMATION).ShowModal()

    def handleSelectedItem(self, event):
        selectedId = event.GetItem().GetText()
        if not selectedId: return
        self.selectedItem = selectedId
        print(selectedId)

    def refreshItemClick(self, event):
        self.StockView.listCtrlStok.DeleteAllItems()
        Stok = self.stockModel.get(columns="*",orderByColumn='id_barang', orderByDirection='DESC', limit=self.StockView.limitData.GetValue())
        for rowIndex, row in enumerate(Stok):
            self.StockView.listCtrlStok.InsertItem(rowIndex, row[0])
            for columnIndex, col in enumerate(self.StockView.columns):
                self.StockView.listCtrlStok.SetItem(rowIndex, columnIndex, str(row[columnIndex]))

    #add item controller

    def saveItemClick(self, event):
        self.AddItemView.Hide()
        product_name = self.AddItemView.namaBarang.GetValue()
        category = self.AddItemView.jenisBarang.GetValue()
        unit_price = self.AddItemView.hargaBarang.GetValue()
        unit_quantity = self.AddItemView.jumlahBarang.GetValue()

        try:
            if self.id == None:
                result = self.stockModel.insert(values=[product_name, category, int(unit_price), int(unit_quantity)],
                                                  columns=['nama_barang', 'jenis_barang', 'harga_barang', 'jumlah_barang'])
            else:
                result = self.stockModel.update(
                    colValues={'nama_barang': product_name, 'jenis_barang': category, 'harga_barang': unit_price, 'jumlah_barang': unit_quantity},
                    identifierValue=self.id, identifierColumn='id_barang')

        except Exception as err:
            wx.MessageDialog(None, str(err), 'An error occured.', style=wx.OK | wx.ICON_ERROR).ShowModal()

        finally:
            if self.id == None:
                wx.MessageDialog(None, 'New Data successfully added.', 'Success',
                                 style=wx.OK | wx.ICON_INFORMATION).ShowModal()

            else:
                wx.MessageDialog(None, 'Data has been updated.', 'Update Success',
                                 style=wx.OK | wx.ICON_INFORMATION).ShowModal()

    def refreshIncomeClick(self, event):
        self.IncomeView.listCtrlTranc.DeleteAllItems()
        penghasilan = self.incomeModel.get(columns="*", orderByColumn='id_transaksi', orderByDirection='DESC',limit=self.IncomeView.limitData.GetValue())
        for rowIndex, row in enumerate(penghasilan):
            self.IncomeView.listCtrlTranc.InsertItem(rowIndex, row[0])
            for columnIndex, col in enumerate(self.IncomeView.columns):
                self.IncomeView.listCtrlTranc.SetItem(rowIndex, columnIndex, str(row[columnIndex]))

        # Employee Controller
    def addEmpClick(self, event):
        self.AddEmployeeView.Show()

    def editEmpClick(self, event):
        if self.selectedEmp == None: return

        karyawan = self.pegawaiModel.find(self.selectedEmp, column='id_pegawai')
        self.AddEmployeeView.setEmployeeName(karyawan[1])
        self.AddEmployeeView.setEmployeeAddress(karyawan[2])
        self.AddEmployeeView.setEmployeePhoneNumber(karyawan[3])
        self.AddEmployeeView.setEmployeeUsername(karyawan[4])
        self.AddEmployeeView.setEmployeePassword(karyawan[5])
        self.id = self.selectedEmp
        self.AddEmployeeView.Show()

    def deleteEmpClick(self, event):
        if self.selectedEmp == None: return
        r = wx.MessageDialog(None, 'This data will be deleted permanently.', 'Are you sure',
                             style=wx.ICON_WARNING | wx.YES_NO | wx.NO_DEFAULT).ShowModal()

        if r == wx.ID_YES:
           self.pegawaiModel.delete(value=self.selectedEmp, column='id_pegawai')
           wx.MessageDialog(None, 'Employee has been deleted.', 'Delete Success',
                            style=wx.OK | wx.ICON_INFORMATION).ShowModal()

    def handleSelectedEmp(self, event):
        selectedId = event.GetItem().GetText()
        if not selectedId: return
        self.selectedEmp = selectedId
        print(selectedId)

    def refreshEmpClick(self, event):
        self.EmployeeView.listCtrlPegawai.DeleteAllItems()
        Pegawai = self.pegawaiModel.get(columns="*", orderByColumn='id_pegawai', orderByDirection='DESC', limit=self.EmployeeView.limitData.GetValue())
        for rowIndex, row in enumerate(Pegawai):
            self.EmployeeView.listCtrlPegawai.InsertItem(rowIndex, row[0])
            for columnIndex, col in enumerate(self.EmployeeView.columns):
                self.EmployeeView.listCtrlPegawai.SetItem(rowIndex, columnIndex, str(row[columnIndex]))

        # add Employee controller

    def saveEmpClick(self, event):
        self.AddEmployeeView.Hide()
        Employee_Name = self.AddEmployeeView.namaPegawai.GetValue()
        Employee_Address = self.AddEmployeeView.alamatPegawai.GetValue()
        Employee_PhoneNumber = self.AddEmployeeView.telpPegawai.GetValue()
        Employee_Username = self.AddEmployeeView.usernameEmp.GetValue()
        Employee_Password = self.AddEmployeeView.passwordEmp.GetValue()
        try:
            if self.id == None:
                result = self.pegawaiModel.insert(values=[Employee_Name, Employee_Address, int(Employee_PhoneNumber), Employee_Username, Employee_Password],
                                                      columns=['nama_pegawai', 'alamat_pegawai', 'telp_pegawai', 'username', 'password'])
            else:
                result = self.pegawaiModel.update(
                    colValues={'nama_pegawai': Employee_Name, 'alamat_pegawai': Employee_Address, 'telp_pegawai': Employee_PhoneNumber, 'username': Employee_Username, 'password': Employee_Password},
                    identifierValue=self.id, identifierColumn='id_pegawai')

        except Exception as err:
            wx.MessageDialog(None, str(err), 'An error occured.', style=wx.OK | wx.ICON_ERROR).ShowModal()

        finally:
            if self.id == None:
                wx.MessageDialog(None, 'New Data successfully added.', 'Success',
                                style=wx.OK | wx.ICON_INFORMATION).ShowModal()

            else:
                wx.MessageDialog(None, 'Data has been updated.', 'Update Success',
                                style=wx.OK | wx.ICON_INFORMATION).ShowModal()



    def HomeMenuBtnClick(self, event):
        self.StockView.Hide()
        self.EmployeeView.Hide()
        self.IncomeView.Hide()
        self.TransactionView.Hide()
        self.homePemilikView = classHomePemilik(parent=None)
        self.homePemilikView.Show()
        self.homePemilikView.stock.Bind(wx.EVT_BUTTON, self.stockClick)
        self.homePemilikView.transaction.Bind(wx.EVT_BUTTON, self.transactionClick)
        self.homePemilikView.employee.Bind(wx.EVT_BUTTON, self.employeeClick)
        self.homePemilikView.income.Bind(wx.EVT_BUTTON, self.incomeClick)
        self.homePemilikView.Bind(wx.EVT_MENU, self.LogoutMenu)
        

    def LogoutMenu(self, event):
        self.homePemilikView.Hide()
        self.homePegawaiView.Hide()
        self.loginView.Show()

    def HomeMenuPegawaiBtnClick(self, event):
        self.StockViewP.Hide()
        self.TransactionViewP.Hide()
        self.homePegawaiView = classHomePegawai(parent=None)
        self.homePegawaiView.Show()
        self.homePegawaiView.stock.Bind(wx.EVT_BUTTON, self.stockPegawaiClick)
        self.homePegawaiView.transaction.Bind(wx.EVT_BUTTON, self.transactionPegawaiClick)
        self.homePegawaiView.Bind(wx.EVT_MENU, self.LogoutMenu)


    #================
    def main(self):
        self.loginView.Show()


























