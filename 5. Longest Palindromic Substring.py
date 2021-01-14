#expand from center method - consider the cases where palindrome of even or odd length
#time complexity - O(n^2) -> expansion is checked for every string twice to find the palindrome of even length or odd length
#space complexity - O(1)
class Solution(object):
    def expandFromCenter(self, s, left, right):
        while (left >= 0 and right < len(s)) and s[left] == s[right]:
                left -= 1
                right += 1
        return right - left - 1
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = end = 0
        if (len(s) == 0):
            return ""
        for i in range(0, len(s)):
            len1 = self.expandFromCenter(s, i, i)
            len2 = self.expandFromCenter(s, i, i+1)
            longPalLen = max(len1, len2)
            if (longPalLen > end-start):
                start = i - ((longPalLen-1) /2)
                end = i + longPalLen/2
                #print(start, 'start')
                #print(end, 'end')
        return s[start:end+1]
    
