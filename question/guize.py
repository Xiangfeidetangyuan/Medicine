from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import  QDialog
from Medicine.question.datiguize import Sub

class SubWin(Sub,QDialog):

    def __init__(self, username):
        super(Sub,self).__init__()
        self.setupUi(self)
        self.username = username
        self.fanhuishouye.clicked.connect(self.f)
        self.kaishidati.clicked.connect(self.kai)
        self.setWindowIcon(QIcon("./images/icon.png"))

    def f(self):
        from Medicine.question.dati import MainWin
        my = MainWin(self.username)
        self.close()
        my.exec()

    def kai(self):
        from Medicine.question.question1 import Q1Win

        q1Win = Q1Win(self.username)

        self.close()
        q1Win.exec()
