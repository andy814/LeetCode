from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sentinel=ListNode()
        sentinel.next=head

        curr=head
        while curr:
            prev=curr
            curr=curr.next
            if prev!=sentinel.next:
                prev.next=sentinel.next
            else:
                prev.next=None
            sentinel.next=prev 


        curr=sentinel
        for i in range(n-1):
            curr=curr.next

        curr.next=curr.next.next
            
        curr=sentinel.next
        while curr:
            prev=curr
            curr=curr.next
            if prev!=sentinel.next:
                prev.next=sentinel.next
            else:
                prev.next=None
            sentinel.next=prev 

        return sentinel.next


sol=Solution()
node1=ListNode(1)
node2=ListNode(2)
node1.next=node2
node2.next=None
print(sol.removeNthFromEnd(node1,1).val)