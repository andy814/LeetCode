from typing import *
from sortedcontainers import SortedList
from collections import Counter,defaultdict
from functools import cache
from collections import deque

class Solution1:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n=len(grid[0])
        def isDiag(i,j):
            nonlocal n
            if i==j:
                return True
            if i+j==n-1:
                return True
            return False
            
        for i in range(n):
            for j in range(n):
                if isDiag(i,j) and grid[i][j]==0:
                    return False
                if not isDiag(i,j) and grid[i][j]!=0:
                    return False
        return True

class Solution2: # single-sided square
    def countHousePlacements(self, n: int) -> int:
        modulo=10**9+7
        @cache
        def dp(n):
            if n==0:
                return 1
            elif n==1:
                return 2
            return (dp(n-2)+dp(n-1))%modulo
        return (dp(n)**2)%modulo

class Solution3:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        def maximumSubarraySum(arr):
            n = len(arr)
            maxSum = -float("inf")
            currSum = 0
            for i in range(n):
                currSum = currSum + arr[i]
                if(currSum > maxSum):
                    maxSum = currSum
                if(currSum < 0):
                    currSum = 0
            return maxSum

        diffLR=[num1-num2 for num1,num2 in zip(nums1,nums2)]
        diffRL=[-num for num in diffLR]
        rMax=sum(nums2)+maximumSubarraySum(diffLR)
        lMax=sum(nums1)+maximumSubarraySum(diffRL)
        return max(rMax,lMax)

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int: # 90% possibility of getting TLE
        n=len(nums)
        edgeDict=defaultdict(set)
        for edge in edges:
            edgeDict[edge[0]].add(edge[1])
            edgeDict[edge[1]].add(edge[0])    
            
        # get pairwise shortest distance( O(n^2) )
        dist=[ [0]*n for _ in range(n) ] # dist[i]: ith node: dist to all other nodes
        
        def standardBFS(src):
            E=edgeDict
            visited=set()
            queue=deque()
            queue.append((src,0))
            while queue:
                currV,d=queue.popleft()
                if currV not in visited:
                    visited.add(currV)
                    dist[src][currV]=d
                    for V in E[currV]:
                        if V not in visited:
                            queue.append((V,d+1))
            return visited      
        for i in range(n):
            standardBFS(i)
            
        #print(dist)
        
        # for each edge, get the xor of two sides ( O(n^2) )
        def getInitList():
            return [0,0]
        XORdict=defaultdict(getInitList) # key: (v1,v2) value: (xor_v1,xor_v2)
        
        
        def getXOR(edge): 
            E=edgeDict
            E[edge[0]].remove(edge[1])
            E[edge[1]].remove(edge[0])

            def BFS(src):
                res=0
                visited=set()
                queue=deque()
                queue.append(src)
                while queue:
                    currV=queue.popleft()
                    if currV not in visited:
                        visited.add(currV)
                        res^=nums[currV]
                        for V in E[currV]:
                            if V not in visited:
                                queue.append(V)
                return res

            xor0=BFS(edge[0])
            xor1=BFS(edge[1])
            XORdict[(edge[0],edge[1])]=(xor0,xor1)
            
            E[edge[0]].add(edge[1])
            E[edge[1]].add(edge[0])
            
            #print(edge,xor0,xor1)
            #print(E)
            #print("done")
            
        for edge in edges:
            getXOR(edge)

        # search all possible pairs, divide into three pairs, do calculation

        ans=float("inf")
        for i in range(len(edges)):
            for j in range(i+1,len(edges)):
                edge1=edges[i]
                edge2=edges[j]
                v11,v12=edge1[0],edge1[1]
                v21,v22=edge2[0],edge2[1]
                part11,part12=XORdict[(v11,v12)]
                if dist[v11][v21]<dist[v12][v21]:
                    major1,p1=part11,part12
                else:
                    major1,p1=part12,part11
                part21,part22=XORdict[(v21,v22)]
                if dist[v21][v11]<dist[v22][v11]:
                    major2,p2=part21,part22
                else:
                    major2,p2=part22,part21
                    
                XORs=[p1,p2,major1^p2]
                #print(part11,part12,part21,part22,major1,major2,p1,p2)
                #print(edge1,edge2,XORs)
                ans=min(ans,max(XORs)-min(XORs))    
                
        return ans