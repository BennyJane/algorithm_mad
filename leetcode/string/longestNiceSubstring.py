# 1763. 最长的美好子字符串 SIMPLE
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def check(child):
            cnt = [0] * 26
            for c in child:
                index = ord(c.lower()) - ord('a')
                if c.islower():
                    cnt[index] = 0 if cnt[index] < 0 else 1
                else:
                    cnt[index] = 0 if cnt[index] > 0 else -1
            return sum(cnt) == 0

        ans = ""
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                tmp = s[i:j + 1]
                if len(tmp) > len(ans) and check(tmp):
                    ans = tmp
        return ans

    def longestNiceSubstring2(self, s: str) -> str:
        def check(child):
            lower_arr = [0] * 26
            upper_arr = [0] * 26
            for c in child:
                if c.islower():
                    lower_arr[ord(c) - ord('a')] = 1
                else:
                    upper_arr[ord(c) - ord('A')] = 1
            for i in range(26):
                if lower_arr[i] != upper_arr[i]:
                    return False
            return True

        ans = ""
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                tmp = s[i:j + 1]
                if len(tmp) > len(ans) and check(tmp):
                    ans = tmp
        return ans


# 2000. 反转单词前缀
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            index = word.index(ch)
            word = word[:index + 1][::-1] + word[index + 1:]
        return word
