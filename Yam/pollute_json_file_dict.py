#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author : Yam
# Data : 2021/4/10 22:52

from JsonPollute import JsonPollute
import os
from tqdm import tqdm
import numpy as np

json_path = r"../json"  # 原始json文件存放路径
polluted_path = r"../input_json"  # 被污染后的json文件存放路径
temp_file_path = r"./temp_file.npy"

# 路径不存在则新建
if not os.path.exists(polluted_path):
    os.mkdir(polluted_path)

# 遍历 json_path 逐个读取文件并生成污染文件
print("init...")
# 加载临时文件
if os.path.exists(temp_file_path):
    labels_dict = np.load(temp_file_path).tolist()
else:  # 临时文件不存在则新建
    labels_dict = {}

for file_name in os.listdir(json_path):
    if file_name.split(".")[-1] != "json":
        # 不是json文件
        continue
    labels_dict.setdefault(file_name, 1)

print("pollute...")
for file_name, label in tqdm(labels_dict.items()):
    if label:  # 需要被污染
        # print(file_name)
        with open(os.path.join(json_path, file_name), "r",
                  encoding="utf8") as file:
            jsp = JsonPollute(file.read(),pollute_rate=0.2)  # 污染比率为 20%
        label,polluted_data = jsp.pollute()
        if not label:  # 污染成功
            labels_dict[file_name] = label  # 更新临时文件的记录
            with open(os.path.join(polluted_path, file_name), "w", encoding="utf8") as file:
                file.write(polluted_data)  # 写入
            np.save(temp_file_path, labels_dict)


