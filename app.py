from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel,QLineEdit,QVBoxLayout,QWidget
import sys


# Subclass MainWindow to customize your main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My app")
        self.setFixedSize(QSize(400,300))

        self.label = QLabel("Click this window")
        self.setCentralWidget(self.label)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, e) -> None:
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e) -> None:
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText('Left Mouse button pressed')
        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText('Right Mouse button  pressed')
        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText('MIDDLE Mouse button pressed')

    def mouseReleaseEvent(self, e) -> None:
        self.label.setText('Mouse released')

    def mouseDoubleClickEvent(self, e) -> None:
        self.label.setText("Mouse Doubleclicked")


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
