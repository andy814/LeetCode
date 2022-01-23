from filecmp import cmp
from re import T
from typing import *
import collections
from functools import cmp_to_key

from gevent import iwait
from sqlalchemy import false

class Solution1:
    def minimumCost(self, cost: List[int]) -> int:
        sortedCost=sorted(cost,reverse=True)
        for i in range(0,len(cost)):
            if i%3==2:
                cost.remove(sortedCost[i])
        return sum(cost)

class Solution2:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        nums=[0]
        for diff in differences:
            nums.append(nums[-1]+diff)
        return max(0,(upper-lower)-(max(nums)-min(nums))+1)


class Node:
    def __init__(self,row,col,price,dist):
        self.row=row
        self.col=col
        self.price=price
        self.dist=dist

def cmpNode(Node1,Node2):
    if Node1.dist==Node2.dist and Node1.price==Node2.price and Node1.row==Node2.row:
        return Node1.col-Node2.col 
    if Node1.dist==Node2.dist and Node1.price==Node2.price:
        return Node1.row-Node2.row 
    if Node1.dist==Node2.dist:
        return Node1.price-Node2.price 
    return Node1.dist-Node2.dist

class Solution3:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        dist=collections.defaultdict(lambda:float("inf")) # saves tuple->int
        visited=set() # saves tuple
        queue=collections.deque() # saves tuple
        queue.append((start[0],start[1]))
        dist[(start[0],start[1])]=0
        m,n=len(grid),len(grid[0])
        while queue:
            curr=queue.popleft()
            if curr not in visited:
                visited.add(curr)
                if curr[0]+1<m and (curr[0]+1,curr[1]) not in visited and grid[curr[0]+1][curr[1]]!=0:
                    queue.append((curr[0]+1,curr[1]))
                    dist[(curr[0]+1,curr[1])]=dist[curr[0],curr[1]]+1
                if curr[0]-1>=0 and (curr[0]-1,curr[1]) not in visited and grid[curr[0]-1][curr[1]]!=0:
                    queue.append((curr[0]-1,curr[1]))
                    dist[(curr[0]-1,curr[1])]=dist[curr[0],curr[1]]+1
                if curr[1]+1<n and (curr[0],curr[1]+1) not in visited and grid[curr[0]][curr[1]+1]!=0:
                    queue.append((curr[0],curr[1]+1))
                    dist[(curr[0],curr[1]+1)]=dist[curr[0],curr[1]]+1
                if curr[1]-1>=0 and (curr[0],curr[1]-1) not in visited and grid[curr[0]][curr[1]-1]!=0:
                    queue.append((curr[0],curr[1]-1))
                    dist[(curr[0],curr[1]-1)]=dist[curr[0],curr[1]]+1

        nodes=[]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]<=pricing[1] and grid[i][j]>=pricing[0] and dist[(i,j)]<float("inf"):
                    nodes.append(Node(i,j,grid[i][j],dist[(i,j)]))

        #nodes.sort(key=lambda n:[n.dist,n.price,n.row,n.col])
        nodes.sort(key=cmp_to_key(cmpNode))
        ret=[]

        for i in range(min(k,len(nodes))):
            node=nodes[i]
            ret.append([node.row,node.col])
        return ret

class Solution4:
    def numberOfWays(self, corridor: str) -> int:
        plantsGroup=[]
        metS=0
        countP=0
        plantMode=False
        if corridor.count("S")%2!=0:
            return 0
        for i in range(len(corridor)):
            if corridor[i]=="S":
                if plantMode:
                    plantMode=False
                    plantsGroup.append(countP+1)
                    countP=0
                    metS=1
                else:
                    metS+=1
                    if metS==2:
                        plantMode=True
            else: # met P
                if plantMode:
                    countP+=1

        ret=1
        for num in plantsGroup:
            ret*=num
        return ret%(1000000000+7)