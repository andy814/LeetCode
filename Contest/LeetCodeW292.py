from functools import cache
import collections
from typing import *
from collections import defaultdict
from sortedcontainers import SortedList
import math

from sqlalchemy import true


class Solution1:
    def largestGoodInteger(self, num: str) -> str:
        prior=["999","888","777","666","555","444","333","222","111","000"]
        for p in prior:
            if p in num:
                return p
        return ""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution2:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        @cache
        def getSumAndNum(root):
            if not root:
                return (0,0)
            else:
                return (getSumAndNum(root.left)[0]+getSumAndNum(root.right)[0]+root.val, 
                getSumAndNum(root.left)[1]+getSumAndNum(root.right)[1]+1)

        @cache
        def getAverageNodes(root):
            if not root:
                return 0
            else:
                avg=(getSumAndNum(root.left)[0]+getSumAndNum(root.right)[0]+root.val)// \
                (getSumAndNum(root.left)[1]+getSumAndNum(root.right)[1]+1)
            isNode=1 if avg==root.val else 0
            return getAverageNodes(root.left)+getAverageNodes(root.right)+isNode

        return getAverageNodes(root)

class Solution3:
    def countTexts(self, pressedKeys: str) -> int: #TLE
        if len(pressedKeys)==1:
            return 1
        comb=[]
        Counter=[1]
        SN_idx=[False] 
        if pressedKeys[0]=="7" or pressedKeys[0]=="9":
            SN_idx[0]=True
            
        for i in range(len(pressedKeys)-1):
            if pressedKeys[i+1]!=pressedKeys[i]:
                Counter.append(1)
                if pressedKeys[i+1]=="7" or pressedKeys[i+1]=="9":
                    SN_idx.append(True)
                else:
                    SN_idx.append(False)
                    
            else:
                Counter[-1]+=1
                
        @cache
        def perm(n,c):
            return math.perm(n,c)
        
        def dfs(key,isSN):
            ans=0
            if isSN:
                for third in range( Counter[key]//4 + 1 ):
                    remain2=( Counter[key]-third*4 )
                    for second in range( remain2//3 + 1 ):
                        remain1=remain2-second*3
                        for first in range(remain1//2 + 1):
                            zero=remain1-first*2
                            numSum=zero+first+second+third
                            ans+=perm(numSum,numSum)// \
                            (perm(third,third)*perm(second,second)*perm(first,first)*perm(zero,zero))

            else:
                for second in range( Counter[key]//3 + 1 ):
                    remain1=Counter[key]-second*3
                    for first in range(remain1//2 + 1):
                        zero=remain1-first*2
                        numSum=zero+first+second
                        ans+=perm(numSum,numSum)// \
                        (perm(second,second)*perm(first,first)*perm(zero,zero))

            ans=ans%(10**9+7)
            comb.append(ans)
        
        for i in range(len(Counter)):
            dfs(i,SN_idx[i])

        #print("d")
        #print(comb)
        ans=1
        for c in comb:
            ans*=c
            ans=ans%(10**9+7)
        
        return ans%(10**9+7)

class Solution3:
    def countTexts(self, keys: str) -> int:
        MOD=10**9+7
        @cache
        def dp(i):
            if i<0:
                return 1
            if i==0:
                return 1
            if i>=3 and keys[i] in "79" and keys[i]==keys[i-1]==keys[i-2]==keys[i-3]:
                return dp(i-1)%MOD+dp(i-2)%MOD+dp(i-3)%MOD+dp(i-4)%MOD
            if i>=2 and keys[i]==keys[i-1]==keys[i-2]:
                return dp(i-1)%MOD+dp(i-2)%MOD+dp(i-3)%MOD
            if i>=1 and keys[i]==keys[i-1]:
                return dp(i-1)%MOD+dp(i-2)%MOD
            return dp(i-1)%MOD

        return dp(len(keys)-1)%MOD

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m=len(grid)
        n=len(grid[0])
        solvable=False
        def dfs(i,j,LeftBrackets):
            nonlocal m
            nonlocal n
            nonlocal solvable
            if i==m-1 and j==n-1 and LeftBrackets==0:
                solvable=True
            curr=grid[i][j]
            if i<m-1:
                if grid[i+1][j]=="(":
                    dfs(i+1,j,LeftBrackets+1)
                else:
                    if LeftBrackets>0:
                        dfs(i+1,j,LeftBrackets-1)

            if j<n-1 and grid[i][j+1]!=curr:
                if grid[i][j+1]=="(":
                    dfs(i,j+1,LeftBrackets+1)
                else:
                    if LeftBrackets>0:
                        dfs(i,j+1,LeftBrackets-1)

        dfs(0,0,0)
        return solvable