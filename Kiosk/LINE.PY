import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt, QEvent


class KeyBlocker(QWidget):
    def __init__(self):
        super().__init__()

        self.blocked_keys = set()  # 차단된 키 목록

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('Key Blocker')

        # 텍스트 편집창
        self.textEdit = QTextEdit(self)

        # 그리드 레이아웃
        gridLayout = QGridLayout()

        # 키보드 버튼 생성
        row = 0
        col = 0
        for i in range(256):
            btn = QPushButton(chr(i), self)
            btn.setCheckable(True)
            btn.setObjectName(chr(i))
            btn.clicked.connect(self.toggleKeyBlock)
            gridLayout.addWidget(btn, row, col)
            col += 1
            if col == 16:
                col = 0
                row += 1

        # 레이아웃 구성
        layout = QVBoxLayout()
        layout.addLayout(gridLayout)
        layout.addWidget(self.textEdit)

        self.setLayout(layout)

        # 키보드 입력 이벤트 필터 등록
        self.textEdit.installEventFilter(self)

    def toggleKeyBlock(self):
        btn = self.sender()
        key = btn.objectName()

        if btn.isChecked():
            self.blocked_keys.add(key)
            btn.setStyleSheet("background-color: darkGray; color: white")
        else:
            self.blocked_keys.discard(key)
            btn.setStyleSheet("")

    def eventFilter(self, obj, event):
        if obj is self.textEdit and event.type() == QEvent.KeyPress:
            key = event.text()
            if key in self.blocked_keys:
                return True

        return super().eventFilter(obj, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = KeyBlocker()
    window.show()
    sys.exit(app.exec_())
