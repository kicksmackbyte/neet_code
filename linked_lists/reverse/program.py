'''

# Prompt

Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.


# Constraints


0 <= The length of the list <= 1000.
-1000 <= Node.val <= 1000


'''


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None

        while(current):
            temp = current.next

            current.next = previous
            previous = current

            current = temp

        return previous


def print_list(node):

    while(node):

        print(node.val)
        node = node.next


d_node = ListNode("D", next=None)
c_node = ListNode("C", next=d_node)
b_node = ListNode("B", next=c_node)
a_node = ListNode("A", next=b_node)

print_list(a_node)

solution = Solution()
reversed_list = solution.reverseList(a_node)

print('\nSolution:')
print_list(reversed_list)
