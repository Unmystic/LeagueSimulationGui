# Form implementation generated from reading ui file 'tournament.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 860)
        Form.setMinimumSize(QtCore.QSize(640, 480))
        Form.setMaximumSize(QtCore.QSize(1280, 1024))
        Form.setStyleSheet("QWidget{\n"
"background-color:rgb(211, 255, 222);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(157, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_tour = QtWidgets.QPushButton(parent=Form)
        self.btn_tour.setMinimumSize(QtCore.QSize(111, 125))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.btn_tour.setFont(font)
        self.btn_tour.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btn_tour.setStyleSheet("QPushButton {\n"
"    background-color:rgb(85, 170, 127);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 5em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}")
        self.btn_tour.setFlat(False)
        self.btn_tour.setObjectName("btn_tour")
        self.verticalLayout_2.addWidget(self.btn_tour)
        self.btn_league = QtWidgets.QPushButton(parent=Form)
        self.btn_league.setMinimumSize(QtCore.QSize(111, 125))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.btn_league.setFont(font)
        self.btn_league.setStyleSheet("QPushButton {\n"
"    background-color:rgb(85, 170, 127);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 5em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}")
        self.btn_league.setFlat(False)
        self.btn_league.setObjectName("btn_league")
        self.verticalLayout_2.addWidget(self.btn_league)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 3, 1, 1)
        self.Match_results = QtWidgets.QTextEdit(parent=Form)
        self.Match_results.setMinimumSize(QtCore.QSize(390, 220))
        self.Match_results.setStyleSheet("QTextEdit{\n"
"background-color:white;\n"
"}")
        self.Match_results.setObjectName("Match_results")
        self.gridLayout.addWidget(self.Match_results, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_title = QtWidgets.QLabel(parent=Form)
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout.addWidget(self.label_title)
        self.label_tour = QtWidgets.QLabel(parent=Form)
        self.label_tour.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_tour.setObjectName("label_tour")
        self.verticalLayout.addWidget(self.label_tour)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 2)
        self.League_table = QtWidgets.QTableWidget(parent=Form)
        self.League_table.setMinimumSize(QtCore.QSize(625, 301))
        self.League_table.setStyleSheet("QTableWidget{\n"
"background-color:rgb(168, 168, 168);\n"
"}")
        self.League_table.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.League_table.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.League_table.setMidLineWidth(1)
        self.League_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.League_table.setAlternatingRowColors(True)
        self.League_table.setObjectName("League_table")
        self.League_table.setColumnCount(10)
        self.League_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 127))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.League_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.League_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.League_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.League_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.League_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.League_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.League_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.League_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.League_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 255, 127))
        brush = QtGui.QBrush(QtGui.QColor(108, 177, 92))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.League_table.setHorizontalHeaderItem(9, item)
        self.League_table.horizontalHeader().setCascadingSectionResizes(True)
        self.League_table.horizontalHeader().setDefaultSectionSize(70)
        self.League_table.horizontalHeader().setMinimumSectionSize(20)
        self.League_table.horizontalHeader().setStretchLastSection(False)
        self.League_table.verticalHeader().setDefaultSectionSize(24)
        self.gridLayout.addWidget(self.League_table, 0, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_tour.setText(_translate("Form", "Simulate \n"
"Tour"))
        self.btn_league.setText(_translate("Form", "Simulate\n"
" all"))
        self.label_title.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Tours simulated</span></p></body></html>"))
        self.label_tour.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">0 of 34</span></p></body></html>"))
        self.League_table.setSortingEnabled(False)
        item = self.League_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Team Name"))
        item = self.League_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Rating"))
        item = self.League_table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Games"))
        item = self.League_table.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Goals"))
        item = self.League_table.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Against"))
        item = self.League_table.horizontalHeaderItem(5)
        item.setText(_translate("Form", "+/-"))
        item = self.League_table.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Wins"))
        item = self.League_table.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Draws"))
        item = self.League_table.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Losses"))
        item = self.League_table.horizontalHeaderItem(9)
        item.setText(_translate("Form", "Points"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
