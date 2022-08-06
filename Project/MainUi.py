# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1163, 595)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 421, 81))
        self.label.setStyleSheet("background-color: rgb(219, 255, 228);\n"
"font: 18pt \"楷体\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_showimages = QtWidgets.QLabel(self.centralwidget)
        self.label_showimages.setGeometry(QtCore.QRect(20, 150, 611, 371))
        self.label_showimages.setStyleSheet("background-color: rgb(224, 255, 231);")
        self.label_showimages.setText("")
        self.label_showimages.setObjectName("label_showimages")
        self.label_showimages1 = QtWidgets.QLabel(self.centralwidget)
        self.label_showimages1.setGeometry(QtCore.QRect(700, 150, 421, 371))
        self.label_showimages1.setStyleSheet("background-color: rgb(224, 255, 231);")
        self.label_showimages1.setText("")
        self.label_showimages1.setObjectName("label_showimages1")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 120, 611, 411))
        self.groupBox.setStyleSheet("font: 18pt \"楷体\";")
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(690, 120, 431, 411))
        self.groupBox_2.setStyleSheet("font: 18pt \"楷体\";")
        self.groupBox_2.setObjectName("groupBox_2")
        self.btn_datashow = QtWidgets.QPushButton(self.centralwidget)
        self.btn_datashow.setGeometry(QtCore.QRect(1010, 40, 101, 41))
        self.btn_datashow.setStyleSheet("font: 14pt \"楷体\";\n"
"background-color: rgb(180, 255, 191);")
        self.btn_datashow.setObjectName("btn_datashow")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "数 据 动 态 可 视 化 示 例"))
        self.groupBox.setTitle(_translate("MainWindow", "线形图"))
        self.groupBox_2.setTitle(_translate("MainWindow", "柱状图"))
        self.btn_datashow.setText(_translate("MainWindow", "展 示"))

