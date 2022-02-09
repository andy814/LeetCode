from fileinput import nextfile
from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def traverse(head):
            while head:
                print(head.val)
                head=head.next
            print("-------")
            
        if not head:
            return None
        sentinel=ListNode()
        sentinel.next=head
        first=head
        second=head.next
        prevSecond=sentinel
        while second:
            traverse(sentinel.next)
            nextFirst=second.next
            nextSecond=nextFirst.next if nextFirst else None
            second.next=first
            first.next=nextFirst
            prevSecond.next=second
            prevSecond=second
            first=nextFirst
            second=nextSecond
        return sentinel.next