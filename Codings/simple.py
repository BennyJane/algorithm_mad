# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
import random
import string

"""
1.如何随机获取26个字母大小写？如果给定不同字母不同的权重值，如果实现根据不同权重获取字母？
英文字母的ASCII标码 97-123

"""
print(string.ascii_letters)  # 获取大小写字符串
print(string.ascii_lowercase)  # 只获取小写字符串
print(string.ascii_uppercase)  # 只获取大写字符串

# chr(int) 返回Unicode字符串
char_list = [chr(i) for i in range(97, 123)]
print(random.choice(char_list))
print(random.sample(char_list, 5))

# 实现权重解决方案

weight_data = {'a': 10, 'b': 15, 'c': 50}


def random_weight(origin: dict) -> object:
    total = sum(origin.values())
    # return a + (b-a) * self.random()
    # 获取0-total之间的随机数
    selected_num = random.uniform(0, total)
    # selected_num = random.randint(0, total)
    sum_wight = 0
    for key in origin.keys():
        sum_wight += origin[key]
        # 大于等于最合理， 末尾total值不包括在内
        if sum_wight >= selected_num:  # 随机数落在该权重内
            return key
    return None


print(random_weight(weight_data))
