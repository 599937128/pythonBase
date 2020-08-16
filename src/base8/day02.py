class User(object):
    __instance__ = None

    def __init__(self, username):
        self.username = username

    @classmethod
    def get_instance(cls, name):
        # 0 None "" 都是false
        if not cls.__instance__:
            cls.__instance__ = User(name)
        return cls.__instance__


u1 = User("张胜男")
u2 = User("李四")
u3 = User.get_instance("王五")
u4 = User.get_instance("赵六")
print(u1 == u2)  # == 判断是不是一个对象, 返回True 则为一个对象
print(u3 == u4)
# 验证单利模式
print("u1的对象的内存地址是%s,u2对象的内存地址是:%s" % (id(u1), id(u2)))
print("u3的对象的内存地址是%s,u4对象的内存地址是:%s" % (id(u3), id(u4)))
