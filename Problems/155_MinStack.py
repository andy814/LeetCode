class MinStack: # space-efficiency: O(n)

    def __init__(self):
        self.stack=[]
        self.minStack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack)==0 or val<=self.minStack[-1]: # <= instead of < because we only check equality in pop()
            self.minStack.append(val)

    def pop(self) -> None:
        if self.stack[-1]==self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
class MinOneStack: #space-efficiency: O(1)
    def __init__(self):
        self.stack=[]
        self.min=float("inf")

    def push(self, val: int) -> None:
        if not self.stack:
            self.min=val
        self.stack.append(val-self.min)
        if val<self.min:
            self.min=val

    def pop(self) -> None:
        if self.stack[-1]<0:
            self.min=self.min-self.stack[-1]
        self.stack.pop()

    def top(self) -> int:
        if self.stack[-1]<0:
            return self.min
        return self.stack[-1]+self.min

    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()