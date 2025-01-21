class Solution(object):
    def fizzBuzz(self, n):
        result = []
        for i in range(n) :
            if i%3 == 0 and i%5 == 0 :
                result.append('FizzBuzz')
            elif i%3 == 0 :
                result.append('Fizz')
            elif i%5 == 0 :
                result.append('Buzz')
            else :
                result.append(i)
        
        print(f'result : {result}')
        return result

obj = Solution()
n = 15
res = obj.fizzBuzz(n)

print(f'Result : {res}')