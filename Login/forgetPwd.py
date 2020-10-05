from PyQt5.QtGui import QIcon
from PyQt5 import uic
from Login.mails import SendMails
import random
import sqlite3


class ForgetPwd:
    def __init__(self):
        self.ui = uic.loadUi("ui/forgetPwd.ui")
        self.changePwdDialog = uic.loadUi("ui/changePwd.ui")
        self.fail = ""
        self._email = ""
        self._captcha = ""
        self._randomNumber = int(random.uniform(999999, 100000))

        self.ui.confirmBtn.clicked.connect(self.toChangePwd)
        self.changePwdDialog.confirmBtn.clicked.connect(self.updatePwd)
        self.ui.getCaptchaBtn.clicked.connect(self.sendEmail)
        self.ui.setWindowIcon(QIcon("./images/icon.png"))

    def sendEmail(self):
        self._email = self.ui.inputUserPhone.text()
        context = "【用药助手】验证码：" + str(self._randomNumber)
        isExistUser = False

        db = sqlite3.connect("./medicine_db.db")
        cursor = db.cursor()

        try:
            cursor.execute("SELECT userEmail From USER WHERE  userEmail = '%s' " % self._email)
            results = cursor.fetchall()
            if results == []:
                isExistUser = False
            else:
                isExistUser = True
                self._email = results[0][0]  # 就是这里
        except:
            print("Error in forgetPwd.sendEmail")
        finally:
            db.close()

        if isExistUser == True:
            s = SendMails("smtp.126.com", "hitwh_jzy@126.com", 'WDTMGFMREVPRBKEE', self._email, "用药助手验证码", context)
            if s.sendE():
                print('提示', '发送成功！')
            else:
                print('提示', '发送失败！')

        else:
            self.fail = uic.loadUi("ui/fail.ui")
            self.fail.ErrorMsg.setText("该用户不存在！")
            self.fail.exec_()

    def toChangePwd(self):
        self._captcha = self.ui.inputCaptcha.text()
        if self._captcha == str(self._randomNumber):
            self.changePwdDialog.exec_()
        else:
            self.fail = uic.loadUi("ui/fail.ui")
            self.fail.ErrorMsg.setText("验证码错误")
            self.fail.exec_()

    def updatePwd(self):
        # 修改密码，并更新提交到数据库
        email = self._email
        pwd1 = self.changePwdDialog.pwd1.text()
        pwd2 = self.changePwdDialog.pwd2.text()
        if pwd1 == "" or pwd2 == "":
            self.fail = uic.loadUi("ui/fail.ui")
            self.fail.ErrorMsg.setText("密码不能为空！")
            self.fail.exec_()

        elif pwd1 != pwd2:
            self.fail = uic.loadUi("ui/fail.ui")
            self.fail.ErrorMsg.setText("两次密码输入不一致！")
            self.fail.exec_()

        else:
            db = sqlite3.connect("./medicine_db.db")
            cursor = db.cursor()
            try:
                cursor.execute("UPDATE user SET userPwd = '%s' WHERE userEmail = '%s'" % (pwd1, email))
                db.commit()
                print("已提交")
                # 此时修改密码整个过程已经结束，弹出通知信息之后，关闭这个对话框与界面。
                self.fail = uic.loadUi("ui/fail.ui")
                self.fail.ErrorMsg.setText("修改密码成功！")
                self.fail.exec_()
                self.changePwdDialog.close()
                self.ui.close()
            except:
                print("Error in ForgetPwd.updatePwd")
            finally:
                db.close()
            print("执行结束")
