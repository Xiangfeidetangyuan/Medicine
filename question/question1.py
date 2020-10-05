from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from Medicine.question.Q1 import q1

score=0

i=0

class Q1Win(QDialog, q1):
    def __init__(self, username):
        super(Q1Win, self).__init__()
        self.username = username
        self.setupUi(self)
        self.setWindowIcon(QIcon("./images/icon.png"))
        conn = sqlite3.connect('./medicine_db.db')
        cu = conn.cursor()
        cursor = conn.execute("SELECT title from question_db WHERE ID=1")
        for it in cursor:
            t = it[0]
            _translate = QtCore.QCoreApplication.translate

            self.label_4.setText(_translate("Form",t))
        a = conn.execute("SELECT chooseA from question_db WHERE ID=1" )
        for it in a:
            id = it[0]
            _translate = QtCore.QCoreApplication.translate
            self.radioButton.setText(_translate("Form", id))
        b = conn.execute("SELECT chooseB from question_db WHERE ID=1")
        for it in b:
            id = it[0]
            self.radioButton_2.setText(_translate("Form", id))
        c = conn.execute("SELECT chooseC from question_db WHERE ID=1")
        for it in c:
            id = it[0]
            self.radioButton_3.setText(_translate("Form", id))
        d = conn.execute("SELECT chooseD from question_db WHERE ID=1")
        for it in d:
            id = it[0]
            self.radioButton_4.setText(_translate("Form", id))

        conn.close()
        self.xiayiti.clicked.connect(self.x)
        self.radioButton_4.toggled.connect(self.b)


    def x(self):
        from Medicine.question.question2 import Q2Win
        q2Win=Q2Win(2, self.username)
        self.close()
        q2Win.exec()

    def b(self):
        global score

        if self.radioButton_4.isChecked():
            from Medicine.question.question2 import Q2Win
            q2Win = Q2Win(2, self.username)
            self.close()
            q2Win.exec()

