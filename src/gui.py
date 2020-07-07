import sys
from PySide2 import QtCore, QtWidgets, QtGui
import time
import lifegame
import numpy as np


class LifeThread(QtCore.QThread):
    signal = QtCore.Signal(list)

    def __init__(self, parent=None):
        super(LifeThread, self).__init__(parent)
        self.life = lifegame.Lifegame((parent.px, parent.py))
        self.isRunning = False
        self.mutex = QtCore.QMutex()

    def __del__(self):
        self.stop()
        self.wait()

    def stop(self):
        with QtCore.QMutexLocker(self.mutex):
            self.isRunning = False

    def run(self):
        self.isRunning = True
        while (self.isRunning):
            self.signal.emit(self.life.do().repeat(
                4, axis=0).repeat(4, axis=1))


class UISmaple(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(UISmaple, self).__init__(parent)
        self.width, self.height = 320, 320
        self.px, self.py = int(self.width / 4), int(self.height / 4)
        self.state = np.zeros((self.width, self.height)).astype(np.uint8)
        img = QtGui.QImage(self.state * 255, self.width, self.height,
                           QtGui.QImage.Format_Grayscale8)
        self.viewer = QtWidgets.QLabel()
        self.viewer.setPixmap(QtGui.QPixmap.fromImage(img))

        self.button1 = QtWidgets.QPushButton('Run')
        self.button2 = QtWidgets.QPushButton('Stop')
        self.button1.clicked.connect(self.run)
        self.button2.clicked.connect(self.stop)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.viewer)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        self.setLayout(layout)

        self.life = LifeThread(self)
        self.life.signal.connect(self.setState)

    def run(self):
        if not self.life.isRunning:
            self.life.start()

    def stop(self):
        self.life.stop()

    def setState(self, state):
        img = QtGui.QImage(state, self.width,
                           self.height, self.width, QtGui.QImage.Format_Grayscale8)
        self.viewer.setPixmap(QtGui.QPixmap.fromImage(img))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    a = UISmaple()
    a.show()
    sys.exit(app.exec_())
