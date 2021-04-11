import os
import shutil

input_path = r"../input_json"
operate_path = r"../json"
target_path = r"../target_json"

# file_name = set()
#
# input_files = os.listdir(input_path)
# for input_file in input_files:
#     file_name.add(input_file)
#
# operated_files = os.listdir(operate_path)
# # for file in operated_files:
# #     if file in file_name:
# #         from_path = os.path.join(operate_path, file)  # 旧文件的绝对路径(包含文件的后缀名)
# #         to_path = target_path + '/' + file  # 新文件的绝对路径
# #         shutil.copy(from_path, to_path)  # 完成复制黏贴
#
# target_files = os.listdir(target_path)
# target_file_name = set()
# for file in target_files:
#     target_file_name.add(file)
#
# print(len(target_file_name))
# print( (len(file_name)))

os.chdir("../")
files = os.listdir()
for file in files:
    try:
        if ".json" in file:  # 需要保留指定的对立面，即批量删除其对立面的       【实际使用时需更改】
            print(file)  # 打印出特定类型之外的文件，即要删除的对象。这样的操作等价于保留指定类型的文件
            #os.remove(file)                                  # 批量删除特定类型文件的核心命令，确定后再操作
    except:
        pass
