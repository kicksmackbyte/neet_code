'''

# Prompt

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list.

Otherwise, return false.

'''

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


solution = Solution()

a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-4)

a.next = b
b.next = c
c.next = d
d.next = b

assert solution.hasCycle(a)


a = ListNode(1)
b = ListNode(2)

a.next = b

assert not solution.hasCycle(a)
