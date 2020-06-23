# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#iterative solution
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prevNode = None
        currNode = head
        #iterate till the end of the list
        #change the reference of every alternate nodes and proceed further
        while currNode != None:
            tempNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = tempNode
        return prevNode
            
