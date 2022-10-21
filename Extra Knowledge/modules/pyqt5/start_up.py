import sys
from PyQt5.QtWidgets import QApplication, QWidget


def main():

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(500, 500)
    w.move(500, 500)
    w.setWindowTitle('Testing Program')
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

# reference:
# https://zetcode.com/gui/pyqt5/firstprograms/