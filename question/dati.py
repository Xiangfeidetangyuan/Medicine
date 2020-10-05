from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import pyqtSignal
from question.datishouye import MainWin
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QDialog


class MainWin(QDialog, MainWin):  # 答题首页类

    def __init__(self, username):
        super().__init__()
        self.setupUi(self)
        self.username = username
        self.guizepushbutton.clicked.connect(self.q2)
        self.datipushbutton.clicked.connect(self.q1)
        self.pushButton.clicked.connect(self.go_back)
        self.setWindowIcon(QIcon("./images/icon.png"))


    def q2(self):
        from Medicine.question.guize import SubWin
        sub = SubWin(self.username)
        self.close()

        sub.exec()

    def q1(self):
        from Medicine.question.question1 import Q1Win

        q1Win=Q1Win(self.username)
        self.close()
        q1Win.exec()

    def go_back(self):
        from Medicine.main_dialog import MainDialog
        dialog = MainDialog(self.username)
        self.close()
        dialog.exec()


    '''def go(self):
        self.show_shouye_signal.emit()#答题首页中返回主界面的按钮
        '''

    '''
    def show_shouye():
        zhujiamianWin.show()
        myWin.hide()
    '''

