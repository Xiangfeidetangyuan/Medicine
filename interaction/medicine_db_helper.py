import sqlite3


class MedicineDBHelper:

    def __init__(self, db_name):
        self.__db_name = db_name
        self.create_table()

    def create_table(self):
        connection = sqlite3.connect(self.__db_name)
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS MEDICINE_LIST(ID TEXT, ITME_NAME TEXT)")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS MEDICINE_INTERACTION(MAIN_NAME TEXT, INTERACTION_NAME TEXT, DEGREE TEXT)")
        connection.commit()
        connection.close()

    def get_medicine_list(self):
        connection = sqlite3.connect(self.__db_name)
        cursor = connection.cursor()
        result_list = cursor.execute("SELECT * FROM MEDICINE_LIST")
        result = result_list.fetchall()
        connection.commit()
        connection.close()
        return result

    def get_interaction_list_by_name_degree(self, main_name, degree):
        connection = sqlite3.connect(self.__db_name)
        cursor = connection.cursor()
        result_list = cursor.execute(
            "SELECT INTERACTION_NAME FROM MEDICINE_INTERACTION WHERE MAIN_NAME = ? AND DEGREE = ?", (main_name, degree))
        connection.commit()
        result = result_list.fetchall()
        connection.close()
        return result
