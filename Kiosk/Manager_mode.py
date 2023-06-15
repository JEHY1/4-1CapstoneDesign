import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *

class Car_Manager_mode(QWidget):
    
    def __init__(self):
        super().__init__()
        uic.loadUi('Manager_mode.ui', self)
        # self.setWindowIcon(QIcon('~.png')) // 아이콘 등록
        self.setWindowTitle('관리자 모드')
