# -*- coding: utf-8 -*-
"""
   寻找完美数
   完美数：一个数，它的所有真约数(不包括本身，包括1)的和等于它
   File Name：     FindPerfectNumber
   Author :       jing
   Date：          2019-05-22
"""

for i in range(1, 1000000000, 1):
    factor = 0
    for j in range(1, i):
        if i % j == 0:
            factor += j
    if factor == i:
        print(i)
