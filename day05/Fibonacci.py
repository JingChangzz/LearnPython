# -*- coding: utf-8 -*-
"""
Fibonacci 数列
F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）
   File Name：     Fibonacci
   Author :       jing
   Date：          2019-05-22
"""

f = [1, 1]
print(f[0])
print(f[1])
for i in range(3, 11):
    f.append(f[i-2]+f[i-3])
    print(f[i-1])
