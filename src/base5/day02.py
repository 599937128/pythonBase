# 只读文件
f = open("text.txt", "r")
# read 不加参数说明是读整个文件  加参数说明是读多少字节的值
content = f.read()
print(content)
f.close()
