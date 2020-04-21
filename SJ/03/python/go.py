# /Users/hyeonseongjun/Desktop/mypro/chromedriver


import pymysql # MySQL Connection 연결 
conn = pymysql.connect(host='localhost', user='root', password='qwer1234',db='Contact', charset='utf8') 
# Connection 으로부터 Cursor 생성 
curs = conn.cursor()

# SQL문 실행
sql = "select * from Number"
curs.execute(sql)

# 데이타 Fetch
rows = curs.fetchall()
print(rows)     # 전체 rows
# print(rows[0])  # 첫번째 row
# print(rows[1])  # 두번째 row

# Connection 닫기
conn.close()