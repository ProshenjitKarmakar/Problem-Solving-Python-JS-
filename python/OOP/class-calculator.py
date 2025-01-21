class MyClass :
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2
    
    def add(self) :
        add = int(self.num1) + int(self.num2)
        print(f"Addition is  : {add}")
    
    def sub(self) : 
        sub = int(self.num1) - int(self.num2)
        print(f"Subtraction is : {sub}")

    def mul(self) : 
        mul = int(self.num1) * int(self.num2)
        print(f"Multiplication is : {mul}")

    def div(self) :
        if self.num1 > self.num2 :
            div = int(self.num1) // int(self.num2)
            print(f"Division is : {div}")
        else :
            print(f"Division not possible! num1 < num2")

 
num1 = int(input("Input first number : "))
num2 = int(input("Input second number : "))


obj1 = MyClass(num1, num2)
obj1.add()
obj1.sub()
obj1.mul()
obj1.div()


