from typing import Optional

from leetcode.utils import TreeNode


# 450. 删除二叉搜索树中的节点
# https://leetcode-cn.com/problems/delete-node-in-a-bst/
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        pre = TreeNode(float("inf"))
        pre.left = root

        def dfs(head: TreeNode):
            if not head:
                return

            if head.val > key:
                if head.left and head.left.val == key:
                    if not head.left.right:
                        head.left = head.left.left
                        return
                    else:
                        child_right = head.left.right
                        child_left = head.left.left
                        head.left = child_right
                        while child_right and child_right.left:
                            child_right = child_right.left
                        child_right.left = child_left
                else:
                    dfs(head.left)
            if head.val < key:
                if head.right and head.right.val == key:
                    if not head.left.right:
                        head.right = head.left.left
                        return
                    else:
                        child_right = head.left.right
                        child_left = head.left.left
                        head.right = child_right
                        while child_right and child_right.left:
                            child_right = child_right.left
                        child_right.left = child_left
                else:
                    dfs(head.right)
        dfs(pre)
        return pre.left
