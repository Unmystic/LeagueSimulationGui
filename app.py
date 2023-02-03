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
        self.w1 = AnotherWindow()
        self.w2 = AnotherWindow()

        l = QVBoxLayout()
        self.setWindowTitle("My App")
        self.setMinimumSize(QSize(640, 480))

        button1 = QPushButton("Push for Window1")
        button1.clicked.connect(
            lambda checked: self.toggle_window(self.w1)
        )
        l.addWidget(button1)

        button2 = QPushButton("Push for Window1")
        button2.clicked.connect(
            lambda checked: self.toggle_window(self.w2)
        )
        l.addWidget(button2)

        w = QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()