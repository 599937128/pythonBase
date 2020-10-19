a = [1, 2, 45, 6, 3, 2, 1, 4, 5]


def change_list(li):
    temp = []
    for i in li:
        if i not in temp:
            temp.append(i)
    return temp


if __name__ == "__main__":
    print(change_list(a))
