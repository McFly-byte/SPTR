# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1106, 623)
        MainWindow.setStyleSheet("background-color: rgb(242, 255, 254);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(200, 10, 901, 571))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setEnabled(True)
        self.tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tab.setObjectName("tab")
        self.pw1 = pg.PlotWidget()
        self.pw2 = pg.PlotWidget()
        self.tab.add
        # self.label = QtWidgets.QLabel(self.tab)
        # self.label.setGeometry(QtCore.QRect(10, 10, 881, 531))
        # self.label.setAlignment(QtCore.Qt.AlignCenter)
        # self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 311, 51))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(0, 10, 891, 531))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(0, 10, 891, 531))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_5 = QtWidgets.QLabel(self.tab_5)
        self.label_5.setGeometry(QtCore.QRect(10, 0, 881, 541))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab_5, "")

        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(30, 40, 131, 31))
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(30, 120, 131, 31))
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(30, 200, 131, 31))
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(30, 280, 131, 31))
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(30, 370, 131, 31))
        self.btn_5.setObjectName("btn_5")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.label.setText(_translate("MainWindow", "我 是 界 面 一"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 2"))
        self.label_2.setText(_translate("MainWindow", "我 是 界 面 二（整合功能示例）"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "2"))
        self.label_3.setText(_translate("MainWindow", "我 是 界 面 三"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "3"))
        self.label_4.setText(_translate("MainWindow", "我 是 界 面 四"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "4"))
        self.label_5.setText(_translate("MainWindow", "我 是 界 面 五"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "5"))

        self.btn_1.setText(_translate("MainWindow", "界面1"))
        self.btn_2.setText(_translate("MainWindow", "界面2"))
        self.btn_3.setText(_translate("MainWindow", "界面3"))
        self.btn_4.setText(_translate("MainWindow", "界面4"))
        self.btn_5.setText(_translate("MainWindow", "界面5"))

