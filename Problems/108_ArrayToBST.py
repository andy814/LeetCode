from typing import *
import collections
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]: #构造出树然后用BFS把节点往数组里面填
        root=self.ArrayToBST(nums)
        return root
        '''
        if root==None:
            return None
        ret=[]
        queue=collections.deque()
        queue.append(root)
        while queue:
            currNode=queue.popleft()
            ret.append(currNode)
            if currNode!=None:
                queue.append(currNode.left)
                queue.append(currNode.right)
        return ret
        '''

    def ArrayToBST(self,aa):
        if len(aa)==0:
            return None
        pIdx=len(aa)//2
        val=aa[pIdx]
        lNode=self.ArrayToBST(aa[:pIdx]) if len(aa[:pIdx])>0 else None
        rNode=self.ArrayToBST(aa[pIdx+1:]) if len(aa[pIdx+1:])>0 else None
        pNode=TreeNode(val,lNode,rNode)
        return pNode
        
sol=Solution()
sol.sortedArrayToBST([-10,-3,0,5,9])