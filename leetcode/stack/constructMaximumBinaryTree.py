from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        max_value = max(nums)
        index = nums.index(max_value)
        node = TreeNode(val=max_value)

        left_node = self.constructMaximumBinaryTree(nums[:index])
        node.left = left_node
        if index + 1 < len(nums):
            right_node = self.constructMaximumBinaryTree(nums[index + 1:])
            node.right = right_node
        return node


# https://leetcode-cn.com/problems/maximum-binary-tree-ii/
# 998. 最大二叉树 II
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            node = TreeNode(val=val)
            return node
        cur = root.val
        # 当前节点值与val的关系
        if cur > val:
            # TODO 简化
            if root.right:
                right_val = root.right.val
                if val > right_val:
                    node = TreeNode(val=val)
                    node.left = root.right
                    root.right = node
                else:
                    node = self.insertIntoMaxTree(root.right, val)
                    root.right = node
            else:
                node = TreeNode(val=val)
                root.right = node
        else:
            node = TreeNode(val=val)
            node.left = root
            root = node
        return root

    def insertIntoMaxTree2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val < val:
            node = TreeNode(val=val)
            node.left = root
            return node
        root.right = self.insertIntoMaxTree2(root.right, val)
        return root
