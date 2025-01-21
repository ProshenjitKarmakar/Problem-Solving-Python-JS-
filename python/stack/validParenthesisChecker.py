

def validParenthesisChecker(parenthesis) :
    stack = []
    start = ['(', '{' , '[']

    for char in parenthesis :
        if char in start :
            stack.append(char)
        else :
            if len(stack) == 0 :
                return False
            else :
                current_item = stack.pop()
                if current_item == '(' :
                    if char != ')' :
                        return False
                elif current_item == '{' :
                    if char != '}' :
                        return False
                elif current_item == '[' :
                    if char != ']' :
                        return False
            
    if len(stack) ==  0 :
        return True
    else :
        return False

res = validParenthesisChecker('([])')

print(f'result : {res}')