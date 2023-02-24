"""
    Time Complexity
    ---------------
    push        O(1)
    pop         O(1)
    is_empty    O(1)
    is_full     O(1)
    peek        O(1)
    size        O(1)
"""


class Stack(object):
    def __init__(self, capacity=5):
        self.stack = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.stack) <= 0

    def is_full(self):
        return len(self.stack) >= self.capacity

    def push(self, item):
        if self.is_full():
            print("Stack Overflow!")
        else:
            self.stack.insert(0, item)

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
        else:
            self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def size(self):
        return len(self.stack)

