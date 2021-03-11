class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actualSum = sum(nums)
        n = len(nums)
        expSum = n*(n+1) // 2
        return expSum-actualSum
