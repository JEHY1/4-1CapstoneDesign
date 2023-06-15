import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from Manager_mode import Car_Manager_mode

class Car_Manager_login(QWidget):
    

    def __init__(self):
        super().__init__()
        uic.loadUi('Manager_login.ui', self)
        self.setWindowTitle('로그인')
        self.btn_login.clicked.connect(self.btn_LoginClicked)

        #DB 연결
        connection = pymysql.connect(
        host='localhost',
        user='root',
        password='qwe123',
        db='Kiosk',
        charset='utf8'
        )

        cursor = connection.cursor()
        query = "SELECT pw FROM admin where id = 'admin';"
        cursor.execute(query)
        global admin_data
        admin_data = cursor.fetchone()
        admin_data = admin_data[0]
        print("admin data is ")
        print(admin_data)

         # 연결 종료
        cursor.close()
        connection.close()
    


    def btn_LoginClicked(self):
        print(self.sender().objectName())
        if admin_data == self.entered_pw.text():
            print("관리자 모드")
            print("entered pw:")
            print(self.entered_pw.text())
            self.Carmanager_mode = Car_Manager_mode()
            self.Carmanager_mode.show()
            self.close()
    
        
            
                





        