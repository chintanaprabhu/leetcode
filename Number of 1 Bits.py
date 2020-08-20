class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        mask = 1
        for i in range(32):
            if n & mask:
                ones += 1
            mask = mask << 1
        return ones
