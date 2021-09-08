class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -sys.maxsize - 1
        if len(nums) == 0:
            return 0
        #maintain current maximum sum of array and absolute maximum sum
        #whenever the current sum goes below 0, reset the current sum to current element of the array
        curr_max_sum = 0
        for num in nums:
            curr_max_sum = max(num, curr_max_sum+num)
            max_sum = max(curr_max_sum, max_sum)
        return max_sum
