class MinStack:

    def __init__(self):
        self.__stack = []
        self.__min_stack = []

    def push(self, val: int) -> None:
        self.__stack.append(val)

        min_val = val if not self.__min_stack else min(val, self.__min_stack[-1])
        self.__min_stack.append(min_val)

    def pop(self) -> None:
        try:
            self.__stack.pop()
            self.__min_stack.pop()
        except IndexError:
            pass

    def top(self) -> int:
        try:
            return self.__stack[-1]
        except IndexError:
            return None

    def getMin(self) -> int:
        return self.__min_stack[-1]


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

    param_3 = obj.top()
    param_4 = obj.getMin()
