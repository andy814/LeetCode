import math
from typing import *
class Solution1:
    def cellsInRange(self, s: str) -> List[str]:
        row1=int(s[1])
        col1=ord(s[0])
        row2=int(s[4])
        col2=ord(s[3])
    
        ret=[]
        for j in range(col1,col2+1):
            for i in range(row1,row2+1):  
                curr=chr(j)+str(i)
                ret.append(curr)
        return ret

class Solution2:
    '''
    def minimalKSum(self, nums: List[int], k: int) -> int: # MLE , 4GB
        #nums.sort()
        #curr=1
        fullList=set(range(1,len(nums)+k+1))
        for num in nums:
            if num in fullList:
                fullList.remove(num)
        fullList=sorted(fullList)
        return sum(fullList[:k])
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20, 23, 24, 26, 27, 28, 30, 31, 34, 36, 37, 38, 39, 41, 42, 43, 45, 46, 48]

    '''
    def minimalKSum(self, nums: List[int], k: int) -> int:
        firstKSum=(k)*(k+1)//2
        curr=k+1
        kSum=firstKSum
        numsSet=set(nums)
        for num in numsSet:
            if num<=k:
                kSum-=num
                while curr in numsSet:
                    curr+=1
                kSum+=curr
                curr+=1
        return kSum

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution3:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodeDict={}
        root=set()
        for node in descriptions:
            nodeDict[node[0]]=TreeNode(node[0],None,None)
            nodeDict[node[1]]=TreeNode(node[1],None,None)
            root.add(node[0])
        for node in descriptions:
            if node[2]:
                nodeDict[node[0]].left=nodeDict[node[1]]
            else:
                nodeDict[node[0]].right=nodeDict[node[1]]
            if node[1] in root:
                root.remove(node[1])
        return nodeDict[list(root)[0]]

class Solution4:
    
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]: # O(logm*n^2) , but not TLE!?
        def GCD(a,b):
            return GCD(b,a%b) if b!=0 else a
        i=0
        while i<len(nums)-1:
            gcd=GCD(nums[i],nums[i+1])
            if gcd>1:
                lcm=(nums[i]*nums[i+1])//gcd
                nums[i]=lcm
                del nums[i+1]
            else:
                i+=1

        return nums

    def replaceNonCoprimes2(self, nums: List[int]) -> List[int]: # O(nlogm)
        stack=[]
        for num in nums:
            while True:
                if not stack:
                    gcd=1
                else:
                    gcd=math.gcd(num,stack[-1])
                if gcd==1:
                    break
                last=stack.pop()
                num=num*last//gcd
            stack.append(num)
        return stack