from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddSentinel=ListNode()
        evenSentinel=ListNode()
        oddCurr=oddSentinel
        evenCurr=evenSentinel
        if not head:
            return None
        isOdd=True
        while head:
            if isOdd:
                oddCurr.next=head
                oddCurr=oddCurr.next
            else:
                evenCurr.next=head
                evenCurr=evenCurr.next
            isOdd=not isOdd
            head=head.next
        oddCurr.next=evenSentinel.next
        evenCurr.next=None
        return oddSentinel.next