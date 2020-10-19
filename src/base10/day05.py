a = [1, 2, 3]
b = [[a[0] + i, a[1] + i, a[2] + i] for i in range(0, 99) if i % 3 == 0]
print(a)
print(b)
