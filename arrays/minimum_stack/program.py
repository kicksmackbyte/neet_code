'''

# Prompt

Design a stack class that supports the push, pop, top, and getMin operations.

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.


# Constraints

-2^31 <= val <= 2^31 - 1.
pop, top and getMin will always be called on non-empty stacks.
each function should run in O(1)O(1) time.


# Constraints



'''


class MinStack:


    def __init__(self):
        self.min = None
        self.stack = []


    def push(self, val: int) -> None:

        if self.min is None:
            self.min = val

        if val < self.min:
            self.min = val

        self.stack.append(val)


    def pop(self) -> None:
        self.stack.pop()

        self.min = None
        for val in self.stack:
            if self.min is None:
                self.min = val

            if val < self.min:
                self.min = val


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min
