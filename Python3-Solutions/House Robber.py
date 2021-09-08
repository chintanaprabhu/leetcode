class Solution:
    def rob(self, nums: List[int]) -> int:
        prevMax = currMax = 0
        for num in nums:
            amount = currMax
            #rob current house along with reviously robbed houses or
            #not rob the current house but rob the house previous house
            currMax = max(currMax, prevMax+num)
            prevMax = amount
        return currMax
