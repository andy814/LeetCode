from typing import *

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        prev=None
        def visit(curr):
            nonlocal prev
            if not curr:
                return
            
            prevRecord=prev
            rightRecord=curr.right
            leftRecord=curr.left
            prev=curr
            
            if prevRecord:
                prevRecord.right=curr
                prevRecord.left=None
            
            if leftRecord:
                visit(leftRecord)
            if rightRecord:
                visit(rightRecord)
                
        visit(root)
        prev.right=None