class MinStack:

    def __init__(self):
        self.Stack=[]
        self.MainStack = []


    def push(self, val: int) -> None:
        self.Stack.append(val)
        if ( not self.MainStack or val<=self.MainStack[-1]):
            self.MainStack.append(val)
         

    def pop(self) -> None:
        
        
        if (self.Stack[-1]==self.MainStack[-1]):
            self.MainStack.pop()
        self.Stack.pop()


    def top(self) -> int:
        return self.Stack[-1]

    def getMin(self) -> int:
        return self.MainStack[-1]


# # Your MinStack object will be instantiated and called as such:
# # obj = MinStack()
# # obj.push(val)
# # obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.getMin()
# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.minStack = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)

#         if not self.minStack or val <= self.minStack[-1]:
#             self.minStack.append(val)

#     def pop(self) -> None:
#         if self.stack[-1] == self.minStack[-1]:
#             self.minStack.pop()

#         self.stack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return self.minStack[-1]