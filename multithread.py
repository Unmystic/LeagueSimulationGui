from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

import time

class Worker(QRunnable):
    """
    Worker thread
    """
    @pyqtSlot()
    def run(self):
        """
        your code goes in this function
        :return:
        """
        print("Thread start")
        time.sleep(5)
        print("Thread complete")


class MainWindow(QMainWindow):


    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.threadpool = QThreadPool()
        print(f"Multithreading with maximum {self.threadpool.maxThreadCount()} threads")
        self.counter = 0

        layout = QVBoxLayout()

        self.l = QLabel("Start")
        b = QPushButton("DANGER!")
        b.pressed.connect(self.oh_no)

        layout.addWidget(self.l)
        layout.addWidget(b)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def oh_no(self):
        worker = Worker()
        self.threadpool.start(worker)

    def recurring_timer(self):
        self.counter +=1
        self.l.setText("Counter: %d" % self.counter)


app = QApplication([])
window = MainWindow()
app.exec()