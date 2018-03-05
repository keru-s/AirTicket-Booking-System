# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ticket.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TicketForm(object):
    def setupUi(self, TicketForm):
        TicketForm.setObjectName("TicketForm")
        TicketForm.resize(725, 395)
        self.gridLayout = QtWidgets.QGridLayout(TicketForm)
        self.gridLayout.setContentsMargins(20, -1, 20, 20)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 30, -1, 30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(TicketForm)
        font = QtGui.QFont()
        font.setFamily("晴圆")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pass_name = QtWidgets.QLabel(TicketForm)
        font = QtGui.QFont()
        font.setFamily("晴圆")
        font.setPointSize(20)
        self.pass_name.setFont(font)
        self.pass_name.setObjectName("pass_name")
        self.horizontalLayout.addWidget(self.pass_name)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tickettable = QtWidgets.QTableWidget(TicketForm)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.tickettable.setFont(font)
        self.tickettable.setAlternatingRowColors(True)
        self.tickettable.setRowCount(10)
        self.tickettable.setObjectName("tickettable")
        self.tickettable.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tickettable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tickettable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tickettable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tickettable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tickettable.setHorizontalHeaderItem(4, item)
        self.tickettable.horizontalHeader().setStretchLastSection(True)
        self.tickettable.verticalHeader().setVisible(False)
        self.tickettable.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tickettable, 1, 0, 1, 1)

        self.retranslateUi(TicketForm)
        QtCore.QMetaObject.connectSlotsByName(TicketForm)

    def retranslateUi(self, TicketForm):
        _translate = QtCore.QCoreApplication.translate
        TicketForm.setWindowTitle(_translate("TicketForm", "取票"))
        self.label.setText(_translate("TicketForm", "姓名:"))
        self.pass_name.setText(_translate("TicketForm", "楚子航"))
        item = self.tickettable.horizontalHeaderItem(0)
        item.setText(_translate("TicketForm", "航班号"))
        item = self.tickettable.horizontalHeaderItem(1)
        item.setText(_translate("TicketForm", "出发地点"))
        item = self.tickettable.horizontalHeaderItem(2)
        item.setText(_translate("TicketForm", "达到地点"))
        item = self.tickettable.horizontalHeaderItem(3)
        item.setText(_translate("TicketForm", "舱位"))
        item = self.tickettable.horizontalHeaderItem(4)
        item.setText(_translate("TicketForm", "取票"))

