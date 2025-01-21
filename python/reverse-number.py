class Solution:
    def isPalindrome(self, x: int) -> bool:
        original_number = x
        reverse = 0
        while x > 0 :
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x // 10
        if original_number == reverse : 
            return True
        else : 
            return False
        
obj = Solution
res = obj.isPalindrome(121)
print(res)