class WordFilter:

    def __init__(self, words: List[str]):
        self.WF = dict()
        n = len(words)
        for idx, word in enumerate(words):
            wordSize = len(word)
            for j in range(1, wordSize+1):
                pfx = word[:j]
                for k in range(wordSize):
                    sfx = word[k:]
                    self.WF[pfx+"|"+sfx] = idx

    def f(self, prefix: str, suffix: str) -> int:
        return self.WF.get((prefix+"|"+suffix), -1)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
