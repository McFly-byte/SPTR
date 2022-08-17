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
import cv2


global openFilepath, video_path
openFilepath = ''
video_path = ''
'''
主界面
'''


class MainCode(QMainWindow, MainUi.Ui_MainWindow):  # MainUi为qt designer生成的主界面设计文件的.py文件
    def __init__(self):
        QMainWindow.__init__(self)
        MainUi.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.status = self.statusBar()
        self.setWindowTitle('基于PyQt5实现同一窗口下多界面切换示例')
        # self.setWindowIcon(QIcon('../images/icon1.png'))  # 设置窗体标题图标
        self.tabWidget.tabBar().hide()
        self.tabWidget.setCurrentIndex(0)
        # self.timer_camera = QtCore.QTimer()                     # 定义定时器，用于控制显示视频的帧率
        # self.btn_openvideo.clicked.connect(self.openVideofile)  # 打开本地视频按钮函数
        # self.btn_bofang.clicked.connect(self.begin)             # 开始播放按钮函数

        # -------------------------------------   按钮触发函数 -----------------------------------------------------------
        self.btn_1.clicked.connect(self.menu_open1_clicked)  # 连接f1函数
        self.btn_2.clicked.connect(self.menu_open2_clicked)  # 连接f1函数
        self.btn_3.clicked.connect(self.menu_open3_clicked)  # 连接f1函数
        self.btn_4.clicked.connect(self.menu_open4_clicked)  # 连接f1函数
        self.btn_5.clicked.connect(self.menu_open5_clicked)  # 连接f1函数

    def menu_open1_clicked(self):
        print(111111)
        self.tabWidget.setCurrentIndex(0)

    def menu_open2_clicked(self):
        print(111111)

        self.tabWidget.setCurrentIndex(1)

    def menu_open3_clicked(self):
        print(111111)
        self.tabWidget.setCurrentIndex(2)

    def menu_open4_clicked(self):
        print(111111)
        self.tabWidget.setCurrentIndex(3)

    def menu_open5_clicked(self):
        print(111111)
        self.tabWidget.setCurrentIndex(4)

    # def openVideofile(self):
    #     global openFilepath, video_path
    #     openFilepath = QFileDialog.getOpenFileName(self, '请选择文件', '')
    #     print("选取的视频文件地址为：", openFilepath[0])
    #     video_path = openFilepath[0]
    #     self.cap = cv2.VideoCapture(video_path)  # 读视频流
    #     print(self.cap)
    #     self.label_videopath.setText(str(video_path))
    #     if openFilepath[0] is "":
    #         md.alert('未读取本地视频文件！')
    #     else:
    #         video_path = ""
    #         md.alert('已读取本地视频文件！')
    #
    # def begin(self):
    #     self.timer_camera.start(30)                        # 定时器开始计时30ms，结果是每过30ms从摄像头中取一帧显示
    #     self.timer_camera.timeout.connect(self.showVideo)  # 打开摆臂设置界面即调用show_camera()

    # def showVideo(self):
    #     global video_path, openFilepath, flag
    #     print(video_path)
    #     if openFilepath is not "":
    #         try:
    #             flag, self.image = self.cap.read()                                  # 从视频流中读取,BGR格式
    #             global show, showImage
    #             show = cv2.resize(self.image, (800, 400))                           # 把读到的帧的大小重新设置为831, 411
    #             show2 = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)                       # 视频色彩转换回RGB，这样才是现实的颜色
    #             showImage = QtGui.QImage(show2.data, show2.shape[1], show2.shape[0],
    #                                      QtGui.QImage.Format_RGB888)                # 把读取到的视频数据变成QImage形式
    #             self.label_showVideo.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage
    #         except Exception as e:
    #             if openFilepath is "":
    #                 self.timer_camera.disconnect()
    #                 md.alert('连接视频路径不能为空！')
    #             else:
    #                 pass
    #         finally:
    #             print('flag:', flag)
    #             if flag is False:
    #                 print('放完一次了！')
    #                 self.label_showVideo.clear()
    #                 self.cap = cv2.VideoCapture(openFilepath[0])  # 读视频流
    #             QApplication.processEvents()
    #     else:
    #         pass  # 预留
    #
    # def alert(self, message_alert):
    #     self.box = QMessageBox(QMessageBox.Warning, "提示框", message_alert)
    #     qyes = self.box.addButton(self.tr("确定"), QMessageBox.YesRole)
    #     self.box.exec_()


# ----------------------------------------    程序入口  -----------------------------------------------------------------
if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # Qt从5.6.0开始，支持High-DPI
    app = QApplication(sys.argv)
    md = MainCode()
    md.show()
    sys.exit(app.exec_())

