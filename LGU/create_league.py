import sys
import random
import statistics
import csv


from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QDialog, QMessageBox, QTableWidgetItem

from newLeague import NewLeague_Dialog


class NewLeague(QDialog,NewLeague_Dialog):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.teams = []
        self.setupUi(self)
        self.show()

        # Correcting ui design
        self.spinBox.lineEdit().setReadOnly(True)
        self.pushStartSimulation.setEnabled(False)

        # Sending signals from buttons to functions
        self.pushCreateTeam.clicked.connect(self.create_team)
        self.pushAddOthers.clicked.connect(self.populate_league)


    def create_team(self):
        if self.lineEdit.text() != "":
            print(self.lineEdit.text())
            self.count += 1
            self.listWidget.addItem(f"{self.count}. {self.lineEdit.text()}")
            teamRating = self.generate_rating()
            self.teams.append({"name": self.lineEdit.text(), "rating": teamRating})
            self.lineEdit.clear()

    def populate_league(self):
        firstName = []
        lastName = []

        with open("Scripts/data/firstName.txt") as file:
            for line in file:
                firstName.append(line.rstrip())
        with open("Scripts/data/lastName.txt") as file:
            for line in file:
                lastName.append(line.rstrip())

        for i in range(self.count, self.spinBox.value(),1):
            x = random.randint(0, 1000)
            random.seed(i + x)
            teamName = f"{firstName[random.randint(0, len(firstName) - 1)]} {lastName[random.randint(0, len(lastName) - 1)]}"
            teamRating = self.generate_rating()
            self.listWidget.addItem(f"{i + 1}. {teamName}")
            self.teams.append({"name": teamName, "rating": teamRating})

        self.write_teamdata()
        self.pushStartSimulation.setEnabled(True)

    def generate_rating(self):
        x = random.randint(0, 1000)
        random.seed(x)
        ratings = [random.uniform(50, 59.99), random.uniform(60.00, 69.99), random.uniform(70.00, 79.99),
                   random.uniform(80.00, 89.99), random.uniform(90.00, 94.99)]
        weights = [5, 10, 30, 40, 15]
        teamRating = round(statistics.fmean(random.choices(ratings, weights, k=5)), 2)
        return teamRating

    def write_teamdata(self):
        with open("Scripts/data/teams.csv", "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "rating"])
            for team in self.teams:
                writer.writerow({"name": team["name"], "rating": team["rating"]})



if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    dialog = NewLeague()
    sys.exit(app.exec())


