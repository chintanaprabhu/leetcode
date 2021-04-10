class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.orderMap = {}
        i = 1
        for o in order:
            self.orderMap[o] = i
            i += 1
        maxLen = len(words[0])
        idx = 0
        prev = words[0]
        for wordIdx in range(1, len(words)):
            l1 = self.orderMap[prev[idx]]
            l2 = self.orderMap[words[wordIdx][idx]]
            if l1 > l2:
                return False
            if l1 == l2:
                if not self.compareWords(prev, words[wordIdx]):
                    return False
            prev = words[wordIdx]
        return True

    def compareWords(self, word1, word2):
        if word1 == word2:
            return True
        i = 0
        minLen = min(len(word1), len(word2))
        while i < minLen and word1[i] == word2[i]:
            i += 1
        if i >= len(word1):
            l1 = 0
        else:
            l1 = self.orderMap[word1[i]]
        if i >= len(word2):
            l2 = 0
            return False
        else:
            l2 = self.orderMap[word2[i]]
        return l1 < l2
        
        
            
