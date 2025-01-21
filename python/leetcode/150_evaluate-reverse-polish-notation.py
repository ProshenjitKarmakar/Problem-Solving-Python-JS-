import math

class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 + num1)
            elif token == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif token == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 * num1)
            elif token == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 // num1 if num2 * num1 > 0 else -(abs(num2) // abs(num1)))
            else:
                stack.append(int(token))

        return stack[0]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
obj = Solution()
result = obj.evalRPN(tokens)

print(f'result : {result}')