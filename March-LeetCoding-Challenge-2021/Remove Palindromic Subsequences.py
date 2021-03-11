class Solution:
    #if the given string is not a palindrome, we would remove all a's first and then all b's 
    #at max 2 steps would be needed to remove all palindromic SUBSEQUENCES from the given string
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        if self.isPalindrome(s):
            return 1
        return 2
    
    def isPalindrome(self, s):
        start = 0 
        end = len(s)-1
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
