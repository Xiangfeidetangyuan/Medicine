from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QDialog, QTableWidget, QAbstractItemView, QHeaderView, QTableWidgetItem, QLabel

from interaction.medicine_db_helper import MedicineDBHelper


class MedicineInteractionDialog(QDialog):
    def __init__(self, name):
        super().__init__()
        self.__name = name
        self.__medicine_db_helper = MedicineDBHelper("./medicine_db.db")
        self.__medicine_interaction_tables = [QTableWidget(self), QTableWidget(self), QTableWidget(self),
                                              QTableWidget(self)]
        self.header_labels = ["禁忌", "严重", "中度", "轻度"]
        self.__label = QLabel(self)
        self.init_dialog()
        self.init_tables()
        self.init_labels()

    def init_labels(self):
        self.__label.setText(self.__name)
        self.__label.setGeometry(240, 30, 160, 40)
        self.__label.setAlignment(Qt.AlignCenter)
        self.__label.setFont(QFont("Roman times", 20, QFont.Bold))

    def init_dialog(self):
        self.setWindowTitle(self.__name + "相互作用禁忌")
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.resize(640, 480)
        self.setWindowIcon(QIcon("./images/icon.png"))

    def init_tables(self):

        for i in range(4):
            self.__medicine_interaction_tables[i].setGeometry(16 + 156 * i, 85, 140, 344)
            self.__medicine_interaction_tables[i].setColumnCount(1)
            self.__medicine_interaction_tables[i].setSelectionMode(QAbstractItemView.SingleSelection)
            self.__medicine_interaction_tables[i].horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.__medicine_interaction_tables[i].setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.__medicine_interaction_tables[i].setSortingEnabled(True)
            self.__medicine_interaction_tables[i].setHorizontalHeaderLabels([self.header_labels[i]])
            self.__medicine_interaction_tables[i].item
            self.add_items_to_interaction_table_i(i)

    def add_interaction_item(self, i, name):
        row = self.__medicine_interaction_tables[i].rowCount()
        self.__medicine_interaction_tables[i].setRowCount(row + 1)
        self.__medicine_interaction_tables[i].setItem(row, 0, QTableWidgetItem(name))

    def add_items_to_interaction_table_i(self, i):
        item_list = self.__medicine_db_helper.get_interaction_list_by_name_degree(self.__name, self.header_labels[i])
        for item in item_list:
            self.add_interaction_item(i, str(item[0]))
