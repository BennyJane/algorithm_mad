from typing import List
import bisect


class Solution:
    # 剑指Offer51.数组中的逆序对
    # https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/
    def reversePairs(self, nums: List[int]) -> int:
        # 存储负数，升序
        q = []
        res = 0
        for v in nums:
            # 二分法查找待插入位置
            # 插入负数，实现按照绝对值大小降序排列
            i = bisect.bisect_left(q, -v)
            # [0, i)的值都小于 -v,因此实际值都大于v
            # [0, i)的长度表示左侧比当前v值大的数量，即逆序对的个数
            res += i
            # 在i索引位置插入：-v
            q[i:i] = [-v]
            # insert方法效率很低，建议使用上面的方法
            # q.insert(i, -v)
        return res

    def reversePairs2(self, nums: List[int]) -> int:
        # 存储已经遍历数据的升序排列
        q = []
        res = 0
        for v in nums:
            # 二分法查找待插入位置
            i = bisect.bisect_right(q, v)
            # q数组中[i:]的值都大于 v，包含索引i
            res += (len(q) - i)
            # 在i索引位置插入v值
            q[i:i] = [v]
            # insert方法效率很低，建议使用上面的方法
            # q.insert(i, v)
        return res


if __name__ == '__main__':
    s = Solution()
    array = [7, 5, 6, 4]
    s.reversePairs(array)
    print(array[1:1])
    array[1:1] = [10]
    print(array)
