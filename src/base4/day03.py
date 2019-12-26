# 函数返回多个结果 默认返回的是元祖 也可以返回列表
def test():
    a = 1
    b = 2
    return a, b


x, y = test()
print(x, y)
x = test()
print(x)
