# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        llLen = 0
        tempHead = head
        while tempHead != None:
            llLen += 1
            tempHead = tempHead.next
        #print(llLen, 'llLen')
        fromEnd = llLen - k
        firstNode = head
        while k > 1:
            firstNode = firstNode.next
            k -= 1
        endNode = head
        while fromEnd > 0:
            endNode = endNode.next
            fromEnd -= 1
        firstNode.val, endNode.val = endNode.val, firstNode.val
        #print(firstNode.val, 'firstNode.val')
        #print(endNode.val, 'endNode.val')
        return head
