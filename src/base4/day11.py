# 匿名函数在排序中的应用
stus = [{"name": "zs", "age": 21}, {"name": "lv", "age": 22}]

a = [2, 3, 45, 6, 7, 78, 1]
print(a)
a.reverse()
print(a)
a.sort(reverse=True)
print(a)

stus.sort(key=lambda x: x["name"])
print(stus)
