'''

# Prompt

Design a Singly Linked List class.

Your LinkedList class should support the following operations:

* LinkedList()
    - will initialize an empty linked list.
* int get(int i)
    - will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
* void insertHead(int val)
    - will insert a node with val at the head of the list.
* void insertTail(int val)
    - will insert a node with val at the tail of the list.
* bool remove(int i)
    - will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
* int[] getValues()
    - return an array of all the values in the linked list, ordered from head to tail.

'''

from typing import List


class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def get(self, index: int) -> int:

        if index >= self.size:
            return -1

        current = self.head

        for _ in range(index):
            current = current.next

        return current.data


    def insertHead(self, val: int) -> None:

        node = LinkedListNode(val)
        node.next = self.head
        self.head = node

        if self.tail is None:
            self.tail = node

        self.size += 1


    def insertTail(self, val: int) -> None:

        node = LinkedListNode(val)

        if self.tail:
            self.tail.next = node

        self.tail = node

        if self.head is None:
            self.head = node

        self.size += 1


    def remove(self, index: int) -> bool:

        if index >= self.size:
            return False

        elif index == 0:
            self.head = self.head.next

        else:

            current = self.head

            for _ in range(index-1):
                current = current.next

            self.size -= 1

            if index == self.size:
                self.tail = current

            else:
                current.next = current.next.next

        return True


    def getValues(self) -> List[int]:

        values = []
        current = self.head

        while current:
            values.append(current.data)
            current = current.next

        return values


linked_list = LinkedList()
linked_list.insertHead(1)
linked_list.insertTail(2)
linked_list.insertHead(0)
linked_list.remove(1)

values = linked_list.getValues()
print(values)
