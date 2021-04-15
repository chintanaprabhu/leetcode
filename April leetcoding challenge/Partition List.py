# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
    #Needs cleaning!!!!
        if not head:
            return
        start = head
        low = None
        high = None
        while start != None:
            if start.val < x:
                low = ListNode(start.val, None)
                break
            start = start.next
        start = head
        while start != None:
            if start.val >= x:
                high = ListNode(start.val, None)
                break
            start = start.next
        sortedList = None
        lowStart = low
        highStart = high
        while head != None:
            node = ListNode(head.val, None)
            #print(node, 'node')
            if node.val < x:
                low.next = node
                low = low.next
            else:
                high.next = node
                high = high.next
            head = head.next
        if low is None:
            return highStart.next
        if high is None:
            return lowStart.next
        low.next = highStart.next
        return lowStart.next
            
                
