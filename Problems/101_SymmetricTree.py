from typing import Optional
 #Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check(node1,node2):
    if ( node1 and not node2) or ( node2 and not node1):
        return False
    if ( not node1 ) and ( not node2 ):
        return True
    return node1.val==node2.val and check(node1.left,node2.right) and check(node1.right,node2.left)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return check(root.left,root.right)



        