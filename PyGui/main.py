from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtWidgets, QtGui
import sys


def window():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setGeometry(200, 200, 400, 300)
    window.setMinimumSize(400, 300)
    window.setMaximumSize(800, 600)
    window.setWindowTitle("myProgram")
    window.setWindowIcon(QtGui.QIcon(
        ".//twitter-logo-vector-png-clipart-1.png"))
    window.show()
    sys.exit(app.exec())


window()
