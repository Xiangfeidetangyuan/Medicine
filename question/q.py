from PyQt5.QtGui import QIcon
from Medicine.question.jieguo import JieGuo
from PyQt5.QtWidgets import  QDialog
from PyQt5.QtCore import pyqtSignal




class JieGuoWin(JieGuo,QDialog):
    # 自定义信号
    show_Main_win_signal = pyqtSignal()

    # show_zhujiemian_win_signal=pyqtSignal()
    def __init__(self, username):
        super(JieGuo,self).__init__()
        self.setupUi(self)
        self.username = username
        self.fanhuidatishouye.clicked.connect(self.go)
        self.fanhuizhujiemian.clicked.connect(self.go_back_index)
        self.setWindowIcon(QIcon("./images/icon.png"))
        # self.fanhuizhujiemian.clicked.connect(self.go_zhujiamian) #结果界面信号

    def go(self):
        from Medicine.question.dati import MainWin
        myWin = MainWin(self.username)
        self.close()
        myWin.exec()

    def go_back_index(self):
        from Medicine.main_dialog import MainDialog
        dialog = MainDialog(self.username)
        self.close()
        dialog.exec()

    '''def go_zhujiemian(self):
        self.show_zhujiemian_win_signal.emit()#结果界面中返回主界面的按钮
        '''

    '''def show_zhujiemian()
        zhujiemianWin.show()
        jieguoWin.hide()
    '''
