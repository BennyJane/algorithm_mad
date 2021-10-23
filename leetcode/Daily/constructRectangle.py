from typing import List
import math


#
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        n = int(math.sqrt(area))

        for i in range(n, 0, -1):
            if area % i == 0:
                m = area // i
                return [m, i]
        return [area, 1]

    # L*W = area and L >= W
    # W * W  <= area
    def constructRectangle2(self, area: int) -> List[int]:
        w = int(math.sqrt(area))
        while w > 0:
            if area % w == 0:
                break
            w -= 1
        return [area // w, w]


if __name__ == '__main__':
    print(math.sqrt(122122))
    sol = Solution()
    sol.constructRectangle(122122)
