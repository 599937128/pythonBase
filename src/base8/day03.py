class User(object):
    __instance__ = None

    def __init__(self, username):
        self.username = username

    def __new__(cls, name):
        if not cls.__instance__: # 保证 object.__new__(cls) 只会调用一次
            cls.__instance__ = object.__new__(cls)
        return cls.__instance__

u1 = User("张胜男")
u2 = User("李四")

print(u1 == u2)  # == 判断是不是一个对象, 返回True 则为一个对象
# 验证单利模式
print("u1的对象的内存地址是%s,u2对象的内存地址是:%s" % (id(u1), id(u2)))
