#DP solution with optimized (constant) space usage
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [1] * n
        d_top = 1
        for col in range(1, m):
            for row in range(1, n):
            #the grid consecutive addition approach
                if row == 1:
                    d[row] = d[row] + d_top
                else:
                    d[row] = d[row-1] + d[row]
        return d[n-1]
