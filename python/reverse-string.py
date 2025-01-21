
def reverseSting(str) :
    newStr = ''

    for s in str :
        newStr = s + newStr

    return newStr

res = reverseSting('proshenjit')

print(f'Reverse str : {res}')