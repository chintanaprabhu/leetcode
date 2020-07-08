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
