import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *

# 주방용품 카테고리 창
class Car_Kitchen(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Kitchen.ui', self)
        # self.setWindowIcon(QIcon('~.png')) // 아이콘 등록
        self.setWindowTitle('키오스크')

        #DB 연결
        connection = pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        db='Kiosk',
        charset='utf8'
        )

        cursor = connection.cursor()
        query = "SELECT Product_name, Product_price, Product_Place FROM product_tbl WHERE Product_Category = '주방용품';"
        cursor.execute(query)

        # 결과를 담을 리스트 생성
        data_list = []

        # 쿼리 결과를 리스트에 추가
        for row in cursor.fetchall():
            data_list.append(list(row))


        # 연결 종료
        cursor.close()
        connection.close()
        
        #DB 자료값이 담긴 리스트를 위젯에 출력
        row_count = len(data_list)
        col_count = len(data_list[0])
        self.Tbl_Product.setRowCount(row_count)
        self.Tbl_Product.setColumnCount(col_count)

        for i, row in enumerate(data_list):
            for j, item in enumerate(row):
                self.Tbl_Product.setItem(i, j, QTableWidgetItem(str(item)))

        # 결과 출력 예시
        print(data_list)