class Animal:
    def __init__(self):
        self.name = '动物'
        self.color = '黄色'

    def eat(self):
        print("=======吃饭=======")

    def sleep(self):
        print("=======睡觉========")


# 继承 继承父类的构造方法
class Dog(Animal):
    # 名字和父类一样 方法的重写
    def __init__(self, name):
        super().__init__()  # 主动调用父类的init方法
        self.name = name

    def eat(self):
        print("狗自己的eat方法")

    def shout(self):
        print("=======大叫========")


class Cat(Animal):
    # 调用自己的init方法 会覆盖父类的init的方法
    # def __init__(self):
    #     print('猫妖厨师花了')
    def catch(self):
        print("=======抓老鼠=======")


class ZangAo(Dog):
    def fight(self):
        print("=========战斗========")


# 如果子类中重写了父类的方法,优先调用子类的方法
dog = Dog('小白')
print(dog.color)
dog.eat()
dog.shout()

cat = Cat()
print(cat.name)
cat.eat()
cat.catch()

zangAo = ZangAo("藏獒")
zangAo.eat()
zangAo.fight()
