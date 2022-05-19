import functools
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent= None

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def DFS(root):
            if root.left:
                root.left.parent=root
                DFS(root.left)
            if root.right:
                root.right.parent=root
                DFS(root.right)

        DFS(root)
        pPath=set([p])
        while p!=root:
            p=p.parent
            pPath.add(p)
        while q not in pPath:
            q=q.parent
        return q