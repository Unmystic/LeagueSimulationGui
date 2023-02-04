import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton

from dialog import Ui_Dialog


class MainWindow(QMainWindow):
    """ Main window"""
    def __init__(self, parent=None):
        super().__init__(parent)
        # Use Push button to activate dialog screen
        self.centralWidget = QPushButton("Employee")
        self.centralWidget.clicked.connect(self.onEmployeeBtnClicked)
        self.setCentralWidget(self.centralWidget)

    def onEmployeeBtnClicked(self):
        """Launches employee dialog"""
        dlg = EmployeeDlg(self)
        dlg.exec()


class EmployeeDlg(QDialog):
    """Employee dialog"""
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of GUI
        self.ui = Ui_Dialog()
        # Run the .setupUI() method to show the Gui
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())