class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        prev = s[0]
        prevSeq = 0
        curSeq = 1
        #track every longest substr of 0's and 1's
        #number of substrings for every consecutive sequence of 0's and 1's is equal to the minimum of consecutive 0's or 1's
        for idx in range(1, len(s)):
            cur = s[idx]
            if cur == prev:
                curSeq += 1
            else:
                count += min(prevSeq, curSeq)
                prevSeq = curSeq
                curSeq = 1
                prev = cur
        count += min(prevSeq, curSeq)
        return count
