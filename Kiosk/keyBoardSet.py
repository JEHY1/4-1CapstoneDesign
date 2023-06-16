import subprocess
import pymysql
from tkinter import *



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

class KioskApp:
    def __init__(self):
        self.window = Tk()
        self.window.title("Kiosk")
        self.window.geometry("500x500")

        self.blocker = KeyBlocker()

        self.win_button = Button(self.window, text="Block Windows Key", command=self.toggleBlockWinKey)
        self.win_button.pack()

        self.f4_button = Button(self.window, text="Block F4 Key", command=self.toggleBlockF4Key)
        self.f4_button.pack()

        self.unblock_button = Button(self.window, text="Unblock All Keys", command=self.unblockAllKeys)
        self.unblock_button.pack()

        self.loadButtonStatus()

        self.window.mainloop()


    def toggleBlockWinKey(self):
        if self.blocker.isBlocked('LWin'):
            self.blocker.stopBlock('LWin')
            self.blocker.updateDatabaseBlockStatus('LWin', 0)
            self.win_button["text"] = "Block Windows Key"
        else:
            self.blocker.startBlock('block_Lwin_keys.ahk', 'LWin')
            self.blocker.updateDatabaseBlockStatus('LWin', 1)
            self.win_button["text"] = "Unblock Windows Key"

    def toggleBlockF4Key(self):
        if self.blocker.isBlocked('F4'):
            self.blocker.stopBlock('F4')
            self.blocker.updateDatabaseBlockStatus('F4', 0)
            self.f4_button["text"] = "Block F4 Key"
        else:
            self.blocker.startBlock('block_f4_key.ahk', 'F4')
            self.blocker.updateDatabaseBlockStatus('F4', 1)
            self.f4_button["text"] = "Unblock F4 Key"

    def unblockAllKeys(self):
        self.blocker.stopBlock('LWin')
        self.blocker.updateDatabaseBlockStatus('LWin', 0)
        self.win_button["text"] = "Block Windows Key"

        self.blocker.stopBlock('F4')
        self.blocker.updateDatabaseBlockStatus('F4', 0)
        self.f4_button["text"] = "Block F4 Key"

    def loadButtonStatus(self):
        blocked_win = self.blocker.getBlockStatusFromDatabase('LWin')
        blocked_f4 = self.blocker.getBlockStatusFromDatabase('F4')

        if blocked_win:
            self.blocker.startBlock('block_Lwin_keys.ahk', 'LWin')
            self.win_button["text"] = "Unblock Windows Key"
        else:
            self.win_button["text"] = "Block Windows Key"

        if blocked_f4:
            self.blocker.startBlock('block_f4_key.ahk', 'F4')
            self.f4_button["text"] = "Unblock F4 Key"
        else:
            self.f4_button["text"] = "Block F4 Key"

    

if __name__ == "__main__":
    app = KioskApp()
