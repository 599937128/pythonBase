import sys, random

print(sys.argv)
a = range(1, 10)
for i in a:
    print(i)
# 列表推导式
b = [1 for i in a]
c = [i for i in a]
d = [i ** 2 for i in a]  # 1到 9的平方
e = [x for x in range(1, 5) for y in range(0, 4)]
f = [(x, y, z) for x in range(1, 5) for y in range(0, 4) for z in range(6, 8)]
d = [i for i in range(1,101) if i % 2 == 1]  # 1到 100的奇数
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(d)
