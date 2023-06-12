import sys
from kitchen import Car_Kitchen
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *

# 메인
class Main(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('./Main.ui', self)
        # self.setWindowIcon(QIcon('~.png')) // 아이콘 등록
        self.setWindowTitle('키오스크')
        self.Btn_Category1.clicked.connect(self.btn_CategoryClicked) # 1번 버튼
        self.Btn_Category2.clicked.connect(self.btn_CategoryClicked) # 2번 버튼, 향후 추가 예정

    # 버튼을 눌렀을때, 창 변환
    def btn_CategoryClicked(self):
        #result = QMessageBox()
        #qmsBox = result.question(result,"주방용품!","주방용품입니다.")
        print(self.sender().objectName())
        
        if self.Btn_Category1.clicked.connect(self.btn_CategoryClicked):
             print("주방용품")
             self.Carkitchen = Car_Kitchen()
             self.Carkitchen.show()
             self.close()

# 위젯 실행
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main_Widget = Main()
    Main_Widget.show()
    sys.exit(app.exec_())