import collections
from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

nodeVal={} # only used for pathSum

visited=collections.defaultdict(lambda:0) # only used for pathSum2
acc=0

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int: # O(nlogn)
        if not root:
            return 0
        return self.processNode(root,0,targetSum)

    def processNode(self,node,index,targetSum): 
        ret=0
        originalIndex=index
        valCount=node.val
        nodeVal[index]=node.val
        while index!=0:
            if valCount==targetSum:
                ret+=1
            index=(index-1)//2
            valCount+=nodeVal[index]
        if valCount==targetSum:
            ret+=1
        if node.left:
            ret+=self.processNode(node.left,2*originalIndex+1,targetSum)
        if node.right:
            ret+=self.processNode(node.right,2*originalIndex+2,targetSum)  
        return ret


    def pathSum2(self, root: Optional[TreeNode], targetSum: int) -> int: # O(n)
        if not root:
            return 0
        global acc
        count=0
        acc+=root.val
        if acc==targetSum:
            count+=1
        if acc-targetSum in visited:
            count+=visited[acc-targetSum]
        visited[acc]+=1
        if root.left:
            count+=self.pathSum2(root.left,targetSum)
        if root.right:
            count+=self.pathSum2(root.right,targetSum)
        visited[acc]-=1
        acc-=root.val
        return count