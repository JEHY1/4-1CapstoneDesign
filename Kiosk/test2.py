import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import subprocess

class KeyBlocker(QWidget):
    def __init__(self):
        super().__init__()

        self.blocked = False
        self.process = None

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 200, 100)
        self.setWindowTitle('Key Blocker')

        self.btnToggle = QPushButton('On', self)
        self.btnToggle.clicked.connect(self.toggleKeyBlock)

        layout = QVBoxLayout()
        layout.addWidget(self.btnToggle)

        self.setLayout(layout)

    def toggleKeyBlock(self):
        if self.blocked:
            self.stopBlock()
        else:
            self.startBlock()

    def startBlock(self):
        self.blocked = True
        self.btnToggle.setText('Off')
        self.process = subprocess.Popen(['C:\\Program Files\\AutoHotkey\\AutoHotkey.exe', 'block_win_keys.ahk'])


    def stopBlock(self):
        self.blocked = False
        self.btnToggle.setText('On')
        self.process.terminate()
        self.process = None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = KeyBlocker()
    window.show()
    sys.exit(app.exec_())
