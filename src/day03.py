# 小明身高1.75, 体重80.5千克请根据bmi(体重除以身高的平方)，计算bim指数 体质
'''
低于18.5过轻
18.5-25正常
25-28过重
28-32肥胖
高于32严重肥胖
'''

h = float(input("请输入身高:"))
w = float(input("请输入体重:"))
print("小明的身高%.2f,体重%.2f" % (h, w))

bmi = w / (h ** 2)
if bmi < 18.5:
    print("过轻")
elif bmi >= 18.5 and bmi < 25:
    print("正常")
elif bmi >= 25 and bmi < 28:
    print("过重")
elif bmi >= 28 and bmi < 32:
    print("肥胖")
else:
    print("过度肥胖")
# 精确小数点后两位
print("小明的bmi指数为%.2f"%bmi)
