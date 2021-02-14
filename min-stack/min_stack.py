Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# 
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

class MinStack:

    def __init__(self):
        self.data = []
        
    def push(self, x: int) -> None:
        return self.data.append(x)

    def pop(self) -> None:
        if len(self.data) == 0:
            return None
        return self.data.pop()

    def top(self) -> int:
        if len(self.data) == 0:
            return None
        return self.data[-1]

    def getMin(self) -> int:
        min = self.data[0]
        for i in self.data:
            if i < min:
                min = i
        return min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
