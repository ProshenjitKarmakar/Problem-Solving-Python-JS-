class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stack = []
        string = ''

        for str in s :
            if str != ' ':
                print(f'letter: {str}')
                string += str
            else:
                if string != '':
                    stack.append(string)
                    string=''
        
        if string != '':
            stack.append(string)
            string = ''
            
        print(f'Max length: {stack}')
        last_word = stack.pop()
        print(f'last word: {last_word}')
        return len(last_word)


test = "   fly me   to   the moon  "
# test = "Today is a nice day"
test= "luffy is still joyboy"
obj = Solution()

obj.lengthOfLastWord(test)
