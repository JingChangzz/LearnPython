# -*- coding: utf-8 -*-
"""
    百钱白鸡问题
    鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，鸡翁、鸡母、鸡雏各几何？
   File Name：     OneHundred
   Author :       jing
   Date：          2019-05-22
"""

"""
    数学列公式：
    x, y, z >= 0
    x + y + z = 100
    5x + 3y + z/3 = 100
    -->  14x + 8y = 200
    -->  y = 25 - 7*x/4
"""

for x in range(0, 16, 1):
    y = 25 - 7 * x / 4
    if y == int(y):
        z = 100 - x - y
        print("x, y, z：%s, %s, %s" % (x, int(y), int(z)))
