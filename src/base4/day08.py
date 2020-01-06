# 1到4的阶乘
i = 1
result = 1
while i <= 4:
    result = result * i
    i += 1
print(result)


# 计算n的阶乘 递归 ----1. 在函数内部调用自己本身 2.本质上是一个方法的循环调用(有可能出现死循环)  3. 一定要定义递归的边界(退出循环)
def test1(n):  # 定义函数就是为了计算你n阶乘的
    if n == 1:
        return 1
    return n * test1(n - 1)


print(test1(5))


# 斐波纳契数列

# 递归函数生成斐波纳契数列
def get_num(n):
    if n == 1 or n == 2:
        return 1
    return get_num(n - 1) + get_num(n - 2)


# 定义空数组
nums = []
for i in range(1, 21):
    nums.append(get_num(i))

print(nums)
