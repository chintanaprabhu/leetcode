#Python sol by math. ( Lagrange's four-square theorem )
class Solution:
    def numSquares(self, n: int) -> int:        
        while( n % 4 == 0 ):
            # Reduction by factor of 4
            n //= 4
        if n % 8 == 7:
            # Quick response for n = 8k + 7
            return 4
        # Check whether n = a^2 + b^2
        for a in range( int(sqrt(n))+1 ):
            b = int( sqrt( n - a*a ) )
            if ( a**2 + b ** 2 ) == n :
                return (a>0) + (b>0)
        # n = a^2 + b^2 + c^2
        return 3
        
#====================================================
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n+1)
        def squareNum(n):
            if n < 0:
                return math.int_max
            if n == 0:
                return 0
            if dp[n] > 0:
                return dp[n]
            minSquare = n
            for i in range(1, int(math.sqrt(n))+1):
                minSquare = min(squareNum(n-(i*i)), minSquare)
            dp[n] = minSquare+1
            return dp[n]
        return squareNum(n)
        
        
  
