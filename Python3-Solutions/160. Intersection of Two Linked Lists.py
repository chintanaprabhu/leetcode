# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None: 
            return
        listA = headA
        listB = headB
        while listA != listB:
            if listA is None:
                listA = headB
            else:
                listA = listA.next
            if listB is None:
                listB = headA
            else:
                listB = listB.next
        return listA
            
