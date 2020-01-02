# 传参数需要注意的东西

def test(x, y):
    x = x.replace("c", "C")
    y.append(10)
    print("x指向的内存地址为:%s" % id(x))
    print("y指向的内存地址为:%s" % id(y))


a = "abccba"
b = [1, 2, 4, 6, 7]
print("a指向的内存地址为:%s" % id(a))
print("b指向的内存地址为:%s" % id(b))
test(a, b)
