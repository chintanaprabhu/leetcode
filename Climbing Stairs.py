#dp with constant memory
class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 2
        if n == 1:
            return first
        for index in range(3, n+1):
            third = second + first
            first = second 
            second = third
        return second
            
            
