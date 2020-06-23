class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        for num in nums:
            #set the bit mask to the number that's been seen once  
            seen_once = ~seen_twice & (seen_once^num)
            #set the bit mask to the number that's been seen twice and
            #clear the one time bit mask for the same number
            seen_twice = ~seen_once & (seen_twice^num)
        return seen_once
