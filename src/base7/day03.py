class User:
    def __init__(self):
        print("=======对象初始化========")

    def __del__(self):
        print("======对象即将被回收,释放内存空间(内存回收)")


u1 = User()
u2 = u1
# 删除u1的引用
del u1
print("====" * 30)
# 删除u2的引用 对象的引用为空
del u2
print("*" * 60)
