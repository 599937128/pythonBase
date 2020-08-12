class User(object):
    name = "zs"  # 公共的类属性
    __password = "123456"  # 私有的类属性

    def __init__(self, sex, userName):
        self.sex = sex
        self.userName = userName


class QQ_User(User):
    pass


u = User("男", "shad")
# 如果对象的属性和类属性相同 如果使用对象访问属性 则访问对象的属性
print(User.name)
#  属性的继承(类属性) 类属性也可以使用类的对象访问类属性
print(QQ_User.name)

# 类属性的修改
User.name = 'lisi'
print(User.name)
# 删除对象的属性
# del u.name
