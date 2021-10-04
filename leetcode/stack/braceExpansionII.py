from typing import List


class Solution:
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


if __name__ == '__main__':
    sol = Solution()
    expression = "{{a,z},a{b,c},{ab,z}}"
    expression = "{a,b}c{d,e}f"
    expression = "{a{x,ia,o}w,{n,{g,{u,o}},{a,{x,ia,o},w}},er}"
    expression = "n{{c,g},{h,j},l}a{{a,{x,ia,o},w},er,a{x,ia,o}w}n"
    # expression = "{a,b},x{c,{d,e}y}"
    sol.braceExpansionII(expression)
