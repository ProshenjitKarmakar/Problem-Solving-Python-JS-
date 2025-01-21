class Solution(object):
    def licenseKeyFormatting(self, s, k):
        count = 0
        string = ''
        result = []

        for letter in reversed(s):
            if letter != '-': 
                string = letter.upper() + string 
                count += 1
                if count == k:  
                    result.append(string)
                    string = ''
                    count = 0

        if string:
            result.append(string)

        return "-".join(reversed(result))


# Test the function
obj = Solution()
s = "2-4A0r7-4k"
k = 4
result = obj.licenseKeyFormatting(s, k)
print(f"Result: {result}")
