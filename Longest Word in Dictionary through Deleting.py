class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        if not s or not d:
            return ""
        output = ""
        outputLen = 0
        strLen = len(s)
        for word in d:
            sIndex = 0
            wordIndex = 0
            if len(s) < len(word):
                continue
            wordLen = len(word)
            while sIndex < strLen and wordIndex < wordLen:
                if s[sIndex] == word[wordIndex]:
                    wordIndex += 1
                sIndex += 1
            if wordIndex == wordLen:
                if wordLen > outputLen:
                    output = word
                    outputLen = wordLen
                elif wordLen == outputLen:
                    output = min(output, word)
        return output
        
