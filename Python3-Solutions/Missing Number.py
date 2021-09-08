class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        distinctNums = len(nums)
        expectedSum = distinctNums * (distinctNums+1) // 2
        calculatedSum = 0
        for num in nums:
            calculatedSum += num
        return expectedSum - calculatedSum
