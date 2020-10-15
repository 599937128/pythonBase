def isnull(str):
    if not str:
        return True
    elif str.strip() == '':
        return True
    else:
        return False


def test():
    print('-----------------------测谁能打开')


if __name__ == '__main__':  # 由python解释器主动执行的代码 该代码为了测试
    test()
