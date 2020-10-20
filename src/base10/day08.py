# 写出一个函数,给定参数n,生成n个元素的值为1~n的随机数且不重复
import random


def create_list(n):
    temp = []
    while True:
        if len(temp) == n:
            break
        i = random.randint(1, n)
        if i not in temp:
            temp.append(i)
    return temp


if __name__ == '__main__':
    print(create_list(8))
