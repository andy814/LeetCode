from typing import *
import functools

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @functools.cache
        def dp(root):
            if not root:
                return 0
            noRub=dp(root.left)+dp(root.right)
            Rub=root.val
            if root.left:
                Rub+=dp(root.left.left)+dp(root.left.right)
            if root.right:
                Rub+=dp(root.right.left)+dp(root.right.right)
            return max(noRub,Rub)

        return dp(root)