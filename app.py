from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


# Subclass MainWindow to customize your main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_is_checked = True

        self.setWindowTitle("My app")
        button = QPushButton("Press Me")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)
        button.setChecked(self.button_is_checked)
        self.setFixedSize(QSize(400,300))

        # Set the central widget as a button
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print("Checked?", self.button_is_checked)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
