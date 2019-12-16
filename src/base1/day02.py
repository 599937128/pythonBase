# 条件判断 if else
age = int(input("请输入年龄："))
sex = input("请输入性别：")
# and表示并且 or 表示或者 not 表示不满足后面的条件
if age >18 and sex =='男':
    print("可以结婚了")
elif sex=='女':
    print("可以生孩子了")
else:
    pass; # 以后需要填出代码，为了语法保证不会出错

