# 班级学生管理
print("=" * 30)
print("学生管理系统".center(30))
print("输入1：添加学生")
print("输入2：查找学生")
print("输入3：修改学生")
print("输入4：删除学生")
print("输入5：查看所有的学生")
print("输入6：退出")
# 一个学生包含许多信息，所以放到一个字典中，学生列表使用列表存储
stus = []
while True:
    operator = input("请输入你想要的操作：")
    if operator == "1":
        name = input("请输入学生的姓名:")
        age = int(input("请输入学生的年龄:"))
        qq = input("请输入学生的QQ号:")
        stu  = {}
        stu["name"] = name
        stu["age"] = age
        stu["qq"] = qq
        stus.append(stu)  # 相当于java 中 集合的add
        print("添加成功")
    if operator == "2":
        name = input("请输入你要查找学生的姓名:")
        for item in stus:
            if item["name"] == name.strip():
                print("%s 学生存在， 年龄为%s， qq号为%s" % (item["name"], item["age"], item["qq"]))
                break
        else:  # 这个是循环执行完成之后没有找到才进行提示，要是找到了就不执行了 这就是python的经典之处
            print("学生%s没有找到" % name)
    if operator == "5":
        print("序号\t名字\t年龄\tqq")
        for i, item in enumerate(stus, 1):
            print("%s\t%s\t%s\t%s\t" % (i, item["name"], item["age"], item["qq"]))
    if operator == 6:
        break
