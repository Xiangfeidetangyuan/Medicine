from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog

from Inform.Inform_DB_helper import InformDBHelper
from Inform.mails import SendMails


class InformMessageBox(QDialog):

    def __init__(self, name, remarks, username):
        super().__init__()

        self.username = username
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(70, 60, 54, 12))

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 54, 12))
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(120, 140, 75, 23))
        self.lineEdit_MedicineNme = QtWidgets.QLineEdit(self)
        self.lineEdit_MedicineNme.setGeometry(QtCore.QRect(120, 60, 113, 20))
        self.lineEdit_MedicineNme.setReadOnly(True)

        self.lineEdit_Remark = QtWidgets.QLineEdit(self)
        self.lineEdit_Remark.setGeometry(QtCore.QRect(120, 90, 113, 20))
        self.lineEdit_Remark.setObjectName("lineEdit_Remark")
        self.lineEdit_Remark.setReadOnly(True)
        self.init_Ui()
        self.setInfromation(name, remarks)

        print("开始计时")
        self.qtimer = QTimer()
        self.qtimer.singleShot(5000, lambda: self.sendEmail(name, remarks))

    def init_Ui(self):
        self.setWindowTitle("用药提醒")
        self.setWindowIcon(QIcon("./images/icon.png"))
        self.resize(400, 300)
        self.label.setText("药品名：")
        self.label_2.setText("备注：")
        self.pushButton.setText("我已知道")
        self.pushButton.clicked.connect(self.onSure_push_button_clicked)

    def setInfromation(self, name, remarks):
        self.lineEdit_MedicineNme.setText(name)
        self.lineEdit_Remark.setText(remarks)

    def onSure_push_button_clicked(self):
        self.close()

    def getUserEmail(self):
        self.informdbhelper = InformDBHelper("./medicine_db.db", self.username)
        print("get")
        return self.informdbhelper.getEmail()

    # 发送邮件
    def sendEmail(self, name, remarks):
        print("send")
        context = "亲爱的用户" + str(self.username) + "，您好。药品：" + name + remarks
        s = SendMails("smtp.126.com", "hitwh_jzy@126.com", "CDDEHUGOTSNVOXQV", self.getUserEmail(), "医药服务助手：用药提醒",
                      context)
        if s.sendE():
            print('提示', '发送成功！')
        else:
            print('提示', '发送失败！')
