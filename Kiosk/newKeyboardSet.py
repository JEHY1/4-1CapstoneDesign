import subprocess
import pymysql
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class KeyBlocker:
    def __init__(self):
        self.processes = {}
        self.db = pymysql.connect(
            host="localhost",
            user="root",
            password="qwe123",
            database="Kiosk"
        )
        self.cursor = self.db.cursor()

    #auto hot key 를 사용해서 ahk 스크립트 실행 
    def startBlock(self, script, key):
        if key not in self.processes: #이미 켜저있는 프로세스의 경우 재실행 하지 않도록
            process = subprocess.Popen(['C:/Program Files/AutoHotkey/AutoHotkey.exe', script])
            self.processes[key] = process #스크립트 실행시 프로세스가 생성->켜져있는 프로세스들을 관리하기 위해 배열에 해당 프로세스를 키값으로 저장
            self.updateDatabaseBlockStatus(key, 1) #프로세스가 실행 중인지 여부 판단을 위해 db로 저장 (실행중: 1 /실행중 아님 : 0) 

    #실행중인 프로세스를 종료
    def stopBlock(self, key):
        if key in self.processes: #실행중인 프로세스인지 판단
            process = self.processes[key]
            process.terminate() #실행중인 프로세스를 강제 종료
            process.communicate()  #완전히 종료될때까지 기다림
            del self.processes[key]
            self.updateDatabaseBlockStatus(key, 0) #db에서 해당 키의 상태값을 0으로 변경

    def isBlocked(self, key):
        return key in self.processes

    #sql 쿼리문 작성하여 db를 업데이트
    def updateDatabaseBlockStatus(self, key, status):
        sql = "UPDATE key_status SET blocked = %s WHERE key_name = %s"
        values = (status, key)
        self.cursor.execute(sql, values)
        self.db.commit() #실제 db업데이트 하기 위해 필요

    #버튼 차단 상태를 db를 통해 확인
    def getBlockStatusFromDatabase(self, key):
        sql = "SELECT blocked FROM key_status WHERE key_name = %s"
        values = (key)
        self.cursor.execute(sql, values)
        result = self.cursor.fetchone()
        if result: #db에 값이 있을 경우 
            return result[0] #키 상태 값을 0,1로 db에 저장되어있음 -> 값을 0또는 1 로 리턴 ->나중에 if 조건문사용
        else:
            return None

class keyboardBlock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("KeyboardBlock")
        self.setGeometry(100, 100, 500, 500)

        self.blocker = KeyBlocker()

        layout = QVBoxLayout(self)

        self.win_button = QPushButton("Block Windows Key")
        layout.addWidget(self.win_button) #버튼을 추가
        self.win_button.clicked.connect(self.toggleBlockWinKey)

        self.altf4_button = QPushButton("Block Alt+F4 Key")
        layout.addWidget(self.altf4_button)
        self.altf4_button.clicked.connect(self.toggleBlockAltF4Key)

        self.alt_button = QPushButton("Block Alt Key")
        layout.addWidget(self.alt_button)
        self.alt_button.clicked.connect(self.toggleBlockAltKey)

        self.unblock_button = QPushButton("Unblock All Keys")
        layout.addWidget(self.unblock_button)
        self.unblock_button.clicked.connect(self.unblockAllKeys)

        self.back_button = QPushButton("Back")
        layout.addWidget(self.back_button)
        self.back_button.clicked.connect(self.back_clicked)

        self.loadButtonStatus()


    #윈도우 키 차단 활성/비활성 ->  그 후 윈도우키 차단 여부에 따라 버튼을 다르게 표현 
    def toggleBlockWinKey(self):
        if self.blocker.isBlocked('LWin'): #윈도우키가 차단되어 있을 경우
            self.blocker.stopBlock('LWin') #위에 설명했던 차단 함수 호출
            self.blocker.updateDatabaseBlockStatus('LWin', 0) #db 변경 함수 호출 (키 상태값 0으로)
            self.win_button.setText("Block Windows Key") #버튼 이름 변경
            self.win_button.setStyleSheet("") #버튼 스타일 초기화(배경색)
        else: #차단되어 있지 않을 경우
            self.blocker.startBlock('./ahk/block_Lwin_keys.ahk', 'LWin') #ahk 파일의 스크립트를 실행하여 키 차단
            self.blocker.updateDatabaseBlockStatus('LWin', 1) #db 변경 함수 호출 (키 상태값 1로)
            self.win_button.setText("Unblock Windows Key") #버튼 이름 변경
            self.win_button.setStyleSheet("background-color: #888888; color: white;") #버튼 어둡게

    def toggleBlockAltF4Key(self):
        if self.blocker.isBlocked('Alt+F4'):
            self.blocker.stopBlock('Alt+F4')
            self.blocker.updateDatabaseBlockStatus('Alt+F4', 0)
            self.altf4_button.setText("Block Alt+F4 Key")
            self.altf4_button.setStyleSheet("")
        else:
            self.blocker.startBlock('./ahk/block_alt+f4_key.ahk', 'Alt+F4')
            self.blocker.updateDatabaseBlockStatus('Alt+F4', 1)
            self.altf4_button.setText("Unblock Alt+F4 Key")
            self.altf4_button.setStyleSheet("background-color: #888888; color: white;")

    def toggleBlockAltKey(self):
        if self.blocker.isBlocked('Alt'):
            self.blocker.stopBlock('Alt')
            self.blocker.updateDatabaseBlockStatus('Alt', 0)
            self.alt_button.setText("Block Alt Key")
            self.alt_button.setStyleSheet("")
        else:
            self.blocker.startBlock('./ahk/block_Alt_key.ahk', 'Alt')
            self.blocker.updateDatabaseBlockStatus('Alt', 1)
            self.alt_button.setText("Unblock Alt Key")
            self.alt_button.setStyleSheet("background-color: #888888; color: white;")

    #모든 키 차단 해제하기
    def unblockAllKeys(self):
        #함수들 호출~
        self.blocker.stopBlock('LWin')
        self.blocker.updateDatabaseBlockStatus('LWin', 0)
        self.win_button.setText("Block Windows Key")
        self.win_button.setStyleSheet("")

        self.blocker.stopBlock('Alt+F4')
        self.blocker.updateDatabaseBlockStatus('Alt+F4', 0)
        self.altf4_button.setText("Block Alt+F4 Key")
        self.altf4_button.setStyleSheet("")

        self.blocker.stopBlock('Alt')
        self.blocker.updateDatabaseBlockStatus('Alt', 0)
        self.alt_button.setText("Block Alt Key")
        self.alt_button.setStyleSheet("")

    #버튼의 차단 상태를 받아오기 처음 창을 띄웠을때 상태를 받아오기 위함
    def loadButtonStatus(self):
        blocked_win = self.blocker.getBlockStatusFromDatabase('LWin') #db에서 해당 키의 키 상태 값을 읽어오는 함수 호출
        blocked_altf4 = self.blocker.getBlockStatusFromDatabase('Alt+F4')
        blocked_alt = self.blocker.getBlockStatusFromDatabase('Alt')

        if blocked_win:
            self.blocker.startBlock('./ahk/block_Lwin_keys.ahk', 'LWin') #프로세스 재실행 (재실행 하지 않으면 2번 클릭해야 됨)
            self.win_button.setText("Unblock Windows Key")
            self.win_button.setStyleSheet("background-color: #888888; color: white;")
        else:
            self.win_button.setText("Block Windows Key")

        if blocked_altf4:
            self.altf4_button.setText("Unblock Alt+F4 Key")
            self.altf4_button.setStyleSheet("background-color: #888888; color: white;")
        else:
            self.altf4_button.setText("Block Alt+F4 Key")

        if blocked_alt:
            self.alt_button.setText("Unblock Alt Key")
            self.alt_button.setStyleSheet("background-color: #888888; color: white;")
        else:
            self.alt_button.setText("Block Alt Key")

    #관리자 모드로 돌아가는 버튼
    def back_clicked(self): 
        from Manager_mode import Car_Manager_mode
        self.Carmanager_mode = Car_Manager_mode()
        self.Carmanager_mode.showFullScreen()
        self.close()

if __name__ == "__main__":
    app = QApplication([])
    window = keyboardBlock()
    window.showFullScreen()
    app.exec()