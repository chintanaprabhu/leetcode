class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            #reverse the string and cast to an integer
            x = int(str(x)[::-1])      
        if x < 0:
            #reverse the string and cast to an integer
            x = -1 *int(str(abs(x))[::-1])
        if x < -2**31-1 or x > 2**31-1:
                return 0
        return x
            
        
