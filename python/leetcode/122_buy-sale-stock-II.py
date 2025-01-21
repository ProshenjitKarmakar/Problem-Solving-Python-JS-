class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0

        for i in range(1, len(prices)) :
            if prices[i] > prices[i-1] :
                profit += prices[i] - prices[i-1]

        print(f'profit : {profit}')
        return profit

obj = Solution()

test1 = [7,1,5,3,6,4]
test1 = [1,2,3,4,5]
test1 = [7,6,4,3,1]

obj.maxProfit(test1)
        