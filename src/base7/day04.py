class Animal:
    def __init__(self):
        self.name = '动物'

    def eat(self):
        print("=======吃饭=======")

    def sleep(self):
        print("=======睡觉========")


# 继承 继承父类的构造方法
class Dog(Animal):
    def __init__(self, name):
        self.name = name

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


dog = Dog('小白')
dog.eat()
dog.shout()

cat = Cat()
print(cat.name)
cat.eat()
cat.catch()

zangAo = ZangAo("藏獒")
zangAo.eat()
zangAo.fight()
