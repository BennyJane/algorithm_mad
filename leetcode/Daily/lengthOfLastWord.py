class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split(" ")
        for i in range(len(l), 0, -1):
            temp = l[i].strip()
            if len(temp) > 0:
                return len(temp)
        return 0