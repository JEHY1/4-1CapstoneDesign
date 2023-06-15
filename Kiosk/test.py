import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton

class TextInputWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('텍스트 입력 예제')
        layout = QVBoxLayout()

        self.label = QLabel("입력된 텍스트:")
        layout.addWidget(self.label)

        self.text_input = QLineEdit()
        layout.addWidget(self.text_input)

        button = QPushButton('입력')
        button.clicked.connect(self.handle_button_click)
        layout.addWidget(button)

        self.setLayout(layout)

    def handle_button_click(self):
        text = self.text_input.text()
        self.label.setText("입력된 텍스트: " + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TextInputWindow()
    window.show()
    sys.exit(app.exec_())
