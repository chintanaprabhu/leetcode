class Solution:
    def reverseBits(self, n: int) -> int:
        rightBit = 1
        leftBit = 2147483648
        reverse = 0
        for i in range(16):
            left = n & rightBit
            right = n & leftBit
            if left:
                reverse = reverse | leftBit
            if right:
                reverse = reverse | rightBit
            leftBit = leftBit >> 1
            rightBit = rightBit << 1
        return reverse
            
            
