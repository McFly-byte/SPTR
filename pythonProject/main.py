import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import new_sw

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = new_sw.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())


# DONE_TODO　pyqtgraph 嵌入到 pyqt里
# DONE_TODO 完成后面几个文件
# DONE_TODO 分栏
# DONE_TODO 外参传递
# TODO　把主题强度图整到软件里
# TODO browser全屏
# TODO　困惑度显示ｘｙ坐标
# DONE_TODO 多线程跑余弦相似度
# TODO 美化
# TODO 循环进度条
# TODO 封装
# TODO 写申请书