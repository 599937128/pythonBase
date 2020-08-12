class A(object):

    name = '张三'
    def test1(self):
        print("---------A的test1方法")

    # 标示为类方法classMethod 类方法cls,代表当前的类
    @classmethod
    def test2(cls):
        cls.name = '李四'
        print("---------A的test2方法--类方法")

a = A()
a.test2()
A.test2()
print(A.name)
