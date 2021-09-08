class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        return n & (-n) == n # -n is 2's complement of n --> -n = ~n+1
    #bitwise AND it with given n (which has just 1 bit set) to know if it's a power of 2
    #Ex: 2=0010; 4=0100; 8=1000; 16=10000
            
            
