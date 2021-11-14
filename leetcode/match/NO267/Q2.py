from typing import Optional

from leetcode.match.NO265.Q2 import ListNode


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        array = list()
        while cur:
            array.append(cur.val)
        n = len(array)
        newHead = ListNode(-1)
        pre = newHead
        nextLength = 1
        left = 0
        while left < n:
            realLength = nextLength
            if left + nextLength >= n:
                realLength = n - left
            if realLength % 2 == 0:
                for i in range(left + realLength - 1, left - 1, -1):
                    pre.next = ListNode(array[i])
                    pre = pre.next
            else:
                for i in range(left, left + realLength):
                    pre.next = ListNode(array[i])
                    pre = pre.next

            nextLength += 1
            left += realLength
        return newHead.next

    def reverseEvenLengthGroups1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        nextLength = 1

        while cur:
            stack = list()

            temp = nextLength
            realLength = 0
            nextNode = cur
            while temp > 0 and nextNode:
                stack.append(nextNode.val)
                nextNode = nextNode.next
                temp -= 1
                realLength += 1
            if realLength % 2 == 0:
                while stack:
                    cur.next = ListNode(stack.pop())
                    cur = cur.next
                cur.next = nextNode
            cur = nextNode
            nextLength += 1
        return head
