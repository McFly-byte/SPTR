# # *-*encoding:utf-8
# import sys
# import untitled
# import addition
# from PyQt5 import QtWidgets, QtGui
# from PyQt5.QtWidgets import QFileDialog
#
#
# class Mywindow(QtWidgets.QMainWindow,untitled.Ui_MainWindow):
#     def __init__(self,parent = None):
#         # super(Mywindow, self).__init__()
#         QtWidgets.QMainWindow.__init__(self,parent)
#         self.setupUi(self)
#
#     def p1_ck(self):
#         self.name = self.line1.text()
#         self.age = self.line2.text()
#         self.age = int(self.age)
#         c = addition.get_info(self.name,self.age)
#         self.text.append(c)
#
#         # self.location = QFileDialog.getOpenFileName(self,'Open tif:','./',"Tif Files (*.tif);;All Files (*)")
#         # #彩蛋：获取文件夹路径
#
# if __name__ == '__main__':
#     # MAIN
#     app = QtWidgets.QApplication(sys.argv)
#     window = Mywindow()
#     window.resize(700, 600)
#     window.show()
#     sys.exit(app.exec_())

# -*- coding: utf-8 -*-
"""
    基于PyQt5实现数据动态可视化示例
"""
# -------------------------------------- 引入依赖模块 --------------------------------------------------------------------

import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore
import MainUi

global data_jishu
data_jishu = 0


class MainCode(QMainWindow, MainUi.Ui_MainWindow):  # MainUi为qt designer生成的主界面设计文件的.py文件
    def __init__(self):
        QMainWindow.__init__(self)
        MainUi.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.status = self.statusBar()
        self.setWindowTitle('基于PyQt5实现数据动态可视化示例')
        self.setWindowIcon(QIcon('../images/tubiao.png'))  # 设置窗体标题图标
        self.timer_data = QTimer()  # 定义定时器
        self.btn_datashow.clicked.connect(self.btn_datashow_clicked)  # 导出数据按钮函数

    def btn_datashow_clicked(self):
        self.timer_data.start(1000)
        self.timer_data.timeout.connect(self.datashow)

    # 数据可视化示例
    def datashow(self):
        global data_jishu
        data_jishu += 1
        print(data_jishu)
        try:
            if data_jishu is 21:
                data_jishu = 0
                QApplication.processEvents()  # 刷新
            else:
                self.label_showimages.setPixmap(QPixmap('../dataview/sample/datashow/' + str(data_jishu) + '.png'))
                self.label_showimages1.setPixmap(QPixmap('../dataview/sample/datashow/test.png'))
                self.label_showimages1.setScaledContents(True)  # 图片自适应大小

                self.label_showimages.setScaledContents(True)  # 图片自适应大小
                QApplication.processEvents()  # 刷新
        except Exception as e:
            pass

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # Qt从5.6.0开始，支持High-DPI
    app = QApplication(sys.argv)
    md = MainCode()
    md.show()
    sys.exit(app.exec_())

