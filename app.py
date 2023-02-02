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
        self.setFixedSize(QSize(400, 300))
        widget = QLabel("Hellow")
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        widget.setPixmap(QPixmap('Lab.jpg'))

        self.setCentralWidget(widget)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
