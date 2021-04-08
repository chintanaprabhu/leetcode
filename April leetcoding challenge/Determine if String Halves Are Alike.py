class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        sLen = len(s)
        s1 = s[:sLen//2]
        s2 = s[sLen//2:]
        return self.countVowels(s1) == self.countVowels(s2)
    
    def countVowels(self, s):
        vowels = 0
        for ch in s:
            if ch.lower() in 'aeiou':
                vowels += 1
        return vowels
