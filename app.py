import random
import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QPushButton, QWidget, QVBoxLayout, QLabel


class AnotherWindow(QWidget):
    """
    This window is a Qwidget. if it has no parent,
    it appear as floating window.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setMinimumSize(QSize(320, 240))
        self.label = QLabel(f"Another window {random.randint(0,100)}")
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None
        self.setWindowTitle("My App")
        self.setMinimumSize(QSize(640, 480))
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
            self.w.show()
        else:
            self.w.close()
            self.w = None


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()