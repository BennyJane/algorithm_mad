# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

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
