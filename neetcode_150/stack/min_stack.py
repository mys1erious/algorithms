class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if len(self.min_stack) > 0:
            return self.min_stack[-1]
        return None


# # Your MinStack object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MinStack()
    obj.push(3)
    obj.push(4)
    obj.push(5)
    obj.push(2)
    obj.push(6)
    obj.pop()
    obj.pop()

    print(obj.top())
    print(obj.getMin())
