class MyStack:

    def __init__(self):
        self.queue = []
        self.queue_temp = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        
        for i in range(len(self.queue) - 1):
            self.queue_temp.append(self.queue.pop(0))

        final_val = self.queue.pop()

        temp_len = len(self.queue_temp)

        for i in range(temp_len):
            self.queue.append(self.queue_temp.pop(0))

        return final_val
        


    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:

        if len(self.queue) > 0:
            return False

        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
