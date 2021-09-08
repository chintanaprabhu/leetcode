from random import randint
from bisect import bisect_right

class Solution:

    def __init__(self, w: List[int]):
        self.prefixWeight = w
        for i in range(1, len(w)):
            self.prefixWeight[i] = self.prefixWeight[i-1] + w[i]
         
    def pickIndex(self) -> int:
        sum_of_all_weight = self.prefixWeight[-1]
        randVal = randint(0, sum_of_all_weight-1)
        index = bisect_right(self.prefixWeight, randVal) #an insertion point which comes after (to the right of) any existing entries of randVal in prefixWeight.
        return index
