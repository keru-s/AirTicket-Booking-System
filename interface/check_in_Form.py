# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check_in_Form.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_checkinForm(object):
    def setupUi(self, checkinForm):
        checkinForm.setObjectName("checkinForm")
        checkinForm.resize(476, 334)
        self.IDcheckButton = QtWidgets.QPushButton(checkinForm)
        self.IDcheckButton.setGeometry(QtCore.QRect(170, 230, 121, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.IDcheckButton.setFont(font)
        self.IDcheckButton.setObjectName("IDcheckButton")
        self.layoutWidget = QtWidgets.QWidget(checkinForm)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 120, 321, 83))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.IDLine = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adamas")
        font.setPointSize(20)
        self.IDLine.setFont(font)
        self.IDLine.setObjectName("IDLine")
        self.verticalLayout.addWidget(self.IDLine)
        self.layoutWidget1 = QtWidgets.QWidget(checkinForm)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 30, 123, 50))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/取票系统.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("晴圆")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)

        self.retranslateUi(checkinForm)
        QtCore.QMetaObject.connectSlotsByName(checkinForm)

    def retranslateUi(self, checkinForm):
        _translate = QtCore.QCoreApplication.translate
        checkinForm.setWindowTitle(_translate("checkinForm", "Form"))
        self.IDcheckButton.setText(_translate("checkinForm", "确认"))
        self.label.setText(_translate("checkinForm", "身份证号:"))
        self.label_3.setText(_translate("checkinForm", "取票"))

