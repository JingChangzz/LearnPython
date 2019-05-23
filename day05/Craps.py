# -*- coding: utf-8 -*-
"""
玩家掷两个骰子，每个骰子点数为1-6，如果第一次点数和为7或11，则玩家胜；
如果点数和为2、3或12，则玩家输庄家胜。
若和为其他点数，则记录第一次的点数和，玩家继续掷骰子，直至点数和等于第一次掷出的点数和则玩家胜；若掷出的点数和为7则庄家胜。
   File Name：     Craps
   Author :       jing
   Date：          2019-05-23
"""
import random

times = 1
random1 = random.randint(1, 6)
random2 = random.randint(1, 6)
first = random1 + random2
print("第%s次骰子：%s, %s" % (times, random1, random2))
if first in (7, 11):
    print("player win")
elif first in (2, 3, 12):
    print("master win")
else:
    while True:
        random3 = random.randint(1, 6)
        random4 = random.randint(1, 6)
        times += 1
        print("第%s次骰子：%s, %s" % (times, random3, random4))
        if random3 + random4 == 7:
            print("master win")
            break
        elif random3 + random4 == first:
            print("player win")
            break
        else:
            continue
