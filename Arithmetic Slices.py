class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        dp = [0] * len(A)
        for i in range(len(A)-2):
            if A[i+1]-A[i] == A[i+2]-A[i+1]:
                dp[i+2] = dp[i+1]+1
        return sum(dp)
