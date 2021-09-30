
// 173. 二叉搜索树迭代器
// https://leetcode-cn.com/problems/binary-search-tree-iterator/solution/javashi-yong-zhan-yi-ci-die-dai-bu-xu-yao-ti-qian-/
class BSTIterator {

    private final Deque<TreeNode> queue = new ArrayDeque<>();

    public BSTIterator(TreeNode node) {
        while (node != null) {
            queue.addLast(node);
            node = node.left;
        }
    }

    public int next() {
        TreeNode curr = queue.pollLast();
        TreeNode node = curr.right; // 右子树遍历
        while (node != null) {
            queue.addLast(node);
            node = node.left;
        }
        return curr.val;
    }

    public boolean hasNext() {
        return !queue.isEmpty();
    }
}
