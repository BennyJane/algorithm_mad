class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 字典树定义

class Trie:
    def __init__(self):
        self.cache = dict()
        self.isEnd = False

    def addWord(self, word: str):
        pre = self
        for c in word:
            if c not in pre.cache:
                pre.cache[c] = Trie()
            pre = pre.cache[c]
        pre.isEnd = True

    def search(self, word: str) -> bool:
        """
        检索单词是否存在，需要保证最后一个节点的isEnd=True
        :param word:
        :return:
        """
        tail = self.findTail(word)
        return tail is not None and tail.isEnd

    def startWith(self, prefix: str) -> bool:
        tail = self.findTail(prefix)
        return tail is not None

    def findTail(self, word: str):
        pre = self
        for c in word:
            if c not in pre.cache:
                return None
            pre = pre.cache[c]
        return pre
