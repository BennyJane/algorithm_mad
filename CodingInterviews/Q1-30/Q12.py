# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
"""
=================================================================================
【勾股数元组】

和167题类似。
参考题目： https://blog.csdn.net/weixin_42304045/article/details/80456176?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-7&spm=1001.2101.3001.4242


https://blog.csdn.net/weixin_39781462/article/details/82669183
https://blog.csdn.net/SEVENY_/article/details/82748930?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-6.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-6.control
=================================================================================
"""


def Solution(start, end):
    res = []
    nums = [i for i in range(start, end + 1)]
    sqrt_nums = [i ** 2 for i in range(start, end + 1)]

    def gcd(m, n):
        # m， n 不为 0
        # 求两个数的最大公约数,若为1则互为质数,返回TRUE
        while m != 0:
            # m, n = n % m, m
            temp = m
            m = n % m  # m 取两者的余数
            n = temp
        if n == 1:
            return True
        else:
            return False

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            first = sqrt_nums[i]
            second = sqrt_nums[j]
            third = first + second
            if third in sqrt_nums:
                third_index = sqrt_nums.index(third)
                a = nums[i]
                b = nums[j]
                c = nums[third_index]
                # 判断两两是否互为质数
                if gcd(a, b) and gcd(a, c) and gcd(b, c):
                    res.append((a, b, c))
    return res


def Solution2(n, m):
    result = []
    ori = [i for i in range(n, m + 1)]
    ori_2 = [i ** 2 for i in ori]  # 避免后续重复计算

    # 判断两个数值是否互为质数
    def gcd(a, b) -> bool:
        """默认a,b 都是正整数"""
        while b != 0:
            # 连续用除数/余数，直到余数为0，跳出循环
            a, b = b, a % b
        if a == 1:
            return True
        else:
            return False

    _len = len(ori)
    for i in range(_len):
        for j in range(i, _len):  # FIXME 从i开始，避免重复
            third = ori_2[i] + ori_2[j]
            if third in ori_2:  # 三个数字可以构成勾股定理
                first_value = ori[i]
                second_value = ori[j]
                third_value = ori[ori_2.index(third)]
                if gcd(first_value, second_value) and \
                        gcd(first_value, third_value) and \
                        gcd(second_value, third_value):
                    result.append((first_value, second_value, third_value))

    return result


if __name__ == '__main__':
    start, end = 1, 20
    print(Solution(start, end))

    print(Solution2(start, end))
