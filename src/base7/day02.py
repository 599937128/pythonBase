class User:
    def __init__(self, pw):
        if len(pw) >= 6:
            self.__password = pw
        else:
            print("密码为%s,密码不符合规定")

    def __str__(self):
        self.__say_hello()
        return '秘密为%s' % self.__password  # __属性为私有属性

    def __say_hello(self):  # 私有方法
        return 'hello'

    def get_password(self):
        return self.__password


u1 = User('123123')
print(u1.get_password())
print(u1)
