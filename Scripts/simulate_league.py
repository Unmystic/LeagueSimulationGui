import sys
import random
import statistics
import csv


from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QMainWindow, QDialog, QMessageBox, QTableWidgetItem, QWidget

from Scripts.tournament import Ui_Form
from Scripts.schedule import Schedule
from Scripts.match_engine import Match
from Scripts import check_HoF


class League(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # Setting the icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/images/ball.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle("Simulate tournament")

        self.teams = {}
        self.table = []
        self.calendar = []
        self.tour = 0
        Schedule()
        self.create_table()
        self.League_table.setFont(QtGui.QFont('Segoe UI', 11))
        self.draw_table()
        self.fill_calendar()

        self.Match_results.setFontPointSize(12)

        self.update_label()
        # Connect buttons to corresponding functions
        self.btn_league.clicked.connect(self.simulate_games)
        self.btn_tour.clicked.connect(self.simulate_tour)

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
        # Simulating whole tournament using Match (from match_engine.py)
        count_games = 0
        self.tour += 1
        self.publish_tourdata()
        self.btn_tour.setEnabled(False)
        for game in self.calendar:
            # print(game[0]['home'],game[0]['away'] )
            count_games += 1
            match = Match(game[0]['home'], game[0]['away'], self.table)
            result, self.table = match.match_data()
            self.Match_results.append(result)

            if count_games == (len(self.teams) // 2):
                if self.tour == (len(self.teams) - 1) * 2 :
                    pass
                else:
                    self.tour += 1
                    self.publish_tourdata()
                    count_games = 0
                    self.update_label()

        self.table.sort(reverse=True, key=self.Myfunc)
        self.draw_table()
        self.btn_league.setEnabled(False)

        # updating Label
        self.tour = (len(self.teams) - 1) * 2
        self.update_label()

        if self.table[0]['losses'] == 0:
            hof_table = check_HoF.table_hof()
            check_HoF.compare_results(team=self.table[0], hof_table=hof_table)


    def Myfunc(self, e):
        """sort list with dictionary by one of values"""
        return e['points']

    def publish_tourdata(self):
        self.Match_results.append("\n")
        self.Match_results.setFontItalic(True)
        self.Match_results.setFontUnderline(True)
        self.Match_results.append(f"Tour {self.tour} match results are :")
        self.Match_results.setFontItalic(False)
        self.Match_results.setFontUnderline(False)
        self.Match_results.append("\n")

    def simulate_tour(self):
        games_in_tour = len(self.teams) // 2
        if len(self.calendar) == games_in_tour:
            self.btn_tour.setEnabled(False)
            self.btn_league.setEnabled(False)

        self.tour += 1
        self.publish_tourdata()

        for i in range(games_in_tour):

            match = Match(self.calendar[i][0]['home'], self.calendar[i][0]['away'], self.table)
            result, self.table = match.match_data()
            self.Match_results.append(result)

        for i in range(games_in_tour):
            self.calendar.pop(0)

        self.table.sort(reverse=True, key=self.Myfunc)
        self.draw_table()
        # showing number of simulated tours
        self.update_label()

        if len(self.calendar) == 0 and self.table[0]['losses'] == 0:
            hof_table = check_HoF.table_hof()
            check_HoF.compare_results(team=self.table[0], hof_table=hof_table)





if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    league = League()
    sys.exit(app.exec())