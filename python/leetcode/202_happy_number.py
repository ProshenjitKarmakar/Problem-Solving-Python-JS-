class Solution:
    def sumOfSquare(self, num: int) -> int:
        result = 0
        while num: 
            last_digit = num % 10
            result += last_digit ** 2
            num //= 10
        return result
    
    def isHappy(self, n: int) -> bool:
        mapped = set()
        while n not in mapped:
            mapped.add(n)
            n = self.sumOfSquare(n)
            if n == 1:
                return True
        return False

# Test cases
obj = Solution()
test_cases = [19, 2, 100, 1, 7, 1111111]  # Add diverse inputs

for n in test_cases:
    result = obj.isHappy(n)
    print(f'Is {n} a happy number? {result}')