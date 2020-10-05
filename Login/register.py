from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
import sqlite3

class Register:

    def __init__(self):
        self.ui = uic.loadUi('ui/register.ui')
        self._failDialog = uic.loadUi('ui/fail.ui')
        self._successDialog = uic.loadUi('ui/registerSuccess.ui')
        self.ui.submitUser.clicked.connect(self.submit)  # 注意发信号不带括号！
        self.ui.inputEmail.returnPressed.connect(self.submit)
        self.ui.setWindowIcon(QIcon("./images/icon.png"))

    def submit(self):
        name = self.ui.inputUserName.text()
        pwd1 = self.ui.inputUserPwd1.text()
        pwd2 = self.ui.inputUserPwd2.text()
        email = self.ui.inputEmail.text()
        if self.isNull(name, pwd1, pwd2, email):
            self._failDialog.ErrorMsg.setText("注册信息不能为空")
            self._failDialog.exec_()
            return

        if pwd1 != pwd2:
            self._failDialog.ErrorMsg.setText("两次密码输入不一致！")
            self._failDialog.exec_()
            return

            # 检查数据库中是否有相同的name
        if not self.isValidID(name, "userName"):
            self._failDialog.ErrorMsg.setText("用户名重复啦，换一个呗")
            self._failDialog.exec_()

        elif not self.isValidID(email, "userEmail"):
            self._failDialog.ErrorMsg.setText("此邮箱已被注册")
            self._failDialog.exec_()
        else:
            db = sqlite3.connect("./medicine_db.db")
            cursor = db.cursor()
            try:
                cursor.execute("INSERT INTO USER (userName,userPwd,userEmail) VALUES (?,?,?)",
                               (name, pwd1, email))  # 请您别忘了执行SQL语句。。。
                db.commit()  # 这句话相当于保存！！！一定要加
                self._successDialog.exec_()  # 成功了，过会关闭注册界面
                self.ui.close()
            except:
                print("Error in Register.insert")
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

    def isNull(self, name, pwd1, pwd2, email):
        if name != '' and pwd1 != '' and pwd2 != '' and email != '':
            return False
        else:
            return True

