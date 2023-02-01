from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel,QMenu
import sys


# Subclass MainWindow to customize your main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My app")
        self.setFixedSize(QSize(400,300))

    def contextMenuEvent(self, e) -> None:
        context = QMenu(self)
        context.addAction(QAction("test1", self))
        context.addAction(QAction("test2", self))
        context.addAction(QAction("test3", self))
        context.exec(e.globalPos())



app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()


#signal based approach
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("My app")
#         self.setFixedSize(QSize(400,300))
#         self.show()
#         self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
#         self.customContextMenuRequested.connect(self.on_context_menu)
#
#     def on_context_menu(self, pos) -> None:
#         context = QMenu(self)
#         context.addAction(QAction("test1", self))
#         context.addAction(QAction("test2", self))
#         context.addAction(QAction("test3", self))
#         context.exec(self.mapToGlobal(pos))