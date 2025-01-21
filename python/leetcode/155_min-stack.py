class MinStack(object):

    def __init__(self):
        self.stack= []
        self.min_stack= []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        
            

    def pop(self):
        if self.stack :
            value = self.stack.pop()
        if self.min_stack and self.min_stack[-1] == value:
            self.min_stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None
        

    def getMin(self):
        if self.min_stack :
            return self.min_stack[-1]
        else:
            return None
        

obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)

obj.pop()
param_3 = obj.top()
print(f'param_3 : {param_3}')
param_4 = obj.getMin()
print(f'param_4 : {param_4}')
