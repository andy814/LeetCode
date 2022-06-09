from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        sentinel=ListNode()
        sentinel.next=head
        curr=head
        prev=sentinel
        while curr and curr.next:
            next=curr.next
            deleteFlag=False
            while next and next.val==curr.val:
                deleteFlag=True
                next=next.next
            if deleteFlag:
                prev.next=next
                curr=next
            else:
                prev=curr
                curr=next 
        return sentinel.next