from PyQt5 import QtCore, QtGui, QtWidgets


class JieGuo(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(969, 650)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 90, 141, 71))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(200, 140, 321, 31))
        self.label_2.setObjectName("label_2")
        self.fanhuidatishouye = QtWidgets.QPushButton(Form)
        self.fanhuidatishouye.setGeometry(QtCore.QRect(190, 260, 141, 71))
        self.fanhuidatishouye.setObjectName("fanhuidatishouye")
        self.fanhuizhujiemian = QtWidgets.QPushButton(Form)
        self.fanhuizhujiemian.setGeometry(QtCore.QRect(480, 260, 141, 71))
        self.fanhuizhujiemian.setObjectName("fanhuizhujiemian")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(350, 90, 251, 31))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "医药知识问答"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">点击下列按钮返回</span></p></body></html>"))
        self.label_3.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">答题结束</span></p></body></html>"))
        self.fanhuidatishouye.setText(_translate("Form", "返回答题首页"))
        self.fanhuizhujiemian.setText(_translate("Form", "返回主界面"))
