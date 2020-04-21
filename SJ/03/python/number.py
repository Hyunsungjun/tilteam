from random import *
#번호생성
def Create():
    i = str(randrange(1,9999)).zfill(4)
    j = str(randrange(1,9999)).zfill(4)
    return f"010{i}{j}"
# print(f"VALUES ({Create()})")
#디비에 입력
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='qwer1234',db='Contact', charset='utf8') 
cursor = conn.cursor() 

# 데이터베이스 생성
# sql = "CREATE DATABASE Contact" 
# cursor.execute(sql) 
 
# 테이블 생성
sql = '''CREATE TABLE Number (
    id int(20) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Phone varchar(255)
)'''
cursor.execute(sql) 

# # 데이터 입력
# sql = "INSERT INTO Number (showPhone) VALUES (%s) WHERE NOT EXISTS SELECT * FROM Number WHERE Phone = %s" #일단 나중에 수정
# sql = "INSERT INTO Number (Phone) VALUES (%s)" 



# x=0
# sql = "select * from Number where not exists (select * from Phone=%s)"
# while x<20000:
#     Phone = Create()
#     cursor.execute(sql,(f"{Phone}"))
#     # cursor.execute(sql,data)
#     # cursor.execute(sql)
#     x = x+1
# # data = (Create(),Create())
# # data = (f"{Create()}-{Create()}")
#     if not len(cursor.fetchall()):
#         sql = "INSERT INTO Number (Phone) VALUES (%s)"  
#         cursor.execute(sql,(f"{Phone}"))

conn.commit() 
conn.close()

        # Delete from Number where id between 1 and 5 컬럼 삭제 쿼리
        # autoincrement가 적용된 id값 재정렬 하기;
        # SET @id = 0;
        # update Number set Number.id=@id:=@id+1;
        # SELECT * FROM Number; 
        # 중복입력 방지 쿼리
        # INSERT INTO table (field) 
        # WHERE NOT EXISTS (SELECT * FROM table WHERE field='value')
