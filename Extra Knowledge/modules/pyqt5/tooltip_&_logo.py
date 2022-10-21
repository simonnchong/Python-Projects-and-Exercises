import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon



class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        # create button and set tooltip for it
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint()) # give a recommened size for it
        btn.move(50, 50)

        # set the window title and icon
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('dog.png'))

        # combination resive and move method
        # set the x, y position on screen, and width and height of the window
        # setGeometry(x, y, width, height)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')


        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()