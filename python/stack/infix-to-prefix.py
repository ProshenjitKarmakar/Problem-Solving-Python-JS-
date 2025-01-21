
def isOperator(x) :
    if x == '+' :
        return True
    elif x == '-' :
        return True
    elif x == '*' :
        return True
    elif x =='/' :
        return True
    elif x =='(' :
        return True
    else :
        return False
    


# Python code to convert infix to prefix expression
 
def isalpha(x) :
    if x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' :
        return True
    else : 
        return False
    
def isdigit(x) :
    if x in '0123456789' :
        return True
    else : 
        return False

class InfixToPrefix : 
    def __init__(self) -> None:
        self.operator = []
        self.operand = []
        self.output = ''

    def infixToPrefix (self, exp) :
        exp = '(' + exp +  ')'
        for i in range(len(exp)) :
            if isalpha(exp[i]) :
                print(f'Operand {exp[i]}')
            else : 
                print(f'Operator {exp[i]}')

obj = InfixToPrefix()
obj.infixToPrefix('(A*B)+(C/D)')