from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []    
        ret=[]
        def dfs(trace,prefixSum,currNode):
            isLeaf=True
            #print("prefixSum:",prefixSum)
            if currNode.left:
                trace.append(currNode.val)
                dfs(trace,prefixSum+currNode.val,currNode.left)   
                trace.pop()
                isLeaf=False
            if currNode.right:
                trace.append(currNode.val)
                dfs(trace,prefixSum+currNode.val,currNode.right)
                trace.pop()
                isLeaf=False
            if isLeaf and prefixSum+currNode.val==targetSum:
                addRet=trace.copy()
                addRet.append(currNode.val)
                ret.append(addRet)
        dfs([],0,root)
        return ret