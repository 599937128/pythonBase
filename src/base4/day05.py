# 不定长参数
def test(x, y, *args, z=10):  # args 里面的就是元祖
    print(x, y)
    print(args)
    sum1 = x + y
    for i in args:
        sum1 += i
    print(sum1)


test(2, 3, 4, 5, 6, 7, z=20)


def test2(x, *args, **kwargs):  # 相当于字典
    print(x)
    print(args)
    print(kwargs)
    sum1 = x
    for i in args:
        sum1 += i
    for i in kwargs.values():
        sum1 += i
    print(sum1)


test2(2, 3, 4, num1=5, num2=6)

# 集合的拆包
nums = [2, 3]
nums2 = {"num1": 5, "num2": 6}

test2(1, *nums, **nums2)
