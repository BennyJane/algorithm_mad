from typing import List

from pip._internal.utils.misc import pairwise


# 944.删列造序
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # 空间复杂度为 O(m)，改用下标枚举可以达到 O(1)
        return sum(any(x > y for x, y in pairwise(col)) for col in zip(*strs))

    @staticmethod
    def test():
        str_list = ["cba", "daf", "ghi"]

        for col in zip(*str_list):
            print(col)
            for x, y in pairwise(col):
                print(x, y)


if __name__ == '__main__':
    Solution.test()
