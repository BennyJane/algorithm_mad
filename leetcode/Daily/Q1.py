from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        for i in range(n):
            row = [0 for _ in range(n)]
            col = [0 for _ in range(n)]
            for j in range(n):
                rowStr = board[i][j]
                if rowStr != ".":
                    row[int(rowStr) - 1] += 1
                colStr = board[j][i]
                if colStr != ".":
                    col[int(colStr) - 1] += 1

            if not Solution.check(row):
                return False
            if not Solution.check(col):
                return False

        startPoints = []
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                temp = [i, j]
                startPoints.append(temp)

        width = 3
        index = 0
        while index < len(startPoints):
            count = [0 for _ in range(n)]
            point = startPoints[index]
            for i in range(width):
                for j in range(width):
                    x = point[0] + i
                    y = point[1] + j
                    s = board[x][y]
                    if s != ".":
                        count[int(s) - 1] += 1
            if not Solution.check(count):
                return False
            index += 1

        return True

    @staticmethod
    def check(arr: List[int]):
        for c in arr:
            if c > 1:
                return False
        return True


if __name__ == '__main__':
    res = [
        [".", ".", "4", ".", ".", ".", "6", "3", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["5", ".", ".", ".", ".", ".", ".", "9", "."],
        [".", ".", ".", "5", "6", ".", ".", ".", "."],
        ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
        [".", ".", ".", "7", ".", ".", ".", ".", "."],
        [".", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."]]

    sol = Solution()
    sol.isValidSudoku(res)
