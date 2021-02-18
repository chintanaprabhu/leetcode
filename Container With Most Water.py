class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return
        l1 = height[0]
        l2 = height[len(height)-1]
        i = 0
        j = len(height)-1
        area = 0
        while i < j:
            area = max(area, min(l1,l2)*(j-i))
            if l1 < l2:
                i += 1
                l1 = height[i]
            else:
                j -= 1
                l2 = height[j]
        return area
