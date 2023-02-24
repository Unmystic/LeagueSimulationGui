import sys
import csv
import os.path

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QDialog, QMessageBox, QTableWidgetItem
from Scripts.mainw import Ui_MainWindow
from Scripts.create_league import NewLeague
from Scripts.about import AboutDialog
from Scripts.tutorial import Tutorial
from Scripts.hall_of_fame import HallOfFame
from Scripts.check_HoF import create_hof


class LeagueSimulator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        if os.path.exists("Scripts/data/hof.csv") is False:
            create_hof()

        # Connecting menu and buttons to appropriate functions
        self.btn_new.clicked.connect(self.new_league)
        self.actionNew_League.triggered.connect(self.new_league)

        self.btn_hof.clicked.connect(self.show_hof)
        self.actionShow_Hall_of_Fame.triggered.connect(self.show_hof)

        self.btn_exit.clicked.connect(self.exit_button)
        self.actionExit.triggered.connect(self.exit_button)

        self.btn_about.clicked.connect(self.about_app)
        self.actionAbout.triggered.connect(self.about_app)

        self.actionTutorial.triggered.connect(self.tutorial)

    def new_league(self):
        dialog = NewLeague()
        dialog.exec()

    def about_app(self):
        dialog = QtWidgets.QDialog()
        ui = AboutDialog()
        ui.setupUi(dialog)
        dialog.exec()

    def tutorial(self):
        dialog = QtWidgets.QDialog()
        ui = Tutorial()
        ui.setupUi(dialog)
        dialog.exec()

    def show_hof(self):
        dialog = HallOfFame()
        dialog.exec()

    def exit_button(self):
        sys.exit()

