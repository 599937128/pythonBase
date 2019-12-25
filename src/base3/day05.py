# 求3个数的平均值
def avg_number3(a, b, c):
    if is_numbuer(a) and is_numbuer(b) and is_numbuer(c):
        return (a + b + c) / 3
    else:
        print("不能计算平均值")


def is_numbuer(a):
    if not isinstance(a, (int, float)):
        print("传入的实参%s,不是一个数字类型" % a)
        return False
    else:
        return True


avg = avg_number3(2, 4, 6)
avg = avg_number3(2, 4, "6")
print(avg)
