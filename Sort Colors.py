class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rightOfZero = currIndex = 0
        leftOfTwo = len(nums)-1
        while currIndex <= leftOfTwo:
            if(nums[currIndex] == 0):
                nums[rightOfZero], nums[currIndex] = nums[currIndex], nums[rightOfZero]
                rightOfZero += 1
                currIndex += 1
                continue
            if(nums[currIndex] == 2):
                nums[leftOfTwo], nums[currIndex] = nums[currIndex], nums[leftOfTwo]
                leftOfTwo -= 1
                continue
            currIndex += 1
        
            
    
        
                    
        
                    
        Sort Colors
