from PyQt5.QtWidgets import (QWidget, QSlider,
                             QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 200, 30)
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('mute.png'))
        self.label.setGeometry(250, 40, 80, 30)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QSlider')
        self.show()

    def changeValue(self, value):

        if value == 0:
            # the icon doesnt work here
            self.label.setPixmap(QPixmap('mute.jpg'))
        elif 0 < value <= 30:

            self.label.setPixmap(QPixmap('min.jpg'))
        elif 30 < value < 80:

            self.label.setPixmap(QPixmap('med.jpg'))
        else:

            self.label.setPixmap(QPixmap('max.jpg'))


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()