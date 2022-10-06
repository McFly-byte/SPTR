from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class ChildWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.pgb = QProgressBar(self)

        self.timer = QBasicTimer()
        self.step = 0


    def initUI(self):
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowTitle('子窗口')
        self.resize(280, 230)

    def timerEvent(self, event):
        if self.step >= 100:
            self.step = 0
        self.step = self.step + 1
        self.pgb.setValue(self.step)

    def onStart(self):
        self.timer.start(10, self)

    def onStop(self):
        self.timer.stop()

class FatherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('TestWindow')
        self.resize(400, 300)

        self.btn = QPushButton('打开新窗口', self)
        self.btn.clicked.connect(self.btnClicked)

        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        self.setLayout(layout)

        self.show()

    def btnClicked(self):
        self.chile_Win = ChildWindow()
        self.chile_Win.show()
        self.chile_Win.onStart()
        self.chile_Win.exec_()

        for i in range( 1000000 ):
            print( i )

        self.chile_Win.onStop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建主窗口
    window = FatherWindow()
    # 显示窗口
    window.show()
    # 运行应用，并监听事件
    sys.exit(app.exec_())