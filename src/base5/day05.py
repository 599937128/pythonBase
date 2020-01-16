# 获取某一类文件下是否包含hello的文件
import os

file_list = []


# 递归函数,该函数中所有的目录都采用绝对路径, parent_dir -- 文件所在的父目录的绝对路径 file_name表示当前要去处理的文件或者是目录
def find_hello(parent_dir, file_name):
    file_abspath = os.path.join(parent_dir, file_name) # 当前要处理的文件或者是目录的绝对路径
    if os.path.isdir(file_abspath): # 判断当前的文件是一个目录
        for f in os.listdir(file_abspath):
            find_hello(file_abspath, f) # 递归调用自己本身
    else:
        if file_abspath.endswith('py'):  # 如果是以py文件结尾的 则进行操作即可
            if read_and_find_hello(file_abspath):  # 如果文件中包含有hello则返回true
                file_list.append(file_abspath)
    return file_list

def read_and_find_hello(py_file):
    flag = False
    f = open(py_file, encoding='utf-8')
    while True:
        line = f.readline()
        if line == '':  # 文件读到最后一行循环终止
            break
        elif 'hello' in line:
            flag = True
            break
    f.close()
    return flag


list = find_hello("D:/python/pyIdeaPro/pyBase", "src")
print(list)
