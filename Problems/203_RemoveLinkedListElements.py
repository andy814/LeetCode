from typing import *
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]: # without setinel
        if not head:
            return None
        while head.val==val:
            if head.next:
                head=head.next
            else:
                return None
        curr=head.next
        prev=head
        while curr:
            if curr.val==val:
                curr=curr.next
                prev.next=curr
            else:
                prev=curr
                curr=curr.next
        return head

    def removeElements2(self, head: Optional[ListNode], val: int) -> Optional[ListNode]: 
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        curr=head
        while curr:
            if curr.val==val:
                curr=curr.next
                prev.next=curr
            else:
                prev=curr
                curr=curr.next
        return dummy.next