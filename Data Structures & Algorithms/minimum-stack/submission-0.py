class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.minStack:
            minVal = min(value, self.minStack[-1])
        else:
            minVal = value
        self.minStack.append(minVal)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]