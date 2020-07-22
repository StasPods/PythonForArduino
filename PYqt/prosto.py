import sys
#from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtWidgets

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    w = QtWidgets()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())
