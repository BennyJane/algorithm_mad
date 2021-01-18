# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

"""
十进制转为其它进制
- 迭代方法

连续相除法：
    - 第一次： 初始值 / 进制数 = 商  ... 余数
    - 第N次： 上一次的商 / 进制数 = 商  ... 余数
    - 终止条件： 商=0；每次获取的余数需要保存到列表内
    - 最后： 余数列表倒排后，拼成字符串（需要通过映射将>=10的余数转为字母）
"""


def Solution(n, m):
    num_sign = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'b', 'C', 'D', 'E', 'F']
    mod_list = []  # 存储余数
    while True:
        n, y = divmod(n, m)  # 数值 / 进制，获取商、余数
        mod_list.append(y)  # 保存余数
        if n == 0:
            break
    print(mod_list)
    mod_list.reverse()
    result = [str(num_sign[i]) for i in mod_list]
    return "".join(result)


if __name__ == '__main__':
    n, m = 1000, 16
    print(Solution(n, m))
