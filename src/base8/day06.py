class Person(object):
    def __init__(self, name):
        self.name = name

    def work(self):
        print(self.name + "开始工作了")
        #         person完成work,需要一把斧头
        # 在原始社会,人需要一把斧头
        #         axe = StoneAxe("花岗岩斧头")
        #         axe.cut_tree()
        # axe = SteelAxe("钢铁的斧头")
        # axe.cut_tree()
        #         工厂类创建
        axe = Steel_Axe_Factory().create_axe()
        axe.cut_tree()


class Axe(object):
    def __init__(self, name):
        self.name = name

    def cut_tree(self):
        print("%s斧头开始砍树" % self.name)


class StoneAxe(Axe):
    def cut_tree(self):
        print("使用石头做的斧头砍树")


class SteelAxe(Axe):
    def cut_tree(self):
        print("使用钢铁做的斧头砍树")


# 工厂方法模式
class Factory(object):
    def create_axe(self):
        pass


class Stone_Axe_Factory(Factory):
    def create_axe(self):
        return StoneAxe("花岗岩斧头")

class Steel_Axe_Factory(Factory):
    def create_axe(self):
        return SteelAxe("加钢斧头")


u = Person("张三")
u.work()
