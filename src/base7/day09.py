class A(object):

    name = '张三'
    def test1(self):
        print("---------A的test1方法")

    # 标示为类方法classMethod 类方法cls,代表当前的类
    @classmethod
    def test2(cls):
        cls.name = '李四'
        print("---------A的test2方法--类方法")

    @staticmethod    # 静态方法 属于类 没有默认传递的参数  可以通过类对象和类名调用
    def test3():
        # 静态方法修改类属性
        A.name = '王五'
        print("--------A的test3方法----静态方法")

a = A()
a.test2()
A.test2()
A.test3()
print(A.name)
