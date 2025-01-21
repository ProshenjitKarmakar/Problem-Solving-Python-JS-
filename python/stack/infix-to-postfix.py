class InfixToPrefix :
    def __init__(self) -> None:
        self.operatorStack = []
        self.exp = ''

    def isOperator(self, x) :
        if x == '+' :
            return True
        elif x == '-' :
            return True
        elif x == '/' :
            return True
        elif x =='^' :
            return True
        elif x ==')' :
            return True
        else :
            return False 

    def reverseString(self, exp) :
        str = ''
        for i in exp :
            str = i + str
        return str

    def infixToPrefixConversion(self, expression) :
        reverse_str = self.reverseString(expression)

        for str in reverse_str :
            if str == '(':
                while self.operatorStack and self.operatorStack[-1] != ')':
                    operand = self.operatorStack.pop()
                    self.exp += operand

                if self.operatorStack and self.operatorStack[-1] == ')':
                    self.operatorStack.pop()
            elif self.isOperator(str) :
                self.operatorStack.append(str)
            else :
                self.exp += str

        print(f'Result {self.exp}')
        print(f'Result {self.operatorStack}')

obj = InfixToPrefix()

exp1 = 'K+L-M*N+(O^P)*W/U/V*T+Q'
exp2 = '(A+B)+(C/B)'

obj.infixToPrefixConversion(exp2)