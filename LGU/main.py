import sys
from PyQt6.QtWidgets import QApplication
from LeagueSimulation import LeagueSimulator

app = QApplication(sys.argv)

library = LeagueSimulator()

sys.exit(app.exec())