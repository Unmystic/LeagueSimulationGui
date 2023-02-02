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
        widget = QSlider(Qt.Orientation.Horizontal)
        widget.setMinimum(2)
        widget.setMaximum(20)
        widget.setSingleStep(2)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    def value_changed(self,i):
        print(i)
    def slider_position(self,p):
        print("position", p)
    def slider_pressed(self):
        print("Pressed!")
    def slider_released(self):
        print("Released!")





app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
