import sys
from PySide2 import QtCore, QtWidgets, QtGui
import time


class UISmaple(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(UISmaple, self).__init__(parent)

        self.img1 = QtGui.QImage('../assets/test.png')
        self.img2 = QtGui.QImage('../assets/test.jpg')
        self.img = self.img1
        self.button1 = QtWidgets.QPushButton('TEST')
        self.button2 = QtWidgets.QPushButton('TEST2')
        self.viewer = QtWidgets.QLabel()
        self.viewer.setPixmap(QtGui.QPixmap.fromImage(self.img))
        self.viewer.resize(320, 240)
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.viewer)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    a = UISmaple()
    a.show()
    sys.exit(app.exec_())
