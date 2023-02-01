from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from random import choice

window_titles = [
    "My app",
    "My a[[",
    "my app",
    "My sifgg",
    "This is surprising",
    "this is not so rare",
    "Something went wrong"
]


# Subclass MainWindow to customize your main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.n_times_clicked = 0

        self.setWindowTitle("My app")
        self.button = QPushButton("Press Me")
        self.button.clicked.connect(self.the_button_was_clicked)
        self.setFixedSize(QSize(400,300))

        self.windowTitleChanged.connect(self.the_window_title_changed)
        # Set the central widget as a button
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked")
        new_window_title = choice(window_titles)
        print(f"Setting window title : {new_window_title}")
        self.setWindowTitle(new_window_title)


    def the_window_title_changed(self, window_title):
        print(f"Window title changed: {window_title}")

        if window_title == "Something went wrong":
            self.button.setDisabled(True)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
