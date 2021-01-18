# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
"""
=================================================================================
【最大矩阵和】 动态规划
最大子序和
https://leetcode-cn.com/problems/max-submatrix-lcci/solution/er-wei-zhuan-yi-wei-by-yyy-108/
参考Q65题目：一维数组的最大子序和


=================================================================================
"""


# 处理二维数组
def Solution2(matrix):
    def getMaxSumOfCols(cols):  # 找到一维数组的最大值
        n = len(cols)
        _max = cols[0]
        before_sum = cols[0]
        for i in range(1, n):
            if before_sum < 0:  # 前缀和小于0， 舍弃前面的累加值； 无论当前值为正、负，前缀和只会使得当前值更小
                before_sum = cols[i]
            else:
                before_sum = before_sum + cols[i]  # TODO 当前值的正负，不需要判断
            if before_sum > _max:
                _max = before_sum
        return _max

    # 确定行列数值
    row_num = len(matrix)
    col_num = len(matrix[0])
    _final_max = float("-inf")  # 极小值

    """
    遍历所有子矩阵
    """
    for c1 in range(col_num):  # 起始列
        col_sum = [0] * row_num  # 单列数组
        for c2 in range(c1, col_num):  # 列宽
            for r1 in range(row_num):
                col_sum[r1] += matrix[r1][c2]  # FIXME 累加的形式，计算单行c1-c2的和

            # print("col_sum", col_sum)
            max_col = getMaxSumOfCols(col_sum)
            # print("max_col", max_col)
            if max_col > _final_max:
                _final_max = max_col
    return _final_max


def Solution3(matrix):
    def getMaxOneMatrix(l):
        # FIXME 传入的是可变对象（列表）， 必须使用深拷贝，避免影响主程序中列表内容
        import copy
        ori = copy.deepcopy(l)
        for i in range(1, len(ori)):
            if ori[i - 1] >= 0:
                ori[i] = ori[i] + ori[i - 1]
        return max(ori)

    r_num = len(matrix)
    c_num = len(matrix[0])
    _final_max = float("-inf")

    for c1 in range(c_num):
        col_sum = [0 for _ in range(r_num)]
        for c2 in range(c1, c_num):
            for r in range(r_num):
                # FIXME 必须是累加符号
                col_sum[r] += matrix[r][c2]
            _max = getMaxOneMatrix(col_sum)
            if _max > _final_max:
                _final_max = _max
    return _final_max


if __name__ == '__main__':
    l1 = [
        [-3, 5, -1, 5],
        [2, 4, -2, 4],
        [-1, 3, -1, 3]
    ]

    print(Solution2(l1))

    l2 = [
        [-3, 5, -1, 5],
        [-1, 3, -1, 3],
        [2, 4, -2, 4],
        [2, 5, 4, -1],
    ]

    print(Solution2(l2))

    l3 = [
        [-3, 5, -1, 5],
        [-1, 3, -1, 3],
        [2, 4, -2, 4],
        [2, 5, 4, -1],
    ]

    print(Solution3(l3))

"""
for c1 in range(col_num):  # 起始列
    col_sum = [0] * row_num  # 单列数组
    for c2 in range(c1, col_num):  # 列宽
        for r1 in range(row_num):
            col_sum[r1] += matrix[r1][c2]   # FIXME 累加的形式，计算单行c1-c2的和

当c1=0时，
    - col_sum 存储了 0-0、0-1、 0-2、 0-3四种列宽的子矩阵，
        - 0-0 列下的子矩阵（行数不同）: 1 2 3 1-2 2-3 1-3, 子矩阵的最大和使用getMaxSumOfCols单独处理

"""
