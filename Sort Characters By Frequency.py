class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        d = Counter(s)
        result = ""
        while d:
            char = (max(d,key=d.get))
            result += char*d[char]
            d.pop(char)
        return result
