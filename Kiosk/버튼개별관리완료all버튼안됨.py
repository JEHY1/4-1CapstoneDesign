import subprocess
from tkinter import *

class KeyBlocker:
    def __init__(self):
        self.processes = {}

    def startBlock(self, script, key):
        if key not in self.processes:
            process = subprocess.Popen(['C:/Program Files/AutoHotkey/AutoHotkey.exe', script])
            self.processes[key] = process

    def stopBlock(self, key):
        if key in self.processes:
            process = self.processes[key]
            process.terminate()
            del self.processes[key]

    def isBlocked(self, key):
        return key in self.processes

class KioskApp:
    def __init__(self):
        self.window = Tk()
        self.window.title("Kiosk")
        self.window.geometry("200x100")

        self.blocker = KeyBlocker()

        self.win_button = Button(self.window, text="Block Windows Key", command=self.toggleBlockWinKey)
        self.win_button.pack()

        self.f4_button = Button(self.window, text="Block F4 Key", command=self.toggleBlockF4Key)
        self.f4_button.pack()

        self.unblock_button = Button(self.window, text="Unblock All Keys", command=self.unblockAllKeys)
        self.unblock_button.pack()

        self.window.mainloop()

    def toggleBlockWinKey(self):
        if self.blocker.isBlocked('LWin'):
            self.blocker.stopBlock('LWin')
            self.win_button["text"] = "Block Windows Key"
        else:
            self.blocker.startBlock('block_win_keys.ahk', 'LWin')
            self.win_button["text"] = "Unblock Windows Key"

    def toggleBlockF4Key(self):
        if self.blocker.isBlocked('F4'):
            self.blocker.stopBlock('F4')
            self.f4_button["text"] = "Block F4 Key"
        else:
            self.blocker.startBlock('block_f4_key.ahk', 'F4')
            self.f4_button["text"] = "Unblock F4 Key"

    def unblockAllKeys(self):
        for key in self.blocker.processes.keys():
            self.blocker.stopBlock(key)

        self.win_button["text"] = "Block Windows Key"
        self.f4_button["text"] = "Block F4 Key"

if __name__ == "__main__":
    app = KioskApp()
