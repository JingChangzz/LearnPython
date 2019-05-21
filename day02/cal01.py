"""
运算符
"""

a = 1
b = 4
c = 7
d = 8
e = 13

a += b      # a = a+b
c -= a
d /= e
e *= b

print("a =", a)
print("c =", c)
print("d =", d)
print("e =", e)

flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print("flag1 =", flag1)
print("flag2 =", flag2)
print("flag3 =", flag3)
print("flag4 =", flag4)
print("flag5 = ", flag5)
print(flag1 is True)
print(flag2 is not False)
