class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = 0
        for num in nums:
            #XOR of same bits return 0 and 
            #we end up with the unique element upon traversing the  complete list
            #Ref:Utilize the property of XOR, A ⊕ A = 0, to cancel those elements which appeared twice.
            unique ^= num 
        return unique
