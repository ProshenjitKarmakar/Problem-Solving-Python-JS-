class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        new_str = ''

        while (i < len(s) and j < len(t)) :
            if(s[i] == t[j]) :
                new_str += t[j]
                i+=1
                j+=1
            else :
                j+=1

        print(f'str : {new_str}')
        if new_str == s :
            return True
        else :
            return False
        

        

obj  = Solution()
res = obj.isSubsequence('', 'a')


print(f'Result : {res}')

# Input: s = "abc", t = "ahbgdc"
# Output: true
