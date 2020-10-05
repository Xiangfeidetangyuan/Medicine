
from PyQt5 import QtCore, QtGui, QtWidgets


class q1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(987, 676)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(400, 80, 151, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 160, 691, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(140, 220, 41, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(190, 220, 441, 21))
        self.label_4.setObjectName("label_4")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(140, 270, 231, 19))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(140, 300, 115, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(140, 330, 115, 19))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Form)
        self.radioButton_4.setGeometry(QtCore.QRect(140, 360, 115, 19))
        self.radioButton_4.setObjectName("radioButton_4")
        self.xiayiti = QtWidgets.QPushButton(Form)
        self.xiayiti.setGeometry(QtCore.QRect(320, 410, 201, 51))
        self.xiayiti.setObjectName("xiayiti")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(140, 480, 651, 81))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "医药知识问答"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">回答问题</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">亲爱的用户：感谢您使用医药知识百度问答，请回答下面的问题：</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Q1：</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">下面哪一个不是药物的名称？（单选题）</span></p></body></html>"))
        self.radioButton.setText(_translate("Form", "A.阿司匹林"))
        self.radioButton_2.setText(_translate("Form", "B.板蓝根"))
        self.radioButton_3.setText(_translate("Form", "C.福尔马林"))
        self.radioButton_4.setText(_translate("Form", "D.甲烷"))
        self.xiayiti.setText(_translate("Form", "下一题"))

