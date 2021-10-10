from leetcode.utils import TreeNode


# 114. 二叉树展开为链表
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        left = root.left
        right = root.right
        if left:
            root.left = None
            root.right = left
            root = root.right
            self.flatten(root.right)
        if right:
            root.right = right
            root.left = None
            root = root.right
            self.flatten(root.right)

