class Solution:
    # convert the array into a non-decreasing array by ensuring nums[i] >= nums[i-1]
    # if more than one non-decreasing pairs found, return False
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        nd = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            cur = nums[i]
            if prev > cur:
                if nd == 1:
                    return False
                nd += 1
                if i < 2 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
            prev = nums[i]
        return True
