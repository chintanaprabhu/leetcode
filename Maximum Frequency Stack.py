class FreqStack:

    def __init__(self):
        #dict to keep track of frequency of every unique element of stack
        self.hashMap = dict()
        #dict to keep track of all the elements of similar frequency and the order in which they
        #were pushed in the stack
        self.freqTable = dict()
        self.maxFreq = 0

    def push(self, x: int) -> None:
        freq = self.hashMap.get(x,0) + 1
        self.hashMap[x] = freq
        self.maxFreq = max(self.maxFreq, freq)
        if self.freqTable.get(freq):
            self.freqTable[freq].append(x)
        else:
            self.freqTable[freq] = [x]       
        
    def pop(self) -> int:
        ele = self.freqTable[self.maxFreq].pop()
        self.hashMap[ele] -= 1
        if not self.freqTable[self.maxFreq]:
            self.maxFreq -= 1
        return ele
