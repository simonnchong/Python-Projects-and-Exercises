import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        setting = menubar.addMenu('Setting')

        impMenu = QMenu('Import', self) # create a parent menu
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)

        newAct = QAction('New', self)

        brightness_setting = QMenu('Adjust Brightness', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        setting.addMenu(brightness_setting)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Submenu')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()