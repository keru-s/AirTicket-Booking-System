# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'refund.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RefundForm(object):
    def setupUi(self, RefundForm):
        RefundForm.setObjectName("RefundForm")
        RefundForm.resize(830, 478)
        self.gridLayout = QtWidgets.QGridLayout(RefundForm)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 30, -1, 30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(RefundForm)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/退货.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(RefundForm)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tickettable = QtWidgets.QTableWidget(RefundForm)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.tickettable.setFont(font)
        self.tickettable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tickettable.setAlternatingRowColors(True)
        self.tickettable.setTextElideMode(QtCore.Qt.ElideNone)
        self.tickettable.setRowCount(10)
        self.tickettable.setObjectName("tickettable")
        self.tickettable.setColumnCount(6)
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
        item = QtWidgets.QTableWidgetItem()
        self.tickettable.setHorizontalHeaderItem(5, item)
        self.tickettable.horizontalHeader().setStretchLastSection(True)
        self.tickettable.verticalHeader().setVisible(False)
        self.tickettable.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tickettable)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(RefundForm)
        QtCore.QMetaObject.connectSlotsByName(RefundForm)

    def retranslateUi(self, RefundForm):
        _translate = QtCore.QCoreApplication.translate
        RefundForm.setWindowTitle(_translate("RefundForm", "Form"))
        self.label.setText(_translate("RefundForm", "退票"))
        item = self.tickettable.horizontalHeaderItem(0)
        item.setText(_translate("RefundForm", "姓名"))
        item = self.tickettable.horizontalHeaderItem(1)
        item.setText(_translate("RefundForm", "航班号"))
        item = self.tickettable.horizontalHeaderItem(2)
        item.setText(_translate("RefundForm", "出发地点"))
        item = self.tickettable.horizontalHeaderItem(3)
        item.setText(_translate("RefundForm", "达到地点"))
        item = self.tickettable.horizontalHeaderItem(4)
        item.setText(_translate("RefundForm", "舱位等级"))
        item = self.tickettable.horizontalHeaderItem(5)
        item.setText(_translate("RefundForm", "退票"))

