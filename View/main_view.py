# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_view.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from View.DBManager import DatabaseManager

class Ui_MainWindow(object):

    def __init__(self):
        super().__init__()
        self.DBManager = DatabaseManager()
        self.data = None
        self.filtered_data = None


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 1005)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_year_select = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_year_select.setGeometry(QtCore.QRect(510, 0, 121, 31))
        self.comboBox_year_select.setObjectName("comboBox_year_select")
        self.comboBox_month_select = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_month_select.setGeometry(QtCore.QRect(620, 0, 121, 31))
        self.comboBox_month_select.setObjectName("comboBox_month_select")
        self.comboBox_type_select = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_type_select.setGeometry(QtCore.QRect(810, 0, 121, 31))
        self.comboBox_type_select.setObjectName("comboBox_type_select")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 80, 381, 883))
        self.listWidget.setObjectName("listWidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(380, 80, 821, 883))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.label_customer_name = QtWidgets.QLabel(self.centralwidget)
        self.label_customer_name.setGeometry(QtCore.QRect(10, 0, 71, 16))
        self.label_customer_name.setObjectName("label_customer_name")
        self.label_customer_name_data = QtWidgets.QLabel(self.centralwidget)
        self.label_customer_name_data.setGeometry(QtCore.QRect(100, 0, 250, 16))
        self.label_customer_name_data.setObjectName("label_customer_name_data")
        self.label_total_weight = QtWidgets.QLabel(self.centralwidget)
        self.label_total_weight.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label_total_weight.setObjectName("label_total_weight")
        self.label_total_weight_data = QtWidgets.QLabel(self.centralwidget)
        self.label_total_weight_data.setGeometry(QtCore.QRect(100, 20, 81, 16))
        self.label_total_weight_data.setObjectName("label_total_weight_data")
        self.label_total = QtWidgets.QLabel(self.centralwidget)
        self.label_total.setGeometry(QtCore.QRect(10, 40, 81, 16))
        self.label_total.setObjectName("label_total")
        self.label_total_data = QtWidgets.QLabel(self.centralwidget)
        self.label_total_data.setGeometry(QtCore.QRect(100, 40, 81, 16))
        self.label_total_data.setObjectName("label_total_data")
        self.label_total_data_ZH = QtWidgets.QLabel(self.centralwidget)
        self.label_total_data_ZH.setGeometry(QtCore.QRect(100, 60, 81, 16))
        self.label_total_data_ZH.setObjectName("label_total_data_ZH")
        self.label_month_select = QtWidgets.QLabel(self.centralwidget)
        self.label_month_select.setGeometry(QtCore.QRect(400, 5, 81, 21))
        self.label_month_select.setObjectName("label_month_select")
        self.label_monthly_total_weight = QtWidgets.QLabel(self.centralwidget)
        self.label_monthly_total_weight.setGeometry(QtCore.QRect(400, 30, 91, 16))
        self.label_monthly_total_weight.setObjectName("label_monthly_total_weight")
        self.pushButton_import = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_import.setGeometry(QtCore.QRect(1090, 0, 113, 31))
        self.pushButton_import.setObjectName("pushButton_import")
        self.pushButton_export = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_export.setGeometry(QtCore.QRect(1090, 50, 113, 31))
        self.pushButton_export.setObjectName("pushButton_export")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(1090, 25, 113, 31))
        self.pushButton_save.setObjectName("pushButton_save")
        self.label_monthly_total = QtWidgets.QLabel(self.centralwidget)
        self.label_monthly_total.setGeometry(QtCore.QRect(400, 50, 91, 16))
        self.label_monthly_total.setObjectName("label_monthly_total")
        self.label_monthly_total_weight_data = QtWidgets.QLabel(self.centralwidget)
        self.label_monthly_total_weight_data.setGeometry(QtCore.QRect(515, 30, 61, 16))
        self.label_monthly_total_weight_data.setObjectName("label_monthly_total_weight_data")
        self.label_monthly_total_data = QtWidgets.QLabel(self.centralwidget)
        self.label_monthly_total_data.setGeometry(QtCore.QRect(515, 50, 61, 16))
        self.label_monthly_total_data.setObjectName("label_monthly_total_data")
        self.label_monthly_total_data_ZH = QtWidgets.QLabel(self.centralwidget)
        self.label_monthly_total_data_ZH.setGeometry(QtCore.QRect(640, 50, 61, 16))
        self.label_monthly_total_data_ZH.setObjectName("label_monthly_total_data_ZH")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.MenuBar = QtWidgets.QAction(MainWindow)
        self.MenuBar.setObjectName("MenuBar")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")

        self.pushButton_save.setDisabled(True)

        self.listWidget.itemSelectionChanged.connect(self.selection_changed)
        self.pushButton_save.clicked.connect(self.save_table)
        self.comboBox_month_select.currentTextChanged.connect(self.selection_changed)
        self.comboBox_year_select.currentTextChanged.connect(self.selection_changed)
        self.comboBox_type_select.currentTextChanged.connect(self.selection_changed)

        self.retranslateUi(MainWindow)
        self.set_main_window_data()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DATE"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CARNUM"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "PRODUCTNAME"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "WEIGHT"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "PRICE"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "TOTAL"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "MEMO"))
        self.label_customer_name.setText(_translate("MainWindow", "客户:"))
        self.label_customer_name_data.setText(_translate("MainWindow", "未选择"))
        self.label_total_weight.setText(_translate("MainWindow", "Total Weight:"))
        self.label_total_weight_data.setText(_translate("MainWindow", "TotalWeight"))
        self.label_total.setText(_translate("MainWindow", "Total:"))
        self.label_total_data.setText(_translate("MainWindow", "Total"))
        self.label_total_data_ZH.setText(_translate("MainWindow", "Total"))
        self.label_month_select.setText(_translate("MainWindow", "时间选择："))
        self.label_monthly_total_weight.setText(_translate("MainWindow", "Monthly To W"))
        self.pushButton_import.setText(_translate("MainWindow", "Import"))
        self.pushButton_export.setText(_translate("MainWindow", "Export"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.label_monthly_total.setText(_translate("MainWindow", "Monthly Total"))
        self.label_monthly_total_weight_data.setText(_translate("MainWindow", "TextLabel"))
        self.label_monthly_total_data.setText(_translate("MainWindow", "TextLabel"))
        self.label_monthly_total_data_ZH.setText(_translate("MainWindow", "TextLabel"))
        self.MenuBar.setText(_translate("MainWindow", "Import"))
        self.actionExport.setText(_translate("MainWindow", "Export"))

    def set_main_window_data(self):
        for customer in self.DBManager.get_customer_list():
            self.listWidget.addItem(customer[0])
        self.DBManager.execute('SELECT DISTINCT Month FROM ORDERS')
        months = self.DBManager.fetch_all()
        self.comboBox_month_select.addItem('查看所有月份')
        for month in months:
            self.comboBox_month_select.addItem(str(month[0])+ '月')
        self.DBManager.execute('SELECT DISTINCT Year FROM ORDERS')
        years = self.DBManager.fetch_all()
        self.comboBox_year_select.addItem('查看所有年份')
        for year in years:
            self.comboBox_year_select.addItem(str(year[0]) + '年')
        self.comboBox_year_select.setCurrentIndex(0)
        self.comboBox_type_select.addItem('水泥')
        self.comboBox_type_select.addItem('砂石')
        self.comboBox_type_select.setCurrentIndex(0)

    def selection_changed(self):
        if not self.listWidget.selectedItems():
            return;
        self.tableWidget.clearContents()
        self.pushButton_save.setDisabled(False)
        customer_name = self.listWidget.selectedItems()[0].text()
        self.label_customer_name_data.setText(customer_name)
        self.data = self.DBManager.get_data(customer_name)
        row = 0
        self.filtered_data = self.data
        print(self.filtered_data)
        self.filter_by_month()
        print(self.filtered_data)
        self.filter_by_year()
        print(self.filtered_data)
        self.filter_by_type()
        print(self.filtered_data)
        self.tableWidget.setRowCount(len(self.filtered_data))
        for i in self.filtered_data:
            self.tableWidget.setItem(row, 0
                                     , QTableWidgetItem(f'''{i[0]}/{i[1]}/{i[2]}'''))
            for j in range(3, 5):
                self.tableWidget.setItem(row, j-2
                                         , QTableWidgetItem(i[j]))
            for j in range(6, 8):
                self.tableWidget.setItem(row, j-3
                                         , QTableWidgetItem(str(i[j])))
            self.tableWidget.setItem(row, 6
                                     , QTableWidgetItem(i[8]))
            row += 1

    def save_table(self):
        r = self.tableWidget.rowCount()
        c = self.tableWidget.columnCount()
        temp = []
        for i in range(0, r):
            sub_temp = ()
            for j in range(0, c):
                if self.tableWidget.item(i,j):
                    #TODO: implement save
                    pass

    def filter_by_month(self):
        selection = self.comboBox_month_select.currentText()
        if selection == '查看所有月份':
            return
        month = selection.strip('月')
        print(month)
        temp_data = []
        for i in self.filtered_data:
            if i[1] == int(month):
                temp_data.append(i)
        self.filtered_data = temp_data

    def filter_by_year(self):
        selection = self.comboBox_year_select.currentText()
        if selection == '查看所有年份':
            return
        year = selection.strip('年')
        temp_data = []
        for i in self.filtered_data:
            if i[0] == int(year):
                temp_data.append(i)
        self.filtered_data = temp_data

    def filter_by_type(self):
        selection = self.comboBox_type_select.currentText()
        if selection ==  '水泥':
            selection = 0
        else:
            selection = 1
        temp_data = []
        for i in self.filtered_data:
            if i[9] == selection:
                temp_data.append(i)
        self.filtered_data = temp_data
