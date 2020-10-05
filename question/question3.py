from PyQt5 import QtCore
import sqlite3
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal

from Medicine.question.Q3 import q3





class Q3Win(QDialog, q3):
    # 自定义信号
    show_Q2_win_signal = pyqtSignal()
    show_JieGuo_win_signal = pyqtSignal()

    def __init__(self, username):
        global i
        super(Q3Win, self).__init__()
        self.setWindowIcon(QIcon("./images/icon.png"))
        self.setupUi(self)
        self.username = username
        conn = sqlite3.connect('./medicine_db.db')
        cu = conn.cursor()
        cursor = conn.execute("SELECT title from question_db WHERE ID=4")
        for it in cursor:
            t = it[0]
            _translate = QtCore.QCoreApplication.translate

            self.label_4.setText(_translate("Form", t))
        a = conn.execute("SELECT chooseA from question_db WHERE ID=4")
        for it in a:
            id = it[0]
            _translate = QtCore.QCoreApplication.translate
            self.radioButton.setText(_translate("Form", id))
        b = conn.execute("SELECT chooseB from question_db WHERE ID=4")
        for it in b:
            id = it[0]
            self.radioButton_2.setText(_translate("Form", id))
        c = conn.execute("SELECT chooseC from question_db WHERE ID=4")
        for it in c:
            id = it[0]
            self.radioButton_3.setText(_translate("Form", id))
        d = conn.execute("SELECT chooseD from question_db WHERE ID=4")
        for it in d:
            id = it[0]
            self.radioButton_4.setText(_translate("Form", id))
        conn.close()

        self.shangyiti2.clicked.connect(self.s)
        self.tijiao.clicked.connect(self.x)
        self.radioButton_2.toggled.connect(self.c)

    def s(self):
        from Medicine.question.question2 import Q2Win
        q3Win= Q2Win(3, self.username)
        self.close()
        q3Win.exec()

    def x(self):
        from Medicine.question.q import JieGuoWin
        r=JieGuoWin(self.username)
        self.close()
        r.exec()

    def c(self):
        from Medicine.question.q import JieGuoWin
        if self.radioButton_2.isChecked():
            q1Win = JieGuoWin(self.username)
            self.close()
            q1Win.exec()




