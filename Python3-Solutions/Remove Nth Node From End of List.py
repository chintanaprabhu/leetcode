# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #use a dummy node to make removal of node easier
        dummy = ListNode(0, head)
        first = second = dummy
        #run the first pointer till the end of the list maintaining the difference of n steps
        #between first and second pointer
        while first.next != None:
            #once first pointer has reached n steps ahead of second pointer
            #move second pointer till the node to be removed
            if n <= 0:
                second = second.next
            first = first.next
            n -= 1
        #change the "next" of previous node to the node next to the removed node 
        to_remove = second.next
        second.next = to_remove.next
        to_remove.next = None
        return dummy.next
