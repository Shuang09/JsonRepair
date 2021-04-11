#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author : Yam
# Data : 2021/4/10 22:54

"""
检查json文件
"""

from JsonPollute import json_check
import os
from tqdm import tqdm

# check_path = r"../json"
check_path = r"../input_json"

for file_name in tqdm(os.listdir(check_path)):
    if file_name.split(".")[-1] != "json":
        # 不是json文件
        continue
    try:
        with open(os.path.join(check_path, file_name), encoding="utf8") as file:
            data = file.read()
            label,_ = json_check(data)
            # if not label:
            #     print("invalid file {}".format(file_name))
            if label:
                print("valid file {}".format(file_name))
    except Exception as e:
        print("Error [{}] happened at file {}".format(e, file_name))