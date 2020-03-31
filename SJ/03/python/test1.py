import pandas as pd
import pymysql
from random import *
import numpy as np


# 전화번호 생성
def Create():
    i = str(randrange(1,9999)).zfill(4)
    j = str(randrange(1,9999)).zfill(4)
    return f"010{i}{j}"

# x : 전화번호 담긴 리스트
x = [ Create() for _ in range(20000)]
sample_var = list(range(0, 20000))

df = pd.DataFrame()
# df['id'] = sample_var
df['Phone'] = x
# print(x)
print(sample_var)