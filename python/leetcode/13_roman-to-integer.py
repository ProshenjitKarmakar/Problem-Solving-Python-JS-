class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = roman[s[-1]]
        
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]

        print(f'Result: {result}')
        return result

obj = Solution()
test = 'MCMXCIV'
# test = 'LVIII'
test = 'IV'
obj.romanToInt(test)