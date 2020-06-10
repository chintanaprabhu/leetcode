class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #import bisect
        #return bisect_left(nums,target)
        
        #use binary search to find the index
        
        #if target is larger than the last element of nums, return last index
        if target > nums[len(nums)-1]:  #ususual to use a negative subscript 
            return len(nums)
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo+hi)//2
            if(nums[mid]==target):
                return mid
            if(nums[mid]<target):
                lo=mid+1
            else:
                hi=mid
        return lo
