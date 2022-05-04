from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sumNumber=0
        def dfs(prevSum,currNode):
            nonlocal sumNumber
            currSum=prevSum*10+currNode.val
            if not currNode.left and not currNode.right: # isleaf
                sumNumber+=currSum
                return 
            if currNode.left:
                dfs(currSum,currNode.left)
            if currNode.right:
                dfs(currSum,currNode.right)
        dfs(0,root)