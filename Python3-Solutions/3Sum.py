class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        #maintain a centre pointer and check all the combinations with the elements
        #from its either sides
        for c in range(len(nums) - 1):
            l = 0
            r = len(nums) - 1
            while l < c and c < r:
                temp = nums[l] + nums[c] + nums[r]
                if temp == 0:
                    if (nums[l], nums[c], nums[r]) not in result:
                        result.add((nums[l], nums[c], nums[r]))
                    l += 1
                    r -= 1
                #move right pointer in the sorted array
                elif temp > 0:
                    r -= 1
                #move left pointer in the sorted array
                else:
                    l += 1

        return list(result)
###############################################
#reduce 3sum to 2sum 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        allTriplets = set()
        nums.sort()
        n = len(nums)
        for i, curr in enumerate(nums):
            l = i+1
            r = n-1
            while l < r:
                if curr + nums[l] + nums[r] == 0:
                    allTriplets.add((curr,nums[l],nums[r]))
                    l += 1
                    r -= 1
                    continue
                    
                if curr + nums[l] + nums[r] < 0:                    
                    l += 1
                else:
                    r -= 1
        return allTriplets
