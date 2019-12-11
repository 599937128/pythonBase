# continue 的使用
i = 1
while i <= 10:
    i += 1
    if i % 2 == 0:
        print("打印偶数%d" % i)
        continue
    print("当前的i为%d" % i)