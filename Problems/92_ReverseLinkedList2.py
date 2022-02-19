from fileinput import nextfile
from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]: # space:O(n)
        vals=[]
        while head:
            vals.append(head.val)
            head=head.next
        if left!=1:
            vals[left-1:right]=vals[right-1:left-2:-1]
        else:
            vals[left-1:right]=vals[right-1::-1]
            
        sentinel=ListNode()
        curr=sentinel
        for val in vals:
            nextNode=ListNode(val)
            curr.next=nextNode
            curr=curr.next
        return sentinel.next

    def reverseBetween_inPlace(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]: # space:O(1)
        if not head or right==1:
            return head
        p1=p2=p3=p4=None
        sentinel=ListNode()
        sentinel.next=head
        prev=sentinel
        curr=sentinel.next
        idx=0
        while curr:
            idx+=1
            next=curr.next
            if idx==left-1:
                p1=curr
            if idx==left:
                p2=curr
            if idx==right:
                p3=curr
            if idx==right+1:
                p4=curr
            if left<idx<=right:
                curr.next=prev
            prev=curr
            curr=next
        if p1:
            p1.next=p3
            p2.next=p4
            return sentinel.next
        else:
            sentinel.next=p3
            p2.next=p4
            return sentinel.next