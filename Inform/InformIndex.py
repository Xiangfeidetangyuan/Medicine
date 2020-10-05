from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QTime
from Inform.InformList import InformList
from Inform.setInform import SetInform


class InformIndex(QDialog):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.setInform_pushButton = QtWidgets.QPushButton(self)
        self.InformList_pushButton = QtWidgets.QPushButton(self)
        self.GoBack_pushButton = QtWidgets.QPushButton(self)
        self.init_informindex()
        self.init_buttons()
        self.setWindowIcon(QIcon("./images/icon.png"))

    def init_informindex(self):

        self.setWindowTitle("医药服务助手： 提醒首页")
        self.resize(800, 600)
        self.setWindowFlags(Qt.WindowCloseButtonHint)

    def init_buttons(self):
        self.init_setInform_pushButton()
        self.init_InformList_pushButton()
        self.init_GoBack_pushButton()

    def init_setInform_pushButton(self):
        self.setInform_pushButton.setGeometry(350, 180, 140, 40)
        self.setInform_pushButton.clicked.connect(self.on__setInform_pushButton_clicked)
        self.setInform_pushButton.setText("设置提醒")

    def init_InformList_pushButton(self):
        self.InformList_pushButton.setGeometry(350, 240, 140, 40)
        self.InformList_pushButton.clicked.connect(self.on_InformList_pushButton_clicked)
        self.InformList_pushButton.setText("提醒列表")

    def init_GoBack_pushButton(self):
        self.GoBack_pushButton.setGeometry(645, 545, 140, 40)
        self.GoBack_pushButton.setText("返回")
        self.GoBack_pushButton.clicked.connect(self.on_GoBack_pushButton_clicked)

    def on__setInform_pushButton_clicked(self):
        dialog = SetInform(self.username, None, None, None, None)
        self.close()
        dialog.exec()

    def on_InformList_pushButton_clicked(self):
        dialog = InformList(self.username)
        self.close()
        dialog.exec()

    # 返回按钮
    def on_GoBack_pushButton_clicked(self):
        from main_dialog import MainDialog
        dialog = MainDialog(self.username)
        self.close()
        dialog.exec()

