# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UserMainWindow(object):
    def setupUi(self, UserMainWindow):
        UserMainWindow.setObjectName("UserMainWindow")
        UserMainWindow.resize(950, 470)
        UserMainWindow.setIconSize(QtCore.QSize(20, 20))
        self.centralwidget = QtWidgets.QWidget(UserMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.maingridLayout = QtWidgets.QGridLayout()
        self.maingridLayout.setObjectName("maingridLayout")
        self.gridLayout.addLayout(self.maingridLayout, 0, 0, 1, 1)
        UserMainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(UserMainWindow)
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
        UserMainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.s_fli_action = QtWidgets.QAction(UserMainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/飞机.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.s_fli_action.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.s_fli_action.setFont(font)
        self.s_fli_action.setObjectName("s_fli_action")
        self.pas_action = QtWidgets.QAction(UserMainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/常旅客.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pas_action.setIcon(icon1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pas_action.setFont(font)
        self.pas_action.setObjectName("pas_action")
        self.uns_book_action = QtWidgets.QAction(UserMainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/退货.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uns_book_action.setIcon(icon2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.uns_book_action.setFont(font)
        self.uns_book_action.setObjectName("uns_book_action")
        self.toolBar.addAction(self.s_fli_action)
        self.toolBar.addAction(self.pas_action)
        self.toolBar.addAction(self.uns_book_action)

        self.retranslateUi(UserMainWindow)
        QtCore.QMetaObject.connectSlotsByName(UserMainWindow)

    def retranslateUi(self, UserMainWindow):
        _translate = QtCore.QCoreApplication.translate
        UserMainWindow.setWindowTitle(_translate("UserMainWindow", "主界面"))
        self.toolBar.setWindowTitle(_translate("UserMainWindow", "toolBar"))
        self.s_fli_action.setText(_translate("UserMainWindow", "查询航班"))
        self.pas_action.setText(_translate("UserMainWindow", "常用旅客"))
        self.uns_book_action.setText(_translate("UserMainWindow", "退订机票"))
        self.uns_book_action.setIconText(_translate("UserMainWindow", "退订机票"))

