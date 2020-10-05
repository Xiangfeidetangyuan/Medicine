from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QDialog, QPushButton
from Inform.Inform_DB_helper import Inform, InformDBHelper


class SetInform(QDialog):
    def __init__(self, username, name, frequdency, remark, id):
        super().__init__()
        self.username = username
        self.resize(800, 600)
        self.setWindowTitle("医药服务助手：设置提醒")
        self.setWindowIcon(QIcon("./images/icon.png"))

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(300, 130, 100, 30)

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(300, 160, 100, 30)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(300, 190, 100, 30)
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(300, 230, 100, 30)
        self.label.setText("时间：")
        self.label_2.setText("重复：")
        self.label_3.setText("药品名：")
        self.label_4.setText("备注：")

        self.timeEdit = QtWidgets.QTimeEdit(self)
        self.timeEdit.setGeometry(360, 130, 118, 22)
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit.setTime(QTime.currentTime())

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setText("设置")
        self.pushButton.setGeometry(340, 300, 100, 30)
        self.pushButton.clicked.connect(self.setInform)

        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(360, 160, 111, 22)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "1次")
        self.comboBox.setItemText(1, "2次")
        self.comboBox.setItemText(2, "3次")
        self.comboBox.setItemText(3, "4次")
        self.comboBox.setItemText(4, "5次")
        self.comboBox.setItemText(5, "6次")
        self.comboBox.setItemText(6, "7次")
        self.lineEdit_MedicineName = QtWidgets.QLineEdit(self)
        self.lineEdit_MedicineName.setGeometry(360, 200, 113, 20)
        self.lineEdit_MedicineName.setObjectName("lineEdit_MedicineName")
        self.lineEdit_Remark = QtWidgets.QLineEdit(self)
        self.lineEdit_Remark.setGeometry(360, 240, 113, 20)
        self.lineEdit_Remark.setObjectName("lineEdit_Remark")
        self.goback_pushbutton = QPushButton(self)
        self.goback_pushbutton.setText("返回")
        self.goback_pushbutton.clicked.connect(self.on_gobackpushbutton_clicked)
        self.goback_pushbutton.setGeometry(645, 545, 140, 40)

        self.informhelper = InformDBHelper("./medicine_db.db", self.username)
        self.id = id

        if name:
            self.setText(name, frequdency, remark)

    # 设置展示文本
    def setText(self, name, frequdency, remark):
        self.lineEdit_MedicineName.setText(name)
        self.lineEdit_Remark.setText(remark)
        self.comboBox.setCurrentIndex(frequdency - 1)

    # 设置提醒
    def setInform(self):
        # 药品名判空处理
        if self.lineEdit_MedicineName.text() == "":
            QMessageBox.warning(self, "warning", "药名不能为空")
        else:
            # 存入数据库
            informdemo = Inform(self.lineEdit_MedicineName.text(), self.lineEdit_Remark.text(),
                                self.comboBox.currentIndex() + 1,
                                self.timeEdit.time().hour(), self.timeEdit.time().minute(), 1)
            self.informhelper.add(informdemo)
            if self.id:
                self.informhelper.delInform(self.id)
            from Inform.InformIndex import InformIndex
            dialog = InformIndex(self.username)
            self.close()
            dialog.exec()

    # 返回按钮
    def on_gobackpushbutton_clicked(self):
        from Inform.InformIndex import InformIndex
        dialog = InformIndex(self.username)
        self.close()
        dialog.exec()
