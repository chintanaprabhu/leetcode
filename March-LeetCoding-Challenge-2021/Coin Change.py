class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minCoins = [amount+1] * (amount+1)
        minCoins[0] = 0
        for val in range(1, amount+1):
            for coin in coins:
                if coin > val:
                    continue
                # incrementally build an array to contain the minimum number of coins needed to make the amount using coin in coins
                # if we are using coin in coins to make the amount, lookup in the minCoins array for the number of coins needed to make (current amount - coin)
                # in minCoins
                minCoins[val] = min(minCoins[val], minCoins[val-coin]+1)
        return -1 if minCoins[amount] == amount+1 else minCoins[amount]
