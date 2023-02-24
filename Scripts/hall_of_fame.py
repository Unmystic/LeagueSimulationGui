import csv
import sys

from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QMainWindow, QDialog, QMessageBox, QTableWidgetItem

from Scripts.hof import Ui_HoF


class HallOfFame(QDialog, Ui_HoF):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.HallofFame.setFont(QtGui.QFont('Segoe UI', 11))

        self.top = []
        self.check_top()
        self.show_the_best()

    def check_top(self):

        with open("Scripts/data/hof.csv", "r", newline='') as file:
            fieldnames = ['name', 'rating', 'gamesPlayed',
                          'goalDifference', 'wins', 'draws', 'points']
            reader = csv.DictReader(file, fieldnames=fieldnames)
            next(reader)
            for row in reader:
                team = {'name': row['name'], 'rating': row['rating'], 'gamesPlayed': row['gamesPlayed'],
                        'goalDifference': row['goalDifference'], 'wins': row['wins'], 'draws': row['draws'],
                        'points': row['points']}

                self.top.append(team)

    def show_the_best(self):

        for i, team in enumerate(self.top):
            self.HallofFame.setItem(i, 0, QTableWidgetItem(f"{team['name']}"))
            self.HallofFame.setItem(i, 1, QTableWidgetItem(f"{team['rating']}"))
            self.HallofFame.setItem(i, 2, QTableWidgetItem(f"{team['gamesPlayed']}"))
            self.HallofFame.setItem(i, 5, QTableWidgetItem(f"{team['goalDifference']}"))
            self.HallofFame.setItem(i, 3, QTableWidgetItem(f"{team['wins']}"))
            self.HallofFame.setItem(i, 4, QTableWidgetItem(f"{team['draws']}"))
            self.HallofFame.setItem(i, 6, QTableWidgetItem(f"{team['points']}"))
        self.HallofFame.resizeColumnsToContents()




if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    dialog = HallOfFame()
    sys.exit(app.exec())