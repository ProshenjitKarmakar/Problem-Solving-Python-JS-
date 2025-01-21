class Solution(object):
    def addBinary(self, a, b):
        a_int = int(a, 2)
        b_int = int(b, 2)

        sum = a_int + b_int

        binary = bin(sum)[2:]
        return binary
        

obj = Solution()

a = "1010"
b = "1011"
result = obj.addBinary(a, b)

print(f'result : {result}')