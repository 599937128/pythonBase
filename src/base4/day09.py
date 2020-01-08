# 匿名函数

# 普通函数
def test1(a, b):
    return a + b


print(test1(11, 33))

# 匿名函数 函数体仅仅 只是支持表达式

funct1 = lambda x, y: x + y

print(funct1(22, 44))
