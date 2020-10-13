# 异常的捕获
try:
    a = 1
    print(a)
    i = 1 / 0  # 第三行没有执行
except (NameError, ZeroDivisionError) as ex: # ex 刚刚捕获的异常对象
    print(ex)
    print("出现名称异常")  # 异常被捕获到就不会之行代码了

