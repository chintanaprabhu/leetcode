#binary search - O(log(n))
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        start, end = 0, n-1
        while start <= end:
            pivot = start + (end - start) // 2
            hIndex = n - pivot
            if citations[pivot] == hIndex:
                return hIndex
            elif citations[pivot] < hIndex:
                start = pivot + 1
            else:
                end = pivot - 1
        return n - start
