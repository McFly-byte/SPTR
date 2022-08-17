# File: I_know_pygraph/software
# user: mcfly
# IDE: PyCharm
# Create Time: 2022/8/10 11:50
"""
This example demonstrates a very basic use of flowcharts: filter data,
displaying both the input and output of the filter. The behavior of
the filter can be reprogrammed by the user.

Basic steps are:
  - create a flowchart and two plots
  - input noisy data to the flowchart
  - flowchart connects data to the first plot, where it is displayed
  - add a gaussian filter to lowpass the data, then display it in the second plot.
"""

import numpy as np

import pyqtgraph as pg
import pyqtgraph.metaarray as metaarray
from pyqtgraph.flowchart import Flowchart
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph.Qt import QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QWidget, QSizePolicy


# #### 主界面
class Ui_MainWindow(QMainWindow):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # self.lda_button = QtWidgets.QPushButton(self.centralwidget)
        # # self.lda_button.setGeometry(QtCore.QRect(140, 120, 171, 41))
        # self.lda_button.setObjectName("lda_button")
        # # self.lda_button.setSizeIncrement(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # 图层嵌入到软件中
        # self.win = QtWidgets.QMainWindow() # win对应MainWindow
        # self.win.setWindowTitle('pyqtgraph example: Flowchart')
        # self.cw = QtWidgets.QWidget()  # cw 对应centralwidget
        # self.win.setCentralWidget(self.cw)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        # self.gridLayoutWidget.setGeometry(QtCore.QRect(170, 80, 551, 391))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setObjectName("layout")

        # self.layout.setRowStretch(0,1) # 设置行比例系数
        # self.layout.setRowStretch(1, 4)
        # self.layout.setColumnStretch(0, 1)  # 设置行比例系数
        # self.layout.setColumnStretch(1, 4)
        # self.cw.setLayout(self.layout)
        # self.centralwidget.setLayout(self.layout)


        # self.layout.addWidget(self.lda_button,0,0,1,1)  # 控件 行 列 占用行数 占用列数
        # self.lda_button.clicked.connect(self.Slot)

        # names = ['%', 'CE', 'C', '←',
        #          '1/x', 'x²', '√x', '÷',
        #          '7', '8', '9', '×',
        #          '4', '5', '6', '-',
        #          '1', '2', '3', '+',
        #          '±', '0', '.', '=']
        #
        # # 上面四排的位置列表
        # poss = [(row, col) for row in range(6) for col in range(4)]
        # # print( pos)
        #
        # for pos, name in zip(poss, names):
        #     print(pos, name)
        #     btn = QtWidgets.QPushButton(name, MainWindow)
        #     btn.setMinimumSize(60, 40)
        #     self.layout.addWidget(btn, *pos)

        pw1 = pg.PlotWidget()
        pw2 = pg.PlotWidget()
        self.layout.addWidget(pw1,0,1)
        self.layout.addWidget(pw2,0,2)

        MainWindow.setCentralWidget( self.centralwidget )

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def Slot(self):
        print("yes")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "主题模型可视化"))
        # self.lda_button.setText(_translate("MainWindow", "LDA主题模型训练"))


