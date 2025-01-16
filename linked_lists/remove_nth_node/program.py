'''

# Prompt

You are given the beginning of a linked list head, and an integer n.
Remove the nth node from the end of the list and return the beginning of the list.


# Constraints

* The number of nodes in the list is sz.
* 1 <= sz <= 30
* 0 <= Node.val <= 100
* 1 <= n <= sz


'''


from typing import Optional


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def length(self):
        l = 0

        node = self
        while node:
            node = node.next
            l += 1

        return l


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        pos = head.length() - n

        if pos <= 1:
            return head.next

        node = head
        prev = None
        while pos > 0:
            prev = node
            node = node.next
            pos -= 1

        if prev:
            prev.next = node.next

        return head


d = ListNode(4)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)

solution = Solution()
answer = solution.removeNthFromEnd(a, 2)
