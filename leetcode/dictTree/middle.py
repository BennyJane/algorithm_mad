from functools import reduce
from typing import List
import collections


# 648. 单词替换
class Solution:
    # 暴力求解： 不会超时
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # 根节点需要去重
        dict_set = set(dictionary)
        words = sentence.split()

        ans = []
        for c in words:
            # 处理单词每个子序列，判断是否为词根
            n = len(c)
            # 长度为1-n，索引范围
            for i in range(1, n):
                child = c[:i]
                if child in dict_set:
                    ans.append(child)
                    break
            else:
                ans.append(c)
        return " ".join(ans)

    # 字典树
    def replaceWords2(self, dictionary: List[str], sentence: str) -> str:
        # TODO 使用lambda 定义了建议字典树
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for root in dictionary:
            reduce(dict.__getitem__, root, trie)[END] = root

        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur or END in cur:
                    break
                cur = cur[letter]
            return cur.get(END, word)

        return " ".join(map(reduce, sentence.split()))
