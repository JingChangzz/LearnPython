# -*- coding: utf-8 -*-
"""
跑马灯程序
   File Name：     horse_race_lamp
   Author :       jing
   Date：          2019-05-26
"""
import os
import time

content = "杨千嬅My Beautiful Live演唱会"
while True:
    os.system("clear")   # 需要设置环境变量 TREM=xterm-color
    print(content)
    time.sleep(0.2)
    content = content[1:] + content[0]
