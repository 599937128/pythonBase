# 全局变量的修改 全局变量 定义在函数调用之前
names = ["zhangsan", "lisi", "wanghwu"]
student = {"name": "zhaoliu"}
a = "lvliao"
b = 200


# 在函数中修改全局变量 1 如果变量为可变类型 则可以直接修改该全局变量的内容  2 如果是可变类型 修改的则是变量的引用
def test1():
    print("全局变量为%s" % names)
    names[2] = "lvliao"
    student["age"] = 23
    global a
    a = "laogao"  # 修改全局变量
    global b  # 声明为全局变量
    b += 1


test1()
print(names)
print(student)
print(a)
print(b)
