#peak and valley solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        sell = prices[0]
        i = 0
        while i < len(prices)-1:
            while i < len(prices)-1 and prices[i] >= prices[i+1]: #find the lowest price to buy 
                i += 1
            buy = prices[i]
            while i < len(prices)-1 and prices[i] <= prices[i+1]: #find the highest price to sell 
                i += 1
            sell = prices[i]
            max_profit += sell-buy
        return max_profit
            
