import sys
import random
import statistics
import csv


from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QDialog, QMessageBox, QTableWidgetItem, QWidget

from tournament import Ui_Form
from schedule import Schedule
from match_engine import Match


class League(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.teams = {}
        self.table = []
        self.calendar = []
        self.tour = 0
        Schedule()
        self.create_table()
        self.draw_table()
        self.fill_calendar()

        self.update_label()
        # Connect buttons to corresponding functions
        self.btn_league.clicked.connect(self.simulate_games)

    def update_label(self):
        self.label_tour.setText(f"{self.tour} of {(len(self.teams) - 1) * 2}")
        self.label_tour.setStyleSheet("QLabel{""font-size:14pt; font-weight:700; text-decoration: underline;""}")


    def create_table(self):
        with open("Scripts/data/teams.csv", "r") as file:
            reader = csv.DictReader(file, fieldnames=["name", "rating"])
            for row in reader:
                self.teams[row["name"]] = row["rating"]

        for team in self.teams:
            self.table.append(
                {'name': team, 'rating': self.teams[team], 'gamesPlayed': 0, 'goalsScored': 0, 'goalsConceded': 0,
                 'goalDifference': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'points': 0})

    def draw_table(self):

        self.League_table.setRowCount(len(self.teams))

        for i,team in enumerate(self.table):
            self.League_table.setItem(i, 0, QTableWidgetItem(f"{team['name']}"))
            self.League_table.setItem(i, 1, QTableWidgetItem(f"{team['rating']}"))
            self.League_table.setItem(i, 2, QTableWidgetItem(f"{team['gamesPlayed']}"))
            self.League_table.setItem(i, 3, QTableWidgetItem(f"{team['goalsScored']}"))
            self.League_table.setItem(i, 4, QTableWidgetItem(f"{team['goalsConceded']}"))
            self.League_table.setItem(i, 5, QTableWidgetItem(f"{team['goalDifference']}"))
            self.League_table.setItem(i, 6, QTableWidgetItem(f"{team['wins']}"))
            self.League_table.setItem(i, 7, QTableWidgetItem(f"{team['draws']}"))
            self.League_table.setItem(i, 8, QTableWidgetItem(f"{team['losses']}"))
            self.League_table.setItem(i, 9, QTableWidgetItem(f"{team['points']}"))
        self.League_table.resizeColumnsToContents()


    def fill_calendar(self):
        # Populate calendar with games
        with open("Scripts/data/schedule.csv", "r") as file:
            reader = csv.DictReader(file, fieldnames=["tour", "homeTeam", "awayTeam"])
            for row in reader:
                home = {}
                home["tour"] = row["tour"]
                home["name"] = row["homeTeam"]
                home["rating"] = self.teams[row["homeTeam"]]

                away = {}
                away["tour"] = row["tour"]
                away["name"] = row["awayTeam"]
                away["rating"] = self.teams[row["awayTeam"]]

                self.calendar.append([{"home": home, "away": away}])

    def simulate_games(self):

        for game in self.calendar:
            # print(game[0]['home'],game[0]['away'] )
            match = Match(game[0]['home'], game[0]['away'], self.table)
            result, self.table = match.match_data()

        self.table.sort(reverse=True, key=self.Myfunc)
        self.draw_table()

    def Myfunc(self, e):
        """sort list with dictionary by one of values"""
        return e['points']


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    league = League()
    sys.exit(app.exec())