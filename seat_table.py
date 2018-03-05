# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seat_table.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SeatForm(object):
    def setupUi(self, SeatForm):
        SeatForm.setObjectName("SeatForm")
        SeatForm.resize(529, 242)
        self.gridLayout = QtWidgets.QGridLayout(SeatForm)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 20, -1, 20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(SeatForm)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.flight_num = QtWidgets.QLabel(SeatForm)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        self.flight_num.setFont(font)
        self.flight_num.setObjectName("flight_num")
        self.horizontalLayout.addWidget(self.flight_num)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.seat_table = QtWidgets.QTableWidget(SeatForm)
        self.seat_table.setAutoScrollMargin(20)
        self.seat_table.setObjectName("seat_table")
        self.seat_table.setColumnCount(4)
        self.seat_table.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.seat_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.seat_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.seat_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.seat_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.seat_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.seat_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.seat_table.setHorizontalHeaderItem(3, item)
        self.seat_table.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.seat_table, 1, 0, 1, 1)

        self.retranslateUi(SeatForm)
        QtCore.QMetaObject.connectSlotsByName(SeatForm)

    def retranslateUi(self, SeatForm):
        _translate = QtCore.QCoreApplication.translate
        SeatForm.setWindowTitle(_translate("SeatForm", "舱位查询"))
        self.label.setText(_translate("SeatForm", "航班号:"))
        self.flight_num.setText(_translate("SeatForm", "HU9066"))
        item = self.seat_table.verticalHeaderItem(0)
        item.setText(_translate("SeatForm", "1"))
        item = self.seat_table.verticalHeaderItem(1)
        item.setText(_translate("SeatForm", "2"))
        item = self.seat_table.verticalHeaderItem(2)
        item.setText(_translate("SeatForm", "3"))
        item = self.seat_table.horizontalHeaderItem(0)
        item.setText(_translate("SeatForm", "舱位等级"))
        item = self.seat_table.horizontalHeaderItem(1)
        item.setText(_translate("SeatForm", "票价"))
        item = self.seat_table.horizontalHeaderItem(2)
        item.setText(_translate("SeatForm", "剩余数量"))
        item = self.seat_table.horizontalHeaderItem(3)
        item.setText(_translate("SeatForm", "购买"))

