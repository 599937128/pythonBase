def extendList(val, list=[]):
    list.append(val)
    return list


list1 = extendList(10)
list2 = extendList(123, ['a', 'b', 'c'])
list3 = extendList('a')
print("list1----为%s" % list1)
print("list2----为%s" % list2)
print("list3----为%s" % list3)
