
def isOperator(x) :
    if x == '+' :
        return True
    elif x == '-' :
        return True
    elif x == '*' :
        return True
    elif x =='/' :
        return True
    else :
        return False
    

class PrefixToInfix : 
    def __init__(self) -> None:
        self.stack = []
        self.infix = ''

    def preToInfix (self, exp) : 

        for i in range(len(exp) -1, -1, -1) :

            if isOperator(exp[i]) :
                print(self.stack)
                operand2 = self.stack.pop()
                operand1 = self.stack.pop()
                expression = '(' + operand2 + exp[i] + operand1 + ')'
                self.stack.append(expression)
            else : 
                self.stack.append(exp[i])

        print(self.stack)

obj = PrefixToInfix()
obj.preToInfix('*+AB-CD')