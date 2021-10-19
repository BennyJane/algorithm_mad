class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        res = self.trie.findPrefix(word)
        return True


class Trie:
    def __init__(self):
        # 键：前一个字符；值： 存储下一个字符的Trie
        self.cache = {}
        self.isEnd = False

    def insert(self, word: str):
        cur_node = self
        for c in word:
            if not cur_node.cache.get(c):
                cur_node.cache[c] = Trie()
            cur_node = cur_node.cache.get(c)
        cur_node.isEnd = True

    def findPrefix(self, prefix: str) -> bool:
        cur_node = self
        for c in prefix:
            if c == ".":
                pass
            elif cur_node.cache.get(c):
                cur_node = cur_node.cache.get(c)
            else:
                return False
        return cur_node.isEnd
