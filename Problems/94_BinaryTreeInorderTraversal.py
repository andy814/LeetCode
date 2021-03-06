from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        ret=[root.val]
        return self.inorderTraversal(root.left)+ret+self.inorderTraversal(root.right)

    def inorderTraversal_iter(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        if root==None:
            return []
        ret=[root.val]
        return self.inorderTraversal(root.left)+ret+self.inorderTraversal(root.right)