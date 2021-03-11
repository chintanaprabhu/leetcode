class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        if not words:
            return
        set1 = set(words)
        set2 = set(words)
        for word in set1:
            for i in range(1, len(word)):
                if word[i::] in set2:
                    set2.remove(word[i::])
        refLen = 0
        for word in set2:
            refLen += len(word)+1
        return refLen
        
