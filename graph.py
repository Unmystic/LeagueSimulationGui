
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPen

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature_1 = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        temperature_2 = [50, 35, 44, 22, 38, 32, 27, 38, 32, 44]

        # Setting background color using current window colorscheme to correlate with the whole app
        # color = self.palette().color(QtGui.QPalette.Window) #if it works
        self.graphWidget.setBackground('w')
        # plot data: x, y values, pen - line profile
        pen = pg.mkPen(color=(255, 0, 0), width=2, style=Qt.PenStyle(2))
        # add legend before plotting
        self.graphWidget.addLegend(offset=(-50, -50))

        self.graphWidget.plot(hour, temperature_1, name="Sensor 1", pen=pen, symbol="+", symbolSize=15, symbolBrush=('b'))
        self.graphWidget.setTitle("Your Title here", color='b', size='20pt')

        styles = {'color': 'g', 'font-size': '15px'}
        self.graphWidget.setLabel(axis='left', text='Temperature (Celsius)', **styles)
        self.graphWidget.setLabel(axis='bottom', text='Hour (H)', **styles)

        #Show grid
        self.graphWidget.showGrid(x=True, y=True)
        #Set Range
        self.graphWidget.setXRange(0, 10, padding=0)
        self.graphWidget.setYRange(20, 55, padding=0)

        # Adding second plot
        pen = pg.mkPen(color=(0, 255, 0), width=2, style=Qt.PenStyle(3))
        self.graphWidget.plot(hour, temperature_2, name="Sensor 2", pen=pen, symbol="+", symbolSize=15, symbolBrush=('y'))
        """
        Alternatively you could move plotting to new function:
        def plot(self, x, y, plotname, color):
            pen = pg.mkPen(color=color)
            self.graphWidget.plot(x, y, name=plotname, pen=pen, symbol='+', symbolSize=30, symbolBrush=(color))
        self.plot(hour, temperature_1, "Sensor1", 'r')
        self.plot(hour, temperature_2, "Sensor2", 'b')
        """
        # To clear the lines call .clear()
        # self.graphWidget.clear()

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()