from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        sumVal=l1.val+l2.val
        if sumVal>9:
            carry=1
            sumVal-=10
        head=ListNode(sumVal)
        prev=head
        while l1.next or l2.next:
            if not l1.next:
                l2=l2.next
                sumVal=l2.val+carry
            elif not l2.next:
                l1=l1.next
                sumVal=l1.val+carry
            else:
                l1=l1.next
                l2=l2.next
                sumVal=l1.val+l2.val+carry
            carry=0
            if sumVal>9:
                carry=1
                sumVal-=10
            sumNode=ListNode(sumVal)
            prev.next=sumNode
            prev=sumNode
        if carry:
            sumNode=ListNode(1)
            prev.next=sumNode
        return head