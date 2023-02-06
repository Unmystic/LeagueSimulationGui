from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

import time

class Worker(QRunnable):
    """
    Worker thread
    Inherits from Qrunnable to handler worker thread setup
    :param callback : The function callback to run on this worker threads. Supplied args and kwargs would be run on
                        this thread
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pas to the callback function
    """

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constrictor arguments
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        """
        your code goes in this function
        :return:
        """
        print("Thread start")
        self.fn(*self.args, **self.kwargs)
        time.sleep(3)
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

    def execute_this_fn(self, name):
        print(f"Hello, {name}!")

    def oh_no(self):
        worker = Worker(self.execute_this_fn, name="Dio")
        self.threadpool.start(worker)

    def recurring_timer(self):
        self.counter +=1
        self.l.setText("Counter: %d" % self.counter)


app = QApplication([])
window = MainWindow()
app.exec()