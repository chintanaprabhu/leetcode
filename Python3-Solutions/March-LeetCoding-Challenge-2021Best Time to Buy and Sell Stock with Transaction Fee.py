class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = -prices[0]
        sell = 0
        for day in range(1, len(prices)):
            prevBuy = buy
            buy = max(buy, sell-prices[day])
            sell = max(sell, prices[day]+prevBuy-fee)
        return sell
            
            
