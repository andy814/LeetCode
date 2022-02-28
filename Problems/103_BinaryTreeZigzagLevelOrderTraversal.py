from collections import deque
import collections
from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=collections.deque([root,None])
        ret=[[]]
        metNone=False
        while queue:
            curr=queue.popleft()
            if curr:
                ret[-1].append(curr.val)
                metNone=False
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            else:
                if metNone:
                    return ret
                queue.append(None)
                ret.append([])
                metNone=True            
        for i in range(1,len(ret),2):
            ret[i].reverse()
        return ret if len(ret[-1])!=0 else ret[:-1]