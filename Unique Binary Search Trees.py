class Solution:
    #catalan number -> DP solution with O(n) space
    def numTrees(self, n: int) -> int:
        G = [0] * (n+1)
        G[0] = G[1] = 1
        for i in range (2,n+1):
            for j in range (1,i+1):
                #repeatedly find the number of unique subtrees with i as the root
                G[i] += G[j-1] * G[i-j]
        return G[n]
