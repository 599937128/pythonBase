# 列表有序可重复
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
names2 = ["lv", "liao", "lu", "yan"]
# 第一种迭代方式 显示序号
j = 0
print("序号\t姓名")
for i in names2:
    j += 1
    print("%d\t%s" % (j, i))
print("="*30)
# 第二种方式 枚举方式 enumerate() 内置函数
for i,item in enumerate(names2, 1):   # 从1开始计数
    print("%d\t%s" % (i, item))