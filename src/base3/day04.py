# 判断传入实参的类型
def sum_num2(a, b):
    if not isinstance(a, (int, float)):
        print("传入的a是%s,不是一个数字类型" % a)
        return
    elif not isinstance(b, (int, float)):
        print("传入的b是%s,不是一个数字类型" % b)
        return
    else:
        sum = a + b
        return sum


sum  = sum_num2(3,"sss")
sum  = sum_num2("3","sss")
sum = sum_num2(3, 22)
print(sum)
