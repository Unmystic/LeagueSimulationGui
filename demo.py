from PyQt6 import QtCore, QtGui, QtWidgets
from power_bar import PowerBar


app = QtWidgets.QApplication([])
volume = PowerBar()
volume.show()
app.exec()