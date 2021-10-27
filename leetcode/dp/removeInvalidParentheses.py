from typing import List


# 经典题目：多种解决方案对比，技巧比较多

# 301. 删除无效的括号 （Hard）
# https://leetcode-cn.com/problems/remove-invalid-parentheses/
"""
思路：
暴力：找出合法子序列的数量以及删除字符个数，再筛选删除字符个树最小的数量
暴力：先计算最少删除字符个数，然后找出长度为target的合法子序列，统计数量
暴力：
"""
class Solution:
    # 长度较小，25以内，可以考虑暴力求解
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # 计算需要被删除的左右括号数目
        left_rm, right_rm = 0, 0
        # 模拟栈操作
        # TODO 该方法，即可以检测括号合法性，也可以统计出需要删除非法括号的最小数量
        for c in s:
            if c == "(":
                left_rm += 1
            elif c == ")":  # 弹出右括号，需要考虑左括号数量
                if left_rm == 0:
                    right_rm += 1
                if left_rm > 0:
                    left_rm -= 1
        # 回溯法
        valid_expressions = set()
        n = len(s)

        def dfs(index, leftRemove, rightRemove, exp: List[str]):
            if index == n:
                if leftRemove == 0 and rightRemove == 0 and self.isValid(exp):
                    valid_expressions.add("".join(exp))
                return
            cur = s[index]
            # 情况1： 删除当前符号
            if cur == "(" and leftRemove > 0:
                dfs(index + 1, leftRemove - 1, rightRemove, exp)
            if cur == ")" and rightRemove > 0:
                dfs(index + 1, leftRemove, rightRemove - 1, exp)

            # 情况2： 保留当前符号
            exp.append(cur)
            if cur != "(" and cur != ")":
                dfs(index + 1, leftRemove, rightRemove, exp)
            elif cur == "(":
                dfs(index + 1, leftRemove, rightRemove, exp)
            elif cur == ")":
                dfs(index + 1, leftRemove, rightRemove, exp)

            # 回溯法
            exp.pop()

        dfs(0, left_rm, right_rm, [])
        return list(valid_expressions)

    def isValid(self, word: str):
        count = 0
        for c in word:
            if c == "(":
                count += 1
            if c == ")":
                if count == 0:
                    return False
                else:
                    count -= 1
        return count == 0


class Solution1:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        lremove, rremove = 0, 0
        for c in s:
            if c == '(':
                lremove += 1
            elif c == ')':
                if lremove == 0:
                    rremove += 1
                else:
                    lremove -= 1

        def isValid(str):
            cnt = 0
            for c in str:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        def helper(s, start, lcount, rcount, lremove, rremove):
            if lremove == 0 and rremove == 0:
                if isValid(s):
                    res.append(s)
                return

            for i in range(start, len(s)):
                # FIXME 剪枝操作，同类型连续符号只需要考虑其中一个（最后一个）
                if i > start and s[i] == s[i - 1]:
                    continue
                # 如果剩余的字符无法满足去掉的数量要求，直接返回
                if lremove + rremove > len(s) - i:
                    break
                # 尝试去掉一个左括号
                if lremove > 0 and s[i] == '(':
                    helper(s[:i] + s[i + 1:], i, lcount, rcount, lremove - 1, rremove);
                # 尝试去掉一个右括号
                if rremove > 0 and s[i] == ')':
                    helper(s[:i] + s[i + 1:], i, lcount, rcount, lremove, rremove - 1);
                # TODO 无效操作？？？？
                # 统计当前字符串中已有的括号数量
                if s[i] == '(':
                    lcount += 1
                elif s[i] == ')':   # FIXME 不需要考虑左括号
                    if lcount > 0:
                        lcount -= 1
                    else:
                        rcount += 1
                # 当前右括号的数量大于左括号的数量则为非法,直接返回.
                if rcount > lcount:
                    break

        helper(s, 0, 0, 0, lremove, rremove)
        return res


# 广度优先搜索
class Solution3:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        ans = []
        currSet = set([s])

        while True:
            for ss in currSet:
                if isValid(ss):
                    ans.append(ss)
            if len(ans) > 0:
                return ans
            nextSet = set()
            for ss in currSet:
                for i in range(len(ss)):
                    if i > 0 and ss[i] == s[i - 1]:
                        continue
                    if ss[i] == '(' or ss[i] == ')':
                        nextSet.add(ss[:i] + ss[i + 1:])
            currSet = nextSet
        return ans


# 枚举子状态
class Solution4:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def checkValid(str, lmask, left, rmask, right):
            pos1, pos2 = 0, 0
            cnt = 0

            for i in range(len(str)):
                if pos1 < len(left) and i == left[pos1]:
                    if lmask & (1 << pos1) == 0:
                        cnt += 1
                    pos1 += 1
                elif pos2 < len(right) and i == right[pos2]:
                    if rmask & (1 << pos2) == 0:
                        cnt -= 1
                        if cnt < 0:
                            return False
                    pos2 += 1

            return cnt == 0

        def recoverStr(lmask, left, rmask, right):
            pos1, pos2 = 0, 0
            res = ""

            for i in range(len(s)):
                if pos1 < len(left) and i == left[pos1]:
                    if lmask & (1 << pos1) == 0:
                        res += s[i]
                    pos1 += 1
                elif pos2 < len(right) and i == right[pos2]:
                    if rmask & (1 << pos2) == 0:
                        res += s[i]
                    pos2 += 1
                else:
                    res += s[i]

            return res

        def countBit(x):
            res = 0
            while x != 0:
                x = x & (x - 1)
                res += 1
            return res

        lremove, rremove = 0, 0
        left, right = [], []
        ans = []
        cnt = set()

        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
                lremove += 1
            elif s[i] == ')':
                right.append(i)
                if lremove == 0:
                    rremove += 1
                else:
                    lremove -= 1

        m, n = len(left), len(right)
        maskArr1, maskArr2 = [], []
        for i in range(1 << m):
            if countBit(i) != lremove:
                continue
            maskArr1.append(i)
        for i in range(1 << n):
            if countBit(i) != rremove:
                continue
            maskArr2.append(i)
        for mask1 in maskArr1:
            for mask2 in maskArr2:
                if checkValid(s, mask1, left, mask2, right):
                    cnt.add(recoverStr(mask1, left, mask2, right))

        return [val for val in cnt]
