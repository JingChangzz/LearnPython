"""
寻找水仙花数
水仙花数：一个3位数，他的每一位的3次幂的和等于它本身
"""

for i in range(100, 1000, 1):
    one = i // 100
    two = (i - one * 100) // 10
    three = i - one * 100 - two * 10
    if one ** 3 + two ** 3 + three ** 3 == i:
        print(i)
