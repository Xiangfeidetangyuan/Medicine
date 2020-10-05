
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWin(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(805, 635)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(600, 500, 161, 71))
        self.pushButton.setObjectName("pushButton")
        self.guizepushbutton = QtWidgets.QPushButton(Dialog)
        self.guizepushbutton.setGeometry(QtCore.QRect(220, 180, 151, 81))
        self.guizepushbutton.setObjectName("guizepushbutton")
        self.datipushbutton = QtWidgets.QPushButton(Dialog)
        self.datipushbutton.setGeometry(QtCore.QRect(220, 290, 151, 81))
        self.datipushbutton.setObjectName("datipushbutton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 80, 261, 61))
        self.label.setIndent(-1)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "医药知识问答"))
        self.pushButton.setText(_translate("Dialog", "返回"))
        self.guizepushbutton.setText(_translate("Dialog", "答题规则"))
        self.datipushbutton.setText(_translate("Dialog", "进入答题"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">医药百科知识问答</span></p></body></html>"))
