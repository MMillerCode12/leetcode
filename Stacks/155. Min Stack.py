class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        min_push = val

        if len(self.min) == 0:
            self.min.append(min_push)
        else:
            if self.stack[-1] < self.min[-1]:
                self.min.append(self.stack[-1])
            else:
                self.min.append(self.min[-1])

    def pop(self) -> None:
        self.min.pop(-1)
        self.stack.pop(-1)
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
