# 设置默认的缺省值参数 有缺省参数必须放置到最后面
def test(x, y, z=10, w=10):
    print(x, y, z)
    return x + y + z


sum1 = test(1, 2)
print(sum1)

sum2 = test(1, 2, z=30)
print(sum2)
