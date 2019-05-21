"""
输入的年份是否是闰年
"""
while True:
    year = input("请输入年份:")
    if isinstance(year, int):
        break
    else:
        print("请输入整数！")

result = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(result)
