import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from openpyxl.descriptors import slots

import software
import data_process

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = software.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
