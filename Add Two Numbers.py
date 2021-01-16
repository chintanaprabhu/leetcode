# python3 implementation
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newHead = ListNode(-1)
        outputPtr = newHead
        carry = 0
        
        while (l1 != None or l2 != None):
            if l1 == None: val1 = 0
            else: val1 = l1.val
            if l2 == None: val2 = 0
            else: val2 = l2.val
            summation = val1 + val2 + carry
            unitsVal = summation % 10
            newNode = ListNode(unitsVal)
            carry = summation // 10
            outputPtr.next = newNode
            outputPtr = outputPtr.next
            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next
        if carry:
            newNode = ListNode(carry)
            outputPtr.next = newNode
            outputPtr = outputPtr.next
        return newHead.next
        
