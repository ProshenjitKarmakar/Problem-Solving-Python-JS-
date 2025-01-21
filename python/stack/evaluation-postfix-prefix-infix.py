class Evaluation :

    def __init__(self) -> None:
        self.postfix = []

    def isOperator(self, x) :
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
        
    def postfixExpression(self, expression) :
        exp = ''
        for num in expression :
            if num != ' ' :
                exp += num
            else :
                if self.isOperator(exp) :
                    print(f'exp : {exp}')
                    operand1 = self.postfix.pop()
                    operand2 = self.postfix.pop()
                    if exp == '+' :
                        cal = int(operand2) + int(operand1)
                    elif exp == '-' :
                        cal = int(operand2) - int(operand1)
                    elif exp == '*' :
                        cal = int(operand2) * int(operand1)
                    elif exp == '/' :
                        cal = int(operand2) / int(operand1)
                    print('cal', cal)
                    self.postfix.append(int(cal))
                    exp = ''
                else :
                    self.postfix.append(exp)
                    exp = ''
        print(f'result {self.postfix}')

obj = Evaluation()
test1 = '2 3 1 * + 9 - '
test2 = '100 200 + 2 / 5 * 7 + '

obj.postfixExpression(test1)