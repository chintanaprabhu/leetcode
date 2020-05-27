class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counter = {0:-1}    #if the difference between the number of extra 0's and 2' is 0, look from index -1 of the given array to find the max subarray length
        diff = 0
        max_subarr = 0
        for i,j in enumerate(nums):
            if(j == 0):
                diff=diff-1
            else:
                diff=diff+1
            if diff in counter:
                max_subarr = max(max_subarr, i-counter[diff])
            else:
                counter[diff] = i
        return max_subarr
