'''

# Prompt

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
The new list should be made up of nodes from list1 and list2.


# Constraints

0 <= The length of the each list <= 100.
-100 <= Node.val <= 100


'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = None
        node = None
        merged_list = None

        while(True):

            val = None

            if list1 and list2:

                val_1 = list1.val
                val_2 = list2.val

                if val_1 <= val_2:

                    val = val_1
                    list1 = list1.next

                else:

                    val = val_2
                    list2 = list2.next


            elif list1:

                val = list1.val
                list1 = list1.next

            elif list2:

                val = list2.val
                list2 = list2.next

            else:
                break

            node = ListNode(val)

            if not head:
                head = node
                merged_list = node

            else:
                merged_list.next = node
                merged_list = node

        return head



def print_list(node):

    while(node):

        print(node.val)
        node = node.next


arr_1 = [1, 3, 7, 8, 11, 13]
arr_2 = [0, 2, 2, 7, 11, 15]

next_ = None

for a in arr_1[::-1]:

    node = ListNode(a, next_)
    next_ = node

list_1 = node


next_ = None

for a in arr_2[::-1]:

    node = ListNode(a, next_)
    next_ = node

list_2 = node

print_list(list_1)
print()
print_list(list_2)
print()

solution = Solution()
merged_list = solution.mergeTwoLists(list_1, list_2)
print_list(merged_list)
