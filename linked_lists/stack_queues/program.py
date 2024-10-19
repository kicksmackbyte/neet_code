'''

# Prompt

Implement a last-in-first-out (LIFO) stack using only two queues.

Implement the MyStack class:
    * void push(int x) Pushes element x to the top of the stack.
    * int pop() Removes the element on the top of the stack and returns it.
    * int top() Returns the element on the top of the stack.
    * boolean empty() Returns true if the stack is empty, false otherwise.


You must use only standard operations of a queue
    * append
    * peek/pop from front
    * size
    * isEmpty


# Constraints

1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.

Follow-up:
    * Can you implement the stack using only one queue?



'''


class MyStack:

    def __init__(self):
        self.queue = []


    def push(self, x: int) -> None:
        self.queue.append(x)


    def pop(self) -> int:

        length = len(self.queue)
        for i in range(length-1):
            element = self.queue.pop(0)
            self.queue.append(element)

        return self.queue.pop(0)


    def top(self) -> int:

        element = self.pop()
        self.push(element)

        return element


    def empty(self) -> bool:
        return not(bool(self.queue))


stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.queue)
print(stack.top())
stack.pop()
print(stack.queue)
