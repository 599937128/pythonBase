class Person:
    def __init__(self, name, age, height):  # 有参构造函数 初始化对象的方法
        self.name = name
        self.age = age
        self.height = height

    def introduec(self):
        print("姓名%s--年龄%s--身高%s" % (self.name, self.age, self.height))


p1 = Person("zhangsan", 19, 180)
p1.introduec()
