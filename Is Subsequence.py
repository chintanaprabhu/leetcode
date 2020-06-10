class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        index_t = -1
        for index_s in range(len(s)):
            while index_t < len(t)-1:
                index_t += 1
                if s[index_s] == t[index_t]:
                    break
            if index_t == len(t)-1 and index_s <= len(s)-1:
                return False
        return True
                
