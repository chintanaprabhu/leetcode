class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or target is None:
            return [-1,-1]
        if target < nums[0] or target > nums[len(nums)-1]:
            return [-1,-1]
        self.ranges = []
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (end+start) // 2
            if nums[mid] == target:
                self.getRange(nums, 0, len(nums), mid)
                return self.ranges
            elif target > nums[mid]:
                start = mid+1
            else:
                end = mid-1
        return [-1,-1]

    def getRange(self, nums, start, end, mid):
        loRange = mid
        hiRange = mid
        while(loRange >= start) and nums[loRange] == nums[mid]:
            loRange -= 1
        self.ranges.append(loRange+1)
        while(hiRange < end) and nums[hiRange] == nums[mid]:
            hiRange += 1
        self.ranges.append(hiRange-1)
        
