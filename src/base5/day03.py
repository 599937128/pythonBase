# 文件的拷贝
source_file = "C:\\Users\\Admin\\Desktop\\timg.jpg"
dest_file = "copy-" + source_file[source_file.rfind("\\") + 1:]
print("目标文件的名称为%s" % dest_file)
source_f = open(source_file, "rb")

dest_f = open(dest_file, "wb")

# 读取原始文件
centent = source_f.read()

dest_f.write(centent)

source_f.close()
dest_f.close()
