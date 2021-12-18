from typing import List


class Solution1:
    # 419. 甲板上的战舰
    # 岛屿的数量
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                if i - 1 >= 0 and board[i - 1][j] == "X":
                    continue
                if j - 1 >= 0 and board[i][j - 1] == "X":
                    continue
                ans += 1

        return ans

    def countBattleships2(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])

        ans = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                ans += 1
                x, y = i, j
                while x + 1 < m and board[x + 1][y] == "X":
                    board[x + 1][y] = "."
                    x += 1
                # 初始变量必须重新初始化，避免上面x的修改，影响后续的执行
                x, y = i, j
                while y + 1 < n and board[x][y + 1] == "X":
                    board[x][y + 1] = "."
                    y += 1
        return ans

    def countBattleships3(self, board: List[List[str]]) -> int:
        ans = 0
        m, n = len(board), len(board[0])
        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch == 'X':
                    row[j] = '.'
                    for k in range(j + 1, n):
                        if row[k] != 'X':
                            break
                        row[k] = '.'
                    for k in range(i + 1, m):
                        if board[k][j] != 'X':
                            break
                        board[k][j] = '.'
                    ans += 1
        return ans

