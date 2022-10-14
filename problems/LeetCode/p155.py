class MinStack:

    def __init__(self):
        self.data = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.data.append(val)
        m = min(val, self.minimum[-1] if self.minimum else val)
        self.minimum.append(m)

    def pop(self) -> None:
        self.data.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.minimum[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(5)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()