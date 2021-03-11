# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return
        headAcopy = headA
        headBcopy = headB
        listAlen = 0
        listBlen = 0
        while headAcopy is not None:
            listAlen += 1
            headAcopy = headAcopy.next
        while headBcopy is not None:
            listBlen += 1
            headBcopy = headBcopy.next
        if listAlen > listBlen:
            while listAlen != listBlen:
                headA = headA.next
                listAlen -= 1
        else:
            while listAlen != listBlen:
                headB = headB.next
                listBlen -= 1
        while headA is not None or headB is not None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return
            
