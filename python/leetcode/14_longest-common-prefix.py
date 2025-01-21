class Solution:
    def longestCommonPrefix(self, strings) -> str:
        if not strings :
            return ""
        
        init = strings[0]
        new_str = ''

        for j in range(1, len(strings)):
            current_str = strings[j]

            for i in range(min(len(init), len(current_str))) :
                if(current_str[i] == init[i]) :
                    new_str += current_str[i]
                else :
                    break

            init = new_str
            new_str = ''

        if init == '' :
            return ""
        
        print(f'New String: {init}')
        return init
                



obj= Solution()

test = ["flower","flow","flight"]
test = ["dog","dacecar","dar"]
obj.longestCommonPrefix(test)