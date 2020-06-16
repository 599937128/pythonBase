class User:
    def __str__(self):
        return "用户名称为:%s,密码为:%s" % (self.userName, self.passWord)

    def set_passWord(self, pw):
        if len(pw) > 6:
            self.passWord = pw
        else:
            print("秘密为%s,长度不符合规定" % pw)


u1 = User()
u1.userName = 'lv'
u1.set_passWord('1234567')
print(u1)
