from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog

from Medicine.question.Q2 import q2


from Medicine.question.question3 import Q3Win

c=0
i=0
class Q2Win(QDialog, q2):
    # 自定义信号

    def __init__(self,count, username):
        global c
        c=count
        i = count
        super(Q2Win, self).__init__()
        self.setupUi(self)
        self.username = username
        self.setWindowIcon(QIcon("./images/icon.png"))
        conn = sqlite3.connect('./medicine_db.db')
        cu = conn.cursor()
        cursor = conn.execute("SELECT title from question_db WHERE ID=?", (i,))
        for it in cursor:
            t = it[0]
            _translate = QtCore.QCoreApplication.translate
            self.label_3.setText(_translate("Form",str(i)+"."))
            self.label_4.setText(_translate("Form", t))
        a = conn.execute("SELECT chooseA from question_db WHERE ID=?",(i,))
        for it in a:
            id = it[0]
            _translate = QtCore.QCoreApplication.translate
            self.radioButton.setText(_translate("Form", id))
        b = conn.execute("SELECT chooseB from question_db WHERE ID=?",(i,))
        for it in b:
            id = it[0]
            self.radioButton_2.setText(_translate("Form", id))
        c = conn.execute("SELECT chooseC from question_db WHERE ID=?",(i,))
        for it in c:
            id = it[0]
            self.radioButton_3.setText(_translate("Form", id))
        d = conn.execute("SELECT chooseD from question_db WHERE ID=?",(i,))
        for it in d:
            id = it[0]
            self.radioButton_4.setText(_translate("Form", id))

        if i==2:

           self.xiayiti2.clicked.connect(self.next)
           self.shangyiti.clicked.connect(self.be)
           self.radioButton_2.toggled.connect(self.x)


        if i==3:
            self.radioButton_2.setChecked(False)
            self.xiayiti2.clicked.connect(self.ne)
            self.shangyiti.clicked.connect(self.b)
            self.radioButton_2.toggled.connect(self.c)

    def next(self):

        q3Win=Q2Win(3, self.username)
        self.close()
        q3Win.exec()
    def be(self):

        from Medicine.question.question1 import Q1Win
        q1Win= Q1Win(self.username)
        self.close()
        q1Win.exec()

    def ne(self):

        q4Win=Q3Win(self.username)
        self.close()
        q4Win.exec()

    def b(self):

        q1Win= Q2Win(2, self.username)

        self.close()
        q1Win.exec()

    def x(self):
        if self.radioButton_2.isChecked():
            q1Win = Q2Win(3, self.username)

            self.close()
            q1Win.exec()




    def c(self):

        from Medicine.question.question3 import Q3Win

        if self.radioButton_2.isChecked():
            q1Win = Q3Win(self.username)

            self.close()
            q1Win.exec()








