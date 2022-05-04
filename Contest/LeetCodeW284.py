from typing import *
class Solution1:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        keyIndices=[]
        for i,num in enumerate(nums):
            if num==key:
                keyIndices.append(i)
        ans=[]
        for i in range(len(nums)):
            for j in keyIndices:
                if -k<=i-j<=k:
                    ans.append(i)
                    break
        return ans

class Solution2:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        ans=0
        digSet=set()
        for d in dig:
            digSet.add(tuple(d))
        for artifact in artifacts:
            rlen=range(artifact[2]-artifact[0]+1)
            clen=range(artifact[3]-artifact[1]+1)
            flag=True
            for r in rlen:
                for c in clen:
                    if (r+artifact[0],c+artifact[1]) not in digSet:
                        flag=False
            if flag:
                ans+=1
        return ans

class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k&1 and len(nums)==1:
            return -1

        if k>len(nums):
            if k-len(nums)&1:
                return max(nums)
            else:
                return max(nums[:-1])
        
        return max( max(nums[:k-1]),nums[k] )

        #
        #[73,63,62,16,95,92,93,52,89,36,75,79,67,60,42,93,93,74,94,73,35,86,96],59

class Solution3:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k&1 and len(nums)==1:
            return -1

        #print(k-len(nums))
        if k>len(nums):
            return max(nums)
        
        if k==1:
            return nums[1]
        
        if k==len(nums):
            return max(nums[:-1])
            
        if k==0:
            return nums[0]
        
        return max( max(nums[:k-1]),nums[k] )


class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        self.count = n
    
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)
        if px==py:
            return False
        self.count-=1
        if self.rank[px]>self.rank[py]:
            self.parent[py]=px
            self.rank[px]+=self.rank[py]
        else:
            self.parent[px]=py
            self.rank[py]+=self.rank[px]
        return True
                
class Solution4:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
        heapq.heapify(edges)
        res = 0
        ds = DSU(n)
        while edges and ds.count!=1:
            cost,u,v = heapq.heappop(edges)
            if ds.union(u,v):
                res += cost
        return res
