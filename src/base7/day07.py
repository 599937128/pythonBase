class User(object):
    name = "zs" # 公共的类属性
    __password = "123456" # 私有的类属性
    def __init__(self, sex, userName):
        self.sex = sex
        self.userName = userName

u = User("男", "shad")
print(User.name)