from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QAbstractItemView
from PyQt5.QtCore import Qt
from department import departmentIndex
from department import departmentSearch
from department import departmentSearchResult
from department import departmentLetter
from department import departmentList
import sqlite3

uname = ''


####################### 科室首页界面#########################
class departmentIndex__Dialog(departmentIndex.Ui_Dialog, QDialog):
    def __init__(self, username):
        super(departmentIndex__Dialog, self).__init__()
        self.setupUi(self)
        self.username = username
        global uname
        uname = username
        self.pushButton_3.clicked.connect(self.on_exit_push_button_clicked)
        self.pushButton_2.clicked.connect(self.openletter_clicked)
        self.pushButton.clicked.connect(self.opensearch_clicked)
        self.setWindowIcon(QIcon("./images/icon.png"))

    def on_exit_push_button_clicked(self):
        from Medicine.main_dialog import MainDialog
        dialog = MainDialog(self.username)
        self.close()
        dialog.exec()

    # 按钮-症状查询
    def opensearch_clicked(self):
        dialog = departmentSearch__Dialog()
        self.close()
        dialog.exec()

    # 字母选择
    def openletter_clicked(self):
        dialog = departmentLetter__Dialog()
        self.close()
        dialog.exec()


####################### 科室症状搜索结果界面#########################
class departmentSearchResult__Dialog(departmentSearchResult.Ui_Dialog, QDialog):
    def __init__(self, item):
        super(departmentSearchResult__Dialog, self).__init__()
        self.item = item
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.on_exit_push_button_clicked)
        self.pushButton_4.clicked.connect(self.rerearch_button_clicked)
        self.lineEdit.setText(self.item)
        self.init_tableview()
        self.setWindowIcon(QIcon("./images/icon.png"))

    # 初始化显示表格
    def init_tableview(self):
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["序号", "科室名称"])
        self.tableWidget.setColumnWidth(0, 60)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSortingEnabled(True)
        self.tableview()
        self.tableWidget.itemDoubleClicked.connect(self.show_select_item)
        self.tableWidget.setToolTip("双击查看科室详情")

    # 双击表格-弹出详情列表
    def show_select_item(self):
        item_name = self.tableWidget.selectedItems()[1].text()
        dialog = departmentList__Dialog(item_name)
        self.close()
        dialog.exec()

    # 初始化表格数据
    def tableview(self):
        # 连接数据库，获取数据
        conn = sqlite3.connect("./medicine_db.db")
        # 创建一个游标 curson
        cursor = conn.cursor()
        sql = "select * from zhengzhuang"
        cursor.execute(sql)
        values = cursor.fetchall()
        # 关闭游标：
        cursor.close()
        # 关闭连接
        conn.close()
        result = set()
        # 按照条件搜索数据
        for v in values:
            if self.item in v[0]:
                result.add(v[1])
        # 显示数据
        for num, item in enumerate(result):
            self.add_item(str(num + 1), item)

    # 逐行显示数据
    def add_item(self, item_id, item_name):
        row = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(row + 1)
        self.tableWidget.setItem(row, 0, QTableWidgetItem(item_id))
        self.tableWidget.item(row, 0).setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(row, 1, QTableWidgetItem(item_name))
        self.tableWidget.item(row, 1).setTextAlignment(Qt.AlignCenter)

    # 返回按钮
    def on_exit_push_button_clicked(self):
        from Medicine.main_dialog import MainDialog
        dialog = MainDialog(uname)
        self.close()
        dialog.exec()

    # 重新选择按钮
    def rerearch_button_clicked(self):
        dialog = departmentSearch__Dialog()
        self.close()
        dialog.exec()


####################### 科室症状搜索界面#########################
class departmentSearch__Dialog(departmentSearch.Ui_Dialog, QDialog):
    def __init__(self):
        super(departmentSearch__Dialog, self).__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.on_exit_push_button_clicked)
        self.pushButton.clicked.connect(self.search_button_clicked)
        self.setWindowIcon(QIcon("./images/icon.png"))

    # 查询按钮
    def search_button_clicked(self):
        print(self.lineEdit.text())
        dialog = departmentSearchResult__Dialog(self.lineEdit.text())
        self.close()
        dialog.exec()

    # 返回按钮
    def on_exit_push_button_clicked(self):
        dialog = departmentIndex__Dialog(uname)
        self.close()
        dialog.exec()


####################### 科室详情界面#########################
class departmentList__Dialog(departmentList.Ui_Dialog, QDialog):
    def __init__(self, keshiname):
        self.keshiname = keshiname
        super(departmentList__Dialog, self).__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.on_exit_push_button_clicked)
        self.lineEdit.setText(self.keshiname)
        self.init_tableview()
        self.setWindowIcon(QIcon("./images/icon.png"))

    # 初始化表格
    def init_tableview(self):
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["病症", "病状描述"])
        self.tableWidget.setColumnWidth(1, 60)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSortingEnabled(True)
        self.tableview()
        # self.tableWidget.setToolTip("双击查看科室详情")

    # 数据显示
    def tableview(self):
        conn = sqlite3.connect("./medicine_db.db")
        # 创建一个游标 curson
        cursor = conn.cursor()
        sql = "select * from zhengzhuang"
        cursor.execute(sql)
        values = cursor.fetchall()
        # 关闭游标：
        cursor.close()
        # 关闭连接
        conn.close()
        result = []
        # 按照条件 - 选择数据
        for v in values:
            if self.keshiname in v[1]:
                result.append([v[0], v[2]])
        # 显示数据
        for num, item in enumerate(result):
            self.add_item(item[0], item[1])

    # 逐条显示数据
    def add_item(self, item_id, item_name):
        row = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(row + 1)
        self.tableWidget.setItem(row, 0, QTableWidgetItem(item_id))
        self.tableWidget.item(row, 0).setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(row, 1, QTableWidgetItem(item_name))
        self.tableWidget.item(row, 1).setTextAlignment(Qt.AlignCenter)

    # 返回按钮
    def on_exit_push_button_clicked(self):
        dialog = departmentIndex__Dialog(uname)
        self.close()
        dialog.exec()


####################### 科室字母查询界面#########################
class departmentLetter__Dialog(departmentLetter.Ui_Dialog, QDialog):
    def __init__(self):
        super(departmentLetter__Dialog, self).__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.on_exit_push_button_clicked)
        self.setWindowIcon(QIcon("./images/icon.png"))
        # 字母按钮列表
        self.pushButtonls = [self.pushButton_A,
                             self.pushButton_B,
                             self.pushButton_C,
                             self.pushButton_D,
                             self.pushButton_E,
                             self.pushButton_F,
                             self.pushButton_G,
                             self.pushButton_H,
                             self.pushButton_I,
                             self.pushButton_J,
                             self.pushButton_K,
                             self.pushButton_L,
                             self.pushButton_M,
                             self.pushButton_N,
                             self.pushButton_O,
                             self.pushButton_P,
                             self.pushButton_Q,
                             self.pushButton_R,
                             self.pushButton_S,
                             self.pushButton_T,
                             self.pushButton_U,
                             self.pushButton_V,
                             self.pushButton_W,
                             self.pushButton_X,
                             self.pushButton_Y,
                             self.pushButton_Z]
        # 字母按钮列表的槽函数
        self.pushButton_A.clicked.connect(self.button_A_click)
        self.pushButton_B.clicked.connect(self.button_B_click)
        self.pushButton_C.clicked.connect(self.button_C_click)
        self.pushButton_D.clicked.connect(self.button_D_click)
        self.pushButton_E.clicked.connect(self.button_E_click)
        self.pushButton_F.clicked.connect(self.button_F_click)
        self.pushButton_G.clicked.connect(self.button_G_click)
        self.pushButton_H.clicked.connect(self.button_H_click)
        self.pushButton_I.clicked.connect(self.button_I_click)
        self.pushButton_J.clicked.connect(self.button_J_click)
        self.pushButton_K.clicked.connect(self.button_K_click)
        self.pushButton_L.clicked.connect(self.button_L_click)
        self.pushButton_M.clicked.connect(self.button_M_click)
        self.pushButton_N.clicked.connect(self.button_M_click)
        self.pushButton_O.clicked.connect(self.button_N_click)
        self.pushButton_P.clicked.connect(self.button_O_click)
        self.pushButton_Q.clicked.connect(self.button_P_click)
        self.pushButton_R.clicked.connect(self.button_R_click)
        self.pushButton_S.clicked.connect(self.button_S_click)
        self.pushButton_T.clicked.connect(self.button_T_click)
        self.pushButton_U.clicked.connect(self.button_U_click)
        self.pushButton_V.clicked.connect(self.button_V_click)
        self.pushButton_W.clicked.connect(self.button_W_click)
        self.pushButton_X.clicked.connect(self.button_X_click)
        self.pushButton_Y.clicked.connect(self.button_Y_click)
        self.pushButton_Z.clicked.connect(self.button_Z_click)

        self.initbutton()
        self.tiaojian = ''
        self.tableWidget.itemDoubleClicked.connect(self.show_select_item)
        self.init_tableview()

    # 字母按钮的槽函数----具体功能为更新数据，重新显示数据
    def button_A_click(self):
        self.tiaojian = 'A';
        self.init_tableview()

    def button_B_click(self):
        self.tiaojian = 'B';
        self.init_tableview()

    def button_C_click(self):
        self.tiaojian = 'C';
        self.init_tableview()

    def button_D_click(self):
        self.tiaojian = 'D';
        self.init_tableview()

    def button_E_click(self):
        self.tiaojian = 'E';
        self.init_tableview()

    def button_F_click(self):
        self.tiaojian = 'F';
        self.init_tableview()

    def button_G_click(self):
        self.tiaojian = 'G';
        self.init_tableview()

    def button_H_click(self):
        self.tiaojian = 'H';
        self.init_tableview()

    def button_I_click(self):
        self.tiaojian = 'I';
        self.init_tableview()

    def button_J_click(self):
        self.tiaojian = 'J';
        self.init_tableview()

    def button_K_click(self):
        self.tiaojian = 'K';
        self.init_tableview()

    def button_L_click(self):
        self.tiaojian = 'L';
        self.init_tableview()

    def button_M_click(self):
        self.tiaojian = 'M';
        self.init_tableview()

    def button_N_click(self):
        self.tiaojian = 'N';
        self.init_tableview()

    def button_O_click(self):
        self.tiaojian = 'O';
        self.init_tableview()

    def button_P_click(self):
        self.tiaojian = 'P';
        self.init_tableview()

    def button_Q_click(self):
        self.tiaojian = 'Q';
        self.init_tableview()

    def button_R_click(self):
        self.tiaojian = 'R';
        self.init_tableview()

    def button_S_click(self):
        self.tiaojian = 'S';
        self.init_tableview()

    def button_T_click(self):
        self.tiaojian = 'T';
        self.init_tableview()

    def button_U_click(self):
        self.tiaojian = 'U';
        self.init_tableview()

    def button_V_click(self):
        self.tiaojian = 'V';
        self.init_tableview()

    def button_W_click(self):
        self.tiaojian = 'W';
        self.init_tableview()

    def button_X_click(self):
        self.tiaojian = 'X';
        self.init_tableview()

    def button_Y_click(self):
        self.tiaojian = 'Y'
        self.init_tableview()

    def button_Z_click(self):
        self.tiaojian = 'Z'
        self.init_tableview()

    # 初始化字母按钮的状态-部分按钮为不能用状态
    def initbutton(self):
        # 所有按钮均不使能
        for item in self.pushButtonls:
            item.setEnabled(False)

        conn = sqlite3.connect("./medicine_db.db")
        # 创建一个游标 curson
        cursor = conn.cursor()
        sql = "select * from keshi"
        cursor.execute(sql)
        values = cursor.fetchall()
        # 关闭游标：
        cursor.close()
        # 关闭连接
        conn.close()

        result = set()
        # 获取数据
        for v in values:
            result.add(v[1].upper())
        # 更新按钮状体
        for item in result:
            item = ord(item) - ord('A')
            print(item)
            self.pushButtonls[item].setEnabled(True)

    # 初始化表格
    def init_tableview(self):
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["序号", "科室名称"])
        self.tableWidget.setColumnWidth(0, 60)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.clearContents()
        self.tableview()

        self.tableWidget.setToolTip("双击查看科室详情")

    # 表格数据-双击进入详情页
    def show_select_item(self):
        item_name = self.tableWidget.selectedItems()[1].text()
        dialog = departmentList__Dialog(item_name)
        self.close()
        dialog.exec()

    # 初始化表格数据
    def tableview(self):
        conn = sqlite3.connect("./medicine_db.db")
        # 创建一个游标 curson
        cursor = conn.cursor()
        sql = "select * from keshi"
        cursor.execute(sql)
        values = cursor.fetchall()
        # 关闭游标：
        cursor.close()
        # 关闭连接
        conn.close()

        result = []
        # 按照字母条件-选择数据
        for v in values:
            if self.tiaojian in v[1]:
                result.append(v[0])
        # 显示数据
        for num, item in enumerate(result):
            self.add_item(num, str(num + 1), item)

    # 逐条显示数据
    def add_item(self, num, item_id, item_name):
        row = self.tableWidget.rowCount()
        row = num
        self.tableWidget.setRowCount(row + 1)
        self.tableWidget.setItem(row, 0, QTableWidgetItem(item_id))
        self.tableWidget.item(row, 0).setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(row, 1, QTableWidgetItem(item_name))
        self.tableWidget.item(row, 1).setTextAlignment(Qt.AlignCenter)

    # 返回按钮
    def on_exit_push_button_clicked(self):
        dialog = departmentIndex__Dialog(uname)
        self.close()
        dialog.exec()
