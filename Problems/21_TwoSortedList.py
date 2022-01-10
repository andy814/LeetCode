# Definition for singly-linked list.
from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        merged=[] # list of values
        if l1:
            curr=l1
            next=l1.next
            while next:
                merged.append(curr.val)
                curr=next
                next=next.next
            merged.append(curr.val)
        if l2:
            curr=l2
            next=l2.next
            while next:
                merged.append(curr.val)
                curr=next
                next=next.next
            merged.append(curr.val)
        
        if merged:
            merged.sort()
            head=ListNode(merged[0]) # get a list of nodes
            curr=None
            prev=head
            for i in range(1,len(merged)) :
                curr=ListNode(merged[i])
                prev.next=curr
                prev=curr
                if i == len(merged)-1:
                    curr.next=None
            return head
        
        else:
            return None

        '''

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        merged=[] # list of values
        curr1=l1
        curr2=l2
        while curr1 and curr2:
            if curr1.val<curr2.val:
                merged.append(curr1.val)
                curr1=curr1.next
            else:
                merged.append(curr2.val)
                curr2=curr2.next
        while curr1:
                merged.append(curr1.val)
                curr1=curr1.next
        while curr2:
                merged.append(curr2.val)
                curr2=curr2.next

        if merged:
            merged.sort()
            head=ListNode(merged[0]) # get a list of nodes
            curr=None
            prev=head
            for i in range(1,len(merged)) :
                curr=ListNode(merged[i])
                prev.next=curr
                prev=curr
                if i == len(merged)-1:
                    curr.next=None
            return head
        
        else:
            return None
        

node=ListNode(1)
node2=ListNode(3)
node.next=node2
node3=ListNode(5)
node2.next=node3

node4=ListNode(2)
node5=ListNode(4)
node4.next=node5

print(Solution().mergeTwoLists(node,node4))
