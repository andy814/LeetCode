from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        curr=head
        vals=[]
        while curr:
            vals.append(curr.val)
            curr=curr.next
        
        def buildTree(start,end):
            if start>end:
                return None
            mid=(start+end)//2
            currNode=TreeNode(vals[mid])
            currNode.left=buildTree(start,mid-1)
            currNode.right=buildTree(mid+1,end)
        
        return buildTree(0,len(vals)-1)
