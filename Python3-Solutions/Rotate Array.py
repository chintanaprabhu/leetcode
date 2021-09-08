class Solution:
    def reverse(self, nums: List[int], start, end):
		# reverse array elements within [start, end] interval
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
            
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        k = k % size
        # reverse all elements
        self.reverse(nums, 0, size-1)
        # reverse first k elements
        self.reverse(nums, 0, k-1)
        # reverse last (size - k) elements 
        self.reverse(nums, k, size-1)
        return
