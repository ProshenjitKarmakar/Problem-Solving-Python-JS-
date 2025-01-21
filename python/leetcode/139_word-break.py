class Solution(object):
    def wordBreak(self, s, wordDict):
        sub_arr = []
        word = ''
        for letter in s :
            word += letter

            if word in wordDict :
                sub_arr.append(word)
                word = ''
        
        if word :
            return False
        
        return ''.join(sub_arr) == s
 

obj = Solution()
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
res = obj.wordBreak(s, wordDict)
print(f'result: {res}')