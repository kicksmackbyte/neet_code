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

        print()


    def get(self, index: int) -> int:

        node = self.__get_node(index)
        val = node.val if node else -1

        return val


    def addAtHead(self, val: int) -> None:

        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:

        self.addAtIndex(self.length, val)


    def addAtIndex(self, index: int, val: int) -> None:

        if (index == 0) and (self.length == 0):

            node = LinkedListNode(val=val, next=None, previous=None)

            self.head = node
            self.tail = node

        elif (index == 0):

            node = LinkedListNode(val=val, next=self.head, previous=None)

            self.head.previous = node
            self.head = node

        elif index == self.length:

            node = LinkedListNode(val=val, next=None, previous=self.tail)

            self.tail.next = node
            self.tail = node

        elif index < self.length:

            node = self.__get_node(index)

            new_node = LinkedListNode(val=val, next=node, previous=node.previous)

            if node.previous:
                node.previous.next = new_node

            node.previous = new_node

        else:
            return

        self.length += 1


    def deleteAtIndex(self, index: int) -> None:

        if (index == 0) and (self.head):

            self.head = self.head.next

            if self.head:
                self.head.previous = None

        elif (index == self.length-1):

            self.tail = self.tail.previous
            self.tail.next = None

        elif (0 < index) and (index < self.length):

            node = self.__get_node(index)
            node.previous.next = node.next

            if node.next:
                node.next.previous = node.previous

        else:
            return

        self.length -= 1



if False:
    obj = MyLinkedList()
    obj.print()

    obj.addAtHead(1)
    obj.print()

    obj.addAtTail(3)
    obj.print()

    obj.addAtIndex(1, 2)
    obj.print()

    obj.get(1)
    obj.print()

    obj.deleteAtIndex(2)
    obj.print()

elif True:

    obj = MyLinkedList()

    obj.addAtIndex(1, 2)
    obj.print()

    obj.addAtIndex(3, 4)
    obj.print()

    obj.addAtTail(1)
    obj.print()

    obj.get(0)
    obj.print()

    obj.deleteAtIndex(0)
    obj.print()

    obj.get(0)
    obj.print()
