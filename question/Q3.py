from PyQt5 import QtCore, QtGui, QtWidgets


class q3(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(960, 687)
        self.shangyiti2 = QtWidgets.QPushButton(Form)
        self.shangyiti2.setGeometry(QtCore.QRect(200, 450, 171, 51))
        self.shangyiti2.setObjectName("shangyiti2")
        self.radioButton_4 = QtWidgets.QRadioButton(Form)
        self.radioButton_4.setGeometry(QtCore.QRect(160, 380, 115, 19))
        self.radioButton_4.setObjectName("radioButton_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(150, 180, 691, 41))
        self.label_2.setObjectName("label_2")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(160, 320, 115, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(160, 350, 115, 19))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(420, 100, 151, 51))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(210, 240, 441, 21))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(160, 240, 41, 31))
        self.label_3.setObjectName("label_3")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(160, 290, 231, 19))
        self.radioButton.setObjectName("radioButton")
        self.tijiao = QtWidgets.QPushButton(Form)
        self.tijiao.setGeometry(QtCore.QRect(470, 450, 141, 51))
        self.tijiao.setObjectName("tijiao")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(140, 480, 651, 81))
        self.label_5.setObjectName("label_5")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "医药知识问答"))
        self.shangyiti2.setText(_translate("Form", "上一题"))
        self.radioButton_4.setText(_translate("Form", "D.甲烷"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">亲爱的用户：感谢您使用医药知识百度问答，请回答下面的问题：</span></p></body></html>"))
        self.radioButton_2.setText(_translate("Form", "B.板蓝根"))
        self.radioButton_3.setText(_translate("Form", "C.福尔马林"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">回答问题</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">下面哪一个是治疗流感的药物？（单选题）</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "4."))
        self.radioButton.setText(_translate("Form", "A.阿司匹林"))
        self.tijiao.setText(_translate("Form", "提交"))
