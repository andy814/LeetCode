from typing import *
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        rightMost=[]
        def BFS(root):
            queue=collections.deque([(root,0)])
            while queue:
                #print(curr.val,h)
                curr,h=queue.pop()
                if len(rightMost)<=h:
                    rightMost.append(curr.val)
                if curr.right:
                    queue.appendleft((curr.right,h+1))
                if curr.left:
                    queue.appendleft((curr.left,h+1))
        BFS(root)
        return rightMost
                