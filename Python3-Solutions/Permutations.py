class Solution:
    def __init__(self):
        self.permutations = []
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutation = [None] * len(nums)
        self.permuteHelper(nums, permutation, 0)
        return self.permutations
    
    def permuteHelper(self, nums, permutation, curPos):
        if len(nums) == 0:
            # .copy() is for list deep copy 
            # otherwise the self.permutations will only 
            # have a reference to the last added permutation list
            self.permutations.append(permutation.copy())
        else:
            for i in range(len(nums)):
                permutation[curPos] = nums[i]
                # slice the nums array to include only the elements that 
                # haven't been added to the current permutation
                self.permuteHelper(nums[:i]+nums[i+1:], permutation, curPos+1)
