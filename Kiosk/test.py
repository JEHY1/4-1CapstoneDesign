import pymysql

# MySQL 데이터베이스에 접속
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='12345',
    db='Kiosk',
    charset='utf8'
)

# 커서 생성
cursor = connection.cursor()

# SELECT 쿼리 실행
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

# 결과 출력
print(data_list)