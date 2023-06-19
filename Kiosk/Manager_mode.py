from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from newKeyboardSet import KioskApp
from changePassword import Car_changePassword


class Car_Manager_mode(QWidget):
    
    def __init__(self):
        super().__init__()
        uic.loadUi('Manager_mode.ui', self)
        self.setWindowTitle('관리자 모드')
        self.btn_keyboardSet.clicked.connect(self.btn_keyboardSetClicked)
        self.btn_changePassword.clicked.connect(self.btn_changePasswordClicked)
        self.btn_back.clicked.connect(self.btn_backClicked)
        self.btn_quit.clicked.connect(QApplication.quit)

    def btn_keyboardSetClicked(self):
        print(self.sender().objectName())
        self.Carmanager_mode = KioskApp()
        self.Carmanager_mode.showFullScreen()
        self.close()

    def btn_changePasswordClicked(self):
        print(self.sender().objectName())
        self.Carmanager_mode = Car_changePassword()
        self.Carmanager_mode.showFullScreen()
        self.close()

    def btn_backClicked(self):
        print(self.sender().objectName())
        from init import Main
        self.Carmanager_mode = Main()
        self.Carmanager_mode.showFullScreen()
        self.close()    
    
    
    
if __name__ == "__main__":
    app = QApplication([])
    window = Car_Manager_mode()
    window.showFullScreen()
    app.exec()
