from typing import List
from itertools import chain


# 794. 有效的井字游戏
class Solution1:
    """
    不成立情况：
    O的数量比X多
    存在多个三连情况
    """

    def validTicTacToe(self, board: List[str]) -> bool:
        xCnt = oCnt = 0
        for c in chain(*board):
            if c == "X":
                xCnt += 1
            elif c == "O":
                oCnt += 1
        if oCnt > xCnt or xCnt - oCnt > 1:
            return False

        n = 3
        xSuccess = oSuccess = 0  # 三连数量
        # 检测三行与三列
        for row in range(n):
            # 行
            if board[row][0] == board[row][1] == board[row][2]:
                if board[row][0] == "X":
                    xSuccess += 1
                else:
                    oSuccess += 1
            # 列
            if board[0][row] == board[1][row] == board[2][row]:
                if board[0][row] == "X":
                    xSuccess += 1
                else:
                    oSuccess += 1
        if board[0][0] == board[1][1] == board[2][2]:
            if board[1][1] == "X":
                xSuccess += 1
            else:
                oSuccess += 1
        if board[0][2] == board[1][1] == board[2][0]:
            if board[1][1] == "X":
                xSuccess += 1
            else:
                oSuccess += 1
        if oSuccess > 0 and xSuccess > 0:
            return False
        elif xSuccess > 0:
            return xCnt - oCnt == 1
        elif oSuccess > 0:
            return xCnt == oCnt
        else:
            return xCnt - oCnt == 1
