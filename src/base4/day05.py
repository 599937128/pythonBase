# 不定长参数
def test(x, y, *args, z=10):  # args 里面的就是元祖
    print(x, y)
    print(args)
    sum1 = x + y
    for i in args:
        sum1 += i
    print(sum1)


test(2, 3, 4, 5, 6, 7, z=20)
