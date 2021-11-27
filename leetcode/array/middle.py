import math
from typing import List, Optional
import random

# 随机反转数组
from leetcode.match.NO265.Q2 import ListNode


class Solution1:
    """
    idx = x * col + y
    使用单个数字表示矩阵中的坐标,col表示列数
    x的计算方式： idx // col
    y的计算方式： idx % col

    逐步索引随机函数的范围，
    当生成的随机函数不是末尾索引时，当前索引被占用，
    同时，将该索引在map中的对应值修改为末尾索引，
    表示，下次再次访问该索引时，实际占用的是末尾索引
    使用map记录被占用索引，下次再访问时，应该对应的索引位置，
    
    """

    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.total = m * n
        #
        self.map = dict()

    def flip(self) -> List[int]:
        # 随机整数：两端端点都包含在内
        x = random.randint(0, self.total - 1)
        self.total -= 1
        # 查找位置x对应的映射
        # 第一次访问时，返回值为自身；再次访问时，返回值是上次访问的末位索引
        idx = self.map.get(x, x)
        # 将x对应的映射位置，调整为 位置total对应的映射位置
        self.map[x] = self.map.get(self.total, self.total)
        return [idx // self.n, idx % self.n]

    def reset(self) -> None:
        self.total = self.m * self.n
        self.map.clear()


class Solution1_1:

    def __init__(self, m: int, n: int):
        self.m, self.n = m, n
        self.total = m * n
        # 向下取整： math.floor()
        # 确定桶高度
        self.bucketSize = math.floor(math.sqrt(m * n))
        # 初始化桶: 步长为单个桶高，确保最终位置大于 self.total
        self.buckets = [set() for _ in range(0, self.total, self.bucketSize)]

    def flip(self) -> List[int]:
        x = random.randint(0, self.total - 1)
        self.total -= 1
        sumZero = 0  # 计算桶中剩余0的个数
        curr = 0  # 计算当前位置: idx = x * col + y

        for i in range(len(self.buckets)):
            # 计算x在哪个桶中
            if sumZero + self.bucketSize - len(self.buckets[i]) > x:
                # 计算x在桶的那个位置
                for j in range(self.bucketSize):
                    if (curr + j) not in self.buckets[i]:
                        if sumZero == x:
                            self.buckets[i].add(curr + j)
                            return [(curr + j) // self.n, (curr + j) % self.n]
                        sumZero += 1
            curr += self.bucketSize
            sumZero += self.bucketSize - len(self.buckets[i])
        return []

    def reset(self) -> None:
        self.total = self.m * self.n
        for i in range(len(self.buckets)):
            self.buckets[i].clear()


# 382. 链表随机节点
class Solution2:
    # 先遍历链表，计算出链表长度 或 直接转化为数组 random.choice()
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.total = 0
        while head:
            self.total += 1
            head = head.next

    def getRandom(self) -> int:
        x = random.randint(0, self.total - 1)
        pre = self.head
        while x > 0:
            pre = pre.next
        return pre.val


class Solution2_1:

    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        count = 0
        reserve = 0
        cur = self.head
        while cur:
            count += 1
            rand = random.randint(1, count)
            if rand == count:
                reserve = cur.val
            cur = cur.next
        return reserve


# 398. 随机数索引
class Solution3:
    """
    内置函数
    """

    def __init__(self, nums: List[int]):
        count = dict()
        for i, n in enumerate(nums):
            if n in count:
                count[n].append(i)
            else:
                count[n] = [i]
        self.d = count

    def pick(self, target: int) -> int:
        arr = self.d[target]
        return random.choice(arr)


class Solution3_2:
    """
    水塘抽样
    """

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.total = len(nums)

    def pick(self, target: int) -> int:
        cnt = 0
        res = 0
        for i in range(self.total):
            if self.nums[i] == target:
                cnt += 1
                rand = random.randint(1, cnt)
                if rand == cnt:
                    res = i
        return res


if __name__ == '__main__':
    for i in range(0, 10, 3):
        print(i)
