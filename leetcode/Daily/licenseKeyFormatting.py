class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ori = "".join(s.split("-"))
        ori = ori.upper()
        n = len(ori)

        retain = n % k
        index = 0
        ans = ""
        length = 0
        while index < n:
            if index < retain:
                ans += ori[index]
            elif index == retain:
                if len(ans) > 0:
                    ans += "-"
                ans += ori[index]
                length = 1
            else:
                if length == k:
                    ans += "-"
                    ans += ori[index]
                    length = 1
                else:
                    ans += ori[index]
                    length += 1
            index += 1
        return ans

    def licenseKeyFormatting2(self, s: str, k: int) -> str:
        ans = list()
        cnt = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] != "-":
                ans.append(s[i].upper())
                cnt += 1
                if cnt % k == 0:
                    ans.append("-")

        if ans and ans[-1] == "-":
            ans.pop()

        return "".join(ans[::-1])



if __name__ == '__main__':
    sol = Solution()
    sol.licenseKeyFormatting("5F3Z-2e-9-w", 4)
