#two pointer solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
        first=0  
        for sec in range(1, len(nums)):
            if(nums[sec]!=nums[first]):
                first+=1
                nums[first]=nums[sec]
        return first+1
