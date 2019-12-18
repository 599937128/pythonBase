# 字典的使用 dict 对应java中的map 极快的查找速度 无序键值对
d = {"lv": 95, "lu": 75, "wang": 90}
print(d["lv"])

stus = {"name": "zs", "age": 33, "sex": "男"}
print(stus)
# 使用中括号获取值，如果键值不存在，会返回报错，但是如果根据get获取，如果键值不存在则不会报错
stus["name"] = "ww"  # 不存在则新增，存在则进行覆盖
print(stus)
print(stus.get("age"))

# 使用in 判断键存在于字典中
print("name" in stus)

# 删除操作 del 会直接回收内存
del stus["name"]  # 删除该键的性别信息
# del stus  # 删除整个字典信息

# stus.clear() 不会立即清除内存

# 1 len() 获取键的个数
print(len(stus))

# 2 keys() 获取所有的键的列表
print(stus.keys())

for k in stus.keys():
    print(k)
# 3 values() 返回所有的值
for v in stus.values():
    print(v)
# 4 items() 返回所有的键和值
print("=" * 30)
for item in stus.items():
    print("key为:%s, value为:%s" % item)  # item 本事就是元组 所以直接就可以使用这种写法
# 判断某一个key在字典中
key = "name"
print(key in stus)
# print(stus.has_key("age")) has_key 在python3 中废弃
