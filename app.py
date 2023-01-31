from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget

import sys


app = QApplication(sys.argv)

window = QWidget()
window.show()

app.exec()
