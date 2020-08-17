#maintain two different stacks for actual list and the minimum element corresponding to every index of the actual list
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.list.append(x)
        if len(self.min_stack) == 0:
            self.min_stack.append(x)
        elif x < self.min_stack[-1]:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])
        #print(self.min_stack, 'push')
            
    def pop(self) -> None:
        self.min_stack.pop(-1)
        self.list.pop(-1)
        #print(self.min_stack, 'pop')
           
    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        #print(self.min_stack, 'getMin')
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
