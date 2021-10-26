from leetcode.utils import TreeNode
from functools import lru_cache


# 337. 打家劫舍 III
# https://leetcode-cn.com/problems/house-robber-iii/
class Solution:
    # TODO 超时
    def rob(self, root: TreeNode) -> int:
        # def dfs(head, can_robbed=True):
        #     if not head:
        #         return 0
        #     # 分两种情况讨论
        #     temp1 = 0
        #     if can_robbed:  # 可以被偷
        #         temp1 += head.val
        #         temp1 += dfs(head.left, False)
        #         temp1 += dfs(head.right, False)
        #     temp2 = dfs(head.left, True)
        #     temp2 += dfs(head.right, True)
        #     return max(temp1, temp2)

        @lru_cache(None)
        def dfs(child_status: tuple):
            if not child_status[0]:
                return 0
            head, can_robbed = child_status
            # 分两种情况讨论
            temp1 = 0
            if child_status[1]:  # 可以被偷
                temp1 += head.val
                temp1 += dfs((head.left, False))
                temp1 += dfs((head.right, False))
            temp2 = dfs((head.left, True))
            temp2 += dfs((head.right, True))
            return max(temp1, temp2)

        return dfs(root, True)
