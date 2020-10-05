import sqlite3


class Inform:
    def __init__(self, medicineName, remarks, frequency, hour, minute, id):
        self.medicinename = medicineName
        self.remarks = remarks
        self.frequency = frequency
        self.hour = hour
        self.minute = minute
        self.id = 1

class InformDBHelper:

    def __init__(self, db_name, username):
        self.db_name = db_name
        self.username = username

    # 加入数据库
    def add(self, curinform):
    #    print("插入数据……")
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        try:
            sql2 = "INSERT INTO inform (userName, medicineName, remarks, frequency, Time_Hour, Time_Minute, status) values ('{}','{}','{}','{}','{}','{}','{}')"
            sql = sql2.format(self.username, curinform.medicinename, curinform.remarks, curinform.frequency,
                              curinform.hour, curinform.minute, 1)
            cursor.execute(sql)
            connection.commit()
            connection.close()
     #       print("插入提醒成功")
        except Exception as e:
            print(e)

    # 查
    def findALLInform(self):
        connection = sqlite3.connect(self.db_name)
        #print("连接数据库成功")
        cursor = connection.cursor()
        try:
            sql2 = "SELECT medicineName,remarks,frequency,Time_Hour,Time_Minute " \
                   ",informId ,status FROM inform WHERE  inform.userName= ('{}')"
            sql = sql2.format(self.username)
            informlist = cursor.execute(sql)
            inform_result_list = informlist.fetchall()
            connection.commit()
            connection.close()
           # print("查找结果成功")
            if len(inform_result_list) == 0:
              #  print("结果为0")
                return None
            else:
                return inform_result_list
        except Exception as e:
            print(e)

    # 设置状态
    def setStatus(self, id, status):
      #  print("设置状态……" + str(status))
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        try:
            sql = "UPDATE inform set status= '{}' WHERE inform.informID ='{}'".format(status, id)
            cursor.execute(sql)
            connection.commit()
            connection.close()
     #       print("设置状态成功……")
        except Exception as e:
            print(e)

    # 设置次数
    def setFrequdency(self, id, frequdency):
      #  print("设置次数……")
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        try:
            sql = "UPDATE inform SET frequency='{}' WHERE inform.informId= '{}'".format(frequdency, id)
            cursor.execute(sql)
            connection.commit()
            connection.close()
       #     print("设置次数成功……")
        except Exception as e:
            print(e)

    # 删除
    def delInform(self, id):
       # print("删除数据……", id)
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        try:
            sql = "DELETE FROM inform WHERE  inform.informId = '{}'".format(id)
            cursor.execute(sql)
            connection.commit()
            connection.close()
        #    print("删除数据成功……")
        except Exception as e:
            print(e)

    def getEmail(self):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        try:

            email = cursor.execute("SELECT userEmail From user WHERE  userName = '%s' " % self.username)
            res = email.fetchall()
            connection.commit()
            connection.close()
            print("获取邮箱成功……", res[0][0])
            return res[0][0]
        except Exception as e:
            print(e)
