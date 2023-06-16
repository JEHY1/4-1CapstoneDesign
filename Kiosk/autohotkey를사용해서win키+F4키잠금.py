import tkinter as tk
import subprocess

class KeyBlockApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Key Blocker")
        
        self.blocked_win = False
        self.blocked_f4 = False
        
        self.create_widgets()
        
    def create_widgets(self):
        self.btn_toggle_win = tk.Button(self.root, text="Block Windows Key", command=self.toggle_win_key_block)
        self.btn_toggle_win.pack(pady=10)
        
        self.btn_toggle_f4 = tk.Button(self.root, text="Block F4", command=self.toggle_f4_key_block)
        self.btn_toggle_f4.pack(pady=10)
        
    def toggle_win_key_block(self):
        if self.blocked_win:
            self.stop_win_key_block()
            self.blocked_win = False
            self.btn_toggle_win.config(text="Block Windows Key")
        else:
            self.start_win_key_block()
            self.blocked_win = True
            self.btn_toggle_win.config(text="Unblock Windows Key")
        
    def toggle_f4_key_block(self):
        if self.blocked_f4:
            self.stop_f4_key_block()
            self.blocked_f4 = False
            self.btn_toggle_f4.config(text="Block F4")
        else:
            self.start_f4_key_block()
            self.blocked_f4 = True
            self.btn_toggle_f4.config(text="Unblock F4")
        
    def start_win_key_block(self):
        subprocess.Popen(['C:/Program Files/AutoHotkey/AutoHotkey.exe', 'block_win_keys.ahk'])
        
    def stop_win_key_block(self):
        subprocess.Popen(['taskkill', '/IM', 'autohotkey.exe', '/F'])
        
    def start_f4_key_block(self):
        subprocess.Popen(['C:/Program Files/AutoHotkey/AutoHotkey.exe', 'block_f4_keys.ahk'])
        
    def stop_f4_key_block(self):
        subprocess.Popen(['taskkill', '/IM', 'autohotkey.exe', '/F'])
        
    def run(self):
        self.root.mainloop()

app = KeyBlockApp()
app.run()
