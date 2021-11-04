# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
import math
import sys

# 平方与开平方
res = math.pow(10, 2)
res = math.sqrt(res, 2)

"""
==================================================================================
字符串
小写字母的ASCII码大于大写字母
==================================================================================
"""
s = "a"
# ASCII码 =》 字符串 相互转化
print("获取ASCII码", ord(s))
print("获取ASCII码", ord("A"))
print("ASCII码转字符串", chr(ord(s)))

import string

# 获取24字母
print("[A-Z]:", string.ascii_uppercase)
print("[a-z]:", string.ascii_lowercase)
print("[a-zA-Z]:", string.ascii_letters)
print("[0-9]:", string.digits)

print("[赋值字符串 * 10]", "1" * 10)
print("[赋值字符串 * 0]", "1" * 0)

"""
==================================================================================
数值类型
==================================================================================
"""
n = 100
print("[十进制转2进程]：", bin(n).replace("0b", ""))
# 字符串数值 转 16进制
print("16进制", int("8A2E", 16))

"""
==================================================================================
函数调用细节
max(iter, key=f)
sys.stdin.readline()
reversed(iter)
==================================================================================
"""
l = ["a", "abc", "ab", "abcd"]
_max = max(l, key=len)
print("[max 自定义比较函数]： 返回原数据", _max)
print("[max 自定义比较函数]： 返回原数据的长度", len(_max))

# import sys
#
# s = sys.stdin  # 阻塞： 等待输入
# print("s", s.readline())  # readline() 获取输入的内容
# s2 = sys.stdin.readline()  # 直接获取输入的内容
# print("s2", s2)

res = reversed(l)
print("[reversed()的返回值是迭代器]", res)
print("[reversed()的返回值=》转列表]", list(res))

"""
==================================================================================
排序
字符串默认排序： 
    - 按照单个字母的ASCII码排序，小写字母大于大写字母
    - 自定义按照字母出现次数排序，要求次数相同时，按照自然顺序(字母)
==================================================================================
"""
s = "sdkfsalgjsdkADKJKDHGNCH"
print("[sorted]: ", "".join(sorted(s)))
print("[sorted]: ", "".join(sorted(s, key=ord)))


# 取最大值
maxSize = sys.maxsize
maxFloat = float("inf")
minFloat = float("-inf")

if __name__ == '__main__':
    """
    注意事项：
    1. 类变量，最好不要直接使用 l = [], d = {} 方式定义，会因为浅拷贝，造成不同测试用例之间的干扰；
    建议在调用方法内部初始化 L = list() d = dict()
    
    
    """
    pass
