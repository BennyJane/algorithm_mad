from typing import Optional
from collections import deque, defaultdict

from leetcode.utils import TreeNode


class Solution1:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        # 直接使用布尔值表示 层数的奇偶性
        isOdd = False
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            pre = None
            for _ in range(size):
                node = queue.popleft()
                val = node.val
                # 先判断当前数值的奇偶性质
                if isOdd and val & 1 != 0:
                    # 奇数层: 非偶数,直接返回False
                    return False
                if not isOdd and val & 1 != 1:
                    # 偶数层: 非奇数,直接返回False
                    return False

                if pre is not None:
                    # 从第二个值判断大小关系
                    if isOdd and val >= pre:
                        return False
                    if not isOdd and val <= pre:
                        return False
                # 更新前一个值
                pre = val
                # 下一层节点放入队列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # 下一层奇偶性反转
            isOdd = not isOdd
        return True

    def isEvenOddTree2(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        # 0: 偶数 1: 奇数
        level = 0
        while queue:
            # 偶数层：最小值； 奇数层：整数的最大值
            preVal = float("inf") if level == 1 else 0
            nxt = []
            for node in queue:
                val = node.val
                if val % 2 == level:
                    return False
                if (level == 0 and val <= preVal) or (level == 1 and val >= preVal):
                    return False
                preVal = val
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            queue = nxt
            level = 1 - level
        return True

    # FIXME：深度优先, 每一次深度搜索都优先遍历每层的最左侧节点
    def isEvenOddTree3(self, root: Optional[TreeNode]) -> bool:
        """
        需要记录每一个节点，在当前层的前一个节点，用于比较大小
        需要记录每一个节点的层数 ==》寻找前一个节点
        """
        # d = defaultdict(list)
        d = dict()  # 记录不同层号的前一个数值

        def dfs(node, depth: int):
            isOdd = depth % 2 == 1
            if depth not in d:
                d[depth] = 0 if not isOdd else float("inf")
            pre = d.get(depth)
            val = node.val
            # 检测当前val 是否符号条件
            if isOdd:
                if val % 2 == 1 or val >= pre:
                    return False
            else:
                if val % 2 == 0 or val <= pre:
                    return False
            d[depth] = val

            if node.left and not dfs(node.left, depth + 1):
                return False
            if node.right and not dfs(node.right, depth + 1):
                return False
            return True

        return dfs(root, 0)
