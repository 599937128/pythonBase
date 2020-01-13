# 交换两个变量的值
a = 12
b = 13
a, b = b, a  # 借用元祖
print(a, b)

x = 12
y = 20
z = 0
z = x
x = y
y = z

print(x, y)
