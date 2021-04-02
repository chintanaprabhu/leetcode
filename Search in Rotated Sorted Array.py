class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        #run binary search on the 2 sorted subarrays
        while start <= end:
            mid = (end+start) // 2
            if nums[mid] == target:
                return mid
            if nums[start] <= nums[mid]:
                # if first half of the array is sorted and target lies in the first half
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                # search for target in the second half
                else: 
                    start = mid + 1
            # search for target in second half
            else:
                # if second half is sorted and target lies in second half
                if nums[mid] <= nums[end]:
                    if nums[mid] <= target <= nums[end]:
                        start = mid + 1
                    # if target not in second half, search for target in the first half
                    else:
                        end = mid - 1
        return 0 if nums[0] == target else -1
        
