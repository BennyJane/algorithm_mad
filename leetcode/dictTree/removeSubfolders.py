from typing import List


# 1233. 删除子文件夹
# https://leetcode-cn.com/problems/remove-sub-folders-from-the-filesystem/
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        asc_folder = sorted(folder, key=lambda x: len(x.split("/")))
        ans = []
        trie = Trie()
        for f in asc_folder:
            if not trie.search(f):
                ans.append(f)
            trie.add(f)
        return ans


class Trie:
    def __init__(self):
        self.cache = dict()
        self.isEnd = False

    def add(self, word: str):
        cur = self
        for c in word.split("/"):
            if c not in cur.cache:
                cur.cache[c] = Trie()
            cur = cur.cache[c]
        cur.isEnd = True

    # TODO 根据题目要求定义遍历逻辑
    def searchParent(self, prefix: str):
        # 寻找父文件目录
        cur = self
        for c in prefix.split("/"):
            if c not in cur.cache:
                # 路径不同IG
                return False
            cur = cur.cache[c]
            if cur.isEnd:  # 路径长度小于当前文件路径
                return True
        return True


# 直接暴力求解更快速度
class Solution1:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        asc_folder = sorted(folder, key=lambda x: len(x.split("/")))
        ans = set()

        for f in asc_folder:
            ans.add(f)
            for i, v in enumerate(f):
                if v == "/" and f[:i] in ans:
                    ans.remove(v)
                    break
        return list(ans)
