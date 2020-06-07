class Solution:
    #improved Knapsack problem - rather than maintaining a matrix, update the amount when new coin is added to the list of coins
    #cols of the array updated are only where amount >= coin
    def change(self, amount: int, coins: List[int]) -> int:
        change=[0] * (amount+1)
        change[0]=1
        for coin in coins:  #for every coin, look into the prev iteration(row) cobinations and add the combinations which could be made using x-coin
            for x in range(coin, amount+1):  
                change[x] += change[x-coin]
        return change[amount]
        
