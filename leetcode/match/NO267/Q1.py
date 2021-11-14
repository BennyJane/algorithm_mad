from typing import List


# https://leetcode-cn.com/contest/weekly-contest-267/problems/time-needed-to-buy-tickets/
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        target = tickets[k]

        ans = 0
        while target > 0:
            for i, val in enumerate(tickets):
                if val > 0:
                    tickets[i] = val - 1
                    ans += 1
                if i == k and tickets[i] == 0:
                    break
            target -= 1
        return ans
