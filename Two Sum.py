class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for idx, num in enumerate(nums):
            hashMap[num] = idx
        for idx, num in enumerate(nums):
            val = target-num
            if hashMap.get(val, None) and hashMap[val] != idx:
                    return [idx] + [hashMap[val]]
