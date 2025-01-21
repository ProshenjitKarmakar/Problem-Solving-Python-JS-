class Solution(object):

    def factorial(self, n):
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res
    def trailingZeroes2(self, n):
        count = 0
        fac = self.factorial(n)
        
        while fac % 10 == 0 :
            count += 1
            fac = fac // 10
        return count

    def trailingZeroes(self, n):
        count = 0
        while n > 0:
            n //= 5  # Count multiples of 5
            print(f'===n===> {n}')
            count += n
            print(f'===n===> {n}')

        return count
obj = Solution()
n = 1
ans  = obj.trailingZeroes(n)
print(f'Result : {ans}')