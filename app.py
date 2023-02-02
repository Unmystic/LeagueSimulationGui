import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider
)
from PyQt6.QtCore import Qt, QSize


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        #self.setFixedSize(QSize(400, 300))
        widget = QSpinBox()
        # Or widget = QDoubleSpinBox()
        widget.setMinimum(2)
        widget.setMaximum(20)
        # Or widget.setRange(2,20)

        widget.setPrefix("Set ")
        widget.setSuffix(" teams")
        widget.setSingleStep(2)
        widget.lineEdit().setReadOnly(True)

        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.value_change_str)

        self.setCentralWidget(widget)

    def value_changed(self,i):
        print(i)

    def value_change_str(self,s):
        print(s)



app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
