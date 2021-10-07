from leetcode.utils import TreeNode


# 114. 二叉树展开为链表
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.flatten(root.left)
        if root.right:
            right = root.right
            self.flatten(root.right)
            root.left.right = right
            root.right = None
