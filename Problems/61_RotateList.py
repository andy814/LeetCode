from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        vals1=[]
        while head:
            vals1.append(head.val)
            head=head.next
        
        numVals=len(vals1)
        offset=k%numVals
        vals2=[0]*numVals

        for i in range(numVals):
            vals2[(i+offset)%numVals]=vals1[i]
        
        sentinel=ListNode()
        curr=sentinel
        for val in vals2:
            newNode=ListNode(val)
            curr.next=newNode
            curr=curr.next
        return sentinel.next
