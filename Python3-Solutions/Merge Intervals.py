class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        merged = []
        start = intervals[0][0]
        end = intervals[0][1]
        for interval in intervals:
            if interval[0] > end:
                merged.append([start, end])
                start = interval[0]
                end = interval[1]
            end = max(end, interval[1])
        merged.append([start, end])
        return merged
