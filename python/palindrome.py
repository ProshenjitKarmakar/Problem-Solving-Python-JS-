
def printPalindromeNumber(start, end) :
    num1 = 0
    num2 = 1

    for i in range(start, end) :
        print('palindrome: ', num1)
        temp = num1 + num2
        num1 = num2
        num2 = temp


start = int(input('Enter the first number you want to Print: '))
end = int(input('Enter the second number you want to Print: '))

printPalindromeNumber(start, end)