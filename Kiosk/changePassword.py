import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *


class Car_changePassword(QWidget):
    
    def __init__(self):
        super().__init__()
        uic.loadUi('Change_Password.ui', self)
        self.setWindowTitle('비밀번호 변경')
        self.btn_change.clicked.connect(self.btn_changePasswordClicked)
        self.btn_cancel.clicked.connect(self.btn_cancelClicked)

    def btn_changePasswordClicked(self):
        #DB 연결
        self.connection = pymysql.connect(
        host='localhost',
        user='root',
        password='qwe123',
        db='Kiosk',
        charset='utf8',
        )

        cursor = self.connection.cursor()
        query = "SELECT pw FROM admin where id = 'admin';"
        cursor.execute(query)
        global admin_data
        admin_data = cursor.fetchone()
        admin_data = admin_data[0]
        print("admin data is ")
        print(admin_data)

        if admin_data == self.currentPassword.text() and self.newPassword.text() == self.newPasswordRe.text():
            query = "update admin set pw = %s where id = 'admin';"
            cursor.execute(query, self.newPassword.text()) 
            self.connection.commit()
            from Manager_mode import Car_Manager_mode
            self.changePassword = Car_Manager_mode()
            self.changePassword.showFullScreen()
            self.close()

      # 연결 종료
        cursor.close()
        self.connection.close()

    def btn_cancelClicked(self):
        from Manager_mode import Car_Manager_mode
        self.changePassword = Car_Manager_mode()
        self.changePassword.showFullScreen()
        self.close()
    
if __name__ == "__main__":
    app = QApplication([])
    window = Car_changePassword()
    window.showFullScreen()
    app.exec()