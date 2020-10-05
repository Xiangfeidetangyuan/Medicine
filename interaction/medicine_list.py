from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QDialog, QTableWidget, QAbstractItemView, QTableWidgetItem, QLineEdit, \
    QPushButton, QLabel

from interaction.medicine_db_helper import MedicineDBHelper
from interaction.medicine_interaction import MedicineInteractionDialog


class MedicineListDialog(QDialog):
    def __init__(self, username):
        super().__init__()
        self.__username = username
        self.__medicine_db_helper = MedicineDBHelper("./medicine_db.db")
        self.init_dialog()
        self.__medicine_list_table = QTableWidget(self)
        self.__search_line_edit = QLineEdit(self)
        self.init_line_edit()
        self.__clean_push_button = QPushButton(self)
        self.__exit_push_button = QPushButton(self)
        self.__label = QLabel(self)
        self.init_labels()
        self.init_push_buttons()
        self.init_medicine_list_table()

    def init_labels(self):
        self.__label.setText("双击药物名称，查看禁忌详情")
        self.__label.setGeometry(250, 80, 300, 20)
        self.__label.setAlignment(Qt.AlignCenter)
        self.__label.setFont(QFont("Roman times", 10, QFont.Bold))

    def init_dialog(self):
        self.resize(800, 600)
        self.setWindowTitle("药物相互作用查询")
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowIcon(QIcon("./images/icon.png"))

    def init_line_edit(self):
        self.__search_line_edit.setGeometry(200, 28, 280, 30)
        self.__search_line_edit.textChanged.connect(self.list_search)
        self.__search_line_edit.setPlaceholderText("请输入药物名称关键字或序号搜索")

    def list_search(self):
        text = self.__search_line_edit.text()
        row = self.__medicine_list_table.rowCount()
        if text == "":
            for i in range(row):
                self.__medicine_list_table.setRowHidden(i, False)
        else:
            num_list = self.__medicine_list_table.findItems(text, Qt.MatchContains)
            for i in range(row):
                self.__medicine_list_table.setRowHidden(i, True)
            for i in range(len(num_list)):
                self.__medicine_list_table.setRowHidden(num_list[i].row(), False)

    def init_push_buttons(self):
        self.__clean_push_button.setGeometry(500, 28, 100, 30)
        self.__clean_push_button.setText("清空")
        self.__clean_push_button.clicked.connect(self.on_clean_push_button_clicked)
        self.__exit_push_button.setGeometry(645, 545, 140, 40)
        self.__exit_push_button.clicked.connect(self.on_exit_push_button_clicked)
        self.__exit_push_button.setText("返回主页")

    def on_clean_push_button_clicked(self):
        self.__search_line_edit.setText("")

    def init_medicine_list_table(self):
        self.__medicine_list_table.setGeometry(100, 106, 600, 430)
        self.__medicine_list_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.__medicine_list_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.__medicine_list_table.setColumnCount(2)
        self.__medicine_list_table.setHorizontalHeaderLabels(["序号", "药物名称"])
        self.__medicine_list_table.setColumnWidth(0, 60)
        self.__medicine_list_table.horizontalHeader().setStretchLastSection(True)
        self.__medicine_list_table.verticalHeader().setVisible(False)
        self.__medicine_list_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.__medicine_list_table.setSortingEnabled(True)
        self.add_items_to_medicine_list_table()
        self.__medicine_list_table.itemDoubleClicked.connect(self.show_select_item)
        self.__medicine_list_table.setToolTip("双击查看药品的相互作用禁忌")

    def show_select_item(self):
        item_name = self.__medicine_list_table.selectedItems()[1]
        interaction_dialog = MedicineInteractionDialog(item_name.text())
        interaction_dialog.exec()

    def add_medicine_item(self, item_id, item_name):
        row = self.__medicine_list_table.rowCount()
        self.__medicine_list_table.setRowCount(row + 1)
        self.__medicine_list_table.setItem(row, 0, QTableWidgetItem(item_id))
        self.__medicine_list_table.item(row, 0).setTextAlignment(Qt.AlignCenter)
        self.__medicine_list_table.setItem(row, 1, QTableWidgetItem(item_name))
        self.__medicine_list_table.item(row, 1).setTextAlignment(Qt.AlignCenter)

    def add_items_to_medicine_list_table(self):
        item_list = self.__medicine_db_helper.get_medicine_list()
        for item in item_list:
            self.add_medicine_item(item[0], item[1])

    def on_exit_push_button_clicked(self):
        from main_dialog import MainDialog
        dialog = MainDialog(self.__username)
        self.close()
        dialog.exec()
