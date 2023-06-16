from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5 import uic

class Car_Manager_mode(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Manager_mode.ui', self)
        self.setWindowTitle('관리자 모드')

        self.btn_close = QPushButton("Close", self)
        self.btn_close.setGeometry(150, 150, 100, 50)
        self.btn_close.clicked.connect(self.close)

if __name__ == "__main__":
    app = QApplication([])
    window = Car_Manager_mode()
    window.show()
    app.exec()
