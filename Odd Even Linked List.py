# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        evenList = ListNode(-1)
        evenHead = evenList
        oddList = ListNode(-1)
        oddHead = oddList
        length = -1
        while head is not None:
            length += 1
            if length % 2 == 0:
                evenList.next = head
                evenList = evenList.next
            else:
                oddList.next = head
                oddList = oddList.next
            head = head.next
        evenList.next = None
        oddList.next = None
        evenList.next = oddHead.next
        return evenHead.next
#################################Referred solution#############
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        oddList = head
        evenList = head.next
        evenHead = evenList
        while evenList != None and evenList.next != None:
            oddList.next = evenList.next
            oddList = oddList.next
            evenList.next = oddList.next
            evenList = evenList.next
        oddList.next = evenHead
        return head
