
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QAction\
    , QErrorMessage
from View.DBManager import DatabaseManager
from View.XlsxWriter import export_file
from View.ParserWrapper import read_from_file
from PyQt5.QtGui import QIcon
from View.main_ import main_window
selected_file_name = ''
main_window_ref = None
version = '0.1.004'

def sort_by_date(val):
    return val[2]


def sort_by_month(val):
    return val[1]


def sort_by_year(val):
    return val[0]

class Ui_MainWindow(object):

    def __init__(self):
        super().__init__()
        self.DBManager = DatabaseManager()
        self.data = None
        self.filtered_data = None
        self.prev_cur_year = '查看所有年份'
        self.prev_cur_month = '查看所有月份'
        self.prev_cur_type = '水泥'

        main_window_ref = self

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 990)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_year_select = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_year_select.setGeometry(QtCore.QRect(510, 0, 150, 31))
        self.comboBox_year_select.setObjectName("comboBox_year_select")
        self.comboBox_month_select = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_month_select.setGeometry(QtCore.QRect(660, 0, 150, 31))
        self.comboBox_month_select.setObjectName("comboBox_month_select")
        self.comboBox_type_select = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_type_select.setGeometry(QtCore.QRect(810, 0, 121, 31))
        self.comboBox_type_select.setObjectName("comboBox_type_select")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 80, 381, 883))
        self.listWidget.setObjectName("listWidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(380, 80, 1120, 883))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.setColumnWidth(0, 150)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.setColumnWidth(2,200)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.setColumnWidth(6, 350)
        self.label_customer_name = QtWidgets.QLabel(self.centralwidget)
        self.label_customer_name.setGeometry(QtCore.QRect(10, 5, 71, 16))
        self.label_customer_name.setObjectName("label_customer_name")
        self.label_customer_name_data = QtWidgets.QLabel(self.centralwidget)
        self.label_customer_name_data.setGeometry(QtCore.QRect(50, 5, 330, 16))
        self.label_customer_name_data.setObjectName("label_customer_name_data")
        self.label_total_weight = QtWidgets.QLabel(self.centralwidget)
        self.label_total_weight.setGeometry(QtCore.QRect(10, 25, 81, 16))
        self.label_total_weight.setObjectName("label_total_weight")
        self.label_total_weight_data = QtWidgets.QLabel(self.centralwidget)
        self.label_total_weight_data.setGeometry(QtCore.QRect(50, 25, 81, 16))
        self.label_total_weight_data.setObjectName("label_total_weight_data")
        self.label_total = QtWidgets.QLabel(self.centralwidget)
        self.label_total.setGeometry(QtCore.QRect(10, 45, 81, 16))
        self.label_total.setObjectName("label_total")
        self.label_total_data = QtWidgets.QLabel(self.centralwidget)
        self.label_total_data.setGeometry(QtCore.QRect(50, 45, 81, 16))
        self.label_total_data.setObjectName("label_total_data")
        self.label_total_data_ZH = QtWidgets.QLabel(self.centralwidget)
        self.label_total_data_ZH.setGeometry(QtCore.QRect(50, 62, 81, 16))
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
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(1343, 25, 113, 31))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_refresh.setGeometry(QtCore.QRect(1200, 25, 113, 31))
        self.pushButton_refresh.setObjectName("pushButton_refresh")
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
        self.label_monthly_total_data_ZH.setGeometry(QtCore.QRect(625, 50, 61, 16))
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
        self.pushButton_export.setDisabled(True)
        self.pushButton_delete.setDisabled(True)
        self.set_main_window_data()

        self.listWidget.itemSelectionChanged.connect(self.selection_changed)
        self.pushButton_save.clicked.connect(self.save_table)
        self.comboBox_month_select.currentTextChanged.connect(self.selection_changed)
        self.comboBox_year_select.currentTextChanged.connect(self.selection_changed)
        self.comboBox_type_select.currentTextChanged.connect(self.selection_changed)
        self.pushButton_import.clicked.connect(self.open_file_chooser)
        self.pushButton_export.clicked.connect(self.export)
        self.pushButton_delete.clicked.connect(self.delete_month)
        self.pushButton_refresh.clicked.connect(self.refresh)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", f"结算单管理 v{version}"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "日期"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "车号"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "产品名称"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "重量"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "价格"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "总计"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "备忘"))
        self.label_customer_name.setText(_translate("MainWindow", "客户:"))
        self.label_customer_name_data.setText(_translate("MainWindow", "未选择"))
        self.label_total_weight.setText(_translate("MainWindow", "总重:"))
        self.label_total_weight_data.setText(_translate("MainWindow", "TotalWeight"))
        self.label_total.setText(_translate("MainWindow", "总价:"))
        self.label_total_data.setText(_translate("MainWindow", "Total"))
        self.label_total_data_ZH.setText(_translate("MainWindow", "Total"))
        self.label_month_select.setText(_translate("MainWindow", "时间选择："))
        self.label_monthly_total_weight.setText(_translate("MainWindow", "所选范围内总重"))
        self.pushButton_import.setText(_translate("MainWindow", "导入"))
        self.pushButton_export.setText(_translate("MainWindow", "生成结算单"))
        self.pushButton_save.setText(_translate("MainWindow", "保存表格"))
        self.pushButton_delete.setText(_translate("MainWindow", "删除"))
        self.pushButton_refresh.setText(_translate("MainWindow", "刷新"))
        self.label_monthly_total.setText(_translate("MainWindow", "合计"))
        self.label_monthly_total_weight_data.setText(_translate("MainWindow", "TextLabel"))
        self.label_monthly_total_data.setText(_translate("MainWindow", "TextLabel"))
        self.label_monthly_total_data_ZH.setText(_translate("MainWindow", "TextLabel"))


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
        if not self.DBManager:
            return
        cur_year = self.comboBox_year_select.currentText()
        cur_month = self.comboBox_month_select.currentText()
        cur_type = self.comboBox_type_select.currentText()
        if not cur_type or not cur_year or not cur_month:
            return
        if cur_month != '查看所有月份' and cur_year != '查看所有年份':
            self.pushButton_export.setDisabled(False)
            self.pushButton_delete.setDisabled(False)
        else:
            self.pushButton_export.setDisabled(True)
            self.pushButton_delete.setDisabled(True)
        print(self.prev_cur_year, cur_year)
        print(self.prev_cur_month, cur_month)
        print(self.prev_cur_type, cur_type)
        if self.prev_cur_year != cur_year or self.prev_cur_month!=cur_month or self.prev_cur_type!=cur_type:
            self.listWidget.clearSelection()
            self.listWidget.clear()
            self.tableWidget.clearContents()
            self.prev_cur_month = cur_month
            self.prev_cur_year = cur_year
            self.prev_cur_type = cur_type
            for i in self.DBManager.refresh_customer_list(cur_year, cur_month, cur_type):
                self.listWidget.addItem(i[0])
        if not self.listWidget.selectedItems():
            return

        self.pushButton_save.setDisabled(False)
        customer_name = self.listWidget.selectedItems()[0].text()
        self.label_customer_name_data.setText(customer_name)
        self.data = self.DBManager.get_data(customer_name)
        row = 0
        self.filtered_data = self.data
        # print(self.filtered_data)
        self.filter_by_month()
        # print(self.filtered_data)
        self.filter_by_year()
        # print(self.filtered_data)
        self.filter_by_type()
        # print(self.filtered_data)
        self.filtered_data.sort(key = sort_by_date)
        self.filtered_data.sort(key = sort_by_month)
        self.filtered_data.sort(key = sort_by_year)
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
            sub_temp = []
            date = self.tableWidget.item(i,0).text()
            for element in date.split('/'):
                sub_temp.append(int(element))
            sub_temp.append(self.tableWidget.item(i,1).text())
            sub_temp.append(self.tableWidget.item(i, 2).text())
            sub_temp.append(self.listWidget.selectedItems()[0].text())
            sub_temp.append(float(self.tableWidget.item(i, 3).text()))
            sub_temp.append(float(self.tableWidget.item(i, 4).text()))
            sub_temp.append(self.tableWidget.item(i, 6).text())
            selection = self.comboBox_type_select.currentText()
            if selection == '水泥':
                selection = 0
            else:
                selection = 1
            sub_temp.append(selection)
            temp.append(sub_temp)
        cur_customer = self.listWidget.selectedItems()[0].text()
        cur_year = self.comboBox_year_select.currentText()
        cur_month = self.comboBox_month_select.currentText()
        cur_type = self.comboBox_type_select.currentText()
        if cur_type ==  '水泥':
            cur_type = 0
        else:
            cur_type = 1
        # print(self.data)
        to_remove = []
        for i in self.data:
            # print(i[5] == cur_customer)
            if i[5] == cur_customer:
                if cur_year!='查看所有年份':
                    if i[0] == cur_year:
                        if cur_month != '查看所有月份':
                            if i[1] == cur_month:
                                if i[9] == cur_type:
                                    to_remove.append(i)
                elif cur_month != '查看所有月份':
                    if i[1] == cur_month:
                        if i[9] == cur_type:
                            to_remove.append(i)
                else:
                    if i[9] == cur_type:
                        # print('-')
                        to_remove.append(i)
        for i in to_remove:
            self.data.remove(i)
        # print('after delete')
        # print(self.data)
        for i in temp:
            self.data.append(tuple(i))
        # print('after addition')
        # print(self.data)
        # if cur_year != '查看所有年份':
        #     if cur_month != '查看所有月份':
        command = f"DELETE FROM ORDERS WHERE Customer='{cur_customer}' AND Type={cur_type}"
        # elif cur_month != '查看所有月份':
        #     command = f"DELETE FROM ORDERS WHERE Customer='{cur_customer}' AND Type={cur_type} AND Year={cur_year}"
        # else:
        #     command = f"DELETE FROM ORDERS WHERE Customer='{cur_customer}' AND Type={cur_type} AND Year={cur_year} AND Month={cur_month}"
        self.DBManager.execute(command)
        self.DBManager.commit()
        for i in self.data:
            command = f'''INSERT INTO ORDERS VALUES (
            {i[0]}, 
            {i[1]},
            {i[2]},
            '{i[3]}',
            '{i[4]}',
            '{i[5]}',
            {float(i[6])},
            {float(i[7])},
            '{i[8]}',
            {i[9]})
            '''
            self.DBManager.execute(command)
        self.DBManager.commit()

    def filter_by_month(self):
        selection = self.comboBox_month_select.currentText()
        if '月' not in selection:
            return
        if selection == '查看所有月份':
            return
        month = selection.strip('月')
        # print(month)
        temp_data = []
        for i in self.filtered_data:
            if i[1] == int(month):
                temp_data.append(i)
        self.filtered_data = temp_data

    def filter_by_year(self):
        selection = self.comboBox_year_select.currentText()
        if '年' not in selection:
            return
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
        if selection == '':
            return
        if selection ==  '水泥':
            selection = 0
        else:
            selection = 1
        temp_data = []
        for i in self.filtered_data:
            if i[9] == selection:
                temp_data.append(i)
        self.filtered_data = temp_data

    def export(self):
        cur_year = int(self.comboBox_year_select.currentText().strip('年').strip(' '))
        cur_month = int(self.comboBox_month_select.currentText().strip('月').strip(' '))
        cur_type = self.comboBox_type_select.currentText()
        if cur_type ==  '水泥':
            cur_type = 0
        else:
            cur_type = 1
        command = f'SELECT * FROM ORDERS WHERE Year={cur_year} AND Month={cur_month} ' \
                  f'AND Type={cur_type} ORDER BY Customer'
        self.DBManager.execute(command)
        result = self.DBManager.fetch_all()
        dict = {}
        for i in result:
            if i[5] not in dict.keys():
                dict[i[5]] = []
                dict[i[5]].append(i)
            else:
                dict[i[5]].append(i)

        for i in dict.keys():
            export_file(dict.get(i), [cur_year, cur_month], i, cur_type)
        self.pushButton_export.setDisabled(False)

    def open_file_chooser(self):
        file_chooser_window = FileDialog()

    def delete_month(self):
        cur_year = int(self.comboBox_year_select.currentText().strip('年').strip(' '))
        cur_month = int(self.comboBox_month_select.currentText().strip('月').strip(' '))
        cur_type = self.comboBox_type_select.currentText()
        if cur_type ==  '水泥':
            cur_type = 0
        else:
            cur_type = 1
        self.DBManager.execute(f'DELETE FROM ORDERS WHERE Year={cur_year} AND Month={cur_month} AND Type={cur_type}')
        self.DBManager.commit()

    def refresh(self):
        self.comboBox_type_select.clear()
        self.comboBox_month_select.clear()
        self.comboBox_year_select.clear()
        self.listWidget.clear()
        self.tableWidget.clearContents()

        self.DBManager = DatabaseManager()
        for customer in self.DBManager.get_customer_list():
            self.listWidget.addItem(customer[0])

        self.DBManager.execute('SELECT DISTINCT Month FROM ORDERS')
        months = self.DBManager.fetch_all()
        self.comboBox_month_select.addItem('查看所有月份')
        for month in months:
            self.comboBox_month_select.addItem(str(month[0]) + '月')
        self.DBManager.execute('SELECT DISTINCT Year FROM ORDERS')
        years = self.DBManager.fetch_all()
        self.comboBox_year_select.addItem('查看所有年份')
        for year in years:
            self.comboBox_year_select.addItem(str(year[0]) + '年')
        self.comboBox_year_select.setCurrentIndex(0)
        self.comboBox_type_select.addItem('水泥')
        self.comboBox_type_select.addItem('砂石')
        self.comboBox_type_select.setCurrentIndex(0)
        self.listWidget.clearSelection()


class FileDialog(QWidget):

    def __init__(self):
        super().__init__()


        self.title = '打开文件'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.openFileNameDialog()
        self.show()


    def openFileNameDialog(self):
        options = QFileDialog.Options()


        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "打开文件", "",
                                          "逗号分隔(*.csv)", options=options)
        if fileName:
            # if main_window_ref.DBManager:
            #     main_window_ref.DBManager.close()
            #     main_window_ref.DBManager = None
            selected_file_name = fileName
            try:
                read_from_file(fileName)
            except ValueError as e:
                error_dialog = QErrorMessage()
                error_dialog.showMessage(str(e))
                error_dialog.exec_()



