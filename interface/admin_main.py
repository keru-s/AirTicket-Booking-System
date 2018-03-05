# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AdminMainWindow(object):
    def setupUi(self, AdminMainWindow):
        AdminMainWindow.setObjectName("AdminMainWindow")
        AdminMainWindow.resize(885, 494)
        AdminMainWindow.setIconSize(QtCore.QSize(20, 20))
        self.centralwidget = QtWidgets.QWidget(AdminMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.maingridLayout = QtWidgets.QGridLayout()
        self.maingridLayout.setObjectName("maingridLayout")
        self.gridLayout.addLayout(self.maingridLayout, 0, 0, 1, 1)
        AdminMainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(AdminMainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.toolBar.setMaximumSize(QtCore.QSize(150, 500))
        self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar.setMovable(True)
        self.toolBar.setOrientation(QtCore.Qt.Vertical)
        self.toolBar.setIconSize(QtCore.QSize(100, 100))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName("toolBar")
        AdminMainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.fli_ma_action = QtWidgets.QAction(AdminMainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/航班管理.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.fli_ma_action.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.fli_ma_action.setFont(font)
        self.fli_ma_action.setObjectName("fli_ma_action")
        self.ticket_ma_action = QtWidgets.QAction(AdminMainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/旅客管理.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ticket_ma_action.setIcon(icon1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.ticket_ma_action.setFont(font)
        self.ticket_ma_action.setObjectName("ticket_ma_action")
        self.toolBar.addAction(self.fli_ma_action)
        self.toolBar.addAction(self.ticket_ma_action)

        self.retranslateUi(AdminMainWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminMainWindow)

    def retranslateUi(self, AdminMainWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminMainWindow.setWindowTitle(_translate("AdminMainWindow", "主界面"))
        self.toolBar.setWindowTitle(_translate("AdminMainWindow", "toolBar"))
        self.fli_ma_action.setText(_translate("AdminMainWindow", "航班管理"))
        self.ticket_ma_action.setText(_translate("AdminMainWindow", "订单管理"))
        self.ticket_ma_action.setToolTip(_translate("AdminMainWindow", "订单管理"))

