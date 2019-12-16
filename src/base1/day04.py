# 从1加到100 偶数
i = 1
sum = 0
while i <= 100:
    if i%2==0:
       sum += i
    i += 1
print("从1加到100的和%d"%sum)

# 打印一个矩形
x = 1  # 长度
y = 1 # 宽度
while y <= 10:
    while x <= 10:
        print("*", end="")  # print() 默认换行
        x+=1
    x=1
    y+=1
    print("")


