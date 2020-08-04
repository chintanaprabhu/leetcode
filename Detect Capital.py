class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if not word or len(word) == 1:
            return True
        if word[0].isupper() and word[1].isupper():
            for index in range(2, len(word)):
                if not word[index].isupper():
                    return False
        else:
            for index in range(1, len(word)):
                if word[index].isupper():
                    return False
        return True
                
