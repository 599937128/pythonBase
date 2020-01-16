# os 模块的使用  修改文件夹下的所有文件(重命名)
import os

file_list = os.listdir("C:/Users/Admin/Desktop/壁纸")

for f in file_list:
    # print(f)
    dest_file = "re-" + f  # 重新命名后的文件名
    parent_dir = os.path.abspath("C:/Users/Admin/Desktop/壁纸")  # 获得父目录的绝对路径   其实这里是需要根据相对路径获取绝对路径
    # 文件的绝对路径为父目录的路径加上自己的文件名
    source_file = os.path.join(parent_dir, f)
    dest_file = os.path.join(parent_dir, dest_file)
    os.rename(source_file, dest_file)
