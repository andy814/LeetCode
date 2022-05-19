from functools import cache
from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        @cache
        def getSize(root):
            if not root:
                return 0
            return 1+getSize(root.left)+getSize(root.right)

        ls=getSize(root.left)
        curr=root
        while ls!=k-1:
            if ls>k-1:
                curr=curr.left
            else:
                k-=getSize(curr.left)+1
                curr=curr.right
            ls=getSize(curr.left)
        return curr.val