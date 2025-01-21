class Solution(object):
    def findTheDifference(self, s, t):
        mapped = {}

        for string in t :
            if string in mapped :
                mapped[string] += 1
            else :
                mapped[string] = 1

        for string in s :
            if string in mapped:
                mapped[string] -= 1
                if mapped[string] == 0:
                    del mapped[string]
                    
        print(f'Mapped: {mapped}')
        print(f'Mapped: {list(mapped.keys())[0]}')
        return list(mapped.keys())[0]

obj = Solution()
s = "abbcde" 
t = "abbcdef"
obj.findTheDifference(s, t)