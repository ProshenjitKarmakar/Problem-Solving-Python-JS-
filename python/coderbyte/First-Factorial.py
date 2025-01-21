def FirstFactorial(num):
  
    def factorial(num2) :
        if num2 == 0 :
            return 1
        else :
            return num2 * factorial(num2-1)
    res = factorial(num)
    return res

Input = 4
print(FirstFactorial(Input))