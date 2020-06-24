# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #in-place reverse second half of the list
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        first_half_end = self.half_of_list(head)
        second_half_start = self.reverse(first_half_end.next)
        first_half_start = head
        while first_half_start and second_half_start:
            if first_half_start.val != second_half_start.val:
                return False
            first_half_start = first_half_start.next
            second_half_start = second_half_start.next
        return True
        
    def half_of_list(self, head):
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverse(self, head):
        previous = None
        current = head
        while current:
            tempNode = current.next
            current.next = previous
            previous = current
            current = tempNode
        return previous
