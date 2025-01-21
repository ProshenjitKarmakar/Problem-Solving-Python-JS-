class Stack :
    def __init__(self) -> None:
        self.stack =[]

    def append(self, item):
        self.stack.append(item)
        print(f"New Array: {self.stack}")
    
    def pop(self) :
        pop = self.stack.pop()
        print(f'Poped Element: {pop}')
    
    def is_Empty(self) :
        self.stack =[]
        print(f'Empty Array: {self.stack}')

    def stackItems (self) :
        stack = self.stack
        print(f'Stack item :', stack)



stack = Stack()
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
stack.pop()
stack.pop()
stack.pop()

stack.stackItems()


