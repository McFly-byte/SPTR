import sys

import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg


class Ui_MainWindow(QMainWindow):
    y = [1,2]
    x  = 5
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.perplexity_button = QtWidgets.QPushButton(self.centralwidget)
        self.perplexity_button.setText('点击消息弹出消息框')
        self.perplexity_button.clicked.connect(self.show_perplexity)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "主题模型可视化"))
        self.perplexity_button.setText(_translate("MainWindow", "LDA主题模型训练"))

    def show_perplexity(self):
        print("self.y")
        print(self.y)
        if (self.y == []):
            QMessageBox.about(None, '提示', '文件保存路径不存在，是否创建？')  # 默认关闭界面选择No
        else:
            win = pg.GraphicsLayoutWidget(show=True)
            win.setWindowTitle('pyqtgraph example: crosshair')
            label = pg.LabelItem(justify='right')
            win.addItem(label)
            p1 = win.addPlot(row=1, col=0)
            # customize the averaged curve that can be activated from the context menu:
            p1.avgPen = pg.mkPen('#FFFFFF')
            p1.avgShadowPen = pg.mkPen('#8080DD', width=10)

            # p2 = win.addPlot(row=2, col=0)

            region = pg.LinearRegionItem()
            region.setZValue(10)
            # Add the LinearRegionItem to the ViewBox, but tell the ViewBox to exclude this
            # item when doing auto-range calculations.
            # p2.addItem(region, ignoreBounds=True)

            # pg.dbg()
            p1.setAutoVisible(y=True)

            # create numpy arrays
            # make the numbers large to show that the range shows data from 10000 to all the way 0
            # data1 = 10000 + 15000 * pg.gaussianFilter(np.random.random(size=10000), 10) + 3000 * np.random.random(size=10000)
            # data2 = 15000 + 15000 * pg.gaussianFilter(np.random.random(size=10000), 10) + 3000 * np.random.random(size=10000)

            data1 = np.random.normal(size=20)
            # data2 = np.random.normal(size=20) + 10

            p1.plot(data1, pen="r")

            # p1.plot(data2, pen="g")

            # p2d = p2.plot(data1, pen="w")
            # bound the LinearRegionItem to the plotted data
            # region.setClipItem(p2d)

            def update():
                region.setZValue(10)
                minX, maxX = region.getRegion()
                p1.setXRange(minX, maxX, padding=0)

            region.sigRegionChanged.connect(update)

            def updateRegion(window, viewRange):
                rgn = viewRange[0]
                region.setRegion(rgn)

            p1.sigRangeChanged.connect(updateRegion)

            # region.setRegion([1000, 2000])

            # cross hair
            vLine = pg.InfiniteLine(angle=90, movable=False)
            hLine = pg.InfiniteLine(angle=0, movable=False)
            p1.addItem(vLine, ignoreBounds=True)
            p1.addItem(hLine, ignoreBounds=True)

            vb = p1.vb

            def mouseMoved(evt):
                pos = evt[0]  ## using signal proxy turns original arguments into a tuple
                if p1.sceneBoundingRect().contains(pos):
                    mousePoint = vb.mapSceneToView(pos)
                    index = int(mousePoint.x())
                    if index > 0 and index < len(data1):
                        label.setText(
                            "<span style='font-size: 12pt'>x=%0.1f,   <span style='color: red'>y=%0.1f</span>" % (
                            mousePoint.x(), data1[index]))
                    vLine.setPos(mousePoint.x())
                    hLine.setPos(mousePoint.y())

            proxy = pg.SignalProxy(p1.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)
            # p1.scene().sigMouseMoved.connect(mouseMoved)
            pg.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
