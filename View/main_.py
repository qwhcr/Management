import sys
import View
from PyQt5.QtWidgets import QApplication, QMainWindow

main_window = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = View.main_view.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
