import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QLineEdit, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        edit_field = QLineEdit(self)

        edit_field.move(60, 100)
        self.label.move(60, 40)

        edit_field.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 350, 250)
        
        self.show()

    def onChanged(self, text):
        self.label.setText(text)
        self.label.adjustSize()
        self.setWindowTitle(text)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()