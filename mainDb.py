import sys
import mysql.connector
from PyQt5 import QtWidgets, QtCore, QtGui
import MainWindow, login, ManagerLogged, Reserve, Order, Complete, CheckReservation 
from tkinter import messagebox as mb
from datetime import datetime
flag = 0


mydb = mysql.connector.connect(
	host='localhost',
	database='Restaurant',
	user='root', 
	password='12345 6789 MM@@',
	auth_plugin='mysql_native_password'
    )


class MainScreen(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class loginScreen(QtWidgets.QMainWindow, login.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
 
class LoggedInScreen(QtWidgets.QMainWindow, ManagerLogged.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.TableUpdate()
        self.AddStaffButton.clicked.connect(self.AddStaff)
        self.pushButton_2.clicked.connect(self.DeleteStaff)
        self.loadData()
        self.AddItemButton.clicked.connect(self.AddItem)
        self.DeleteItemButton.clicked.connect(self.deleteItem)
        self.UpdateItemButton.clicked.connect(self.updateItem)
        self.loadBookingData()
        self.AddTableButton.clicked.connect(self.addReservation)
        self.showAllReservations()
        self.DeleteTableButton.clicked.connect(self.deleteReservation)
        self.showAllReservations()
        self.UpdateTableButton.clicked.connect(self.updateReservation)
        self.showAllReservations()
        self.RefreshButton.clicked.connect(self.showAllReservations)
        

    def TableUpdate(self):
    	mycursor = mydb.cursor()
    	mycursor.execute("SELECT * FROM Staff")
    	Data = mycursor.fetchall()

    	self.tableWidget.setRowCount(len(Data))
    	i=0
    	while i < len(Data):
    		j=0
    		while j < 3:
    			self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem("{}".format(Data[i][j])))
    			j += 1

    		i +=1

    def AddStaff(self):
    	msg = QtWidgets.QMessageBox()
    	msg.setIcon(QtWidgets.QMessageBox.Critical)
    	msg.setText("Error")
    	msg.setInformativeText("Please fill in the information correctly!")
    	msg.setWindowTitle("Error")
    	try:
    		StaffID = self.AddStaffIDLineEdit.text()
    		FirstName = self.FirstNameAddLineEdit.text()
    		LastName = self.LastNameAddLineEdit.text()
    		mycursor = mydb.cursor()
    		mycursor.execute("INSERT INTO Staff (Staff_id, F_name, L_name) VALUES (%s, %s, %s)", (StaffID, FirstName, LastName))
    		mydb.commit()
    		self.TableUpdate()
    	except:
    		msg.exec_()


    def DeleteStaff(self):
    	msg = QtWidgets.QMessageBox()
    	msg.setIcon(QtWidgets.QMessageBox.Critical)
    	msg.setText("Error")
    	msg.setInformativeText("Wrong Staff ID")
    	msg.setWindowTitle("Error")
    	try:
    		StaffID = self.lineEdit_4.text()
    		mycursor = mydb.cursor()
    		mycursor.execute('DELETE FROM Staff WHERE Staff_id = %(StaffID)s', {'StaffID': StaffID})
    		mydb.commit()
    		self.TableUpdate()
    	except:
    		msg.exec_()
    		


    def loadData(self):
    	cur = mydb.cursor()
    	cur.execute("SELECT * FROM Menu_item")
    	data = cur.fetchall()
    	row = 0

    	self.tableWidget_2.setRowCount(len(data))
    	for val in data:
    		self.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(str(val[0])))
    		self.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(str(val[1])))
    		self.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(str(val[2])))
    		row = row +1


    def AddItem(self):
    	msg = QtWidgets.QMessageBox()
    	msg.setIcon(QtWidgets.QMessageBox.Critical)
    	msg.setText("Error")
    	msg.setInformativeText("Enter the correct datatype")
    	msg.setWindowTitle("Error")

    	try:
    		ID = int(self.AddItemIDLineEdit.text())
    		Description = self.AddItemDescriptionLineEdit.text()
    		Price = float(self.AddItemPriceLineEdit.text())
    	except:
    		msg.exec_()
    		return

    	try:
    		cur = mydb.cursor()
    		sql = " INSERT INTO menu_item(item_id , item_descripton , price) VALUES (%s , %s , %s)" 
    		val = (ID, Description, Price)
    		cur.execute(sql, val)
    		mydb.commit()
    		self.loadData()
    	except:
    		msg.setInformativeText("Choose another ID")
    		msg.exec_()

    def deleteItem(self):
    	msg = QtWidgets.QMessageBox()
    	msg.setIcon(QtWidgets.QMessageBox.Critical)
    	msg.setText("Error")
    	msg.setInformativeText("Enter the correct datatype!")
    	msg.setWindowTitle("Error")
    	try:
    		ID = int(self.DeleteItemLineEdit.text())
    	except:
    		msg.exec_()
    		return
    	try:
    		cur = mydb.cursor()
    		num = "SELECT * FROM Menu_item"
    		cur.execute(num)
    		before = cur.fetchall()
    		sql = "DELETE FROM Menu_item WHERE item_id = %s"
    		val = (ID,)
    		cur.execute(sql, val)
    		mydb.commit()
    		cur.execute(num)
    		after = cur.fetchall()
    		self.loadData()
    		if len(before) == len(after):
    			msg.setInformativeText("The ID does not exist!")
    			msg.exec_()
    	except:
    		msg.setInformativeText("you can not delete a reserved item !")
    		msg.exec_()


    def updateItem(self):
    	msg = QtWidgets.QMessageBox()
    	msg.setIcon(QtWidgets.QMessageBox.Critical)
    	msg.setText("Error")
    	msg.setInformativeText("Enter the correct datatype!")
    	msg.setWindowTitle("Error")
    	try:
    		ID = int(self.UpdateItemIDLineEdit.text())
    		Description = self.UpdateItemDescriptionLineEdit.text()
    		Price = float(self.UpdatePriceLineEdit.text())
    	except:
    		msg.exec_()
    		return

    	cur = mydb.cursor()
    	num = "SELECT * FROM Menu_item"
    	cur.execute()
    	data = cur.fetchall()
    	flag = False
    	for row in data:
    		if row[0] == ID:
    			flag = True
    	if flag == True:
    		sql = "UPDATE Menu_item SET item_descripton = %s, price = %s WHERE item_id = %s"
    		val = (Description, Price, ID)
    		cur.execute(sql, val)
    		mydb.commit()
    		self.loadData()
    	else:
    		msg.setInformativeText("The ID does not exist!")
    		msg.exec_()



    def loadBookingData(self):
    	cur = mydb.cursor()
    	cur.execute("SELECT * FROM booking")
    	data = cur.fetchall()
    	row = 0
    	self.tableWidget_3.setRowCount(len(data))
    	for val in data:
    		self.tableWidget_3.setItem(row, 0, QtWidgets.QTableWidgetItem(str(val[0])))
    		string = str(val[1])
    		newStr = str(int(string[8:10])) + "/" + str(int(string[5:7]))
    		self.tableWidget_3.setItem(row, 1, QtWidgets.QTableWidgetItem(newStr))
    		self.tableWidget_3.setItem(row, 2, QtWidgets.QTableWidgetItem(str(val[2])))
    		self.tableWidget_3.setItem(row, 3, QtWidgets.QTableWidgetItem(str(val[3])))
    		self.tableWidget_3.setItem(row, 4, QtWidgets.QTableWidgetItem(str(val[4])))

    		if val[5] == True:
    			self.tableWidget_3.item(row, 0).setBackground(QtGui.QColor(255, 0, 0))
    			self.tableWidget_3.item(row, 1).setBackground(QtGui.QColor(255, 0, 0))
    			self.tableWidget_3.item(row, 2).setBackground(QtGui.QColor(255, 0, 0))
    			self.tableWidget_3.item(row, 3).setBackground(QtGui.QColor(255, 0, 0))
    			self.tableWidget_3.item(row, 4).setBackground(QtGui.QColor(255, 0, 0))
    		row = row + 1

    def addReservation(self):
    	msg = QtWidgets.QMessageBox()
    	msg.setIcon(QtWidgets.QMessageBox.Critical)
    	msg.setText("Error")
    	msg.setInformativeText("Please enter the correct datatype!")
    	msg.setWindowTitle("Error")
    	try:
    		ID = self.AddTableNoLineEdit.text()
    		capacity = self.AddTableCapacityLineEdit.text()
    		date = self.AddTableDate.text()
    		FTime = self.AddTableFromTime.text()
    		TTime = self.AddTableToTime.text()
    	except:
    		msg.exec_()

    	if ID == '' or capacity == '' or date == '' or FTime == '' or TTime =='':
    		msg.setInformativeText("Please enter all the required fields!")
    		msg.exec_()
    		return

    	dateS = date.split("/")
    	month = int(dateS[0])
    	day = int(dateS[1])
    	TimeFS = FTime.split(":")
    	HF = int(TimeFS[0])
    	MF = int(TimeFS[1])
    	TimeTS = TTime.split(":")
    	HT = int(TimeTS[0])
    	MT = int(TimeTS[1])
    	cur = mydb.cursor()
    	cur.execute("SELECT * FROM booking")
    	data = cur.fetchall()
    	itCan = True
    	isTheDateExist = False
    	for row in data:
    		string = str(row[1])
    		newStrT = str(int(string[8:10])) + "/" + str(int(string[5:7]))
    		TimeFST = str(row[3]).split(":")
    		HFT = int(TimeFST[0])
    		MFT = int(TimeFST[1])
    		TimeTST = str(row[4]).split(":")
    		HTT = int(TimeTST[0])
    		MTT = int(TimeTST[1])

    		if date == newStrT:
    			isTheDateExist = True
    			if (((HF < HFT or ((HF == HFT) and (MF < MFT))) and (HT > HFT or((HT == HFT) and (MT > MFT)))) or ((HF < HTT or ((HF == HTT) and (MF < MTT))) and (HT > HTT or((HT == HTT) and (MT > MTT)))) or((HF > HFT or ((HF == HFT) and (MF >= MFT))) and (HT < HTT or((HTT == HT) and (MT <= MTT))))  ) : 
    				itCan = False

    	if itCan == True or isTheDateExist == False:
    		try:
    			sql = "INSERT INTO booking (booking_id , number_in_party,booking_date,startTime,endTime) VALUES (%s,%s,%s,%s,%s)"
    			dt = "2020" + "-" + dateS[1] + "-" + dateS[0]
    			tt1 = TimeFS[0] + ":" + TimeFS[1] + ":" + "00"
    			tt2 = TimeTS[0] + ":" + TimeTS[1] + ":" + "00"
    			val = (ID, capacity, dt, tt1, tt2)
    			cur.execute(sql, val)
    			mydb.commit()
    			self.loadBookingData()
    		except:
    			msg.setInformativeText("Booking id is UNIQUE!")
    			msg.exec_()
    	else:
    		msg.setInformativeText("Choose another date because we have a reservation!")
    		msg.exec_()
    		itCan = True
    	self.showAllReservations()


    def deleteReservation(self):
    	msg = QtWidgets.QMessageBox()
    	msg.setIcon(QtWidgets.QMessageBox.Critical)
    	msg.setText("Error")
    	msg.setInformativeText("Enter the correct datatype!")
    	msg.setWindowTitle("Error")
    	try:
    		ID = int(self.DeleteTableLineEdit.text())
    	except:
    		msg.exec_()
    		return
    	try:
    		cur = mydb.cursor()
    		num = "SELECT * FROM booking"
    		cur.execute(num)
    		before = cur.fetchall()
    		sql = " DELETE FROM booking WHERE booking_id = %s"
    		val = (ID,)
    		cur.execute(sql, val)
    		mydb.commit()
    		cur.execute(num)
    		after = cur.fetchall()
    		self.loadBookingData()
    		if len(before) == len(after):
    			msg.setInformativeText("The booking ID does not exist!")
    			msg.exec_()
    	except:
    		msg.setInformativeText("That table is not reserved!")
    		msg.exec_()
    	self.showAllReservations()



    def updateReservation(self):
    	msg = QtWidgets.QMessageBox()
    	msg.setIcon(QtWidgets.QMessageBox.Critical)
    	msg.setText("Error")
    	msg.setInformativeText("Please enter the correct datatype!")
    	msg.setWindowTitle("Error")
    	try:
    		ID = self.UpdateTableNoLineEdit.text()
    		capacity= self.UpdateTableCapacityLineEdit.text()
    		date= self.UpdateTableDate.text()
    		FTime=self.UpdateTableFromTime.text()
    		TTime=self.UpdateTableToTime.text()
    	except:
    		msg.exec_()

    	if ID == '' or capacity == '' or date == '' or FTime =='' or TTime == '':
    		msg.setInformativeText("Please enter all the required fields!")
    		msg.exec_()
    		return

    	dateS = date.split("/")
    	month =int(dateS[0])
    	day = int(dateS[1])
    	TimeFS = FTime.split(":")
    	HF = int(TimeFS[0])
    	MF = int(TimeFS[1])
    	TimeTS = TTime.split(":")
    	HT = int(TimeTS[0])
    	MT = int(TimeTS[1])
    	cur = mydb.cursor()
    	cur.execute("SELECT * FROM booking")
    	data = cur.fetchall()
    	itCan = True
    	isTheDateExist = False
    	exist = False
    	for row in data:
    		string = str(row[1])
    		newStrT = str(int(string[8:10])) + "/" + str(int(string[5:7]))
    		TimeFST = str(row[3]).split(":")
    		HFT = int(TimeFST[0])
    		MFT = int(TimeFST[1])
    		TimeTST = str(row[4]).split(":")
    		HTT = int(TimeTST[0])
    		MTT = int(TimeTST[1])
    		if date == newStrT or row[0] == int(ID):
    			if row[0] == int(ID):
    				exist = True
    			if date == newStrT:
    				isTheDateExist = True

    			if (((HF < HFT or ((HF == HFT) and (MF < MFT))) and (HT > HFT or((HT == HFT) and (MT > MFT)))) or ((HF < HTT or ((HF == HTT) and (MF < MTT))) and (HT > HTT or((HT == HTT) and (MT > MTT)))) or((HF > HFT or ((HF == HFT) and (MF >= MFT))) and (HT < HTT or((HTT == HT) and (MT <= MTT))))  ) : 
    				itCan = False

    	if exist == True  and (itCan == True or isTheDateExist == False):
    		try:
    			sql = "UPDATE booking SET number_in_party=%s ,booking_date = %s,startTime =%s,endTime = %s WHERE booking_id = %s"
    			dt = "2020" + "-" + dateS[1] + '-' + dateS[0]
    			tt1 = TimeFS[0] + ":" + TimeFS[1] + ":" + "00"
    			tt2 = TimeTS[0] + ":" + TimeTS[1] + ":" + "00"
    			val = (capacity , dt , tt1 , tt2 , ID)
    			cur.execute(sql , val)
    			mydb.commit()
    			self.loadBookingData()
    		except:
    			msg.setInformativeText("Booking ID is unique! as well as the date with times!")
    			msg.exec_()

    	elif exist == False:
    		msg.setInformativeText("The ID doesn't exist!")
    		msg.exec_()
    	else:
    		msg.setInformativeText("Choose another date, because we have a reservation!")
    		msg.exec_()
    		itCan = True
    	self.showAllReservations()


    def showAllReservations(self):
    	mycursor = mydb.cursor()
    	mycursor.execute("SELECT * FROM booking")
    	bookingData = mycursor.fetchall()

    	row = 0
    	self.tableWidget_4.setRowCount(len(bookingData))

    	for val in bookingData:
    		self.tableWidget_4.setItem(row, 0, QtWidgets.QTableWidgetItem(str(val[0])))
    		self.tableWidget_4.setItem(row, 1, QtWidgets.QTableWidgetItem(str(val[1])))
    		self.tableWidget_4.setItem(row, 2, QtWidgets.QTableWidgetItem(str(val[2])))
    		self.tableWidget_4.setItem(row, 3, QtWidgets.QTableWidgetItem(str(val[3])))
    		self.tableWidget_4.setItem(row, 4, QtWidgets.QTableWidgetItem(str(val[4])))

    		if val[5] == True:
    			mycursor.execute("SELECT * FROM booked_table WHERE Booking_id = %(BookingID)s", {'BookingID': val[0]})
    			tempData = mycursor.fetchone()
    			mycursor.execute("SELECT * FROM Customer WHERE C_id = %(CID)s", {'CID': tempData[2]})
    			customerData = mycursor.fetchone()
    			mycursor.execute("SELECT * FROM Order_Menu_item WHERE Booking_id = %(BookingID)s", {'BookingID': tempData[0]})
    			orderData = mycursor.fetchone()
    			self.tableWidget_4.setItem(row, 5, QtWidgets.QTableWidgetItem(str(customerData[0])))
    			self.tableWidget_4.setItem(row, 6, QtWidgets.QTableWidgetItem(str(customerData[1])))
    			self.tableWidget_4.setItem(row, 7, QtWidgets.QTableWidgetItem(str(customerData[2])))
    			self.tableWidget_4.setItem(row, 8, QtWidgets.QTableWidgetItem(str(customerData[3])))
    			self.tableWidget_4.setItem(row, 9, QtWidgets.QTableWidgetItem(str(orderData[0])))
    			self.tableWidget_4.setItem(row, 10, QtWidgets.QTableWidgetItem(str(orderData[1])))
    			self.tableWidget_4.setItem(row, 11, QtWidgets.QTableWidgetItem(str(orderData[2])))
    			self.tableWidget_4.setItem(row, 12, QtWidgets.QTableWidgetItem(str(orderData[3])))
   				   				
    		row += 1


class ReserveScreen(QtWidgets.QMainWindow, Reserve.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadBookingData()
        self.ReserveButton.clicked.connect(self.Reservation)
    def loadBookingData(self):
    	msg = QtWidgets.QMessageBox()
    	msg.setIcon(QtWidgets.QMessageBox.Critical)
    	msg.setText("Error")
    	msg.setInformativeText("Please enter the correct datatype!")
    	msg.setWindowTitle("Error")
    	cur = mydb.cursor()
    	cur.execute("SELECT * FROM booking")
    	data = cur.fetchall()
    	row = 0
    	Counter = 0
    	for arg in data:
    		if arg[5] != True:
    			Counter += 1

    	self.tableWidget.setRowCount(Counter)
    	ans = 0
    	for val in data:
    		Flag = False
    		if val[5] != True:
    			ans += 1
    			self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(val[0])))
    			string = str(val[1])
    			newStr = str(int(string[8:10])) + "/" + str(int(string[5:7]))
    			self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(newStr))
    			self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(val[2])))
    			self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(val[3])))
    			self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(val[4])))
    			self.comboBox.addItem(str(val[0]))
    			Flag = True
    		if Flag == True:
    			row = row + 1




    def Reservation(self):
    	flag = True
    	msg = QtWidgets.QMessageBox()
    	msg.setIcon(QtWidgets.QMessageBox.Critical)
    	msg.setText("Error")
    	msg.setInformativeText("Please enter the correct datatype!")
    	msg.setWindowTitle("Error")
    	try:
    		BookingNo = self.comboBox.currentText()
    		FirstName = self.FirstNameLineEdit.text()
    		LastName = self.LastNameLineEdit.text()
    		PhNo = self.PhNoLineEdit.text()
    		AddInfo = self.AddInfoLineEdit.text()

    	except:
    		error_dialog.showMessage("Fill out the blanks correctly!")
    	if  FirstName == '' or LastName == '' or PhNo == '':
    		msg.setInformativeText("Fill out the blanks correctly!")
    		msg.exec_()
    		flag = False
    		return
    	if flag == True:
    		mycursor = mydb.cursor()
    		mycursor.execute("INSERT INTO Customer (F_name, L_Name, ph_num) VALUES (%s, %s, %s)", (FirstName, LastName, PhNo))
    		mycursor.execute("INSERT INTO booked_table (Booking_id, details) VALUES (%s, %s)", (BookingNo, AddInfo))
    		mycursor.execute("UPDATE booking SET isReserved = True WHERE Booking_id = %(BookingNo)s", { 'BookingNo' : BookingNo })
    		global Booking
    		Booking = BookingNo
    		self.loadBookingData()


#-------------------------------------------------------------
class OrderScreen(QtWidgets.QMainWindow, Order.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.TableLoad()
        self.AddOrderButton.clicked.connect(self.CustomerOrder)

    def TableLoad(self):
    	print("hi")
    	mycursor = mydb.cursor()
    	mycursor.execute("SELECT * FROM Menu_item")
    	data = mycursor.fetchall()
    	for k in data:
    		print(k)
    	self.tableWidget.setRowCount(len(data))
    	row = 0
    	for val in data:
    		self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(val[0])))
    		self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(val[1])))
    		self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(val[2])))
    		self.comboBox.addItem(str(val[0]))
    		row += 1


    def CustomerOrder(self):
    	error_dialog = QtWidgets.QErrorMessage()
    	try:
    		ItemID = self.comboBox.currentText()
    		Quantity = self.lineEdit.text()
    		AddInfo = self.lineEdit_2.text()
    		BookingID = Booking
    	except:
    		error_dialog.showMessage("Fill out the blanks correctly!")
    	try:
    		mycursor = mydb.cursor()
    		mycursor.execute("INSERT INTO Order_Menu_item (Quantity, comments, item_id, Booking_id) VALUES (%s, %s, %s, %s)", (Quantity, AddInfo, ItemID, BookingID))
    		mydb.commit()
    	except:
    		error_dialog.showMessage("Fill out the blanks correctly!")


class CompleteScreen(QtWidgets.QMainWindow, Complete.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class CheckReservationScreen(QtWidgets.QMainWindow, CheckReservation.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.loadCustomerBooking)

    def loadCustomerBooking(self):
    	msg = QtWidgets.QMessageBox()
    	msg.setIcon(QtWidgets.QMessageBox.Critical)
    	msg.setText("Error")
    	msg.setInformativeText("Please Fill the blanks correctly!")
    	msg.setWindowTitle("Error")
    	try:
    		BookingNo = self.lineEdit.text()
    	except:
    		msg.exec_()

    	if BookingNo == '':
    		msg.exec_()
    		return
    	try:
    		mycursor = mydb.cursor()
    		mycursor.execute("SELECT * FROM booking WHERE booking_id = %(BookingNo)s", {'BookingNo': BookingNo})
    		bookedData = mycursor.fetchone()
    		mycursor.execute("SELECT * FROM booked_table WHERE Booking_id = %(BookingID)s", {'BookingID': bookedData[0]})
    		tempData = mycursor.fetchone()
    		mycursor.execute("SELECT * FROM Customer WHERE C_id = %(CID)s", {'CID': tempData[2]})
    		customerData = mycursor.fetchone()
    		mycursor.execute("SELECT * FROM Order_Menu_item WHERE Booking_id = %(BookingNo)s", {'BookingNo': BookingNo})
    		orderData = mycursor.fetchone()
    	except:
    		msg.setInformativeText("That table is not reserved!")
    		msg.exec_()
    		return

    	self.tableWidget.setRowCount(1)
    	self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(bookedData[0])))
    	self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(bookedData[1])))
    	self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str(bookedData[2])))
    	self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str(bookedData[3])))
    	self.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem(str(bookedData[4])))
    	self.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem(str(customerData[0])))
    	self.tableWidget.setItem(0, 6, QtWidgets.QTableWidgetItem(str(customerData[1])))
    	self.tableWidget.setItem(0, 7, QtWidgets.QTableWidgetItem(str(customerData[2])))
    	self.tableWidget.setItem(0, 8, QtWidgets.QTableWidgetItem(str(customerData[3])))
    	self.tableWidget.setItem(0, 9, QtWidgets.QTableWidgetItem(str(orderData[0])))
    	self.tableWidget.setItem(0, 10, QtWidgets.QTableWidgetItem(str(orderData[1])))
    	self.tableWidget.setItem(0, 11, QtWidgets.QTableWidgetItem(str(orderData[2])))
    	self.tableWidget.setItem(0, 12, QtWidgets.QTableWidgetItem(str(orderData[3])))





def main():
    app = QtWidgets.QApplication(sys.argv)
    MScreen = MainScreen()
    LScreen= loginScreen()
    LIScreen = LoggedInScreen()
    RScreen = ReserveScreen()
    OScreen = OrderScreen()
    CScreen = CompleteScreen()
    CRScreen = CheckReservationScreen()
    window = QtWidgets.QStackedWidget()
    window.addWidget(MScreen)
    window.addWidget(LScreen)
    window.addWidget(LIScreen)
    window.addWidget(RScreen)
    window.addWidget(OScreen)
    window.addWidget(CScreen)
    window.addWidget(CRScreen)
    MScreen.pushButton.clicked.connect(lambda: window.setCurrentIndex(1))
    MScreen.pushButton_3.clicked.connect(lambda: window.setCurrentIndex(6))
    LScreen.pushButton_2.clicked.connect(lambda: window.setCurrentIndex(0))
    LScreen.pushButton.clicked.connect(lambda: LoginAction(LScreen, window, LIScreen))
    MScreen.pushButton_2.clicked.connect(lambda: window.setCurrentIndex(3))
    MScreen.pushButton_2.clicked.connect(lambda: RScreen.loadBookingData())
    RScreen.ReserveButton.clicked.connect(lambda: window.setCurrentIndex(4))
    RScreen.ReserveButton.clicked.connect(lambda:OScreen.TableLoad())
    RScreen.ReserveButton.clicked.connect(lambda:LIScreen.loadBookingData())
    RScreen.pushButton.clicked.connect(lambda: window.setCurrentIndex(0))
    OScreen.AddOrderButton.clicked.connect(lambda: window.setCurrentIndex(5))
    OScreen.pushButton.clicked.connect(lambda: window.setCurrentIndex(3))
    CScreen.pushButton.clicked.connect(lambda: window.setCurrentIndex(0))
    LIScreen.pushButton.clicked.connect(lambda: window.setCurrentIndex(1))
    CRScreen.pushButton.clicked.connect(lambda: window.setCurrentIndex(0))
    CRScreen.pushButton.clicked.connect(lambda: LIScreen.loadBookingData())
    window.resize(800, 600)
    window.show()
    app.exec_()

def LoginAction(LScreen, window, LIScreen):
	msg = QtWidgets.QMessageBox()
	msg.setIcon(QtWidgets.QMessageBox.Critical)
	msg.setText("Error")
	msg.setInformativeText("Please fill in the information correctly!")
	msg.setWindowTitle("Error")
	try:
		Username = LScreen.textEdit.toPlainText()
		Password = LScreen.lineEdit.text()
	except:
		msg.exec_()

	if Username == '' or Password == '':
		msg.exec_()
		return

	mycursor = mydb.cursor()
	mycursor.execute('SELECT * FROM Manager WHERE Manager_id = %(Username)s', { 'Username' : Username })
	checkUsername = mycursor.fetchone()
	if checkUsername != None:
		if checkUsername[3] == Password:
			window.setCurrentIndex(2)
			LIScreen.label_3.setText("<html><head/><body><p><span style=\" color:#fefefe;\">{}</span></p></body></html>".format(checkUsername[1]))

		else:
			msg.setInformativeText("Incorrect Password")
			msg.exec_()
	else:
		msg.setInformativeText("Username does not exist!")
		msg.exec_()




	
	 
if __name__ == '__main__':
    main()
