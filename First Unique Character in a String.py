class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        hashMap = Counter(s)
        for index,char in enumerate(s):
            if(hashMap.get(char) == 1):
                return index
        return -1
