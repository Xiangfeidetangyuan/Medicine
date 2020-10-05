from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(800, 600)
        self.pushButton_3 = QtWidgets.QPushButton(dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(645, 545, 100, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(dialog)
        self.lineEdit.setGeometry(QtCore.QRect(280, 120, 200, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(230, 120, 50, 20))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(dialog)
        self.tableWidget.setGeometry(QtCore.QRect(120, 160, 521, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "科室详细信息"))
        self.pushButton_3.setText(_translate("dialog", "返回"))
        self.label.setText(_translate("dialog", "科室："))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("dialog", "病症"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("dialog", "病症描述"))
