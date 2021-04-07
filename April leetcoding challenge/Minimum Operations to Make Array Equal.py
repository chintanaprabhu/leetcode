#O(n) solution
class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 0:
            ops = 1
            counter = 1
            while n > 2:
                counter += 2
                ops += counter
                n -= 2
        else:
            ops = 0
            counter = 0
            while n > 1:
                counter += 2
                ops += counter
                n -= 2
        return ops
                
            
