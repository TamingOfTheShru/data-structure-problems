# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.size = 0

    def push(self, x: int) -> None:
        # Move all elements from s1 to s2  
        while len(self.s1) != 0:  
            self.s2.append(self.s1[-1])  
            self.s1.pop() 
        # Push item into self.s1  
        self.s1.append(x)  
  
        # Push everything back to s1  
        while len(self.s2) != 0:  
            self.s1.append(self.s2[-1])  
            self.s2.pop() 
        self.size +=1

    def pop(self) -> int:
        if self.s1 is None:
            return -1
        self.size -=1
        return self.s1.pop(-1)

    def peek(self) -> int:
        if self.s1 is None:
            return -1
        return self.s1[-1]
        

    def empty(self) -> bool:
        if self.size == 0:
            return True
        else: 
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
