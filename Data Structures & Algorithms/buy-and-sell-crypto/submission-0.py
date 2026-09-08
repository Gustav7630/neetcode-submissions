class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buypoint = 0 
        sellpoint = 0
        max_profit = 0
        for i in range(1,len(prices)):
            if(prices[i-1] < prices[buypoint]):
                buypoint = i -1
            profit = prices[i] - prices[buypoint]
            if (profit > max_profit):
                max_profit = profit
        
        return max_profit
            