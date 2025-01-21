class Solution(object):
    def simplifyPath(self, path):
        stack = []
        components = path.split('/')

        

        for component in components:
            if component == '' or component == '.':
                continue
            elif component == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(component)
        
        simplified_path = '/' + '/'.join(stack)
        
        if simplified_path != '//' :
            return simplified_path
        else :
            return '/'
    
obj = Solution()
res = obj.simplifyPath("/home/user/Documents/..///Pictures")

print(f'Result : {res}')
        
