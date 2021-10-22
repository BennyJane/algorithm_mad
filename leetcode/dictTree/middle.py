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
        # 返回：默认值均为Trie的字典
        trie = Trie()
        END = True

        for root in dictionary:
            # tire 作为initial参数，在reduce中func方法调用前执行
            # 对trie执行dict.__getitem__方法
            temp = reduce(dict.__getitem__, root, trie)
            temp[END] = root
        print(trie.keys())
        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur or END in cur:
                    break
                cur = cur[letter]
            return cur.get(END, word)

        return " ".join(map(replace, sentence.split()))


if __name__ == '__main__':
    sol = Solution()
    roots = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    sol.replaceWords2(roots, sentence)

    f = lambda x, y: x + y
    res = reduce(f, [1, 2, 3, 4], 10)
    print(res)
