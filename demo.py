from PyQt6 import QtCore, QtGui, QtWidgets
from power_bar import PowerBar


app = QtWidgets.QApplication([])
volume = PowerBar(["#49006a", "#7a0177", "#ae017e", "#dd3497", "#f768a1", "#fa9fb5", "#fcc5c0", "#fde0dd", "#fff7f3"])
volume.setBarPadding(2)
volume.setBarSolidPercent(0.9)
volume.setBackgroundColor('gray')
volume.show()
app.exec()