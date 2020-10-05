import sqlite3
from PyQt5.QtGui import QIcon
from Login.register import Register
from Login.forgetPwd import ForgetPwd
from main_dialog import MainDialog
from PyQt5 import uic


class Login:
    def __init__(self):
        self.ui = uic.loadUi("ui/login.ui")
        self._registerWidget = ""
        self._forgetPwdWidget = ""
        self._failToLogin = uic.loadUi("ui/fail.ui")
        self._mainPage = ""
        self.ui.toRegister.clicked.connect(self.toRegister)
        self.ui.toForgetPwd.clicked.connect(self.toForgetPwd)
        self.ui.inputPwd.returnPressed.connect(self.login)
        self.ui.loginButton.clicked.connect(self.login)
        self.ui.setWindowIcon(QIcon("./images/icon.png"))

    def toRegister(self):
        self._registerWidget = Register()
        self._registerWidget.ui.exec()

    def toForgetPwd(self):
        self._forgetPwdWidget = ForgetPwd()
        self._forgetPwdWidget.ui.exec()

    def login(self):
        username = self.ui.inputUserName.text()
        pwd = self.ui.inputPwd.text()
        isPassed = False
        db = sqlite3.connect("./medicine_db.db")
        cursor = db.cursor()
        sql = "SELECT userName,userPwd From USER " \
              "WHERE  userName = '%s' " % username  # 注意这里的''要加上
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for r in results:
                if r[1] == pwd:  # 注意这里要加【0】，否则是元组对象
                    isPassed = True

        except:
            print("Error: unable to fetch data")
        finally:
            db.close()

        if isPassed == False:
            self._failToLogin.ErrorMsg.setText("用户名或密码错误！")
            self._failToLogin.exec_()
        else:
            # 此时登录成功，本页面关闭，传入用户名，
            self._mainPage = MainDialog(username)
            self.ui.close()
            self._mainPage.exec()

