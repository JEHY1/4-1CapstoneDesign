from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from newKeyboardSet import keyboardBlock
from changePassword import Car_changePassword

class Car_Manager_mode(QWidget):
    
    def __init__(self):
        super().__init__()
        uic.loadUi('./ui/Manager_mode.ui', self)
        self.setWindowTitle('관리자 모드')
        #버튼과 함수 연결
        self.btn_keyboardSet.clicked.connect(self.btn_keyboardSetClicked)
        self.btn_changePassword.clicked.connect(self.btn_changePasswordClicked)
        self.btn_back.clicked.connect(self.btn_backClicked)
        self.btn_quit.clicked.connect(QApplication.quit) #키오스크를 종료하는 버튼

    #키보드 설정화면으로 바꾸기
    def btn_keyboardSetClicked(self):
        print(self.sender().objectName())
        self.Carmanager_mode = keyboardBlock()
        self.Carmanager_mode.showFullScreen()
        self.close()

    #비밀번호 변경 화면으로 바꾸기
    def btn_changePasswordClicked(self):
        print(self.sender().objectName())
        self.Carmanager_mode = Car_changePassword()
        self.Carmanager_mode.showFullScreen()
        self.close()

    #키오스크 메인 화면으로 바꾸기
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