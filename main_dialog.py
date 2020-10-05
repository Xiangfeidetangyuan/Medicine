from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QDialog, QPushButton, QLabel
from Inform.InformIndex import InformIndex
from Inform.InformMessageBox import InformMessageBox
from Inform.Inform_DB_helper import InformDBHelper
from interaction.medicine_list import MedicineListDialog
from department import department
from question.dati import MainWin
from usercenter.userCenter import UserCenter


class MainDialog(QDialog):
    def __init__(self, username):
        super().__init__()
        self.__username = username
        self.__medicine_interaction_push_button = QPushButton(self)
        self.__user_center_push_button = QPushButton(self)
        self.__question_center_push_button = QPushButton(self)
        self.__department_search_push_button = QPushButton(self)
        self.__alarm_clock_push_button = QPushButton(self)
        self.__exit_push_button = QPushButton(self)
        self.init_main_dialog()
        self.init_buttons()
        self.__welcome_label = QLabel(self)
        self.init_labels()
        self._dialog = ""
        self.informdbhelper = InformDBHelper("./medicine_db.db", self.__username)
        self.init_Inform()#计时器

    def init_Inform(self):
       # print("初始化提醒")
        self.qtimer = QTimer()
        self.qtimer.start(15000)
        self.qtimer.timeout.connect(self.msgshow)

    # 从数据库读取 设置闹钟
    def msgshow(self):
        #print("主界面的用户名是"+self.__username)
        result_list = self.informdbhelper.findALLInform()
        #print(result_list)
        #print(QTime.currentTime().minute())
        if result_list:
            for i, (name, remark, frequdency, hour, minute, id, status) in enumerate(result_list, start=1):
                if frequdency > 0 and status == 1:
                    # 设置时间间隔
                    #print("第%d个闹钟设置……", i)
                    if QTime.currentTime().hour() == hour and QTime.currentTime().minute() == minute:
                      #  print("提醒……")
                        messagebox = InformMessageBox(name, remark, self.__username)
                        self.informdbhelper.setFrequdency(id, int(frequdency - 1))
                        messagebox.exec()



    def init_labels(self):
        self.__welcome_label.setText("欢迎：\n" + str(self.__username))
        self.__welcome_label.setGeometry(340, 100, 120, 40)
        self.__welcome_label.setAlignment(Qt.AlignCenter)
        self.__welcome_label.setFont(QFont("Roman times", 12, QFont.Bold))

    def init_main_dialog(self):
        self.resize(800, 600)
        self.setWindowTitle("医药服务助手：首页")
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowIcon(QIcon("./images/icon.png"))

    def init_buttons(self):
        self.init_exit_push_button()
        self.init_medicine_interaction_push_button()
        self.init_user_center_push_button()
        self.init_alarm_clock_push_button()
        self.init_department_search_push_button()
        self.init_question_center_push_button()

    def init_user_center_push_button(self):
        self.__user_center_push_button.setGeometry(340, 240, 120, 120)
        self.__user_center_push_button.clicked.connect(self.on_user_center_push_button_clicked)
        self.__user_center_push_button.setText("个人中心")

    def init_medicine_interaction_push_button(self):
        self.__medicine_interaction_push_button.setGeometry(560, 60, 180, 180)
        self.__medicine_interaction_push_button.clicked.connect(self.on_medicine_interaction_push_button_clicked)
        self.__medicine_interaction_push_button.setText("禁忌查询")

    def init_exit_push_button(self):
        self.__exit_push_button.setGeometry(645, 545, 140, 40)
        self.__exit_push_button.clicked.connect(self.on_exit_push_button_clicked)
        self.__exit_push_button.setText("退出登录")

    def init_alarm_clock_push_button(self):
        self.__alarm_clock_push_button.setGeometry(60, 60, 180, 180)
        self.__alarm_clock_push_button.clicked.connect(self.on_alarm_clock_push_button_clicked)
        self.__alarm_clock_push_button.setText("服药提醒")

    def init_question_center_push_button(self):
        self.__question_center_push_button.setGeometry(560, 360, 180, 180)
        self.__question_center_push_button.clicked.connect(self.on_question_center_push_button_clicked)
        self.__question_center_push_button.setText("医药百科问答")

    def init_department_search_push_button(self):
        self.__department_search_push_button.setGeometry(60, 360, 180, 180)
        self.__department_search_push_button.clicked.connect(self.on_department_search_push_button_clicked)
        self.__department_search_push_button.setText("科室查询")

    def on_exit_push_button_clicked(self):
        #print("退出登录将文件导入项目后，取消下面的注释，根据pycharm的提示，导入模块的主页类就OK了")
        from Medicine.Login.login import Login
        self._dialog = Login()
        self.qtimer.stop()
        self.close()
        self._dialog.ui.exec()

    def on_medicine_interaction_push_button_clicked(self):
        # 创建相互作用窗口
        dialog = MedicineListDialog(self.__username)
        # 关闭本窗口
        self.close()
        # 打开新窗口
        dialog.exec()

    def on_user_center_push_button_clicked(self):
        self._dialog = UserCenter(self.__username)
        self.close()
        self._dialog.ui.exec()

    def on_department_search_push_button_clicked(self):
        dialog = department.departmentIndex__Dialog(self.__username)
        self.close()
        dialog.exec()

    def on_alarm_clock_push_button_clicked(self):
        dialog = InformIndex(self.__username)
        self.close()
        dialog.exec()

    def on_question_center_push_button_clicked(self):
        myWin = MainWin(self.__username)  # 答题首页
        self.close()
        myWin.exec()
