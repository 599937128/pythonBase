# 打印字符串中字符出现的次数

str = input("请输入一个字符串:").strip()   # 去掉空格
res = {}
for i in str:
    if i in res:
        res[i] = res[i] + 1
    else:
        res[i] = 1
print(res)
