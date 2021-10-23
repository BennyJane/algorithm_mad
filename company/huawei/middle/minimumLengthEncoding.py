from typing import List


# 820. 单词的压缩编码
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = set(words)
        arr = sorted(words, key=lambda s: -1 * len(s))
        res = ""
        for s in arr:
            # FIXME 确保s匹配已有字符串的后缀
            temp = s + "#"
            if temp not in res:
                res += temp
        return len(res)

    def minimumLengthEncoding2(self, words: List[str]) -> int:
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])

        return sum(len(word) + 1 for word in good)

    # TODO 字典树解决： 倒序存储


if __name__ == '__main__':
    sol = Solution()
    words = ["feipyxx", "e"]
    sol.minimumLengthEncoding(words)
