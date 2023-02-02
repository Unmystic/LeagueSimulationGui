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
        widget = QLineEdit()
        widget.setMaxLength(2)
        widget.setPlaceholderText("Enter number of teams")
        # widget.setReadOnly(True)
        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)
        widget.setInputMask("00")

        self.setCentralWidget(widget)

    def return_pressed(self):
        print("Return Pressed!")
        self.centralWidget().setText("Boom!")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self,s):
        print("Text edited...")
        print(s)





app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
