# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #locate the mid of the list
        endNode = midNode = head
        num = ""
        llLen = 0
        while endNode != None:
            llLen += 1
            midNode = midNode.next
            endNode = endNode.next
            if endNode:
                llLen += 1
                endNode = endNode.next
        #reverse the second half of the list in place
        prev = None
        cur = midNode
        while cur != None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        #check if the first half and second half of the list are equal
        halfLen = llLen // 2
        while halfLen > 0:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
            halfLen -= 1
        return True
        
            
            
