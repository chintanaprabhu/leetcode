class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n+1))
        #factorial lookup - array of factorials from 0 till n-1
        factorials = [1]
        for i in range(1, n):
            factorials.append(factorials[i-1] * i)
        #decrement k as the factorial space starts from 0! till (n-1)!
        k -= 1
        
        output = []
        for i in range(1, n+1):
            #find the index corresponding to the digit from nums that is part of k_th factorial
            index = k // factorials[n-i]
            #output permutation is formed from left to right
            output.append(str(nums[index]))
            #delete the number already included in the permutation
            del nums[index]
            #update the index as the factorial space has been narrowed down
            k -= index * factorials[n-i]
        return ''.join(output)
