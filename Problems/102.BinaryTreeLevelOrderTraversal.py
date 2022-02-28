import collections
from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=collections.deque([(root,0)])
        height=0
        ret=[]
        while queue:
            curr,height=queue.popleft()
            if len(ret)<=height:
                ret.append([])
            ret[height].append(curr.val)
            if curr.left:
                queue.append((curr.left,height+1))
            if curr.right:
                queue.append((curr.right,height+1))
        return ret
