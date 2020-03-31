import pandas as pd
import pymysql
from random import *
import numpy as np


# 전화번호 생성
def Create():
    i = str(randrange(1,9999)).zfill(4)
    j = str(randrange(1,9999)).zfill(4)
    return f"010{i}{j}"

while True:

    # x : 전화번호 담긴 리스트
    x = [ Create() for _ in range(20000)]
    sample_var = list(range(0, 20000))

    df = pd.DataFrame()
    # df['id'] = sample_var
    df['Phone'] = x

    AA=sum(df.duplicated())
    print(AA)

    if AA==0:
        print('중복이 없습니다')
        break


print()
# 중복된 값 없음
"""
>>> print(sum(df.duplicated()))
>>> 0 
"""
# # pymysql 쓰는 경우
config = {
    'host': 'localhost',    #'호스트 이름',
    'port': 3306,   #'포트이름',
    'user': 'root' ,   #'유저이름',
    'passwd': 'qwer1234' ,  #'비밀번호',
    # 'charset': 'utf-8', #'utf8',
    'db': 'Contact' , #'db이름'
    }

# 사용하는 db마다 설정하는 값이 다르기 때문에 우선 pass
conn = pymysql.connect(**config)
cur = conn.cursor()

query = """insert into Number(Phone) values(%s) """
cur.executemany(query, df.Phone.tolist())
conn.commit()

