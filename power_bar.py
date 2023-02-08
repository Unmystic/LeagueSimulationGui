from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt


class _Bar(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
            QtWidgets.QSizePolicy.Policy.MinimumExpanding
        )


    def sizeHint(self) -> QtCore.QSize:
        return QtCore.QSize(40,120)

    def paintEvent(self, e) -> None:
        painter = QtGui.QPainter(self)
        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor('black'))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)

        # Get current state.
        dial = self.parent()._dial
        vmin, vmax = dial.minimum(), dial.maximum()
        value = dial.value()
        # Calculating number of boxes to draw
        pc = (value - vmin)/ (vmax - vmin)
        n_steps_to_draw = int(pc * 5)
        padding = 5

        # Define our canvas
        d_height = painter.device().height() - (padding * 2)
        d_width = painter.device().width() - (padding * 2)
        # setting parameters of a step
        step_size = int(d_height / 5)
        bar_height = int(step_size * 0.6)
        bar_spacer = int(step_size * 0.4 / 2)   # Top and bottom

        brush.setColor(QtGui.QColor('red'))
        for n in range(5):
            rect = QtCore.QRect(
                padding,
                padding + d_height - ((n+1) * step_size) + bar_spacer,
                d_width,
                bar_height
            )
            painter.fillRect(rect, brush)

        painter.end()

    def _trigger_refresh(self):
        self.update()

class PowerBar(QtWidgets.QWidget):
    """
    Custom Qt Widget to show a power bar and dial.
    Demonstrating compound and custom-drawn widget.
    """

    def __init__(self, steps=5, *args, **kwargs):
        super(PowerBar, self).__init__(*args, **kwargs)

        layout = QtWidgets.QVBoxLayout()
        self._bar = _Bar()
        layout.addWidget(self._bar)

        self._dial = QtWidgets.QDial()
        layout.addWidget(self._dial)

        self.setLayout(layout)
        self._dial.valueChanged.connect(self._bar._trigger_refresh)