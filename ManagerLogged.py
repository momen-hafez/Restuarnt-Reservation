# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManagerLogged.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(859, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 861, 61))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Background.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.RestaurentNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.RestaurentNameLabel.setGeometry(QtCore.QRect(610, 20, 301, 71))
        self.RestaurentNameLabel.setMinimumSize(QtCore.QSize(251, 20))
        self.RestaurentNameLabel.setStyleSheet("font: 75 24pt \"Courier\";\n"
"color:rgb(255, 255, 255)")
        self.RestaurentNameLabel.setObjectName("RestaurentNameLabel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 151, 101))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 30, 101, 41))
        self.label_3.setObjectName("label_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-1, 60, 861, 501))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 311, 471))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(320, 10, 241, 81))
        self.label_4.setObjectName("label_4")
        self.AddStaffIDLabel = QtWidgets.QLabel(self.tab)
        self.AddStaffIDLabel.setGeometry(QtCore.QRect(320, 50, 111, 81))
        self.AddStaffIDLabel.setObjectName("AddStaffIDLabel")
        self.AddStaffIDLineEdit = QtWidgets.QLineEdit(self.tab)
        self.AddStaffIDLineEdit.setGeometry(QtCore.QRect(400, 80, 191, 21))
        self.AddStaffIDLineEdit.setObjectName("AddStaffIDLineEdit")
        self.AddFirstNameLabel = QtWidgets.QLabel(self.tab)
        self.AddFirstNameLabel.setGeometry(QtCore.QRect(320, 80, 121, 81))
        self.AddFirstNameLabel.setObjectName("AddFirstNameLabel")
        self.FirstNameAddLineEdit = QtWidgets.QLineEdit(self.tab)
        self.FirstNameAddLineEdit.setGeometry(QtCore.QRect(400, 110, 191, 21))
        self.FirstNameAddLineEdit.setObjectName("FirstNameAddLineEdit")
        self.AddLastNameLabel = QtWidgets.QLabel(self.tab)
        self.AddLastNameLabel.setGeometry(QtCore.QRect(320, 120, 121, 61))
        self.AddLastNameLabel.setObjectName("AddLastNameLabel")
        self.LastNameAddLineEdit = QtWidgets.QLineEdit(self.tab)
        self.LastNameAddLineEdit.setGeometry(QtCore.QRect(400, 140, 191, 21))
        self.LastNameAddLineEdit.setObjectName("LastNameAddLineEdit")
        self.AddStaffButton = QtWidgets.QPushButton(self.tab)
        self.AddStaffButton.setGeometry(QtCore.QRect(490, 170, 113, 32))
        self.AddStaffButton.setObjectName("AddStaffButton")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(320, 180, 151, 81))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(320, 210, 161, 81))
        self.label_9.setObjectName("label_9")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(400, 240, 191, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 270, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.AddStaffWarning = QtWidgets.QLabel(self.tab)
        self.AddStaffWarning.setGeometry(QtCore.QRect(600, 160, 191, 41))
        self.AddStaffWarning.setObjectName("AddStaffWarning")
        self.DeleteStaffWarning = QtWidgets.QLabel(self.tab)
        self.DeleteStaffWarning.setGeometry(QtCore.QRect(600, 260, 191, 41))
        self.DeleteStaffWarning.setObjectName("DeleteStaffWarning")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 311, 471))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.AddNewItemLabel = QtWidgets.QLabel(self.tab_2)
        self.AddNewItemLabel.setGeometry(QtCore.QRect(320, 10, 171, 81))
        self.AddNewItemLabel.setObjectName("AddNewItemLabel")
        self.ItemIDLabel = QtWidgets.QLabel(self.tab_2)
        self.ItemIDLabel.setGeometry(QtCore.QRect(320, 40, 111, 81))
        self.ItemIDLabel.setObjectName("ItemIDLabel")
        self.ItemDescriptionLabel = QtWidgets.QLabel(self.tab_2)
        self.ItemDescriptionLabel.setGeometry(QtCore.QRect(320, 70, 131, 81))
        self.ItemDescriptionLabel.setObjectName("ItemDescriptionLabel")
        self.ItemPriceLabel = QtWidgets.QLabel(self.tab_2)
        self.ItemPriceLabel.setGeometry(QtCore.QRect(320, 110, 121, 61))
        self.ItemPriceLabel.setObjectName("ItemPriceLabel")
        self.AddItemIDLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.AddItemIDLineEdit.setGeometry(QtCore.QRect(430, 70, 161, 21))
        self.AddItemIDLineEdit.setObjectName("AddItemIDLineEdit")
        self.AddItemDescriptionLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.AddItemDescriptionLineEdit.setGeometry(QtCore.QRect(430, 100, 161, 21))
        self.AddItemDescriptionLineEdit.setObjectName("AddItemDescriptionLineEdit")
        self.AddItemPriceLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.AddItemPriceLineEdit.setGeometry(QtCore.QRect(430, 130, 161, 21))
        self.AddItemPriceLineEdit.setObjectName("AddItemPriceLineEdit")
        self.AddNewItemLabel_2 = QtWidgets.QLabel(self.tab_2)
        self.AddNewItemLabel_2.setGeometry(QtCore.QRect(320, 170, 171, 81))
        self.AddNewItemLabel_2.setObjectName("AddNewItemLabel_2")
        self.DeleteItemLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.DeleteItemLineEdit.setGeometry(QtCore.QRect(430, 230, 161, 21))
        self.DeleteItemLineEdit.setObjectName("DeleteItemLineEdit")
        self.ItemIDLabel_2 = QtWidgets.QLabel(self.tab_2)
        self.ItemIDLabel_2.setGeometry(QtCore.QRect(320, 200, 111, 81))
        self.ItemIDLabel_2.setObjectName("ItemIDLabel_2")
        self.AddItemButton = QtWidgets.QPushButton(self.tab_2)
        self.AddItemButton.setGeometry(QtCore.QRect(480, 160, 113, 32))
        self.AddItemButton.setObjectName("AddItemButton")
        self.DeleteItemButton = QtWidgets.QPushButton(self.tab_2)
        self.DeleteItemButton.setGeometry(QtCore.QRect(480, 260, 113, 32))
        self.DeleteItemButton.setObjectName("DeleteItemButton")
        self.AddNewItemLabel_3 = QtWidgets.QLabel(self.tab_2)
        self.AddNewItemLabel_3.setGeometry(QtCore.QRect(320, 270, 171, 81))
        self.AddNewItemLabel_3.setObjectName("AddNewItemLabel_3")
        self.ItemIDLabel_3 = QtWidgets.QLabel(self.tab_2)
        self.ItemIDLabel_3.setGeometry(QtCore.QRect(320, 300, 111, 81))
        self.ItemIDLabel_3.setObjectName("ItemIDLabel_3")
        self.ItemDescriptionLabel_2 = QtWidgets.QLabel(self.tab_2)
        self.ItemDescriptionLabel_2.setGeometry(QtCore.QRect(320, 330, 131, 81))
        self.ItemDescriptionLabel_2.setObjectName("ItemDescriptionLabel_2")
        self.ItemPriceLabel_2 = QtWidgets.QLabel(self.tab_2)
        self.ItemPriceLabel_2.setGeometry(QtCore.QRect(320, 360, 121, 81))
        self.ItemPriceLabel_2.setObjectName("ItemPriceLabel_2")
        self.UpdateItemIDLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.UpdateItemIDLineEdit.setGeometry(QtCore.QRect(430, 330, 161, 21))
        self.UpdateItemIDLineEdit.setObjectName("UpdateItemIDLineEdit")
        self.UpdateItemDescriptionLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.UpdateItemDescriptionLineEdit.setGeometry(QtCore.QRect(430, 360, 161, 21))
        self.UpdateItemDescriptionLineEdit.setObjectName("UpdateItemDescriptionLineEdit")
        self.UpdatePriceLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.UpdatePriceLineEdit.setGeometry(QtCore.QRect(430, 390, 161, 21))
        self.UpdatePriceLineEdit.setObjectName("UpdatePriceLineEdit")
        self.UpdateItemButton = QtWidgets.QPushButton(self.tab_2)
        self.UpdateItemButton.setGeometry(QtCore.QRect(480, 420, 113, 32))
        self.UpdateItemButton.setObjectName("UpdateItemButton")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 0, 511, 471))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(5)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        self.AddNewTableLabel = QtWidgets.QLabel(self.tab_3)
        self.AddNewTableLabel.setGeometry(QtCore.QRect(520, -20, 171, 81))
        self.AddNewTableLabel.setObjectName("AddNewTableLabel")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(520, 30, 121, 61))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(520, 50, 141, 81))
        self.label_6.setObjectName("label_6")
        self.AddTableNoLineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.AddTableNoLineEdit.setGeometry(QtCore.QRect(600, 50, 231, 21))
        self.AddTableNoLineEdit.setObjectName("AddTableNoLineEdit")
        self.AddTableCapacityLineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.AddTableCapacityLineEdit.setGeometry(QtCore.QRect(600, 80, 231, 21))
        self.AddTableCapacityLineEdit.setObjectName("AddTableCapacityLineEdit")
        self.AddNewTableLabel_2 = QtWidgets.QLabel(self.tab_3)
        self.AddNewTableLabel_2.setGeometry(QtCore.QRect(520, 170, 171, 81))
        self.AddNewTableLabel_2.setObjectName("AddNewTableLabel_2")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(520, 210, 121, 61))
        self.label_7.setObjectName("label_7")
        self.DeleteTableLineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.DeleteTableLineEdit.setGeometry(QtCore.QRect(600, 230, 231, 21))
        self.DeleteTableLineEdit.setObjectName("DeleteTableLineEdit")
        self.AddNewTableLabel_3 = QtWidgets.QLabel(self.tab_3)
        self.AddNewTableLabel_3.setGeometry(QtCore.QRect(520, 260, 171, 81))
        self.AddNewTableLabel_3.setObjectName("AddNewTableLabel_3")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(520, 300, 121, 61))
        self.label_10.setObjectName("label_10")
        self.UpdateTableNoLineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.UpdateTableNoLineEdit.setGeometry(QtCore.QRect(600, 320, 231, 21))
        self.UpdateTableNoLineEdit.setObjectName("UpdateTableNoLineEdit")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(520, 330, 141, 61))
        self.label_11.setObjectName("label_11")
        self.UpdateTableCapacityLineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.UpdateTableCapacityLineEdit.setGeometry(QtCore.QRect(600, 350, 231, 21))
        self.UpdateTableCapacityLineEdit.setObjectName("UpdateTableCapacityLineEdit")
        self.DeleteTableButton = QtWidgets.QPushButton(self.tab_3)
        self.DeleteTableButton.setGeometry(QtCore.QRect(720, 260, 113, 32))
        self.DeleteTableButton.setObjectName("DeleteTableButton")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(520, 90, 111, 61))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(520, 120, 111, 61))
        self.label_13.setObjectName("label_13")
        self.AddTableFromTime = QtWidgets.QTimeEdit(self.tab_3)
        self.AddTableFromTime.setGeometry(QtCore.QRect(600, 140, 118, 24))
        self.AddTableFromTime.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.AddTableFromTime.setObjectName("AddTableFromTime")
        self.AddTableToTime = QtWidgets.QTimeEdit(self.tab_3)
        self.AddTableToTime.setGeometry(QtCore.QRect(730, 140, 118, 24))
        self.AddTableToTime.setObjectName("AddTableToTime")
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(520, 360, 111, 61))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(520, 390, 111, 61))
        self.label_15.setObjectName("label_15")
        self.UpdateTableFromTime = QtWidgets.QTimeEdit(self.tab_3)
        self.UpdateTableFromTime.setGeometry(QtCore.QRect(600, 410, 118, 24))
        self.UpdateTableFromTime.setObjectName("UpdateTableFromTime")
        self.UpdateTableToTime = QtWidgets.QTimeEdit(self.tab_3)
        self.UpdateTableToTime.setGeometry(QtCore.QRect(730, 410, 118, 24))
        self.UpdateTableToTime.setObjectName("UpdateTableToTime")
        self.AddTableButton = QtWidgets.QPushButton(self.tab_3)
        self.AddTableButton.setGeometry(QtCore.QRect(720, 170, 113, 32))
        self.AddTableButton.setObjectName("AddTableButton")
        self.UpdateTableButton = QtWidgets.QPushButton(self.tab_3)
        self.UpdateTableButton.setGeometry(QtCore.QRect(720, 440, 113, 32))
        self.UpdateTableButton.setObjectName("UpdateTableButton")
        self.AddTableDate = QtWidgets.QDateEdit(self.tab_3)
        self.AddTableDate.setGeometry(QtCore.QRect(600, 110, 251, 24))
        self.AddTableDate.setObjectName("AddTableDate")
        self.UpdateTableDate = QtWidgets.QDateEdit(self.tab_3)
        self.UpdateTableDate.setGeometry(QtCore.QRect(600, 380, 251, 24))
        self.UpdateTableDate.setObjectName("UpdateTableDate")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_4.setGeometry(QtCore.QRect(10, 0, 831, 431))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(13)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(12, item)
        self.RefreshButton = QtWidgets.QPushButton(self.tab_4)
        self.RefreshButton.setGeometry(QtCore.QRect(720, 440, 113, 32))
        self.RefreshButton.setObjectName("RefreshButton")
        self.tabWidget.addTab(self.tab_4, "")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 10, 113, 32))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 859, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.RestaurentNameLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Shelby\'s Restaurent</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Welcome back, </span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#fefefe;\">Change</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Staff ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "First Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Last Name"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Add New Staff</span></p></body></html>"))
        self.AddStaffIDLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Staff ID</span></p></body></html>"))
        self.AddFirstNameLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">First Name</span></p></body></html>"))
        self.AddLastNameLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Last Name</span></p></body></html>"))
        self.AddStaffButton.setText(_translate("MainWindow", "Add"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Delete Staff</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Staff ID</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete"))
        self.AddStaffWarning.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.DeleteStaffWarning.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item ID"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Item description"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        self.AddNewItemLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Add New Item</span></p></body></html>"))
        self.ItemIDLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Item ID</span></p></body></html>"))
        self.ItemDescriptionLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Item description</span></p></body></html>"))
        self.ItemPriceLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Price</span></p></body></html>"))
        self.AddNewItemLabel_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Delete Item</span></p></body></html>"))
        self.ItemIDLabel_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Item ID</span></p></body></html>"))
        self.AddItemButton.setText(_translate("MainWindow", "Add"))
        self.DeleteItemButton.setText(_translate("MainWindow", "Delete"))
        self.AddNewItemLabel_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Update Item</span></p></body></html>"))
        self.ItemIDLabel_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Item ID</span></p></body></html>"))
        self.ItemDescriptionLabel_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Item description</span></p></body></html>"))
        self.ItemPriceLabel_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Price</span></p></body></html>"))
        self.UpdateItemButton.setText(_translate("MainWindow", "Update"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Booking No."))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Capacity"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "From Time"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "To Time"))
        self.AddNewTableLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Add New Table</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Table No.</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Capacity</span></p></body></html>"))
        self.AddNewTableLabel_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Delete Table</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Table No.</span></p></body></html>"))
        self.AddNewTableLabel_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Update Table</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Table No.</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Capacity</span></p></body></html>"))
        self.DeleteTableButton.setText(_translate("MainWindow", "Delete"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Date</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Time</span></p></body></html>"))
        self.AddTableFromTime.setDisplayFormat(_translate("MainWindow", "hh:mm"))
        self.AddTableToTime.setDisplayFormat(_translate("MainWindow", "hh:mm"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Date</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Time</span></p></body></html>"))
        self.UpdateTableFromTime.setDisplayFormat(_translate("MainWindow", "hh:mm"))
        self.UpdateTableToTime.setDisplayFormat(_translate("MainWindow", "hh:mm"))
        self.AddTableButton.setText(_translate("MainWindow", "Add"))
        self.UpdateTableButton.setText(_translate("MainWindow", "Update"))
        self.AddTableDate.setDisplayFormat(_translate("MainWindow", "d/M"))
        self.UpdateTableDate.setDisplayFormat(_translate("MainWindow", "d/M"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Booking No."))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Capacity"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "From Time"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "To Time"))
        item = self.tableWidget_4.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", " C-ID"))
        item = self.tableWidget_4.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "FirstName"))
        item = self.tableWidget_4.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "LastName"))
        item = self.tableWidget_4.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Ph No."))
        item = self.tableWidget_4.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Order ID"))
        item = self.tableWidget_4.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableWidget_4.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Comments"))
        item = self.tableWidget_4.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Item ID"))
        self.RefreshButton.setText(_translate("MainWindow", "Refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Page"))
        self.pushButton.setText(_translate("MainWindow", "Logout"))

