
def isOperator(x) :
    if x == '+' : 
        return True
    elif x == '-' :
        return True
    elif x == '*' :
        return True
    elif x == '/' :
        return True
    else :
        return False
    
class PostFixToPrefix :
    def __init__(self) -> None:
        self.stack = []
        self.prefix = ''

    def postToPre(self, exp) :

        for i in range(len(exp)) :
            if isOperator(exp[i]) :
                operand2 = self.stack.pop() 
                operand1 = self.stack.pop() 
                operand = exp[i] + operand1 + operand2
                self.stack.append(operand)
            else : 
                self.stack.append(exp[i])
        print(self.stack)


obj = PostFixToPrefix()
obj.postToPre('ABC/-AK/L-*')
