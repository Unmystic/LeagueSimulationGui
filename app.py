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
        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])

        #Sends current index position
        widget.currentIndexChanged.connect(self.index_changed)

        # There is alternative signal to send text
        widget.currentTextChanged.connect(self.text_changed)

        widget.setEditable(True)
        widget.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)
        widget.setMaxCount(10)

        self.setCentralWidget(widget)

    def index_changed(self, i): # i for int
        print(i)
    def text_changed(self, s): # s for str
        print(s)



app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
