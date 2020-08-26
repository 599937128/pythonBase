class Person(object):
    def __init__(self, name):
        self.name = name

    def work(self, aex_type):
        print(self.name + "开始工作了")
        #         person完成work,需要一把斧头
        # 在原始社会,人需要一把斧头
        #         axe = StoneAxe("花岗岩斧头")
        #         axe.cut_tree()
        # axe = SteelAxe("钢铁的斧头")
        # axe.cut_tree()
#         工厂类创建
        axe = Factory.create_axe(aex_type)
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


# 工厂类
class Factory(object):

    # 生产斧头
    @staticmethod
    def create_axe(type):
        if type == "stone":
            return StoneAxe("花岗岩斧头")
        elif type == "steel":
            return SteelAxe("加钢斧头")
        else:
            print("传入类型不对")


u = Person("张三")
u.work("stone")
