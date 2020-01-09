# 匿名函数

# 匿名函数结合普通函数使用

def test(a, b, func):
    result = func(a, b)
    return result


print(test(22, 33, lambda a, b: a + b))
