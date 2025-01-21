class Solution(object):
    def addStrings(self, num1, num2):
        length = max(len(num1), len(num2))
        carry = 0
        result = ''

        while(length >= 0) :
            a = num1[length] if num1[length] else 0
            b = num2[length] if num2[length] else 0

            result += 
    


num1 = "11", num2 = "123"
obj = Solution()

result = obj.addStrings(num1, num2)
print(f'result : {result}')