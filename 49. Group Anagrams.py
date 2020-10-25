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
        
#for every string - an array of the occurrece of the alphabets is created and matched against any existing
#sting for anagram comparison
#Space - O(KN) -> K is the length of the longest string
#Time - O(KN) 
