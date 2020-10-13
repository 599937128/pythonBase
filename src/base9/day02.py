class PasswordException(Exception):
    def __init__(self, pwd, min_length):
        self.password = pwd
        self.min_lenght = min_length

    def __str__(self):
        return "%s的密码错误,密码的最小长度为%s" % (self.password, self.min_lenght)


def reg(username, password):
    if len(password) < 6:
        raise PasswordException(password, 6)  # raise 抛出指定的异常
    else:
        print("用户名为%s,密码为%s" % (username, password))


try:
    reg('zs', '123')
except Exception as ex:  # 两个exception 会按照顺序之行,如果第一个满足条件,则不会进入第二个异常
    print("第一个Exception")
    print(ex)
except PasswordException as ex:
    print("第二个Exception")
    print(ex)
