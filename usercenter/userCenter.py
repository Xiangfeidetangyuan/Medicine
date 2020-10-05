from PyQt5.QtGui import QIcon
from PyQt5 import uic
import sqlite3


class UserCenter:
    def __init__(self, username):
        self.userName = username  # 传入数据
        self.ui = uic.loadUi('ui/userCenter.ui')
        self._changeInfoDialog = ""
        self.fail = ""
        self.ui.userNameLabel.setText(self.userName + "，你好")
        self.ui.changePwdBtn.clicked.connect(self.changePwd)
        self.ui.changeUserNameBtn.clicked.connect(self.changeUserName)
        self.ui.changeEmailBtn.clicked.connect(self.changeEmail)
        self.ui.returnBackBtn.clicked.connect(self.returnBack)
        self._dialog = ""
        self.ui.setWindowIcon(QIcon("./images/icon.png"))

    def changeEmail(self):
        self._changeInfoDialog = uic.loadUi('ui/changeInfo.ui')
        self._changeInfoDialog.showMsg.setText("请输入新邮箱")
        self._changeInfoDialog.confirmBtn.clicked.connect(self.updateUserEmail)
        self._changeInfoDialog.exec_()

    def returnBack(self):
        from Medicine.main_dialog import MainDialog
        self._dialog = MainDialog(self.userName)
        self.ui.close()
        self._dialog.exec()

    def changePwd(self):
        self._changeInfoDialog = uic.loadUi('ui/changePwd.ui')
        self._changeInfoDialog.confirmBtn.clicked.connect(self.updatePwd)
        self._changeInfoDialog.exec_()

    def changeUserName(self):
        self._changeInfoDialog = uic.loadUi('ui/changeInfo.ui')
        self._changeInfoDialog.showMsg.setText("请输入新用户名")
        self._changeInfoDialog.confirmBtn.clicked.connect(self.updateUserName)
        self._changeInfoDialog.exec_()

    def updateUserEmail(self):
        newEmail = self._changeInfoDialog.inputMsg.text()
        if newEmail == "":
            self.fail = uic.loadUi("ui/fail.ui")
            self.fail.ErrorMsg.setText("请输入新邮箱！")
            self.fail.exec_()

        elif self.isValidID(newEmail, "userEmail") == False:
            self.fail = uic.loadUi("ui/fail.ui")
            self.fail.ErrorMsg.setText("此邮箱已被注册")
            self.fail.exec_()
        else:
            if self.updateDB("userEmail", newEmail, self.userName) == True:
                self.fail = uic.loadUi("ui/fail.ui")
                self.fail.ErrorMsg.setText("修改邮箱成功！")
                self.fail.exec_()
                self._changeInfoDialog.close()
            else:
                self.fail = uic.loadUi("ui/fail.ui")
                self.fail.ErrorMsg.setText("出现问题，修改失败！")
                self.fail.exec_()
                self._changeInfoDialog.close()

    def updateUserName(self):
        newName = self._changeInfoDialog.inputMsg.text()
        if newName == "":
            self.fail = uic.loadUi("ui/fail.ui")
            self.fail.ErrorMsg.setText("请输入用户名！")
            self.fail.exec_()

        elif self.isValidID(newName, "userName") == False:
            self.fail = uic.loadUi("ui/fail.ui")
            self.fail.ErrorMsg.setText("此用户名已被注册")
            self.fail.exec_()
        else:
            if self.updateDB("userName", newName, self.userName) == True:
                self.fail = uic.loadUi("ui/fail.ui")
                self.fail.ErrorMsg.setText("修改用户名成功！")
                self.ui.userNameLabel.setText(newName + "，你好")
                self.userName = newName
                self.fail.exec_()
                self._changeInfoDialog.close()
            else:
                self.fail = uic.loadUi("ui/fail.ui")
                self.fail.ErrorMsg.setText("出现问题，修改失败！")
                self.fail.exec_()
                self._changeInfoDialog.close()

    def updatePwd(self):
        name = self.userName
        pwd01 = self._changeInfoDialog.pwd1.text()
        pwd02 = self._changeInfoDialog.pwd2.text()
        if pwd01 == "" or pwd02 == "":
            self.fail = uic.loadUi("ui/fail.ui")
            self.fail.ErrorMsg.setText("密码不能为空！")
            self.fail.exec_()

        elif pwd01 != pwd02:
            self.fail = uic.loadUi("ui/fail.ui")
            self.fail.ErrorMsg.setText("两次密码输入不一致！")
            self.fail.exec_()

        else:
            if self.updateDB("userPwd", pwd01, name) == True:
                self.fail = uic.loadUi("ui/fail.ui")
                self.fail.ErrorMsg.setText("修改密码成功！")
                self.fail.exec_()
                self._changeInfoDialog.close()
            else:
                self.fail = uic.loadUi("ui/fail.ui")
                self.fail.ErrorMsg.setText("出现问题，修改失败！")
                self.fail.exec_()
                self._changeInfoDialog.close()

    def updateDB(self, updateInfo, updateValue, userName):
        db = sqlite3.connect("./medicine_db.db")
        cursor = db.cursor()
        try:
            cursor.execute("UPDATE user SET '%s' = '%s' WHERE userName = '%s'" % (updateInfo, updateValue, userName))
            db.commit()
            print("已提交")
            return True
        except:
            print("Error in updateDB")
            return False
        finally:
            db.close()

    def isValidID(self, str, Type):
        db = sqlite3.connect("./medicine_db.db")
        cursor = db.cursor()
        sql = "SELECT %s FROM user" % Type  # 注意，查询的时候使用python定义的变量，不需要加引号
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for r in results:
                if r[0] == str:  # 注意这里要加【0】，否则是元组对象
                    return False
            return True
        except:
            print("Error in Register.isVaildID")
        finally:
            db.close()
