class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dist = 0
        mask = 1
        for i in range(32):
            digit1 = x & mask
            digit2 = y & mask
            if digit1 != digit2:
                dist += 1
            mask = mask << 1
        return dist
