class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        buy = prices[0]

        for sell in prices[1:] :
            if sell > buy :
                profit = max(profit, sell - buy)
            else :
                buy = sell
        return profit
    
obj = Solution()
test = [7,1,5,3,6,4]
test = [7,6,4,3,1]
test = [2,4,1]
test = [3,2,6,5,0,3]
test = [2,1,2,1,0,1,2]
res = obj.maxProfit(test)

print(f"result: {res}")