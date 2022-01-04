from collections import defaultdict, deque
from typing import List


# 444. 序列重建
class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        if not sequences:
            return False

        inDeg = defaultdict(int)  # 统计每个节点的入度
        graph = defaultdict(list)  # 构建图
        # 统计
        num_set = set()
        for seq in sequences:
            # 记录sequences中出现的所有数字
            # 等效于
            num_set |= set(seq)
            # 序列含义: 表达节点的前后关系, 前一个节点 指向 后一个节点, 后一个节点入度增加1
            for i in range(len(seq) - 1):
                graph[seq[i]].append(seq[i + 1])
                inDeg[seq[i + 1]] += 1

        # 若数字集合与org长度不等或不一致，直接返回False
        if len(num_set) != len(nums) or set(nums) != num_set: return False

        # 通过BFS排序
        q = deque([node for node in num_set if node not in inDeg])
        res = []
        while q:
            if len(q) > 1: return False  # 若同一层有不止一个则说明结果不唯一
            tmp = q.popleft()
            res.append(tmp)
            if tmp in graph:
                for node in graph[tmp]:
                    inDeg[node] -= 1
                    if not inDeg[node]:
                        q.append(node)

        return res == nums  # 判断是否生成的唯一顺序res与org一致
