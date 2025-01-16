'''

# Prompt

You are given the head of a singly linked-list.
The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln


Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes.
Only nodes themselves may be changed.


'''

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        node = self
        while node:
            print(node.val)
            node = node.next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def _split_list(list_):

            slow = list_
            fast = list_

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return list_, slow


        def _reverse_list(node):

            prev = None

            while node and node.next:

                temp = node.next
                node.next = prev
                prev = node
                node = temp

            node.next = prev
            return node


        def _merge_lists(a, b):

            head = a
            while a or b:
                temp_1 = a.next if a else None
                temp_2 = b.next if b else None

                a.next = b

                if b:
                    b.next = temp_1

                a = temp_1
                b = temp_2

            return head


        #1. Split list in half
        _, b = _split_list(head)

        ##2. Reverse second half of list
        b_reversed = _reverse_list(b)

        ##3. Merge lists
        head = _merge_lists(head, b_reversed)
        return head


solution = Solution()

d = ListNode(8)
c = ListNode(6, d)
b = ListNode(4, c)
a = ListNode(2, b)

solution.reorderList(a)
a.print()
