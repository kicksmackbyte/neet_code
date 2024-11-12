'''
# Prompt

Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.

Your DynamicArray class should support the following operations:

* DynamicArray(int capacity)
    - will initialize an empty array with a capacity of capacity, where capacity > 0.
* int get(int i)
    - will return the element at index i. Assume that index i is valid.
* void set(int i, int n)
    - will set the element at index i to n. Assume that index i is valid.
* void pushback(int n)
    - will push the element n to the end of the array.
    - if the array is full, we should resize the array first.
* int popback()
    - will pop and return the element at the end of the array. Assume that the array is non-empty.
* void resize()
    - will double the capacity of the array.
* int getSize()
    - will return the number of elements in the array.
* int getCapacity()
    - will return the capacity of the array.

'''



class DynamicArray:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.data = [None] * capacity


    def get(self, i: int) -> int:
        return self.data[i]


    def set(self, i: int, n: int) -> None:
        self.data[i] = n


    def pushback(self, n: int) -> None:

        if self.size == self.capacity:
            self.resize()

        self.data[self.size] = n
        self.size += 1


    def popback(self) -> int:

        self.size = self.size - 1
        data = self.data[self.size]

        return data


    def resize(self) -> None:

        self.capacity = 2 * self.capacity
        data = [None] * self.capacity

        for i, d in enumerate(self.data):
            data[i] = self.data[i]

        self.data = data


    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity
