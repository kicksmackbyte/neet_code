'''

# Prompt

Design your implementation of the linked list.
You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list.
Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

    * MyLinkedList() Initializes the MyLinkedList object.

    * int get(int index) Get the value of the indexth node in the linked list.
        - If the index is invalid, return -1.

    * void addAtHead(int val) Add a node of value val before the first element of the linked list.
        - After the insertion, the new node will be the first node of the linked list.

    * void addAtTail(int val) Append a node of value val as the last element of the linked list.

    * void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list.
        - If index equals the length of the linked list, the node will be appended to the end of the linked list.
        - If index is greater than the length, the node will not be inserted.

    * void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.


# Constraints

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.


'''

class LinkedListNode:

    def __init__(self, val=None, next=None, previous=None):

        self.val = val
        self.next = next
        self.previous = previous


class MyLinkedList:


    def __init__(self):

        self.head = None
        self.tail = None
        self.length = 0


    def __get_node(self, index: int) -> LinkedListNode:

        node = None

        if index < self.length:

            node = self.head

            for i in range(index):
                node = node.next

        return node



    def print(self) -> int:

        for i in range(self.length):
            node = self.__get_node(i)
            print(node.val)


    def get(self, index: int) -> int:

        node = self.__get_node(index)
        val = node.val if node else -1

        return val


    def addAtIndex(self, index: int, val: int) -> None:

        node = self.__get_node(index)
        previous = None

        if node:
            previous = node.previous

        new_node = LinkedListNode(val=val, next=node, previous=previous)

        if node:
            node.previous = new_node


        if index == 0:
            self.head = new_node
            self.tail = new_node

        elif index == self.length:
            self.tail = new_node

        self.length += 1


    def deleteAtIndex(self, index: int) -> None:

        node = self.__get_node(index)

        if node:
            previous = node.previous
            next_ = node.next

            if previous:
                previous.next = next_

            if next_:
                next_.previous = previous

        del node
        self.length -= 1


    def addAtHead(self, val: int) -> None:

        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:

        self.addAtIndex(self.length, val)



obj = MyLinkedList()
obj.print()

obj.addAtHead(1)
obj.print()

obj.addAtTail(3)
obj.print()

exit()
obj.addAtIndex(1, 2)
obj.print()

obj.get(1)
obj.print()

obj.deleteAtIndex(1)
obj.print()

obj.get(1)
obj.print()

