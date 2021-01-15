class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        output = [] 
        
        def addRange(lower, upper):
            if lower == upper:
                output.append(str(lower))
            else:
                output.append(str(lower)+"->"+str(upper))
        #if nums is empty, add the range based on lower and upper bounds
        if len(nums) == 0:
            addRange(lower,upper)
            return output
        #handle missing range between lower and nums[0], if any
        if(nums[0] > lower):
            addRange(lower, nums[0]-1)
        #check every consecutive pairs of num in nums and calculate the missing range
        for i in range(1, len(nums)):
            if nums[i]-nums[i-1] > 1:
                addRange(nums[i-1]+1, nums[i]-1)
        #handle missing range between last element of nums and upper, if any
        if(nums[len(nums)-1] < upper):
            addRange(nums[len(nums)-1]+1, upper)
        return output
