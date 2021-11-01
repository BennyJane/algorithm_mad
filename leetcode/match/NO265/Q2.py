from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        points = list()

        pre = head
        index = 0
        while pre and pre.next and pre.next.next:
            if pre.next.val > pre.val and pre.next.val > pre.next.next.val:
                points.append(index + 1)
            if pre.next.val < pre.val and pre.next.val < pre.next.next.val:
                points.append(index + 1)
            pre = pre.next
            index += 1
        if len(points) < 2:
            return [-1, - 1]
        n = len(points)
        minDistance = points[1] - points[0]
        for i in range(2, n):
            minDistance = min(minDistance, points[i] - points[i - 1])

        maxDistance = points[-1] - points[0]

        return [minDistance, maxDistance]
