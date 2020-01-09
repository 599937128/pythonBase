# 匿名函数在动态代码中的使用

def test1(a, b, func):
    results = func(a, b)
    return results


func = input("请输入你要的操作:")
func = eval(func)  # 将字符串变为表达式
result = test1(12, 34, func)
print(result)
