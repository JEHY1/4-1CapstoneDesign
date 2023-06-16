
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from newKeyboardSet import KioskApp

class Car_Manager_mode(QWidget):
    

    def __init__(self):
        super().__init__()
        uic.loadUi('Manager_mode.ui', self)
        self.setWindowTitle('관리자 모드')
        self.btn_keyboardSet.clicked.connect(self.btn_keyboardSetClicked)



    def btn_keyboardSetClicked(self):
        print(self.sender().objectName())
        self.Carmanager_mode = KioskApp()
        self.Carmanager_mode.show()
        self.close()
    
