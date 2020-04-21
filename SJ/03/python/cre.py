import pandas as pd
import pymysql
from random import *
import numpy as np


# 전화번호 생성
def Create():
    i = str(randrange(1,9999)).zfill(4)
    j = str(randrange(1,9999)).zfill(4)
    return f"010{i}{j}"



for i in range(20):
    x = [ Create() for _ in range(1000)]
    sample_var = list(range(0, 1000))
    data = {
        "성":sample_var,
        "핸드폰 번호":x
        }

    sample_var.append("성")
    sample_var.reverse()
    x.append("휴대폰 번호")
    x.reverse()

    dataframe = pd.DataFrame(data)

    dataframe.to_excel('%s.xlsx'%i, header=False, index=False)