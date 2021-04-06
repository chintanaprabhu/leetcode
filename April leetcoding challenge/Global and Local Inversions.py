class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
      # Global inversion : i < j and A[i] > A[j]
      # Local inversion: A[i] > A[i+1] -> adjecent elements inverted
      # All local inversions are global inversions. We need to check for even a single global inversion in the array to prove 
      # that #global inversions != #local inversions. 
      # Max would help us keep track of the largest element from the beginning of the array and 
      # compare with elements to the right of it to be smaller than Max
        Max = -1
        for i in range(0, len(A)-2):
            Max = max(A[i], Max)
            if Max > A[i+2]:
                return False
        return True
