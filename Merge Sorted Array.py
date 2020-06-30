class Solution:
    #two pointer solution starting from last index
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        insert_position = (m+n) - 1
        nums1_index = m-1
        nums2_index = n-1
        while nums2_index >= 0 and nums1_index >= 0:
            if nums1[nums1_index] > nums2[nums2_index] and nums1_index >= 0:
                nums1[insert_position] = nums1[nums1_index]
                nums1_index -= 1
            else:
                nums1[insert_position] = nums2[nums2_index]
                nums2_index -= 1
            insert_position -= 1
        while nums2_index >= 0:
            nums1[insert_position] = nums2[nums2_index]
            nums2_index -= 1
            insert_position -= 1
            
