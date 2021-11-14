from typing import List


class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.vec = 1  # 1 东
        self.allLength = (self.width - 1 + self.height - 1) * 2

    def dfs(self, step):
        if step >= self.allLength:
            step %= self.allLength
            if step == 0:
                if self.x == 0 and self.y == 0 and self.vec == 1:
                    self.vec = 4
                if self.x == 0 and self.y == self.height - 1 and self.vec == 4:
                    self.vec = 3

                if self.y == 0 and self.x == self.width - 1 and self.vec == 2:
                    self.vec = 1
                if self.y == self.height - 1 and self.x == self.width - 1 and self.vec == 3:
                    self.vec = 2
        if step == 0:
            return

        if self.vec == 1:
            res = self.width - 1 - self.x
            if step <= res:
                self.x += step
            else:
                self.x = self.width - 1
                self.vec = 2
                self.dfs(step - res)
        elif self.vec == 2:
            res = self.height - 1 - self.y
            if step <= res:
                self.y += step
            else:
                self.y = self.height - 1
                self.vec = 3
                self.dfs(step - res)
        elif self.vec == 3:
            res = self.x
            if step <= res:
                self.x -= step
            else:
                self.x = 0
                self.vec = 4
                self.dfs(step - res)
        elif self.vec == 4:
            res = self.y
            if step <= res:
                self.y -= step
            else:
                self.y = 0
                self.vec = 1
                self.dfs(step - res)

    def move(self, num: int) -> None:
        self.dfs(num)

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        if self.vec == 1:
            return "East"
        elif self.vec == 2:
            return "North"
        elif self.vec == 3:
            return "West"
        elif self.vec == 4:
            return "South"
