class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        max_index = max_num = 0
        num_of_elements = len(nums)
        #for num[num] corresponding to every number in the array, add a constant value(len of array)
        for index in range(num_of_elements):
            lookup_index = nums[index]%num_of_elements
            nums[lookup_index] += num_of_elements
        #at the end of loop, the array would have been transformed 
        #into an array with one unique max element.
        #This happens as a result of one number at a specific index(which is duplicate) 
        #would be added multiple times making it a max
        
        #return the index of the max_element and transform the array back to its original form
        for index, num in enumerate(nums):
            if num > max_num:
                max_num = num
                max_index = index
            nums[index] %= num_of_elements
        return max_index

#using Floyd's Tortoise and Hare (Cycle Detection) algorithm
class Solution:
    #convert the problem into linked list cycle II problem
    def findDuplicate(self, nums: List[int]) -> int:
        # start hopping from Node_#0
        slow, fast = 0, 0
		# Step_#1
		# Cycle detection
        # Let slow jumper and fast jumper meet somewhere in the cycle 
        while True:
			# slow jumper hops 1 step, while fast jumper hops two steps forward.
            slow = nums[ slow ]
            fast = nums[ nums[fast] ]
            if slow == fast:
                break
		# Step_#2
        # Locate the start node of cycle (i.e., the duplicate number)
        # fast is reset to the start node of the list
        fast = 0
        while True:
            slow = nums[ slow ]
            fast = nums[ fast ]
            if slow == fast:
                break
        return fast
