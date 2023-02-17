import sys

from PyQt6.QtWidgets import QMainWindow, QDialog, QMessageBox, QTableWidgetItem
from mainw import Ui_MainWindow
from newLeague import NewLeague_Dialog


class LeagueSimulator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # Connecting menu and buttons to appropriate functions
        self.btn_new.clicked.connect(self.new_league)
        self.actionNew_League.triggered.connect(self.new_league)

        self.btn_exit.clicked.connect(self.exit_button)
        self.actionExit.triggered.connect(self.exit_button)

    def new_league(self):
        dialog = QDialog()
        ui = NewLeague_Dialog()

        ui.setupUi(dialog)
        ui.spinBox.lineEdit().setReadOnly(True)
        dialog.exec()

    def exit_button(self):
        sys.exit()

