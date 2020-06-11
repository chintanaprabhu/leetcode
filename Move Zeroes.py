class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_ptr=0
        #swap every 0 and non-zero element
        #so that at the end of parsing, all the 0'z are pushed to the end of the array
        for sec_ptr in range(len(nums)):
            if nums[sec_ptr]:
                nums[first_ptr], nums[sec_ptr] = nums[sec_ptr], nums[first_ptr]
                first_ptr += 1
        return nums
            
            
