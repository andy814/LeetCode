from audioop import lin2adpcm
from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversedHead=ListNode()
        reversedHead.next=None
        curr=head
        while curr:
            next=curr.next
            curr.next=reversedHead.next
            reversedHead.next=curr
            curr=next
        return reversedHead.next
        
    def reverseList2(self, head: ListNode) -> ListNode:
        curr=head
        prev=None
        while curr:
            #print(curr.val,",")
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev

    def printList(self,head):
        while head:
            print(head.val," ")
            head=head.next

sol=Solution()
ln1=ListNode(1)
ln2=ListNode(2)
ln3=ListNode(3)
ln4=ListNode(4)
ln5=ListNode(5)
ln1.next=ln2
ln2.next=ln3
ln3.next=ln4
ln4.next=ln5
ln5.next=None
head=sol.reverseList2(ln1)
sol.printList(head)