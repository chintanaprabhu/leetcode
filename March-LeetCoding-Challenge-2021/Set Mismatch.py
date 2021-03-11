class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        if not nums:
            return
        maximum = nums[0]
        actualSum = 0
        numTable = {}
        for num in nums:
            if num in numTable:
                dup = num
            else:
                numTable[num] = 1
            actualSum += num
        n = len(nums)
        expSum = n * (n + 1) // 2
        missing = expSum - (actualSum - dup)
        return [dup, missing]
