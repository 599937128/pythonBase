# 字符串的实用

name = "dashiodhdsa"
print(name[0], name[1], len(name))
# 字符串截取  左闭右开 步长：表示下标位的规律
print(name[0:2])
print(name[::2])
print(name[2:])

# 字符串反转
print(name[-1::-1])

# 没有找到不会报错 返回-1
print(name.find("s"))  # 从左向右
print(name.rfind("s"))  # 从右向左

# 没有找到 直接会报错
print(name.index("s"))  # 从左向右
print(name.rindex("s"))  # 从右向左

# 统计每个字符串出现的次数
print(name.count("z"))

# 字符串的替换
print(name.replace("s", "z"))
print(name.replace("s", "z", 1))  # 1 代表替换的次数
print(name.split("s", 1))  # 1 代表切割的次数 split 不指定 则会将常用的分割 字符的情况 都进行分割
names = "chdsiuofhsiosdshio cfdsa dsmvc"
print(names.partition("s"))  # 将自己本身也当作一个元素 但是仅仅只会截取一次

# 将字符串第一个大写
print(names.capitalize())
# 把每一个字符串都大写
print(names.title())

# 字符串对齐
print(names.ljust(50))
print(names.rjust(50))
print(names.center(40))

# 删除字符串的空白字符 strip
nals = "    adasfd  "
print(nals.lstrip())
print(nals.rstrip())
print(nals.strip())

# 按照换行符分割  必须包含换行符
lines = "cv\ndsiof\njvdf\nsjd"
print(lines.splitlines())

# 判断字符串的组成

print(name.isalpha())
print(name.isdigit())
print(name.isalnum())  # 包含字母或者数字

# 列表转换为字符串
nameList = ['lv', 'lv', 'ly']
print("".join(nameList))
print("-".join(nameList))
