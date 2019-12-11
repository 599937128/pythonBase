print("111","222")
# row_input() python2中只有
print(111+222)
# 在python2中  input()输入的内容作为表达式，而不是字符串， python3作为字符串
name=input("请输入姓名:")
age=input("请输入年龄:")
# python3 input()输入的为字符串
age=int(age)+2
print("你输入的姓名为%s, 年龄为%s"%(name, age))