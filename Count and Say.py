#recursive
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        else:
            prevSeq = self.countAndSay(n-1)
            scan_idx = 0
            count = 1
            currSeq = ""
            while scan_idx < len(prevSeq)-1:
                #if same digit is in the string, increment the count
                if prevSeq[scan_idx+1] == prevSeq[scan_idx]:
                    count += 1
                #update the current sequence with the count and digit of the subsequence
                else:
                    currSeq += str(count) 
                    currSeq += prevSeq[scan_idx]
                    count = 1
                scan_idx += 1
        return currSeq + str(count) + str(prevSeq[scan_idx])
