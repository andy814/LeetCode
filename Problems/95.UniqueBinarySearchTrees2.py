from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: # 拿下！ 
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def recur(start,end):
            if start==end:
                return [None]
            ret=[]
            for i in range(start,end):
                for l in recur(start,i):
                    for r in recur(i+1,end):
                        root=TreeNode(i)
                        root.left=l
                        root.right=r
                        ret.append(root)
            return ret
        return recur(1,n+1)