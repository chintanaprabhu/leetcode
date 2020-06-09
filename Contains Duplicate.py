class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        hashMap = Counter(nums)
        for key,val in hashMap.items():
            if val > 1:
                return True
        return False
