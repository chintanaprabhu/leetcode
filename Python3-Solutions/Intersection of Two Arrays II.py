class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        #to create a hashMap of smaller list:
        if len(nums2) < len(nums1):      
            nums1, nums2 = nums2, nums1
        hashMap = Counter(nums1)
        result = []
        for num in nums2:
            if hashMap.get(num,None):
                hashMap[num] -= 1
                result.append(num)
        return result
        
