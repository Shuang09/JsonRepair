#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author : Yam
# Data : 2021/4/7 15:37

import json
import random


def json_check(json_str):
    """
    to check if json is valid
        1, valid
        0, invalid
    """
    try:
        json.loads(json_str)
    except json.JSONDecodeError:
        return 0, json_str
    else:
        return 1, json_str


class JsonPollute():
    """传入完整的json字符串(str格式)，随机污染后的字符串并标注"""

    def __init__(self, json_str, pollute_rate=0.2):
        """
        :param json_str: 必须是合法的json文件
        :param pollute_rate: 可以是 0 到 1 的浮点数，也可以是大于等于 1 的整数
        """
        assert json_check(json_str)[0], "传入的字符串必须是合法的json文件"
        assert pollute_rate > 0, "pollute_rate 必须是大于0的数"

        self.json_str = json_str
        self.temp_str = None
        self.length = len(json_str)

        # 随机污染的次数
        if pollute_rate < 1:
            # 传入的是比值
            self.__random_nums = max(int(pollute_rate * self.length), 1)
        else:
            # 传入的是次数
            self.__random_nums = min(self.length, int(pollute_rate))

    def __str__(self):
        return self.json_str if type(
            self.json_str) is str else self.json_str.decode()

    def plts(self):
        """polluted times"""
        return self.__random_nums

    def __random_cut(self):
        """随机切片"""
        data = self.temp_str
        index = random.randint(0, self.length - 1)
        prefix = data[:index]
        pick = data[index]
        postfix = data[index + 1:]
        return prefix, pick, postfix

    def random_pop(self):
        """随机选取json字符串中的某个字符，删除"""

        prefix, pick, postfix = self.__random_cut()
        self.length -= 1
        self.temp_str = prefix + postfix
        return

    def random_repeated(self):
        """随机选取json字符串中的某个字符并重复一次"""
        prefix, pick, postfix = self.__random_cut()
        self.length += 1
        self.temp_str = prefix + pick * 2 + postfix
        return

    def random_swap(self):
        """随机选取json字符串中的某个字符并与前后字符交换"""
        prefix, pick, postfix = self.__random_cut()
        if prefix:
            pick, prefix = prefix[-1], prefix[:-1] + pick
        else:
            pick, postfix = postfix[0], pick + postfix[1:]
        self.temp_str = prefix + pick + postfix
        return

    def random_insert(self):
        """随机选取json字符串的某个位置，并在之后随机插入一个字符"""
        prefix, pick, postfix = self.__random_cut()
        add_data = chr(random.randint(32, 126))  # 随机选择 ASCII码表中 32 ~ 126 范围的字符
        self.length += 1
        self.temp_str = prefix + pick + add_data + postfix
        return

    def pollute(self, cw=[1, 1, 1, 1]):
        """
        按照 pollute rate 随机污染 json 字符串
        :param cw: cumulative weights for [pop, swap, repeated, insert], default is [1,1,1,1]
        :return: polluted data
        """
        self.temp_str = self.json_str
        self.length = len(self.temp_str)
        funcs = [self.random_pop, self.random_swap, self.random_repeated,
                 self.random_insert]

        for func in random.choices(funcs, cum_weights=cw, k=self.__random_nums):
            func()
        return json_check(self.temp_str)


if __name__ == '__main__':
    with open("sample.json") as file:
        data = file.read()
        jsp = JsonPollute(data, pollute_rate=0.02)
        label = jsp.pollute()[0]
        print("polluted {} times\nlabel: {}".format(jsp.plts(), label))
