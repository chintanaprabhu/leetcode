class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        d = Counter(s)
        for i,c in enumerate(s):
            if(d[c] == 1):
                return i
        return -1
