from typing import List


# 438. 找到字符串中所有字母异位词
class Solution1:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        width = len(p)
        n = len(s)
        if n < width:
            return []
        ori = dict()
        for c in p:
            ori[c] = ori.get(c, 0) + 1

        def check(tar):
            if len(tar.keys()) != len(ori.keys()):
                return False
            for k, v in ori.items():
                if tar.get(k, -1) != v:
                    return False
            return True

        ans = list()
        left, right = 0, 0
        temp = dict()
        while left < n:
            while right < n and right - left + 1 <= width:
                cur = s[right]
                temp[cur] = temp.get(cur, 0) + 1
                right += 1
            if check(temp):
                ans.append(left)
            leftChar = s[left]
            temp[leftChar] -= 1
            if temp[leftChar] == 0:
                temp.pop(leftChar)
            left += 1
        return ans

    def findAnagrams2(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)

        # 单独处理长度过小的情况
        if s_len < p_len:
            return []
        # 使用输出存储单个字符的数量
        ans = []
        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(p_len):
            # ord()函数，计算单个字符的ASCII码
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1

        if s_count == p_count:
            ans.append(0)

        # 只需要处理剩下的索引
        for i in range(s_len - p_len):
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i + p_len]) - 97] += 1
            # 利用PY中数组相等性质，直接判断
            if s_count == p_count:
                ans.append(i + 1)

        return ans


if __name__ == '__main__':
    sol = Solution1()
    s = "cbaebabacd"
    p = "abc"
    sol.findAnagrams(s, p)
