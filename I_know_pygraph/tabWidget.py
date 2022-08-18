# File: I_know_pygraph/tabWidget
# user: mcfly
# IDE: PyCharm
# Create Time: 2022/8/11 18:13
# -*- coding: utf-8 -*-
"""
    基于PyQt5实现同一窗口下多界面切换
"""
# -------------------------------------- 引入依赖模块 --------------------------------------------------------------------

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5 import QtGui, QtCore
import MainUi


class MainCode(QMainWindow, MainUi.Ui_MainWindow):  # MainUi为qt designer生成的主界面设计文件的.py文件
    def __init__(self):
        QMainWindow.__init__(self)
        MainUi.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.status = self.statusBar()
        self.setWindowTitle('可视化')
        self.tabWidget.tabBar().hide()
        self.tabWidget.setCurrentIndex(0)

        # -------------------------------------   按钮触发函数 -----------------------------------------------------------
        self.btn_1.clicked.connect(self.menu_open1_clicked)  # 连接f1函数
        self.btn_2.clicked.connect(self.menu_open2_clicked)
        self.btn_3.clicked.connect(self.menu_open3_clicked)
        self.btn_4.clicked.connect(self.menu_open4_clicked)
        self.btn_5.clicked.connect(self.menu_open5_clicked)

    def menu_open1_clicked(self):
        print(1)
        self.tabWidget.setCurrentIndex(0)

    def menu_open2_clicked(self):
        print(2)

        self.tabWidget.setCurrentIndex(1)

    def menu_open3_clicked(self):
        print(3)
        self.tabWidget.setCurrentIndex(2)

    def menu_open4_clicked(self):
        print(4)
        self.tabWidget.setCurrentIndex(3)

    def menu_open5_clicked(self):
        print(5)
        self.tabWidget.setCurrentIndex(4)



# ----------------------------------------    程序入口  -----------------------------------------------------------------
if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # Qt从5.6.0开始，支持High-DPI
    app = QApplication(sys.argv)
    md = MainCode()
    md.show()
    sys.exit(app.exec_())

