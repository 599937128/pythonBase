# 带参数的函数
def test(r):
    s = 3.14 * (r ** 2)
    print("圆的面积为%s" % s)


# 调用函数计算圆的面积
r = 9.8
test(r)


def test2(num1, num2):  # num1 和 num2  为形参 不用再之前定义
    sum = num1 + num2
    print("%s加上%s的值为:%s" % (num1, num2, sum))


test2(21, 10)
