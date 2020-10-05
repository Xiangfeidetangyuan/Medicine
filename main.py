from Login.login import Login
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Login()
    dialog.ui.show()

    sys.exit(app.exec_())
