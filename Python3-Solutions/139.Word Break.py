class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # quick lookup table to skip indices that are not dict word prefixes
        memoizeMatch = {}
        def helper(idx):
            if idx == len(s):
                return True
            if idx in memoizeMatch:
                return False
            breakable = False
            for word in wordDict:
                if s[idx:].startswith(word):
                    if helper(idx+len(word)):
                        breakable = True
                        break
            memoizeMatch[idx] = breakable
            return breakable
        return helper(0)
    
    
