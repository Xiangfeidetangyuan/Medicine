
from PyQt5 import QtCore, QtGui, QtWidgets


class Sub(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(961, 629)
        self.fanhuishouye = QtWidgets.QPushButton(Dialog)
        self.fanhuishouye.setGeometry(QtCore.QRect(120, 340, 171, 71))
        self.fanhuishouye.setObjectName("fanhuishouye")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 90, 141, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(200, 100, 701, 141))
        self.label_2.setObjectName("label_2")
        self.fan = QtWidgets.QPushButton(Dialog)
        self.fan.setGeometry(QtCore.QRect(780, 530, 141, 61))
        self.fan.setObjectName("fan")
        self.kaishidati = QtWidgets.QPushButton(Dialog)
        self.kaishidati.setGeometry(QtCore.QRect(380, 340, 171, 61))
        self.kaishidati.setObjectName("kaishidati")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "医药知识问答"))
        self.fanhuishouye.setText(_translate("Dialog", "返回答题首页"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">规则说明：</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">本次答题全为单项选择题，选择正确的一个，选择正确直接跳转到下一题</span></p><p><span style=\" font-size:12pt; font-weight:600;\">确认后可回答下一个问题，</span></p><p><span style=\" font-size:12pt; font-weight:600;\">回答完所有问题后点击提交即可查看答题结果，</span></p><p><span style=\" font-size:12pt; font-weight:600;\">快来展示一下你的知识储备吧</span></p></body></html>"))
        self.fan.setText(_translate("Dialog", "返回"))
        self.kaishidati.setText(_translate("Dialog", "开始答题"))
