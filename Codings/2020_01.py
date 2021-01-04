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
res = random.choice(char_list)



