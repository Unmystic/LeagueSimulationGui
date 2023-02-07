import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QPen
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QApplication, QGraphicsRectItem, QGraphicsEllipseItem, \
    QGraphicsItem

app = QApplication(sys.argv)

# Defining a scene rect of 400x200, with it's origin at 0,0.
# If we don't set this on creation, we can set it later with .setSceneRect
scene = QGraphicsScene(0, 0, 400, 200)

# Draw a rectangle item
rect = QGraphicsRectItem(0, 0, 200, 50)
rect.setPos(50,20)

# Define the brush(fill)
brush = QBrush(Qt.GlobalColor.gray)
rect.setBrush(brush)

# Define the pen(line)
pen = QPen(Qt.GlobalColor.darkCyan)
pen.setWidth(5)
rect.setPen(pen)

# Draw an ellipse item
ellipse = QGraphicsEllipseItem(0, 0, 100, 100)
ellipse.setPos(75, 30)

# Define the brush(fill)
brush = QBrush(Qt.GlobalColor.lightGray)
ellipse.setBrush(brush)

# Define the pen(line)
pen = QPen(Qt.GlobalColor.darkGreen)
pen.setWidth(3)
ellipse.setPen(pen)

# Change stacking order by defining z values
ellipse.setZValue(200)
rect.setZValue(350)  # You can also use  --- rect.stackAfter(ellipse)

scene.addItem(rect)
scene.addItem(ellipse)

# Set flag to enable moving objects
ellipse.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)


view = QGraphicsView(scene)
view.show()
app.exec()