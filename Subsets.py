class Solution:
    def __init__(self):
        self.output = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        self.subsetHelper(nums, 0, len(nums), subset)
        return self.output
    def subsetHelper(self, nums, index, size, subset):
        self.output.append(subset)
        for i in range(index, size):
            self.subsetHelper(nums, i+1, size, subset+[nums[i]])
