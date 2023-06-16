import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout, QGridLayout
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

        # 숫자 버튼
        for i in range(10):
            btn = QPushButton(str(i), self)
            btn.setCheckable(True)
            btn.setObjectName(str(i))
            btn.clicked.connect(self.toggleKeyBlock)
            gridLayout.addWidget(btn, row, col)
            col += 1
            if col == 10:
                col = 0
                row += 1

        # 특수문자 버튼
        special_chars = "!@#$%^&*()_-+={[}]|\\:;\"'<,>.?/"
        for char in special_chars:
            btn = QPushButton(char, self)
            btn.setCheckable(True)
            btn.setObjectName(char)
            btn.clicked.connect(self.toggleKeyBlock)
            gridLayout.addWidget(btn, row, col)
            col += 1
            if col == 10:
                col = 0
                row += 1

        # 영어 대문자 버튼
        for i in range(26):
            char = chr(ord('A') + i)
            btn = QPushButton(char, self)
            btn.setCheckable(True)
            btn.setObjectName(char)
            btn.clicked.connect(self.toggleKeyBlock)
            gridLayout.addWidget(btn, row, col)
            col += 1
            if col == 10:
                col = 0
                row += 1

        # 영어 소문자 버튼
        for i in range(26):
            char = chr(ord('a') + i)
            btn = QPushButton(char, self)
            btn.setCheckable(True)
            btn.setObjectName(char)
            btn.clicked.connect(self.toggleKeyBlock)
            gridLayout.addWidget(btn, row, col)
            col += 1
            if col == 10:
                col = 0
                row += 1

        # 방향키 버튼
        direction_keys = ['Up', 'Down', 'Left', 'Right']
        for key in direction_keys:
            btn = QPushButton(key, self)
            btn.setCheckable(True)
            btn.setObjectName(key)
            btn.clicked.connect(self.toggleKeyBlock)
            gridLayout.addWidget(btn, row, col)
            col += 1
            if col == 10:
                col = 0
                row += 1

        # Ctrl 버튼
        ctrlBtn = QPushButton('Ctrl', self)
        ctrlBtn.setCheckable(True)
        ctrlBtn.setObjectName('Ctrl')
        ctrlBtn.clicked.connect(self.toggleKeyBlock)
        gridLayout.addWidget(ctrlBtn, row, col)

        # Shift 버튼
        shiftBtn = QPushButton('Shift', self)
        shiftBtn.setCheckable(True)
        shiftBtn.setObjectName('Shift')
        shiftBtn.clicked.connect(self.toggleKeyBlock)
        gridLayout.addWidget(shiftBtn, row, col + 1)

        # Alt 버튼
        altBtn = QPushButton('Alt', self)
        altBtn.setCheckable(True)
        altBtn.setObjectName('Alt')
        altBtn.clicked.connect(self.toggleKeyBlock)
        gridLayout.addWidget(altBtn, row, col + 2)

        # Windows 버튼
        winBtn = QPushButton('Win', self)
        winBtn.setCheckable(True)
        winBtn.setObjectName('Win')
        winBtn.clicked.connect(self.toggleKeyBlock)
        gridLayout.addWidget(winBtn, row, col + 3)

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
            if event.modifiers() == Qt.ControlModifier:
                if 'Ctrl' in self.blocked_keys:
                    return True
            if event.modifiers() == Qt.ShiftModifier:
                if 'Shift' in self.blocked_keys:
                    return True
            if event.modifiers() == Qt.AltModifier:
                if 'Alt' in self.blocked_keys:
                    return True
            if event.modifiers() == Qt.MetaModifier:
                if 'Win' in self.blocked_keys:
                    return True

            key = event.text()
            if key in self.blocked_keys:
                return True

        return super().eventFilter(obj, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = KeyBlocker()
    window.show()
    sys.exit(app.exec_())
