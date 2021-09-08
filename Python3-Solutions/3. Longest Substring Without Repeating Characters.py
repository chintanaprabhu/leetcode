class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        i = j = lss = 0
        while j < len(s):
            if s[j] not in substring:
                #increment j whenever a new unique char is added to the set
                substring.add(s[j])
                j += 1
                lss = max(lss, len(substring))
            else:
                #increment i when a repeated char is found in the set
                substring.remove(s[i])
                i += 1
        return lss
                
#====================================================
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = {}
        first, second = -1, 0
        lss = 0
        for i, char in enumerate(s):
            second = i
            last_found = substring.get(char, None)
            if last_found is not None and last_found > first:
                first = last_found
            lss = max(lss, second-first)
            #update the char occurrence index everytime the char is found
            substring[char] = i
        return lss
                
