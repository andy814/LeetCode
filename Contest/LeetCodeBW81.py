from copy import deepcopy
import functools
from typing import *
from collections import Counter
import heapq
from functools import cache
from itertools import combinations
import collections
from matplotlib.style import available
from nose import run_exit
from sortedcollections import SortedList
from collections import deque
import bisect
import math

class Solution1:
    def countAsterisks(self, s: str) -> int:
        ctr=Counter(s)
        total=ctr['*']
        inside=0
        metBar=False
        for i in range(len(s)):
            if s[i]=="|":
                metBar=not metBar
            else:
                if metBar and s[i]=="*":
                    inside+=1
        return total-inside

# record    
class Solution2:
    class UnionFind():
        def __init__(self,n):
            self.p=list(range(n))
            self.rank=[1]*n
            self.size=[1]*n
        
        def find(self,i):
            if i!=self.p[i]:
                self.p[i]=self.find(self.p[i])
            return self.p[i]

        def union(self,i,j): # or you can return False/True to check whether they are connected
            rooti=self.find(i)
            rootj=self.find(j)

            if rooti==rootj:
                return # or return False, used for Kruskal

            if self.rank[rooti]>self.rank[rootj]:
                self.p[rootj]=rooti
                self.size[rooti]+=self.size[rootj]

            elif self.rank[rooti]<self.rank[rootj]:
                self.p[rooti]=rootj
                self.size[rootj]+=self.size[rooti]

            else:
                self.p[rootj]=rooti
                self.rank[rooti]+=1
                self.size[rooti]+=self.size[rootj]

            # add return True when using Kruskal

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        UF=self.UnionFind(n)
        total=n*(n-1)//2
        for edge in edges:
            UF.union(edge[0],edge[1])
        for i in range(n):
            total-= (UF.size[i]*UF.size[i]-1)//2
        return total
        

class Solution3:
    def maximumXOR(self, nums: List[int]) -> int:
        maxLen=bin(max(nums))[2:]
        num1s=[0]*maxLen
        for num in nums:
            binnum=bin(num)[2:]
            for i,ch in enumerate(binnum[::-1]):
                num1s[i]+=int(ch)
        num1s=num1s[::-1]
        num1Bool=[]
        for i in range(len(num1s)):
            flag="1" if num1s[i]>=1 else "0"
            num1Bool.append(flag)
        concatStr="".join(num for num in num1Bool)
        return int(concatStr,2)


class Solution:
    '''
    def distinctSequences(self, n: int) -> int:
        @cache
        def math_gcd(a,b):
            return math.gcd(a,b)
        # total=0
        # def trace(step,prev2,curr):
        #     if step==n:
        #         total+=1
        #         total=total%(10**9 + 7)

        dp=[(0,0,0,0,0,0)]*n+1
        dp[1]=(1,1,1,1,1,1)
        dp[2]=()
        for i in range(3,n):
            dpi=[0]*6
            for j in range(6):
                total=sum(dp[i-1])
                for k in range(6):
                    if math_gcd(j+1,k+1)!=1:
                        total-=dp[i-1][k]
                total-=dp[i-2][j]

                dpi[j]=total
            dp[i]=tuple(dpi)
        
        return sum(dp[n])
    '''

    def distinctSequences(self, n: int) -> int: # top-down
        mod=10**9+7
        @cache
        def dp(n,p,pp):
            if n==0:
                return 1
            else:
                ans=0
                for i in range(1,7):
                    if i!=p and i!=pp and (math.gcd(i,p)==1 or p==0):
                        ans+=dp(n-1,i,p)%mod
                return ans
        return dp(n,0,0)%mod

    from copy import deepcopy
    def distinctSequences(self, n: int) -> int: # bottom-up
        mod=10**9+7
        prev=[[1]*7 for _ in range(7)]
        curr=[[float("inf")]*7 for _ in range(7)]
        for i in range(n-1):
            for p in range(1,7):
                for pp in range(1,7):
                    ans=0
                    for i in range(1,7):
                        if i!=p and i!=pp and (math.gcd(i,p)==1 or p==0):
                            ans+=prev[i][p]%mod
                    curr[p][pp]=ans
            prev=deepcopy(curr)
        return prev[0][0]%mod

