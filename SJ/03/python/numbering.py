from random import *
import pymysql
import pandas as pd
from sqlalchemy import create_engine
import MySQLdb
#번호생성
def Create():
    i = str(randrange(1,9999)).zfill(4)
    j = str(randrange(1,9999)).zfill(4)
    return f"010{i}{j}"

num = []
for i in range(20000):
    num.append(Create())
# print(num)

# SQLAlchemy, pymysql, MySQLdb https://swalloow.github.io/dataframe-to-mysql

# MySQL Connector using pymysql
pymysql.install_as_MySQLdb()

engine = create_engine("mysql+mysqldb://root:"+"qwer1234"+"@localhost/Contact", encoding='utf-8')
conn = engine.connect()


host_name = "localhost"
username = "root"
password = "qwer1234"
database_name = "Contact"    # 데이터베이스 이름을 sakila 로 바꿔줘야 합니다.

db = pymysql.connect(
    host="localhost",  # DATABASE_HOST
    port=3306,
    user="root",  # DATABASE_USERNAME
    passwd="qwer1234",  # DATABASE_PASSWORD
    db="Contact",  # DATABASE_NAME
    charset='utf8'
)

# SQL = "SELECT * FROM Number LIMIT 1"
# df = pd.read_sql(SQL, db)
# df
###########################
# 1. df 불러오기

df = pd.read_sql(SQL, db)

# 2. 난수 col 생성하기

df['ran_var1'] = num # 여기서 df에 난수가 제대로 붙었는지 확인해보세요

# 3. sql에 저장하기
# format에 맞는 db에 저장해주세요
df.to_sql(name=Number, con=engine, if_exists='fail') # to_sql 함수는 안써봐서 제대로 동작하는지 모르겠습니다.
#############
# MySQL에 저장하기
# df.to_sql(name=Contact, con=engine, if_exists='fail')

# query = """insert into db table 이름(컬럼1, 컬럼2, 컬럼n) values(%s, %s, %s... n%s)
# engine.executemany(query, df.values.tolist())"""