class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagrams = defaultdict(list)
        for s in strs:
            char = [0] * 26
            for ch in s:
                char[ord(ch) - ord('a')] += 1
            anagrams[tuple(char)].append(s)
        return anagrams.values()
        
