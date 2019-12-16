# 打印等边三角形
i = int(input("请输入你要打印的边长数:"))

a = 0

while a < i:
    b = 0
    while b < a:  # 打印空格
        print(" ", end="")
        b += 1
    c = i - a
    while c > 0:  # 打印星号
        print("*", end=" ")
        c -= 1
    print("")
    a += 1
