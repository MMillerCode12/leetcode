class Stack:
    def __init__(self):
        self.size = 0
        self.data = []

    def pop(self):
        if self.is_empty():
            return None
        self.size -= 1
        return self.data.pop(-1)

    def push(self, item):
        self.size += 1
        self.data.append(item)

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

# This is just me making a stack data type ^

class Solution:
    def maxDepth(self, s: str) -> int:
        p_stack = Stack()
        max_nest = 0

        for i in s:
            if i == "(":

                p_stack.push(i)

                if p_stack.size() > max_nest:
                    max_nest = p_stack.size()

            elif i == ")":
                p_stack.pop()

        return max_nest

