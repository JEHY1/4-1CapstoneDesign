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

    def startBlock(self, script, key):
        if key not in self.processes: 
            process = subprocess.Popen(['C:/Program Files/AutoHotkey/AutoHotkey.exe', script])
            self.processes[key] = process
            self.updateDatabaseBlockStatus(key, 1)

    def stopBlock(self, key):
        if key in self.processes:
            process = self.processes[key]
            process.terminate()
            process.communicate()  # Wait for the process to exit
            del self.processes[key]
            self.updateDatabaseBlockStatus(key, 0)

    def isBlocked(self, key):
        return key in self.processes

    def updateDatabaseBlockStatus(self, key, status):
        sql = "UPDATE key_status SET blocked = %s WHERE key_name = %s"
        values = (status, key)
        self.cursor.execute(sql, values)
        self.db.commit()

    def getBlockStatusFromDatabase(self, key):
        sql = "SELECT blocked FROM key_status WHERE key_name = %s"
        values = (key,)
        self.cursor.execute(sql, values)
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

class KioskApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kiosk")
        self.setGeometry(100, 100, 500, 500)

        self.blocker = KeyBlocker()

        layout = QVBoxLayout(self)

        self.win_button = QPushButton("Block Windows Key")
        layout.addWidget(self.win_button)
        self.win_button.clicked.connect(self.toggleBlockWinKey)

        self.f4_button = QPushButton("Block F4 Key")
        layout.addWidget(self.f4_button)
        self.f4_button.clicked.connect(self.toggleBlockF4Key)

        self.unblock_button = QPushButton("Unblock All Keys")
        layout.addWidget(self.unblock_button)
        self.unblock_button.clicked.connect(self.unblockAllKeys)

        self.back_button = QPushButton("Back")
        layout.addWidget(self.back_button)
        self.back_button.clicked.connect(self.back_clicked)

        self.loadButtonStatus()

    def toggleBlockWinKey(self):
        if self.blocker.isBlocked('LWin'):
            self.blocker.stopBlock('LWin')
            self.blocker.updateDatabaseBlockStatus('LWin', 0)
            self.win_button.setText("Block Windows Key")
            self.win_button.setStyleSheet("")
        else:
            self.blocker.startBlock('block_Lwin_keys.ahk', 'LWin')
            self.blocker.updateDatabaseBlockStatus('LWin', 1)
            self.win_button.setText("Unblock Windows Key")
            self.win_button.setStyleSheet("background-color: #888888; color: white;")

    def toggleBlockF4Key(self):
        if self.blocker.isBlocked('F4'):
            self.blocker.stopBlock('F4')
            self.blocker.updateDatabaseBlockStatus('F4', 0)
            self.f4_button.setText("Block F4 Key")
            self.f4_button.setStyleSheet("")
        else:
            self.blocker.startBlock('block_f4_key.ahk', 'F4')
            self.blocker.updateDatabaseBlockStatus('F4', 1)
            self.f4_button.setText("Unblock F4 Key")
            self.f4_button.setStyleSheet("background-color: #888888; color: white;")

    def unblockAllKeys(self):
        self.blocker.stopBlock('LWin')
        self.blocker.updateDatabaseBlockStatus('LWin', 0)
        self.win_button.setText("Block Windows Key")
        self.win_button.setStyleSheet("")

        self.blocker.stopBlock('F4')
        self.blocker.updateDatabaseBlockStatus('F4', 0)
        self.f4_button.setText("Block F4 Key")
        self.f4_button.setStyleSheet("")


    def loadButtonStatus(self):
        blocked_win = self.blocker.getBlockStatusFromDatabase('LWin')
        blocked_f4 = self.blocker.getBlockStatusFromDatabase('F4')

        if blocked_win:
            self.blocker.startBlock('block_Lwin_keys.ahk', 'LWin')
            self.win_button.setText("Unblock Windows Key")
            self.win_button.setStyleSheet("background-color: #888888; color: white;")
        else:
            self.win_button.setText("Block Windows Key")

        if blocked_f4:
            self.blocker.startBlock('block_f4_key.ahk', 'F4')
            self.f4_button.setText("Unblock F4 Key")
            self.f4_button.setStyleSheet("background-color: #888888; color: white;")
        else:
            self.f4_button.setText("Block F4 Key")

    def back_clicked(self):
        from Manager_mode import Car_Manager_mode
        self.Carmanager_mode = Car_Manager_mode()
        self.Carmanager_mode.showFullScreen()
        self.close()

if __name__ == "__main__":
    app = QApplication([])
    window = KioskApp()
    window.showFullScreen()
    app.exec()

