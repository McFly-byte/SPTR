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


# DONE-TODO　pyqtgraph 嵌入到 pyqt里
# TODO 完成后面几个文件
# TODO　把主题强度图整到软件里
# TODO 美化
# TODO 写申请书