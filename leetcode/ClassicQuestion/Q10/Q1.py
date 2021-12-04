from typing import List


class Solution1:
    """
    有这样一个数组A，大小为n，相邻元素差的绝对值都是1。
    如：A={4,5,6,5,6,7,8,9,10,9}。
    现在，给定A和目标整数t，请找到t在A中的位置。
    除了依次遍历，还有更好的方法么？

    拓展：有一个int型数组，每两个相邻的数之间的差值不是1就是-1.
    现在给定一个数，要求查找这个数在数组中的位置。
    """

    def FindNumberInArray(self, arr, m, k) -> int:
        if m == 0:  # m == 0时，数组内所有值均为k
            return arr[0]
        n = len(arr)
        index = 0
        while index < n:
            gap = abs(arr[index] - k) // m
            if gap == 0:
                return index
            index += gap
        # 不存在
        return -1


class Solution2:
    """
    给你一个数组，其中数组中的每个值与相邻元素之间的差值的绝对值是m，
    现在给你一个目标值k，找到数组中所有等于k的元素的索引，使用集合返回。
    遍历的元素越少越好，无序
    List fun(List<Integer> list,int m,int k)
    就比如[1,2,3,2,1,0,-1,0,1] m=1 k=3 返回[2] ，
    k一定是数组中的某个值
    """

    def FindNumberInArray(self, arr, m, k) -> List[int]:
        if m == 0:
            return arr
        ans = list()
        nextIndex = abs(arr[0] - k) // m
        while nextIndex < len(arr):
            if nextIndex == 0:
                ans.append(nextIndex)
                # 当前值为k，则下一个k至少需要经过两步才能出现
                nextIndex += 2
            else:
                nextIndex += abs(arr[0] - k) // m
        return ans

    def FindNumberInArray2(self, arr, m, k) -> List[int]:
        if m == 0:
            return arr
        ans = list()
        n = len(arr)
        index = 0
        while index < n:
            gap = abs(arr[index] - k) // m
            if gap == 0:
                ans.append(index)
                index += 2
            else:
                index += gap

        return ans
