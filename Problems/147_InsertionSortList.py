from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        processing=head.next
        head.next=None
        sentinel=ListNode(-float("inf"),head)
        while processing:
            nextProc=processing.next
            curr=sentinel
            prev=None
            while curr and curr.val<processing.val:
                prev=curr
                curr=curr.next
            prev.next=processing
            processing.next=curr
            processing=nextProc
        return sentinel.next
            

