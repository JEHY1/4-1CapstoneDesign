import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from Manager_mode import Car_Manager_mode

class Car_Manager_login(QWidget):
    
    def __init__(self):
        super().__init__()
        uic.loadUi('./ui/Manager_login.ui', self)
        self.setWindowTitle('로그인')
        #버튼과 함수 연결
        self.btn_login.clicked.connect(self.btn_LoginClicked)

        #DB 연결
        connection = pymysql.connect(
        host='localhost',
        user='root',
        password='qwe123',
        db='Kiosk',
        charset='utf8',
        )

        cursor = connection.cursor()
        query = "SELECT pw FROM admin where id = 'admin';"
        cursor.execute(query)
        global admin_data
        admin_data = cursor.fetchone()
        admin_data = admin_data[0] #admin_data에 데이터베이스의 관리자 비밀번호 저장
        print("admin data is ")
        print(admin_data)

         # 연결 종료
        cursor.close()
        connection.close()
    
    def btn_LoginClicked(self):
        if admin_data == self.entered_pw.text(): #.text() 로 해당 텍스트 박스의 값을 가져와서 db의 값과 일치하는지 비교
            self.Carmanager_login = Car_Manager_mode() 
            self.Carmanager_login.showFullScreen()
            self.close()