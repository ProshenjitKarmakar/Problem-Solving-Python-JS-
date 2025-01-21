
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
    

class PrefixToPostfix : 
    def __init__(self) -> None:
        self.stack = []
        self.postfix = ''

    def preToPost(self, exp) :

        for i in range(len(exp) -1, -1, -1) : 
            if isOperator(exp[i]) :
                operand2 = self.stack.pop()
                operand1 = self.stack.pop()
                operand = operand2 + operand1  + exp[i]
                self.stack.append(operand)
                i -= 1
            else :
                self.stack.append(exp[i])
                i -= 1

        print(self.stack)

obj = PrefixToPostfix()
obj.preToPost('*-A/BC-/AKL')