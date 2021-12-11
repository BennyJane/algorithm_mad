from functools import lru_cache
from typing import List

"""
-------------------------------------------------------
括号专题
-------------------------------------------------------
"""


# 1111. 有效括号的嵌套深度
# https://leetcode-cn.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/
class Solution1:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = list()
        d = 0

        for c in seq:
            if c == '(':
                d += 1
                ans.append(d % 2)
            if c == ')':
                ans.append(d % 2)
                d -= 1
        return ans

    def maxDepthAfterSplit2(self, seq: str) -> List[int]:
        ans = []
        d = 0
        for c in seq:
            if c == '(':
                d += 1
                ans.append(d % 2)
            if c == ')':
                ans.append(d % 2)
                d -= 1
        return ans

    def maxDepthAfterSplit3(self, seq: str) -> List[int]:
        ans = list()
        for i, ch in enumerate(seq):
            if ch == '(':
                ans.append(i % 2)
            else:
                ans.append(1 - i % 2)
            # 上面的代码也可以简写成
            # ans.append((i & 1) ^ (ch == '('))
            # C++ 和 Javascript 代码中直接给出了简写的方法
        return ans


# 856. 括号的分数
class Solution2:
    def scoreOfParentheses(self, s: str) -> int:
        stack = list()

        for c in s:
            if c == "(":
                stack.append(c)
            else:
                # 栈顶部是左括号
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                else:
                    pre = 0
                    while stack and stack[-1] != "(":
                        pre += stack.pop()
                    stack.pop()
                    stack.append(pre)
        return sum(stack)  # "()()" 最后栈中可能存在多个值


# 1087. 花括号展开
class Solution3:
    def expand(self, s: str) -> List[str]:
        return []


# 20.有效的括号
class Solution4:
    # 注意:多括号类型 还是 单括号
    def isValid(self, s: str) -> bool:
        stack = list()
        d = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in ("(", "[", "{"):
                stack.append(c)
            else:
                if not stack:
                    return False
                pre = stack.pop()
                if d[c] != pre:
                    return False
        return not stack

    def isValid_ERROR(self, s: str) -> bool:
        # 使用数字记录括号数量
        # FIXME 错误原因 ([)] 无法识别; 仅仅适用于单个括号判断
        dp = [0] * 3

        for c in s:
            if c == "(":
                dp[0] += 1
            elif c == ")":
                dp[0] -= 1
                if dp[0] < 0:
                    return False
            elif c == "[":
                dp[1] += 1
            elif c == "]":
                dp[1] -= 1
                if dp[1] < 0:
                    return False
            elif c == "{":
                dp[2] -= 1
            elif c == "}":
                dp[2] -= 1
                if dp[2] < 0:
                    return False

        return True

    def isValid2(self, s: str) -> bool:
        dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1


# 678.有效的括号字符串 HARD
class Solution5:
    # 包含*符号,可以被当作左右括号 或 空字符串 处理
    # 整体字符串长度在100以内
    def checkValidString(self, s: str) -> bool:
        if len(s) == 0:
            return True
        # 记录索引位置
        stack = list()  # 记录括号
        star = list()  # 记录*号位置
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == "*":
                star.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    if star and star[-1] < i:
                        star.pop()
                    else:
                        return False
            else:
                continue
        if not stack:
            return True
        # 单括号
        # * 作为右括号使用 ==> 所有星号替换为右括号后,等效于基础题目:基于索引判断括号有效性
        # 每个左括号索引右侧(包含左括号在内): 右括号数量必须等于左括号数量
        while stack and star:
            left = stack.pop()
            right = star.pop()
            if left > right:
                return False
        return True

    # 贪心: 星号只存在两种情况: 只转化为左括号 or 只转化为右括号
    def checkValidString2(self, s: str) -> bool:
        minCnt = maxCnt = 0

        for c in s:
            if c == "(":
                minCnt += 1
                maxCnt += 1
            elif c == ")":
                # 任何情况下，未匹配的左括号数量必须非负，
                # 因此当最大值变成负数时，说明没有左括号可以和右括号匹配，返回false。
                minCnt = max(minCnt - 1, 0)
                maxCnt -= 1
                if maxCnt < 0:  # 如果将所有星号当作左括号
                    return False
            else:  # 星号
                minCnt = max(minCnt - 1, 0)
                maxCnt += 1

        return minCnt == 0

    # 上面方法的拆解
    def checkValidString3(self, s: str) -> bool:
        """
        遍历两次，第一次顺序，第二次逆序。
        第一次遇到左括号加一，右括号减一，星号加一，最后保证cnt >= 0,也就是可以保证产生的左括号足够
        第二次遇到右括号加一，左括号减一，星号加一，最后保证cnt >= 0,也就是可以保证产生的右括号足够
        当两次遍历都是True，那么说明有效
        """

        def help(a):
            cnt = 0
            for c in s if a == 1 else reversed(s):
                if c == '(': cnt += a
                if c == ')': cnt += -a
                if c == '*': cnt += 1
                if cnt < 0:
                    return False
            return True

        return help(1) and help(-1)


# 22.括号生成 重点：出现三次
class Solution6:
    # 长度只有8.考虑暴力求解
    # 回溯法
    def generateParenthesis1(self, n: int) -> List[str]:
        ans = list()

        def dfs(p: List[str], left, right):
            if left == 0:  # 同时处理只有left为0 与 left=right=0的情况
                temp = list(p)
                for i in range(right):
                    temp.append(")")
                ans.append("".join(temp))
                return
            elif right == 0 and left > 0:  # 提前结束不合理情况
                return
            # 只有在右括号比左括号数量多的时候,才允许添加右括号
            if right > left:
                p.append(")")
                dfs(p, left, right - 1)
                p.pop()
            # 添加左括号,只需要保证不为0
            if left > 0:
                p.append("(")
                dfs(p, left - 1, right)
                p.pop()

        dfs(["("], n - 1, n)
        return ans

    # 暴力求解
    def generateParenthesis2(self, n: int) -> List[str]:
        ans = list()

        def generate(B: List[str]):
            if len(B) == 2 * n:
                if valid(B):
                    ans.append("".join(B))
            else:
                B.append("(")
                generate(B)
                B.pop()
                B.append(")")
                generate(B)
                B.pop()

        def valid(A):
            cnt = 0
            for c in A:
                if c == "(":
                    cnt += 1
                else:
                    cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0

        generate(list())
        return ans

    def generateParenthesis3(self, n: int) -> List[str]:
        ans = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return ans

    # FIXME 递归函数设计
    @lru_cache(None)
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                # -1 : 表示(a)b中的括号
                for right in self.generateParenthesis(n - 1 - c):
                    ans.append('({}){}'.format(left, right))
        return ans


# 856. 括号的分数
class Solution7:
    """
    最小结构:() -> 1
    相邻结构:AB -> A+B
    嵌套结构:(A) -> 2*A
    """

    # 一题多解
    def scoreOfParentheses(self, s: str) -> int:
        stack = list()

        for c in s:
            if c == "(":
                stack.append(c)
            else:
                # 栈顶部是左括号
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                else:
                    # 处理嵌套结构
                    pre = 0
                    while stack and stack[-1] != "(":
                        pre += stack.pop()
                    stack.pop()
                    stack.append(pre * 2)
        return sum(stack)

    # 分治思想
    """
    先将字符串,拆分为多个相邻结构,然后去除一次外部括号,再重复处理内部字符串(拆相邻结构,去除外部括号...),
    直到内部为空,则返回1; 

    第一个小问题: 如何将字符串拆分为多个平衡字符串? 从前往后遍历，每个左右括号数相等的位置，就是分界点
    第一个小问题: 如何统计一个括号字符串的深度? 
    """

    def scoreOfParentheses2(self, s: str) -> int:
        def dealChild(left, right) -> int:
            balance = score = 0

            last = left
            for i in range(left, right):
                c = s[i]
                if c == '(':
                    balance += 1
                else:
                    balance -= 1
                    if balance == 0:
                        if i - last == 1:
                            score += 1
                        else:
                            score += 2 * (dealChild(last + 1, i))
                        last = i + 1
            return score

        return dealChild(0, len(s))

    def scoreOfParentheses3(self, S):
        def F(i, j):
            # Score of balanced string S[i:j]
            ans = bal = 0

            # Split string into primitives
            for k in range(i, j):
                bal += 1 if S[k] == '(' else -1
                if bal == 0:
                    if k - i == 1:
                        ans += 1
                    else:
                        ans += 2 * F(i + 1, k)
                    i = k + 1

            return ans

        return F(0, len(S))

    # 计算最小结构的深度
    def scoreOfParentheses4(self, S):
        stack = [0]  # The score of the current frame

        for x in S:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)

        return stack.pop()

    def scoreOfParentheses5(self, S):
        ans = bal = 0
        for i, x in enumerate(S):
            if x == '(':
                bal += 1
            else:
                bal -= 1
                if S[i - 1] == '(':
                    ans += 1 << bal
        return ans


# 921.使括号有效的最小添加
class Solution8:
    # 测试用例： )( , ())
    # 贪心思想

    # 统计有效括号的最大字符数量
    def minAddToMakeValid(self, s: str) -> int:
        n = len(s)
        cnt = 0
        stack = list()
        for c in s:
            if c == "(":
                stack.append(c)
            else:
                # FIXME 优先消耗已有的左括号
                if stack and stack[-1] == "(":
                    stack.pop()
                    cnt += 2
        return n - cnt

    def minAddToMakeValid2(self, s: str) -> int:
        n = len(s)
        cnt = 0
        left = 0
        for c in s:
            if c == "(":
                left += 1
            else:
                if left > 0:
                    left -= 1
                    cnt += 2
        return n - cnt

    def minAddToMakeValid3(self, S):
        ans = bal = 0
        for symbol in S:
            bal += 1 if symbol == '(' else -1
            # It is guaranteed bal >= -1
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal


# 1021. 删除最外层的括号 SIMPLE
class Solution9:
    # 寻找嵌套结构
    def removeOuterParentheses(self, s: str) -> str:
        n = len(s)
        left = right = 0
        ans = ""

        bal = 0
        while right < n:
            bal += 1 if s[right] == "(" else -1
            if bal == 0:
                ans += s[left + 1: right]
                left = right + 1
            right += 1

        return ans


# 1087. 花括号展开
class Solution10:
    """
    我们用一个特殊的字符串S来表示一份单词列表，之所以能展开成为一个列表，是因为这个字符串S中存在一个叫做「选项」的概念：
    单词中的每个字母可能只有一个选项或存在多个备选项。如果只有一个选项，那么该字母按原样表示。
    如果存在多个选项，就会以花括号包裹来表示这些选项（使它们与其他字母分隔开），例如 "{a,b,c}" 表示["a", "b", "c"]。
    例子："{a,b,c}d{e,f}"可以表示单词列表["ade", "adf", "bde", "bdf", "cde", "cdf"]。
    请你按字典顺序，返回所有以这种方式形成的单词。

    示例 1：
    输入："{a,b}c{d,e}f"
    输出：["acdf","acef","bcdf","bcef"]
    示例 2：

    输入："abcd"
    输出：["abcd"]

    提示：
    1 <= S.length <= 50
    你可以假设题目中不存在嵌套的花括号
    在一对连续的花括号（开花括号与闭花括号）之间的所有字母都不会相同
    """

    # 花括号不存在嵌套关系
    # 利用差分思想，判断括号左右边界
    def expand(self, s: str) -> List[str]:
        stack = [""]
        n = len(s)

        left = right = 0
        # FIXME 标识字符串是否处于括号内部
        # bal=0 括号外，bal = 1 括号内部
        bal = 0
        while right < n:
            if s[right] == "{":
                bal += 1
                left = right + 1  # 记录括号边界
            elif s[right] == "}":
                bal -= 1
                temp = list()
                for pre in stack:
                    # 直接遍历的方法只适用于都是单字符的情况
                    # 处理不同长度字符的情况 inner = s[left: right].split(",)
                    for c in s[left: right]:
                        if c == ",":
                            continue
                        temp.append(pre + c)
                stack = temp
            elif s[right] != "," and bal == 0:
                # TODO 核心点：判断条件，不为逗号，且bal == 0
                for i, c in enumerate(stack):
                    stack[i] = c + s[right]
            right += 1
        # 确保字典序
        stack.sort()
        return stack

    # 分治|递归
    def expand2(self, s: str) -> List[str]:

        def dfs(prefix: str, s: str) -> None:
            # ---- 剪枝
            if not s:
                res.append(prefix)
                return
            # ---------- 第一个是‘{’
            if s[0].isalpha() == 0:
                tmp = ""
                i = 0
                while i < len(s):
                    if s[i] == '}':
                        tmp = s[1:i]
                        break
                    i += 1
                tmp = tmp.split(',')
                tmp.sort()
                for c in tmp:
                    dfs(prefix + c, s[i + 1:])
            # ---------- 第一个是子母
            else:
                i = 0
                while i < len(s):
                    if s[i] == '{':
                        break
                    i += 1
                dfs(prefix + s[:i], s[i:])

        res = []
        dfs("", s)
        return res


# 1096.花括号展开II  HARD
class Solution11:
    # 分治思想

    # 模拟法
    def braceExpansionII2(self, expression: str) -> List[str]:
        n = len(expression)
        stack = []

        for i, c in enumerate(expression):
            if c == "{":
                stack.append(c)
            elif c == "}":
                set
                pass
            else:
                stack.append(c)
        return []

    # 自己实现：过于繁琐
    def braceExpansionII(self, expression: str) -> List[str]:
        stack = []

        multi_char = ""
        for c in expression:
            if c != '}':
                if c == "," or c == "{":
                    if multi_char:
                        if stack and stack[-1] not in (",", "{"):
                            pre = stack.pop()
                            temp = self.deal(pre, [multi_char])
                            stack.append(temp)
                        else:
                            stack.append(multi_char)
                        multi_char = ""
                    stack.append(c)
                else:
                    multi_char += c
            else:
                # 需要先将multi_char 入栈
                if multi_char:
                    stack.append(multi_char)
                    multi_char = ""

                right = []
                while stack and stack[-1] != "{":
                    pre = stack.pop()
                    if pre == ",":
                        pre2 = stack.pop()
                        right = self.merge(pre2, right)
                    else:
                        right = self.deal(pre, right)
                # 弹出左侧括号
                stack.pop()
                while stack and stack[-1] not in (",", "{"):
                    pre = stack.pop()
                    right = self.deal(pre, right)
                stack.append(right)
        if not stack:
            return [] if not multi_char else [multi_char]
        ans = []
        for arr in stack:
            if arr == ",":
                continue
            ans.extend([c + multi_char for c in arr])
        return sorted(ans)

    def deal(self, pre, arr: List[str]):
        res = list()
        if type(pre) == str:
            pre = [pre]
        if not arr:
            return pre
        for p in pre:
            for b in arr:
                temp = p + b
                if temp not in res:
                    res.append(temp)
        return res

    def merge(self, pre, arr: List[str]):
        if type(pre) == str:
            pre = [pre]
        if not arr:
            return pre
        for p in pre:
            if p not in arr:
                arr.insert(0, p)
        return arr


# 1249. 移除无效的括号
class Solution12:
    # 非法括号： 剩余的左括号； 多余的右括号
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return s
        delIndex = list()
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    delIndex.append(i)
            else:
                pass
        delIndex.extend(stack)
        ans = ""
        for i, c in enumerate(s):
            if i not in delIndex:
                ans += c

        return ans


# 1541.平衡括号字符串的最少插入次数 不熟练
class Solution13:
    # 经典案例： ))())(, )(, ()

    # 情况1： 右括号缺少，直接补充
    # 情况2： 左括号缺少，再遇到下一左括号时，需要先补充左括号，并重置bal

    # FIXME 错误案例： ()())) 不满足两个右括号连续的要求
    def minInsertions(self, s: str) -> int:
        ans = 0
        left = bal = 0
        for c in s:
            if c == "(":
                if bal < 0:
                    cnt = -1 * bal
                    if cnt % 2 == 0:
                        ans += cnt // 2
                    else:
                        ans += cnt // 2 + 2
                    left = 0
                elif bal > 0:
                    ans += bal
                    left = 0
                left += 2
                bal = 2
            else:
                bal -= 1
        if bal > 0:
            ans += bal
        if bal < 0:
            bal = abs(bal)
            if bal % 2 == 0:
                ans += bal // 2
            else:
                ans += bal // 2 + 2
        return ans

    # 分段处理连续右括号的数量
    def minInsertions2(self, s: str) -> int:
        n = len(s)
        left = right = 0
        ans = 0

        # 根据左右符号数量，计算补充括号
        def stats(l, r) -> int:
            if l * 2 == r:
                return 0
            elif l * 2 > r:
                return l * 2 - r
            else:
                cnt = r - l * 2
                if cnt % 2 == 0:
                    return cnt // 2
                else:
                    return cnt // 2 + 2

        index = 0
        while index < n:
            c = s[index]
            if c == "(":
                # 处理匹配规则
                if right > 0:
                    ans += stats(left, right)
                right = left = 0
                index += 1
            else:
                right += 1
            index += 1
        ans += stats(left, right)
        return ans

    def minInsertions3(self, s: str) -> int:
        length = len(s)
        insertions = leftCount = index = 0

        while index < length:
            if s[index] == "(":
                leftCount += 1
                index += 1
            else:
                if leftCount > 0:
                    leftCount -= 1
                else:
                    insertions += 1

                if index < length - 1 and s[index + 1] == ")":
                    index += 2
                else:
                    insertions += 1
                    index += 1

        insertions += leftCount * 2
        return insertions


# 1614. 括号的最大嵌套深度
class Solution14:
    def maxDepth(self, s: str) -> int:
        ans = 0
        bal = 0
        for c in s:
            if c == "(":
                bal += 1
                ans = max(ans, bal)
            elif c == ")":
                bal -= 1

        return ans


# 1003. 检查替换后的词是否有效
class Solution20:
    def isValid(self, s: str) -> bool:
        stack = list()

        for c in s:
            if c == "c":
                if len(stack) < 2:
                    return False
                if stack[-1] == "b" and stack[-2] == "a":
                    stack.pop()
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack  # 最后应该为空


# 17.电话号码的字母组合
class Solution21:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:  # 特例处理
            return list()
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        # 回溯法
        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations
