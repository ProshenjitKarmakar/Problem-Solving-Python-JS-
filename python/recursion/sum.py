def sum(x) :
    if x == 0 :
        return 0
    else :
        return x + sum(x-1)
    

res = sum(5)
print(f'result: {res}')


def printNumber(x) :

    if x > 0 :
        printNumber(x - 1)
    print(f'result: {x}')

printNumber(100)
