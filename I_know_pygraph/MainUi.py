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
        MainWindow.resize(1106, 623)
        MainWindow.setStyleSheet("background-color: rgb(242, 255, 254);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(200, 10, 901, 571))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setEnabled(True)
        self.tab_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tab_2.setObjectName("tab_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 881, 531))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 12pt \"楷体\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_22 = QtWidgets.QWidget()
        self.tab_22.setObjectName("tab_22")
        self.label_2 = QtWidgets.QLabel(self.tab_22)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 311, 51))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 12pt \"楷体\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
#         self.label_videopath = QtWidgets.QLabel(self.tab_22)
#         self.label_videopath.setGeometry(QtCore.QRect(180, 500, 271, 21))
#         self.label_videopath.setStyleSheet("background-color: rgb(255, 255, 255);")
#         self.label_videopath.setText("")
#         self.label_videopath.setObjectName("label_videopath")
#         self.btn_openvideo = QtWidgets.QPushButton(self.tab_22)
#         self.btn_openvideo.setGeometry(QtCore.QRect(660, 500, 91, 31))
#         self.btn_openvideo.setStyleSheet("background-color: rgb(143, 255, 169);\n"
# "font: 12pt \"楷体\";")
#         self.btn_openvideo.setObjectName("btn_openvideo")
#         self.btn_bofang = QtWidgets.QPushButton(self.tab_22)
#         self.btn_bofang.setGeometry(QtCore.QRect(770, 500, 91, 31))
#         self.btn_bofang.setStyleSheet("background-color: rgb(143, 255, 169);\n"
# "font: 12pt \"楷体\";")
#         self.btn_bofang.setObjectName("btn_bofang")
#         self.label_showVideo = QtWidgets.QLabel(self.tab_22)
#         self.label_showVideo.setGeometry(QtCore.QRect(100, 70, 711, 401))
#         font = QtGui.QFont()
#         font.setFamily("楷体")
#         font.setPointSize(14)
#         font.setBold(False)
#         font.setItalic(False)
#         font.setWeight(50)
#         self.label_showVideo.setFont(font)
#         self.label_showVideo.setStyleSheet("background-color: rgb(0, 0, 0);\n"
# "font: 14pt \"楷体\";\n"
# "color: rgb(255, 255, 255);")
#         self.label_showVideo.setText("")
#         self.label_showVideo.setAlignment(QtCore.Qt.AlignCenter)
#         self.label_showVideo.setObjectName("label_showVideo")
        self.label_6 = QtWidgets.QLabel(self.tab_22)
        self.label_6.setGeometry(QtCore.QRect(70, 490, 111, 41))
        self.label_6.setStyleSheet("font: 11pt \"楷体\";")
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab_22, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(0, 10, 891, 531))
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 12pt \"楷体\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(0, 10, 891, 531))
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 12pt \"楷体\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_5 = QtWidgets.QLabel(self.tab_5)
        self.label_5.setGeometry(QtCore.QRect(10, 0, 881, 541))
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 12pt \"楷体\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(30, 40, 131, 31))
        self.btn_1.setStyleSheet("font: 14pt \"楷体\";\n"
"selection-background-color: rgb(189, 255, 191);\n"
"")

        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(30, 120, 131, 31))
        self.btn_2.setStyleSheet("font: 14pt \"楷体\";\n"
"selection-background-color: rgb(189, 255, 191);\n"
"")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(30, 200, 131, 31))
        self.btn_3.setStyleSheet("font: 14pt \"楷体\";\n"
"selection-background-color: rgb(189, 255, 191);\n"
"")
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(30, 280, 131, 31))
        self.btn_4.setStyleSheet("font: 14pt \"楷体\";\n"
"selection-background-color: rgb(189, 255, 191);\n"
"")
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(30, 370, 131, 31))
        self.btn_5.setStyleSheet("font: 14pt \"楷体\";\n"
"selection-background-color: rgb(189, 255, 191);\n"
"")
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.label_2.setText(_translate("MainWindow", "我 是 界 面 二（整合功能示例）"))
        # self.btn_openvideo.setText(_translate("MainWindow", "选择视频"))
        # self.btn_bofang.setText(_translate("MainWindow", "播 放"))
        self.label_6.setText(_translate("MainWindow", "视频文件地址："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_22), _translate("MainWindow", "Tab 1"))
        self.label_3.setText(_translate("MainWindow", "我 是 界 面 三"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "页"))
        self.label_4.setText(_translate("MainWindow", "我 是 界 面 四"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "页"))
        self.label_5.setText(_translate("MainWindow", "我 是 界 面 五"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "页"))
        self.btn_1.setText(_translate("MainWindow", "界面1"))
        self.btn_2.setText(_translate("MainWindow", "界面2"))
        self.btn_3.setText(_translate("MainWindow", "界面3"))
        self.btn_4.setText(_translate("MainWindow", "界面4"))
        self.btn_5.setText(_translate("MainWindow", "界面5"))

# File: I_know_pygraph/cv2
# user: mcfly
# IDE: PyCharm
# Create Time: 2022/8/11 17:52