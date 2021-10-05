from typing import List


class Solution:
    """
    1. 先判断长度是否合适
    2. 再判断是否可以匹配（字母匹配 空字符匹配）
    """

    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        target = len(word)

        for i in range(m):
            temp = ""
            for j in range(n):
                c = board[i][j]
                if c == "#":
                    if len(temp) == target and self.check(temp, word):
                        return True
                    temp = ""
                elif c == " ":
                    temp += "_"
                else:
                    temp += c
            if len(temp) == target and self.check(temp, word):
                return True
        for i in range(n):
            temp = ""
            for j in range(m):
                c = board[j][i]
                if c == "#":
                    if len(temp) == target and self.check(temp, word):
                        return True
                    temp = ""
                elif c == " ":
                    temp += "_"
                else:
                    temp += c
            if len(temp) == target and self.check(temp, word):
                return True
        return False

    def check(self, arr, word):
        n = len(arr)
        left = True
        for i in range(n):
            if arr[i] != "_" and arr[i] != word[i]:
                left = True
                break
        right = True
        for i in range(n - 1, -1, -1):
            if arr[i] != "_" and arr[i] != word[n - 1 - i]:
                right = False
                break
        return left or right
