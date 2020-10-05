from Inform.Inform_DB_helper import InformDBHelper
from Inform.SlideButton import SwitchBtn
from PyQt5.QtWidgets import *
from Inform.setInform import SetInform


class InformList(QDialog):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.informdbhelper = InformDBHelper("./medicine_db.db", self.username)
        self.init_informlist()

    def init_informlist(self):
        self.setWindowTitle("医药服务助手： 提醒列表")
        self.resize(800, 600)
        self.init_layout()
        self.goback_pushbutton = QPushButton(self)
        self.goback_pushbutton.setText("返回")
        self.goback_pushbutton.clicked.connect(self.on_gobackpushbutton_clicked)
        self.goback_pushbutton.setGeometry(645, 545, 140, 40)

    def init_layout(self):
        self.Glayout = QGridLayout(self)

        self.init_label_list()
        result_list = self.informdbhelper.findALLInform()
        if result_list:
            for i, (name, remark, frequdency, hour, minute, id, status) in enumerate(result_list, start=1):
                self.setInfromation(hour, minute, frequdency, remark, status, id, i - 1, name)

    # 使用列表
    def init_label_list(self):
        self.label_time = []
        self.label_frequency = []
        self.label_remark = []
        self.slidebutton = []
        self.deleteButton = []
        self.editButton = []

    # 列表要从0开始
    def init_label(self, i, id, name, frequdency, remark):
        self.label_time.append(i)
        self.label_time[i] = QLabel(self)
        self.label_frequency.append(i)
        self.label_frequency[i] = QLabel(self)
        self.label_remark.append(i)
        self.label_remark[i] = QLabel(self)
        self.deleteButton.append(i)
        self.deleteButton[i] = QPushButton(self)
        self.deleteButton[i].setStyleSheet("QPushButton{border-image: url(./images/delete.jpg)}")
        self.deleteButton[i].setMaximumSize(30, 20)
        self.deleteButton[i].clicked.connect(lambda: self.deleteInform(id))
        self.editButton.append(i)
        self.editButton[i] = QPushButton(self)
        self.editButton[i].setStyleSheet("QPushButton{border-image: url(./images/edit.jpg)}")
        self.editButton[i].setMaximumSize(25, 20)
        self.editButton[i].clicked.connect(lambda: self.editInform(name, frequdency, remark, id))
        self.slidebutton.append(i)
        self.slidebutton[i] = SwitchBtn(self)
        self.slidebutton[i].setMaximumSize(50, 20)
        self.slidebutton[i].setMinimumSize(50, 20)
        self.slidebutton[i].checkedChanged.connect(lambda: self.setState(self.slidebutton[i].checked, id))

    def setInfromation(self, hour, minute, frequdency, remarks, status, id, i, name):
        self.init_label(i, id, name, frequdency, remarks)
        self.Glayout.addWidget(self.label_time[i], 2 * i, 0, 1, 1)
        self.Glayout.addWidget(self.label_frequency[i], 2 * i + 1, 0, 1, 1)
        self.Glayout.addWidget(self.label_remark[i], 2 * i + 1, 1, 1, 1)
        self.Glayout.addWidget(self.slidebutton[i], 2 * i, 2, 1, 2)
        self.Glayout.addWidget(self.deleteButton[i], 2 * i + 1, 2, 1, 1)
        self.Glayout.addWidget(self.editButton[i], 2 * i + 1, 3, 1, 1)
        self.setText(i, hour, minute, frequdency, remarks, name)
        self.Glayout.setVerticalSpacing(10)
        self.Glayout.setHorizontalSpacing(5)
        self.Glayout.setContentsMargins(180, 30, 180, 200)

        if status == 1:
            self.slidebutton[i].checked = False
        else:
            self.slidebutton[i].checked = True

    # 设置文本
    def setText(self, i, hour, minute, frequdency, remarks, name):
        self.label_frequency[i].setText(str(frequdency) + "次")
        self.label_time[i].setText(str(hour) + ":" + str(minute))
        self.label_remark[i].setText(name + remarks)

    # 设置状态
    def setState(self, checked, id):
        if checked:
            self.informdbhelper.setStatus(id, 0)
        else:
            self.informdbhelper.setStatus(id, 1)

    # 删除
    def deleteInform(self, id):
        self.informdbhelper.delInform(id)
        from Inform.InformIndex import InformIndex
        dialog = InformIndex(self.username)
        self.close()
        dialog.exec()

    # 编辑
    def editInform(self, name, frequdency, remark, id):
        dialog = SetInform(self.username, name, frequdency, remark, id)
        self.close()
        dialog.exec()

    # 返回按钮
    def on_gobackpushbutton_clicked(self):
        from Inform.InformIndex import InformIndex
        dialog = InformIndex(self.username)
        self.close()
        dialog.exec()
