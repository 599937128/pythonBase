class A(object):
    def test(self):
        print('A==========test()')


class B(object):
    def test(self):
        print('B===========test()')


class C(A, B):
    def test(self):
        print('C==========test()')


c = C()
c.test()
# 查看多继承的优先关系
print(C.__mro__)
