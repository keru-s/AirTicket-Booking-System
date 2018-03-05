# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SelMainWindow(object):
    def setupUi(self, SelMainWindow):
        SelMainWindow.setObjectName("SelMainWindow")
        SelMainWindow.resize(610, 402)
        SelMainWindow.setIconSize(QtCore.QSize(20, 20))
        self.centralwidget = QtWidgets.QWidget(SelMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 491, 391))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.maingridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.maingridLayout.setContentsMargins(0, 0, 0, 0)
        self.maingridLayout.setObjectName("maingridLayout")
        SelMainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(SelMainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.toolBar.setMaximumSize(QtCore.QSize(120, 400))
        self.toolBar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar.setMovable(True)
        self.toolBar.setOrientation(QtCore.Qt.Vertical)
        self.toolBar.setIconSize(QtCore.QSize(100, 100))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        SelMainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.login_action = QtWidgets.QAction(SelMainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/登陆.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.login_action.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.login_action.setFont(font)
        self.login_action.setObjectName("login_action")
        self.checkin_action = QtWidgets.QAction(SelMainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/取票.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.checkin_action.setIcon(icon1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.checkin_action.setFont(font)
        self.checkin_action.setObjectName("checkin_action")
        self.toolBar.addAction(self.login_action)
        self.toolBar.addAction(self.checkin_action)

        self.retranslateUi(SelMainWindow)
        QtCore.QMetaObject.connectSlotsByName(SelMainWindow)

    def retranslateUi(self, SelMainWindow):
        _translate = QtCore.QCoreApplication.translate
        SelMainWindow.setWindowTitle(_translate("SelMainWindow", "主界面"))
        self.toolBar.setWindowTitle(_translate("SelMainWindow", "toolBar"))
        self.login_action.setText(_translate("SelMainWindow", "登陆"))
        self.login_action.setToolTip(_translate("SelMainWindow", "登陆"))
        self.checkin_action.setText(_translate("SelMainWindow", "取票"))
        self.checkin_action.setToolTip(_translate("SelMainWindow", "取票"))

