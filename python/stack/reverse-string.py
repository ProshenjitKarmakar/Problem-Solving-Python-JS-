
class Solution :
    def __init__(self) :
        self.str = ''
        self.stack =[]

    def reverseString(self, string) :
        for st in string :
            self.stack.append(st)

        for i in range(0, len(self.stack)) :
            pop = self.stack.pop()
            self.str += pop

        print(self.str)

obj = Solution()

obj.reverseString('proshenJiT')

