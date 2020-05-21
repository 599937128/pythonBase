class Person:
    def __init__(self): # 构造方法
        self.name='张三'
        self.age=12
        print("对象初始化")

    def work(self):
        pass


p1 = Person()
print(p1.name)