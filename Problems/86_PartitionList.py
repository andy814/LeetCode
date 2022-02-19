from typing import *
from unittest.mock import sentinel
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]: # space: O(n)
        vals=[]
        while head:
            vals.append(head.val)
            head=head.next
        s=[val for val in vals if val<x]
        el=[val for val in vals if val>=x]  
        vals=s+el
        sentinel=ListNode()
        curr=sentinel
        for val in vals:
            nextNode=ListNode(val)
            curr.next=nextNode
            curr=nextNode
        return sentinel.next

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]: # space: O(1)
        
        sentinel=ListNode(0,head)
        sSent=ListNode()
        lSent=ListNode()
        sCurr=sSent
        lCurr=lSent
        while head:
            if head.val<x:
                sCurr.next=head
                sCurr=sCurr.next
                sCurr.next=None
                sentinel.next=head.next
                head=head.next
            else:
                lCurr.next=head
                lCurr=lCurr.next
                lCurr.next=None
                sentinel.next=head.next
                head=head.next
        sCurr.next=lSent.next
        return sSent.next