import sys
import random
import statistics
import csv



from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QMainWindow, QDialog, QMessageBox, QTableWidgetItem

from Scripts.newLeague import NewLeague_Dialog
from Scripts.simulate_league import League


class NewLeague(QDialog,NewLeague_Dialog):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.teams = []
        self.setupUi(self)
        self.show()

        self.league = None

        # Correcting ui design
        self.spinBox.lineEdit().setReadOnly(True)
        self.pushStartSimulation.setEnabled(False)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/images/ball.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle("Create a new league")

        # Sending signals from buttons to functions
        self.pushCreateTeam.clicked.connect(self.create_team)
        self.pushAddOthers.clicked.connect(self.populate_league)

        # Redirecting to new window
        self.pushStartSimulation.clicked.connect(self.league_simulation)



    def create_team(self):
        if self.lineEdit.text() != "":

            self.count += 1
            self.listWidget.addItem(f"{self.count}. {self.lineEdit.text()}")
            choice = self.comboBox.currentIndex()
            ar, dr, tc = self.generate_rating(choice=choice)
            self.teams.append({"name": self.lineEdit.text(), "attackRating": ar, "defenceRating": dr, "teamCohesion": tc})
            self.lineEdit.clear()

    def populate_league(self):
        firstName = []
        lastName = []
        team_names = []

        with open("Scripts/data/firstName.txt") as file:
            for line in file:
                firstName.append(line.rstrip())
        with open("Scripts/data/lastName.txt") as file:
            for line in file:
                lastName.append(line.rstrip())

        for i in range(self.count, self.spinBox.value(),1):
            teamName = f"{firstName[random.randint(0, len(firstName) - 1)]} {lastName[random.randint(0, len(lastName) - 1)]}"
            if teamName in team_names:
                teamName = f"{firstName[random.randint(0, len(firstName) - 1)]} {lastName[random.randint(0, len(lastName) - 1)]}"
            choice = random.choice([1, 2, 3])
            ar, dr, tc = self.generate_rating(choice)
            self.listWidget.addItem(f"{i + 1}. {teamName}")
            self.teams.append({"name": teamName, "attackRating": ar, "defenceRating": dr, "teamCohesion": tc})
            team_names.append(teamName)

        self.write_teamdata()
        self.pushStartSimulation.setEnabled(True)
        self.pushAddOthers.setEnabled(False)

    def generate_rating(self, choice=2):
        ratings = [random.uniform(50, 59.99), random.uniform(60.00, 69.99), random.uniform(70.00, 79.99),
                   random.uniform(80.00, 89.99), random.uniform(90.00, 94.99)]
        balanced_weights = {"defence": [5, 10, 30, 40, 15], "attack": [5, 10, 30, 40, 15], "team_cohesion": [5, 10, 30, 40, 15]}
        def_weights = {"defence": [5, 10, 25, 40, 20], "attack": [5, 10, 35, 40, 10], "team_cohesion": [5, 10, 30, 35, 20]}
        very_def_weights = {"defence": [5, 10, 25, 35, 25], "attack": [5, 10, 40, 40, 5], "team_cohesion": [5, 10, 35, 40, 10]}
        att_weights = {"defence": [5, 10, 35, 40, 10], "attack": [5, 10, 25, 40, 20], "team_cohesion": [5, 10, 30, 35, 20]}
        very_att_weights = {"defence": [5, 10, 40, 40, 5], "attack": [5, 10, 25, 35, 25], "team_cohesion": [5, 10, 35, 40, 10]}
        weights = [very_def_weights, def_weights, balanced_weights, att_weights, very_att_weights]
        attackRating = round(statistics.fmean(random.choices(ratings, weights[choice]['attack'], k=5)), 2)
        defenceRating = round(statistics.fmean(random.choices(ratings, weights[choice]['defence'], k=5)), 2)
        teamCohesion = round(statistics.fmean(random.choices(ratings, weights[choice]['team_cohesion'], k=5)), 2)
        return attackRating, defenceRating, teamCohesion

    def write_teamdata(self):
        with open("Scripts/data/teams.csv", "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "attackRating", "defenceRating", "teamCohesion"])
            for team in self.teams:
                writer.writerow({"name": team["name"], "attackRating": team["attackRating"], "defenceRating": team["defenceRating"], "teamCohesion": team["teamCohesion"] })

    def league_simulation(self):
        if self.league == None:
            self.league = League()
            self.league.exec()
            self.close()



if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    dialog = NewLeague()
    sys.exit(app.exec())

