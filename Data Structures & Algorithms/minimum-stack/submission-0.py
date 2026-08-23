class MinStack:

    def __init__(self):
        self.stack = []
        self.minV = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minV) <= 0:
            self.minV.append(val)
        else:
            self.minV.append(min(val, self.minV[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minV.pop()
        

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minV) > 0:
            return self.minV[-1]
        
