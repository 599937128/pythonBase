names = ["lv", "liao"]

# 在后面进行拼接
names.append("lu")
print(names)
ages = [1, 2, 3]

# 两个列表合成一个列表
names.extend(ages)

print(names)

# 在任意的地方进行插入
names.insert(2, "ha")
print(names)
# 修改选项
names[5] = 521
print(names)

# 查找元素 in  和  not in
if 3 in names:
    print("存在")

# index 下标位 count 出现的次数
names.insert(2, "ni")

print(names)

print(names.count("lv"))
print(names.index("lu"))

# 删除操作 del pop remove

# 删除 最后一个元素 并且打印
print(names.pop())

# 删除指定内容 remove
names.remove("liao")

print(names)

# 逆转
names.reverse()
print(names)

# sort
# names.sort()  使用排序必须保证元素类型相同
# names.sort(reverse=True)  降序排序
print(names)