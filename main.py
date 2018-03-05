# -*- coding:utf-8 -*-

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QTableWidgetItem, QPushButton, \
    QMessageBox, QHeaderView
from select_main import Ui_SelMainWindow
from login import Ui_LoginForm
from register import Ui_RegisterForm
from check_in_Form import Ui_checkinForm
from user_main import Ui_UserMainWindow
from admin_main import Ui_AdminMainWindow
from flight_search import Ui_Form
from flight_manage import Ui_FlightManagerForm
from seat_table import Ui_SeatForm
from passenger import Ui_PassengerForm
from new_passenger import Ui_New_Pa_Form
from refund import Ui_RefundForm
from ticket import Ui_TicketForm
from flight_information import Ui_FlightInfomationForm
from ticket_manage import Ui_TicketManagerForm
from book_passenger import Ui_BookPassengerForm
from ticket_information import Ui_TicketInformationForm
import pyodbc

# 连接数据库
cnxn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=localhost;'
                      'DATABASE=BookFlight;'
                      'UID=sa;'
                      'PWD=zhanxin')
cursor = cnxn.cursor()


# 设置跨窗体信号
class Communicate(QtCore.QObject):
    # 关闭窗体
    close = QtCore.pyqtSignal()
    # 打开注册窗体
    registerSignal = QtCore.pyqtSignal()
    # 显示登陆窗体
    showLogin = QtCore.pyqtSignal()


# 登陆界面
class MainWin(QMainWindow, Ui_SelMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi(self)
        self.login = LoginIn()
        self.check_in = CheckIn()
        self.register = Register()

        # 初始化跨窗体信号
        self.login.c = Communicate()
        self.login.c.close.connect(self.close)
        self.login.c.registerSignal.connect(self.show_register)

        self.register.c = Communicate()
        self.register.c.showLogin.connect(self.show_login)

        # 动态加载各布局
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.login)
        self.stacked_widget.addWidget(self.check_in)
        self.stacked_widget.addWidget(self.register)
        self.maingridLayout.addWidget(self.stacked_widget, 0, 0)

        self.login_action.triggered.connect(self.show_login)
        self.checkin_action.triggered.connect(self.show_check_in)

    def show_login(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_check_in(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_register(self):
        self.stacked_widget.setCurrentIndex(2)


# 用户或管理员登陆
class LoginIn(QWidget, Ui_LoginForm):
    def __init__(self):
        super(LoginIn, self).__init__()
        self.setupUi(self)
        self.user_main = UserMain()
        self.admin_main = AdminMain()

        # 初始化关闭信号
        self.c = Communicate()

        self.loginButton.clicked.connect(self.choice_id)
        self.registerButton.clicked.connect(self.register)

    def choice_id(self):
        # 用于记录用户名
        global user_account
        # 检查是否输入用户名和密码
        if self.user_name.text() and self.user_password.text():

            # 如果选择用户登陆
            if self.user_rB.isChecked():
                try:
                    # 执行查找用户名和密码的存储过程
                    cursor.execute('exec login_user {0}, {1}'.format(self.user_name.text(), self.user_password.text()))
                    exist = cursor.fetchall()
                    # 如果数据库中存在该用户，则exist为真，否则为空
                    if exist:
                        user_account = self.user_name.text()
                        self.c.close.emit()
                        self.user_main.show()
                    else:
                        QMessageBox.warning(self, "错误", '用户名或密码错误')
                except Exception as e:
                    print(e)
            elif self.admin_rB.isChecked():
                try:
                    # 执行查找管理员的用户名和密码的存储过程
                    cursor.execute('exec login_admin {0}, {1}'.format(self.user_name.text(), self.user_password.text()))
                    exist = cursor.fetchall()
                    # 如果数据库中存在该管理员，则exist为真，否则为空
                    if exist:
                        user_account = self.user_name.text()
                        self.c.close.emit()
                        self.admin_main.show()
                    else:
                        QMessageBox.warning(self, "错误", '用户名或密码错误')
                except Exception as e:
                    print(e)

        else:
            QMessageBox.warning(self, "错误", "输入不能为空")

    def register(self):
        self.c.registerSignal.emit()


# 注册帐号
class Register(QWidget, Ui_RegisterForm):
    def __init__(self):
        super(Register, self).__init__()
        self.setupUi(self)

        self.c = Communicate()

        self.reg_Button.clicked.connect(self.reg)
        self.cancel_Button.clicked.connect(self.show_login)

    # 注册帐号
    def reg(self):
        # 用户输入检测
        if not (self.reg_name.text() and self.reg_password.text() and self.reg_re_password.text()):
            QMessageBox.warning(self, "错误", "输入不能为空")
        elif self.reg_password.text() != self.reg_re_password.text():
            QMessageBox.warning(self, "错误", "两次密码不一致")
        # 用户注册
        elif self.user_reg_rB.isChecked():
            try:
                cursor.execute('exec check_user_name {0}'.format(self.reg_name.text()))
                rows = cursor.fetchall()

                if rows:
                    QMessageBox.warning(self, "错误", "该用户名已存在")
                else:
                    cursor.execute('exec sign_up_user {0}, {1}'.format(self.reg_name.text(), self.reg_password.text()))
                    # 提交数据进入数据库
                    cnxn.commit()
                    QMessageBox.about(self, "成功", "注册成功")
            except Exception as e:
                print(e)
        # 管理员注册
        elif self.admin_reg_rB.isChecked():
            try:
                cursor.execute('exec check_admin_name {0}'.format(self.reg_name.text()))
                rows = cursor.fetchall()

                if rows:
                    QMessageBox.warning(self, "错误", "该用户名已存在")
                else:
                    cursor.execute('exec sign_up_admin {0}, {1}'.format(self.reg_name.text(), self.reg_password.text()))
                    # 提交数据进入数据库
                    cnxn.commit()
                    QMessageBox.about(self, "成功", "注册成功")
            except Exception as e:
                print(e)

    # 显示登陆窗体
    def show_login(self):
        self.c.showLogin.emit()


# 取票
class CheckIn(QWidget, Ui_checkinForm):
    def __init__(self):
        super(CheckIn, self).__init__()
        self.setupUi(self)

        self.ticket = Ticket()

        self.IDcheckButton.clicked.connect(self.check)

    def check(self):
        global pass_id
        pass_id = self.IDLine.text()
        try:

            cursor.execute('exec checkin_pass {0}'.format(pass_id))
            exist = cursor.fetchall()
            if exist:
                self.ticket.show_ticket()
            else:
                QMessageBox.warning(self, "警告", "输入的身份证号错误")
        except Exception as e:
            print(e)


# 取票界面
class Ticket(QWidget, Ui_TicketForm):
    reflush = QtCore.pyqtSignal()

    def __init__(self):
        super(Ticket, self).__init__()
        self.setupUi(self)
        self.reflush.connect(self.show_ticket)

    def show_ticket(self):
        try:
            self.tickettable.clearContents()
            cursor.execute("exec checkin {0}".format(pass_id))
            rows = cursor.fetchall()
            self.show()
            if rows:
                self.pass_name.setText(rows[0].name)
                # 将订票信息传入表格
                for index, row in enumerate(rows):
                    newItem = QTableWidgetItem(row.flight_num)
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tickettable.setItem(index, 0, newItem)

                    newItem = QTableWidgetItem(row.dep_loc)
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tickettable.setItem(index, 1, newItem)

                    newItem = QTableWidgetItem(row.arr_loc)
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tickettable.setItem(index, 2, newItem)

                    newItem = QTableWidgetItem(row.seat_level)
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tickettable.setItem(index, 3, newItem)

                    ticket = QPushButton()
                    ticket.setText('取票')
                    ticket.clicked.connect(self.update_ticket)
                    self.tickettable.setCellWidget(index, 4, ticket)
            else:
                QMessageBox.about(self, '抱歉', "该旅客无订票信息")

        except Exception as e:
            print(e)

    def update_ticket(self):
        name = self.pass_name.text()
        try:
            sender = self.sender()
            row = self.tickettable.indexAt(sender.pos()).row()
            cursor.execute('exec update_ticket {0},{1},{2}'.format(name,
                                                                   self.tickettable.item(row, 0).text(),
                                                                   self.tickettable.item(row, 3).text()))
            cnxn.commit()
        except Exception as e:
            print(e)
        QMessageBox.about(self, ' ', '取票成功')
        self.reflush.emit()


# 旅客系统主界面
class UserMain(QMainWindow, Ui_UserMainWindow):
    def __init__(self):
        super(UserMain, self).__init__()
        self.setupUi(self)

        # 初始化窗体，为后面的动态加载做准备
        self.search = Search()
        self.passenger = Passenger()
        self.refund = Refund()

        # 加载stackedlayout，让widget可以动态切换
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.search)
        self.stacked_widget.addWidget(self.passenger)
        self.stacked_widget.addWidget(self.refund)
        self.maingridLayout.addWidget(self.stacked_widget, 0, 0)
        self.search.show_flight()

        # 为工具栏设置触发器
        self.s_fli_action.triggered.connect(self.show_search)
        self.pas_action.triggered.connect(self.show_passenger)
        self.uns_book_action.triggered.connect(self.show_ticket)

    def show_search(self):
        self.stacked_widget.setCurrentIndex(0)
        self.search.show_flight()

    def show_passenger(self):
        self.stacked_widget.setCurrentIndex(1)
        self.passenger.show_passenger()

    def show_ticket(self):
        self.stacked_widget.setCurrentIndex(2)
        self.refund.show_ticket()


# 常用旅客
class Passenger(QWidget, Ui_PassengerForm):
    def __init__(self):
        super(Passenger, self).__init__()
        self.setupUi(self)

        # 重新设置列宽,使其自适应
        for i in range(0, 4):
            self.passengertable.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)

        self.c = Communicate()
        # 初始化功能
        self.add_pa_info = AddPassenger()
        self.update_pa_info = UpdatePassenger()
        self.new_pass.clicked.connect(self.add_pa_info.show)
        self.update_pas.clicked.connect(self.show_up_pa_info)
        self.del_pas.clicked.connect(self.del_pa_info)
        # 如果就新建完用户或者修改完用户信息，则刷新列表
        self.add_pa_info.c.close.connect(self.show_passenger)
        self.update_pa_info.c.close.connect(self.show_passenger)
        self.c.close.connect(self.show_passenger)

    # 展示常用旅客窗体
    def show_passenger(self):
        try:
            cursor.execute('exec show_common_passenger {0}'.format(user_account))
            rows = cursor.fetchall()

            # 清空表格里面的内容
            self.passengertable.clearContents()
            # 将常用旅客信息填入表格
            for index, row in enumerate(rows):
                newItem = QTableWidgetItem(row.name)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.passengertable.setItem(index, 0, newItem)
                newItem = QTableWidgetItem(row.sex)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.passengertable.setItem(index, 1, newItem)
                newItem = QTableWidgetItem(row.ID_num)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.passengertable.setItem(index, 2, newItem)
                newItem = QTableWidgetItem(row.telephone)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.passengertable.setItem(index, 3, newItem)
        except Exception as e:
            print(e)

    # 展示修改信息窗体
    def show_up_pa_info(self):
        i = self.passengertable.currentRow()
        self.update_pa_info.show_former_info(self.passengertable.item(i, 0).text(),
                                             self.passengertable.item(i, 1).text(),
                                             self.passengertable.item(i, 2).text(),
                                             self.passengertable.item(i, 3).text())

    # 删除旅客信息
    def del_pa_info(self):
        row = self.passengertable.currentRow()
        reply = QMessageBox.information(self, '警告', '确认删除' + self.passengertable.item(row, 0).text() + '吗？',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                cursor.execute(
                    'exec delete_pa_info {0},{1}'.format(user_account, self.passengertable.item(row, 2).text()))
                cnxn.commit()
            except Exception as e:
                print(e)
            self.c.close.emit()


# 新增旅客
class AddPassenger(QWidget, Ui_New_Pa_Form):
    def __init__(self):
        super(AddPassenger, self).__init__()
        self.setupUi(self)

        self.c = Communicate()
        self.add_info.clicked.connect(self.addinfo)

    def addinfo(self):
        # 获取用户输入的新增旅客信息
        p_name = self.p_name_Edit.text()
        p_sex = self.comboBox.currentText()
        p_ID = self.p_ID_Edit.text()
        p_tele = self.p_tele_Edit.text()
        try:
            cursor.execute('exec add_pa_info {0},{1},{2},{3},{4}'.format(user_account, p_name, p_sex, p_ID, p_tele))
            cnxn.commit()
        except Exception as e:
            print(e)
        self.c.close.emit()
        self.close()


# 旅客信息修改，复用new_passenger的界面
class UpdatePassenger(QWidget, Ui_New_Pa_Form):
    def __init__(self):
        super(UpdatePassenger, self).__init__()
        self.setupUi(self)
        self.label.setText('用户信息修改')
        self.add_info.setText('修改')

        self.c = Communicate()
        self.old_id_num = 0

        self.add_info.clicked.connect(self.update_info)

    def show_former_info(self, name, sex, id_num, telephone):
        # 将选中信息提前放入编辑栏，方便修改
        self.old_id_num = id_num
        self.p_name_Edit.setText(name)
        self.comboBox.setCurrentText(sex.strip())
        self.p_ID_Edit.setText(id_num)
        self.p_tele_Edit.setText(telephone)
        self.show()

    def update_info(self):
        # 获取用户修改后的信息
        p_name = self.p_name_Edit.text()
        p_sex = self.comboBox.currentText()
        p_id = self.p_ID_Edit.text()
        p_tele = self.p_tele_Edit.text()
        try:
            cursor.execute('exec update_pa_info {0},{1},{2},{3},{4},{5}'.
                           format(user_account, p_name, p_sex, str(self.old_id_num), p_id, p_tele))
            cnxn.commit()
        except Exception as e:
            print(e)
        self.c.close.emit()
        self.close()


# 航班查询
class Search(QWidget, Ui_Form):
    # s_signal = QtCore.pyqtSignal()
    flight_info = QtCore.pyqtSignal(str, str, str, str, str)

    def __init__(self):
        super(Search, self).__init__()
        self.setupUi(self)
        # 初始化座位查询窗口
        self.seat = Seat()

    # 显示所有航班
    def show_flight(self):
        try:
            # 查询航班信息
            cursor.execute('select * from flight order by dep_loc,arr_loc')
            rows = cursor.fetchall()

            # 将航班信息填入表格
            for index, row in enumerate(rows):
                newItem = QTableWidgetItem(row.flight_num)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(index, 0, newItem)
                newItem = QTableWidgetItem(row.dep_loc)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(index, 1, newItem)
                newItem = QTableWidgetItem(row.arr_loc)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(index, 2, newItem)
                newItem = QTableWidgetItem(row.dep_time.split(':')[0] + ':' + row.dep_time.split(':')[1])
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(index, 3, newItem)
                newItem = QTableWidgetItem(row.arr_time.split(':')[0] + ':' + row.arr_time.split(':')[1])
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(index, 4, newItem)
                # 加入购票按钮
                book_f = QPushButton()
                book_f.setText('购票')
                book_f.clicked.connect(self.search_ticket)
                self.tableWidget.setCellWidget(index, 5, book_f)
        except Exception as e:
            print(e)
        self.searchflight.clicked.connect(self.search_flight)

    # 进行航班搜索
    def search_flight(self):
        dep_loc = self.deploc.text()
        arr_loc = self.arrloc.text()
        if dep_loc is '' and arr_loc is '':
            self.show_flight()
        else:
            try:
                # 查询航班信息
                if dep_loc is '' and arr_loc:
                    cursor.execute(r"select * from flight where arr_loc='{0}' order by dep_loc,arr_loc".format(arr_loc))
                elif arr_loc is '' and dep_loc:
                    cursor.execute(r"select * from flight where dep_loc='{0}' order by dep_loc,arr_loc".format(dep_loc))
                else:
                    cursor.execute('exec search_flight {0}, {1}'.format(dep_loc, arr_loc))
                rows = cursor.fetchall()
                self.tableWidget.clearContents()
                # 将航班信息填入表格
                for index, row in enumerate(rows):
                    newItem = QTableWidgetItem(row.flight_num)
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(index, 0, newItem)
                    newItem = QTableWidgetItem(row.dep_loc)
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(index, 1, newItem)
                    newItem = QTableWidgetItem(row.arr_loc)
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(index, 2, newItem)
                    newItem = QTableWidgetItem(row.dep_time.split(':')[0] + ':' + row.dep_time.split(':')[1])
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(index, 3, newItem)
                    newItem = QTableWidgetItem(row.arr_time.split(':')[0] + ':' + row.arr_time.split(':')[1])
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(index, 4, newItem)
                    # 加入购票按钮
                    book_f = QPushButton()
                    book_f.setText('购票')
                    book_f.clicked.connect(self.search_ticket)
                    self.tableWidget.setCellWidget(index, 5, book_f)
            except Exception as e:
                print(e)

    # 通过航班号 获取舱位信息
    def search_ticket(self):
        # 获取航班号
        sender = self.sender()
        index = self.tableWidget.indexAt(sender.pos())
        item = self.tableWidget.item(index.row(), 0)
        self.seat.seat_table_show(item.text())

    # 在订票信息窗体里显示所有航班
    def ticket_inf_show_flight(self):
        self.show()
        try:
            # 查询航班信息
            cursor.execute('select * from flight order by dep_loc,arr_loc')
            rows = cursor.fetchall()

            # 将航班信息填入表格
            for index, row in enumerate(rows):
                newItem = QTableWidgetItem(row.flight_num)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(index, 0, newItem)
                newItem = QTableWidgetItem(row.dep_loc)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(index, 1, newItem)
                newItem = QTableWidgetItem(row.arr_loc)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(index, 2, newItem)
                newItem = QTableWidgetItem(row.dep_time.split(':')[0] + ':' + row.dep_time.split(':')[1])
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(index, 3, newItem)
                newItem = QTableWidgetItem(row.arr_time.split(':')[0] + ':' + row.arr_time.split(':')[1])
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(index, 4, newItem)
                # 加入修改按钮
                book_f = QPushButton()
                book_f.setText('修改')
                book_f.clicked.connect(self.update_ticket)
                self.tableWidget.setCellWidget(index, 5, book_f)
        except Exception as e:
            print(e)
        self.searchflight.clicked.connect(self.ticket_inf_search_flight)

    # 在订票信息窗体里进行航班搜索
    def ticket_inf_search_flight(self):
        dep_loc = self.deploc.text()
        arr_loc = self.arrloc.text()
        try:
            # 查询航班信息
            cursor.execute('exec search_flight {0}, {1}'.format(dep_loc, arr_loc))
            rows = cursor.fetchall()
            self.tableWidget.clearContents()
            # 将航班信息填入表格
            for index, row in enumerate(rows):
                newItem = QTableWidgetItem(row.flight_num)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(index, 0, newItem)
                newItem = QTableWidgetItem(row.dep_loc)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(index, 1, newItem)
                newItem = QTableWidgetItem(row.arr_loc)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(index, 2, newItem)
                newItem = QTableWidgetItem(row.dep_time.split(':')[0] + ':' + row.dep_time.split(':')[1])
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(index, 3, newItem)
                newItem = QTableWidgetItem(row.arr_time.split(':')[0] + ':' + row.arr_time.split(':')[1])
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(index, 4, newItem)
                # 加入修改按钮
                book_f = QPushButton()
                book_f.setText('修改')
                book_f.clicked.connect(self.update_ticket)
                self.tableWidget.setCellWidget(index, 5, book_f)
        except Exception as e:
            print(e)

    # 向管理员订单管理界面发送修改后的航班号
    def update_ticket(self):
        # 获取管理员点击按钮的位置
        sender = self.sender()
        index = self.tableWidget.indexAt(sender.pos())
        row = index.row()
        try:
            self.flight_info.emit(self.tableWidget.item(row, 0).text(), self.tableWidget.item(row, 1).text(),
                                  self.tableWidget.item(row, 2).text(), self.tableWidget.item(row, 3).text(),
                                  self.tableWidget.item(row, 4).text())
        except Exception as e:
            print(e)


# 座位查询
class Seat(QWidget, Ui_SeatForm):
    def __init__(self):
        super(Seat, self).__init__()
        self.setupUi(self)
        self.book_passenger = Booking()

    # 显示座位信息
    def seat_table_show(self, item):
        # 记录航班号
        global fli_num
        fli_num = item
        # 执行存储过程，查询对应航班号的剩余座位
        try:
            self.show()
            cursor.execute('exec flight_seat {0}'.format(item))
            rows = cursor.fetchall()

            # 设置标签栏的航班号
            self.flight_num.setText(rows[0].flight_num)
            # 将座位信息传入表格
            for index, row in enumerate(rows):
                newItem = QTableWidgetItem(row.seat_level)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.seat_table.setItem(index, 0, newItem)
                newItem = QTableWidgetItem('￥' + str(row.price).split('.')[0])
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.seat_table.setItem(index, 1, newItem)
                newItem = QTableWidgetItem(str(row.remain_num))
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.seat_table.setItem(index, 2, newItem)
                ticket = QPushButton()
                ticket.setText('购票')
                ticket.clicked.connect(self.show_b_p)
                self.seat_table.setCellWidget(index, 3, ticket)
        except Exception as e:
            print(fli_num)
            print(e)

    # 调用常用旅客窗口
    def show_b_p(self):
        # 记录舱位等级
        global seat_level
        sender = self.sender()
        index = self.seat_table.indexAt(sender.pos())
        if self.seat_table.item(index.row(), 2).text() == '0':
            QMessageBox.information(self, '抱歉', '该舱位已经售完')
        else:
            seat = self.seat_table.item(index.row(), 0)
            seat_level = seat.text()
            self.book_passenger.show_common_passenger()
            self.close()


# 常用旅客选择和购票
class Booking(QWidget, Ui_BookPassengerForm):
    def __init__(self):
        super(Booking, self).__init__()
        self.setupUi(self)

        self.add_pa_info = AddPassenger()
        self.update_pa_info = UpdatePassenger()

        self.new_pass.clicked.connect(self.add_pa_info.show)
        self.update_pas.clicked.connect(self.show_up_pa_info)
        self.book.clicked.connect(self.book_ticket)

        # 如果就新建完用户或者修改完用户信息，则刷新列表
        self.add_pa_info.c.close.connect(self.show_common_passenger)
        self.update_pa_info.c.close.connect(self.show_common_passenger)
        # 调整表格列宽
        for i in range(0, 3):
            self.passengertable.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)

    # 展示常用旅客窗体
    def show_common_passenger(self):
        try:
            cursor.execute('exec show_common_passenger {0}'.format(user_account))
            rows = cursor.fetchall()

            # 将常用旅客信息填入表格
            for index, row in enumerate(rows):
                newItem = QTableWidgetItem(row.name)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.passengertable.setItem(index, 0, newItem)
                newItem = QTableWidgetItem(row.sex)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.passengertable.setItem(index, 1, newItem)
                newItem = QTableWidgetItem(row.ID_num)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.passengertable.setItem(index, 2, newItem)
                newItem = QTableWidgetItem(row.telephone)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.passengertable.setItem(index, 3, newItem)
        except Exception as e:
            print(e)
        self.show()

    # 展示修改信息窗体
    def show_up_pa_info(self):
        i = self.passengertable.currentRow()
        self.update_pa_info.show_former_info(self.passengertable.item(i, 0).text(),
                                             self.passengertable.item(i, 1).text(),
                                             self.passengertable.item(i, 2).text(),
                                             self.passengertable.item(i, 3).text())

    # 订票
    def book_ticket(self):
        # 获得用户选中的行,以获取旅客身份证号
        row = self.passengertable.currentRow()
        id_num = self.passengertable.item(row, 2).text()
        try:
            cursor.execute('exec check_ticket_exist {0},{1}'.format(fli_num, id_num))
            exist = cursor.fetchall()
            if exist:
                QMessageBox.information(self, '提示', '该用户已订票，请勿重复订票')
            else:
                cursor.execute('exec book_ticket {0},{1},{2}'.format(fli_num, id_num, seat_level))
                cursor.execute
                cnxn.commit()
                QMessageBox.information(self, '提示', '购票成功')
        except Exception as e:
            print(e)


# 退票
class Refund(QWidget, Ui_RefundForm):
    reflush = QtCore.pyqtSignal()

    def __init__(self):
        super(Refund, self).__init__()
        self.setupUi(self)

        self.reflush.connect(self.show_ticket)

    def show_ticket(self):
        try:
            cursor.execute('exec show_ticket {0}'.format(user_account))
            rows = cursor.fetchall()

            self.tickettable.clearContents()
            # 将订票信息传入表格
            for index, row in enumerate(rows):
                newItem = QTableWidgetItem(row.name)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tickettable.setItem(index, 0, newItem)

                newItem = QTableWidgetItem(row.flight_num)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tickettable.setItem(index, 1, newItem)

                newItem = QTableWidgetItem(row.dep_loc)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tickettable.setItem(index, 2, newItem)

                newItem = QTableWidgetItem(row.arr_loc)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tickettable.setItem(index, 3, newItem)

                newItem = QTableWidgetItem(row.seat_level)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tickettable.setItem(index, 4, newItem)

                ticket = QPushButton()
                ticket.setText('退票')
                ticket.clicked.connect(self.confirm)
                self.tickettable.setCellWidget(index, 5, ticket)

        except Exception as e:
            print(e)

    def confirm(self):
        sender = self.sender()
        row = self.tickettable.indexAt(sender.pos()).row()
        reply = QMessageBox.question(self, '确认', '是否退票？', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            try:
                cursor.execute('exec refuse_ticket {0},{1}'.format(self.tickettable.item(row, 1).text(),
                                                                   self.tickettable.item(row, 0).text()))
                cnxn.commit()
            except Exception as e:
                print(e)
        self.reflush.emit()


# 管理员系统主界面
class AdminMain(QMainWindow, Ui_AdminMainWindow):
    def __init__(self):
        super(AdminMain, self).__init__()
        self.setupUi(self)

        # 初始化窗体，为后面的动态加载做准备
        self.flight = FlightManage()
        self.ticket = TicketManage()

        # 加载stacked layout，让widget可以动态切换
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.flight)
        self.stacked_widget.addWidget(self.ticket)
        self.maingridLayout.addWidget(self.stacked_widget, 0, 0)

        # 为工具栏设置触发器
        self.fli_ma_action.triggered.connect(self.show_flight_m)
        self.ticket_ma_action.triggered.connect(self.show_ticket_m)

    def show_flight_m(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_ticket_m(self):
        self.stacked_widget.setCurrentIndex(1)
        self.ticket.show_all_ticket()


# 航班管理
class FlightManage(QWidget, Ui_FlightManagerForm):
    def __init__(self):
        super(FlightManage, self).__init__()
        self.setupUi(self)
        self.show_flight()

        # 重新设置列宽,使其自适应
        for i in range(3, 5):
            self.flighttable.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)

        self.seat_details = SeatDetails()
        self.flight_information = FlightInformation()

        self.searchflight.clicked.connect(self.sf)
        self.addButton.clicked.connect(self.add_fli_inf)
        self.updateButton.clicked.connect(self.update_fli_inf)
        self.delButton.clicked.connect(self.delete_fli_inf)

        self.flight_information.c.close.connect(self.show_flight)

    # 搜索指定城市的航班
    def sf(self):
        dep_loc = self.deploc.text()
        arr_loc = self.arrloc.text()
        if dep_loc and arr_loc:
            try:
                # 查询航班信息
                cursor.execute('exec search_flight {0}, {1}'.format(dep_loc, arr_loc))
                rows = cursor.fetchall()

                self.flighttable.clearContents()
                # 将航班信息填入表格
                for index, row in enumerate(rows):
                    newItem = QTableWidgetItem(row.flight_num)
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.flighttable.setItem(index, 0, newItem)
                    newItem = QTableWidgetItem(row.dep_loc)
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.flighttable.setItem(index, 1, newItem)
                    newItem = QTableWidgetItem(row.arr_loc)
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.flighttable.setItem(index, 2, newItem)
                    newItem = QTableWidgetItem(row.dep_time.split(':')[0] + ':' + row.dep_time.split(':')[1])
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.flighttable.setItem(index, 3, newItem)
                    newItem = QTableWidgetItem(row.arr_time.split(':')[0] + ':' + row.arr_time.split(':')[1])
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.flighttable.setItem(index, 4, newItem)
                    # 加入详情按钮,点击之后显示座位信息
                    seat_details = QPushButton()
                    seat_details.setText('详情')
                    seat_details.clicked.connect(self.show_seat_detail)
                    self.flighttable.setCellWidget(index, 5, seat_details)
            except Exception as e:
                print(e)
        else:
            self.show_flight()

    # 展示所有航班
    def show_flight(self):
        try:
            cursor.execute('select * from flight order by dep_loc,arr_loc')
            rows = cursor.fetchall()

            self.flighttable.clearContents()

            # 将航班信息填入表格
            for index, row in enumerate(rows):
                newItem = QTableWidgetItem(row.flight_num)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.flighttable.setItem(index, 0, newItem)
                newItem = QTableWidgetItem(row.dep_loc)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.flighttable.setItem(index, 1, newItem)
                newItem = QTableWidgetItem(row.arr_loc)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.flighttable.setItem(index, 2, newItem)
                newItem = QTableWidgetItem(row.dep_time.split(':')[0] + ':' + row.dep_time.split(':')[1])
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.flighttable.setItem(index, 3, newItem)
                newItem = QTableWidgetItem(row.arr_time.split(':')[0] + ':' + row.arr_time.split(':')[1])
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.flighttable.setItem(index, 4, newItem)
                # 加入详情按钮,点击之后显示座位信息
                seat_details = QPushButton()
                seat_details.setText('详情')
                seat_details.clicked.connect(self.show_seat_detail)
                self.flighttable.setCellWidget(index, 5, seat_details)
        except Exception as e:
            print(e)

    # 显示航班上的座位信息
    def show_seat_detail(self):
        try:
            # 获取航班号
            sender = self.sender()
            index = self.flighttable.indexAt(sender.pos())
            item = self.flighttable.item(index.row(), 0)
            self.seat_details.seat_table_show(item.text())
        except Exception as e:
            print(e)

    # 增加一个航班
    def add_fli_inf(self):
        self.flight_information.show_fli_info()
        self.show_flight()

    # 修改航班信息
    def update_fli_inf(self):
        row = self.flighttable.currentRow()
        if row < 0:
            QMessageBox.warning(self, '警告', '请选中一行')
        else:
            self.flight_information.show_up_fli_info(self.flighttable.item(row, 0).text(),
                                                     self.flighttable.item(row, 1).text(),
                                                     self.flighttable.item(row, 2).text(),
                                                     self.flighttable.item(row, 3).text(),
                                                     self.flighttable.item(row, 4).text())
            self.show_flight()

    # 删除航班信息
    def delete_fli_inf(self):
        row = self.flighttable.currentRow()
        flight_num = self.flighttable.item(row, 0).text()
        cursor.execute('exec del_fli_inf {0}'.format(flight_num))
        cnxn.commit()
        QMessageBox.information(self, '提示', '删除完成')
        self.show_flight()


# 航班座位详情,复用座位查询界面
class SeatDetails(QWidget, Ui_SeatForm):
    def __init__(self):
        super(SeatDetails, self).__init__()
        self.setupUi(self)
        self.book_passenger = Booking()

    # 显示座位信息
    def seat_table_show(self, item):

        # 执行存储过程，查询对应航班号的剩余座位
        try:
            self.show()
            cursor.execute('exec flight_seat %s' % item)
            rows = cursor.fetchall()

            # 设置标签栏的航班号
            self.flight_num.setText(rows[0].flight_num)
            self.seat_table.setHorizontalHeaderLabels(['舱位等级', '价格', '剩余数量', '已售数量'])
            # 将座位信息传入表格
            for index, row in enumerate(rows):
                newItem = QTableWidgetItem(row.seat_level)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.seat_table.setItem(index, 0, newItem)
                newItem = QTableWidgetItem('￥' + str(row.price).split('.')[0])
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.seat_table.setItem(index, 1, newItem)
                newItem = QTableWidgetItem(str(row.remain_num))
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.seat_table.setItem(index, 2, newItem)
                newItem = QTableWidgetItem(str(row.ordered_num))
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.seat_table.setItem(index, 3, newItem)
        except Exception as e:
            print(e)


# 显示航班信息 窗体,用于增加和修改航班
class FlightInformation(QWidget, Ui_FlightInfomationForm):
    def __init__(self):
        super(FlightInformation, self).__init__()
        self.setupUi(self)

        self.c = Communicate()

    # 显示航班信息窗体
    def show_fli_info(self):
        self.show()
        # 清空之前输入的内容
        self.fli_num_lE.clear()
        self.dep_loc_lE.clear()
        self.arr_loc_lE.clear()
        self.dep_time_lE.clear()
        self.arr_time_lE.clear()
        self.eco_price_lE.clear()
        self.eco_order_lE.clear()
        self.eco_remain_lE.clear()
        self.busi_price_lE.clear()
        self.busi_order_lE.clear()
        self.busi_remain_lE.clear()
        self.frist_price_lE.clear()
        self.frist_order_lE.clear()
        self.frist_remain_lE.clear()

        self.add_fli_inf.clicked.connect(self.add_info)

    # 显示需要修改的航班数据
    def show_up_fli_info(self, fli_num, dep_loc, arr_loc, dep_time, arr_time):
        self.show()
        self.fli_num_lE.setText(fli_num)
        self.fli_num_lE.setEnabled(False)
        self.dep_loc_lE.setText(dep_loc)
        self.arr_loc_lE.setText(arr_loc)
        self.dep_time_lE.setText(dep_time)
        self.arr_time_lE.setText(arr_time)
        try:
            cursor.execute('exec flight_seat {0}'.format(fli_num))
            rows = cursor.fetchall()

            for index, row in enumerate(rows):
                if row.seat_level == '经济舱':
                    self.eco_price_lE.setText(str(row.price).split('.')[0])
                    self.eco_order_lE.setText(str(row.ordered_num))
                    self.eco_remain_lE.setText(str(row.remain_num))
                elif row.seat_level == '商务舱':
                    self.busi_price_lE.setText(str(row.price).split('.')[0])
                    self.busi_order_lE.setText(str(row.ordered_num))
                    self.busi_remain_lE.setText(str(row.remain_num))
                elif row.seat_level == '头等舱':
                    self.frist_price_lE.setText(str(row.price).split('.')[0])
                    self.frist_order_lE.setText(str(row.ordered_num))
                    self.frist_remain_lE.setText(str(row.remain_num))

        except Exception as e:
            print(e)
        self.add_fli_inf.clicked.connect(self.update_info)

    # 增加航班
    def add_info(self):
        try:
            fli_num = self.fli_num_lE.text()
            dep_loc = self.dep_loc_lE.text()
            arr_loc = self.arr_loc_lE.text()
            dep_time = self.dep_time_lE.text()
            arr_time = self.arr_time_lE.text()

            # 注意这条sql语句，两个时间需要打上单引号，让其被识别为字符串类型
            cursor.execute(r"exec insert_fli_info {0},{1},{2},'{3}','{4}'"
                           .format(fli_num, dep_loc, arr_loc, dep_time, arr_time))
            cursor.execute('exec insert_fli_seat_info {0},{1},{2},{3},{4}'
                           .format(fli_num, '经济舱', self.eco_price_lE.text(), self.eco_order_lE.text(),
                                   self.eco_remain_lE.text()))
            cursor.execute('exec insert_fli_seat_info {0},{1},{2},{3},{4}'
                           .format(fli_num, '商务舱', self.busi_price_lE.text(), self.busi_order_lE.text(),
                                   self.busi_remain_lE.text()))
            cursor.execute('exec insert_fli_seat_info {0},{1},{2},{3},{4}'
                           .format(fli_num, '头等舱', self.frist_price_lE.text(), self.frist_order_lE.text(),
                                   self.frist_remain_lE.text()))
            cnxn.commit()
        except Exception as e:
            print(e)

        QMessageBox.information(self, '', '增加完成')
        self.add_fli_inf.clicked.disconnect(self.add_info)
        self.c.close.emit()
        self.close()

    # 修改航班
    def update_info(self):
        try:
            fli_num = self.fli_num_lE.text()
            dep_loc = self.dep_loc_lE.text()
            arr_loc = self.arr_loc_lE.text()
            dep_time = self.dep_time_lE.text()
            arr_time = self.arr_time_lE.text()
            # 注意这条sql语句，两个时间需要打上单引号，让其被识别为字符串类型
            cursor.execute(r"exec update_fli_info {0},{1},{2},'{3}','{4}'"
                           .format(fli_num, dep_loc, arr_loc, dep_time, arr_time))
            cursor.execute('exec update_fli_seat_info {0},{1},{2},{3},{4}'
                           .format(fli_num, '经济舱', self.eco_price_lE.text(), self.eco_order_lE.text(),
                                   self.eco_remain_lE.text()))
            cursor.execute('exec update_fli_seat_info {0},{1},{2},{3},{4}'
                           .format(fli_num, '商务舱', self.busi_price_lE.text(), self.busi_order_lE.text(),
                                   self.busi_remain_lE.text()))
            cursor.execute('exec update_fli_seat_info {0},{1},{2},{3},{4}'
                           .format(fli_num, '头等舱', self.frist_price_lE.text(), self.frist_order_lE.text(),
                                   self.frist_remain_lE.text()))
            cnxn.commit()
        except Exception as e:
            print(e)
        QMessageBox.information(self, '', '修改完成')

        self.add_fli_inf.clicked.disconnect(self.update_info)
        self.c.close.emit()
        self.close()


# 订票管理
class TicketManage(QWidget, Ui_TicketManagerForm):
    def __init__(self):
        super(TicketManage, self).__init__()
        self.setupUi(self)

        self.ticketUpdate = TicketUpdate()

        # 重新设置列宽,使其自适应
        for i in range(1, 4):
            self.tickettable.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)
        self.ticketUpdate.refresh.connect(self.show_all_ticket)
        self.updateButton.clicked.connect(self.update_ticket)
        self.delButton.clicked.connect(self.delete_ticket)

    # 显示所有已订票但未取票的信息
    def show_all_ticket(self):
        try:
            cursor.execute(
                r'select name,flight_num,dep_loc,arr_loc,seat_level,ID_num from ticket_info order by name')
            rows = cursor.fetchall()
            self.tickettable.clearContents()

            # 将航班信息填入表格
            for index, row in enumerate(rows):
                newItem = QTableWidgetItem(row.name)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tickettable.setItem(index, 0, newItem)
                newItem = QTableWidgetItem(row.flight_num)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tickettable.setItem(index, 1, newItem)
                newItem = QTableWidgetItem(row.dep_loc)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tickettable.setItem(index, 2, newItem)
                newItem = QTableWidgetItem(row.arr_loc)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tickettable.setItem(index, 3, newItem)
                newItem = QTableWidgetItem(row.seat_level)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tickettable.setItem(index, 4, newItem)
                newItem = QTableWidgetItem(row.ID_num)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tickettable.setItem(index, 5, newItem)
        except Exception as e:
            print(e)

    # 更新订单信息
    def update_ticket(self):
        row = self.tickettable.currentRow()
        if row < 0:
            QMessageBox.warning(self, '警告', '请先选一行')
        else:
            self.ticketUpdate.show_update_ticket(self.tickettable.item(row, 1).text(),
                                                 self.tickettable.item(row, 5).text(),
                                                 self.tickettable.item(row, 0).text(),
                                                 self.tickettable.item(row, 4).text())

    # 删除订单信息
    def delete_ticket(self):

        try:
            row = self.tickettable.currentRow()
            if row < 0:
                QMessageBox.warning(self, '提示', '请选择要删除的订票信息')
            else:
                cursor.execute(
                    r"delete from ticket where flight_num='{0}' and ID_num='{1}'".format(
                        self.tickettable.item(row, 1).text(),
                        self.tickettable.item(row, 5).text()))
                cnxn.commit()
        except Exception as e:
            print(e)
        QMessageBox.information(self, '提示', '删除成功')
        self.show_all_ticket()


# 订票信息修改窗体
class TicketUpdate(QWidget, Ui_TicketInformationForm):
    refresh = QtCore.pyqtSignal()

    def __init__(self):
        super(TicketUpdate, self).__init__()
        self.setupUi(self)
        self.old_flight_num = 0
        self.old_seat_level = '经济舱'
        self.up_flight = Search()
        self.up_flight.flight_info.connect(self.fill_information)
        self.update_ticket_fli.clicked.connect(self.connect_flight)
        self.updateButton.clicked.connect(self.up_ticket_into_db)

    # 将要修改的航班信息填入窗体
    def show_update_ticket(self, flight_num, id_num, name, s_level):
        self.show()
        self.old_flight_num = flight_num
        self.old_seat_level = s_level
        self.name_IE.setText(name)
        self.ID_IE.setText(id_num)
        self.comboBox.setCurrentText(s_level.strip())
        try:
            cursor.execute(r"select * from flight where flight_num='{0}'".format(flight_num))
            fli_inf = cursor.fetchall()
            self.fli_num_IE.setText(fli_inf[0].flight_num)
            self.dep_loc_IE.setText(fli_inf[0].dep_loc)
            self.arr_loc_IE.setText(fli_inf[0].arr_loc)
            self.dep_time_IE.setText(fli_inf[0].dep_time.split(':')[0] + ':' + fli_inf[0].dep_time.split(':')[1])
            self.arr_time_IE.setText(fli_inf[0].arr_time.split(':')[0] + ':' + fli_inf[0].arr_time.split(':')[1])

        except Exception as e:
            print(e)

    # 连接选择航班的窗体
    def connect_flight(self):
        self.up_flight.ticket_inf_show_flight()

    # 将管理选择好的航班填入订单信息窗体
    def fill_information(self, flight_num, dep_loc, arr_loc, dep_time, arr_time):
        self.fli_num_IE.setText(flight_num)
        self.dep_loc_IE.setText(dep_loc)
        self.arr_loc_IE.setText(arr_loc)
        self.dep_time_IE.setText(dep_time)
        self.arr_time_IE.setText(arr_time)
        self.up_flight.close()

    # 将修改后的订单信息加入数据库
    def up_ticket_into_db(self):
        try:
            cursor.execute(r"exec update_ticketing '{0}','{1}','{2}','{3}','{4}'".format(self.old_flight_num,
                                                                                         self.fli_num_IE.text(),
                                                                                         self.ID_IE.text(),
                                                                                         self.old_seat_level,
                                                                                         self.comboBox.currentText()))
            cnxn.commit()
        except Exception as e:
            print(e)
        QMessageBox.information(self, '提示', '修改成功')
        self.refresh.emit()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWin()
    main.show()
    sys.exit(app.exec_())
