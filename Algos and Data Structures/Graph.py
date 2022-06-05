from typing import *
import collections
import heapq

def BellmanFord(edges: List[List[int]], N: int, K: int) -> int:
    # used for dense graph 
    # O(VE)
    # no negative cycle
    # N: number of vertices
    # K: source
    # edges: [from,to,weight]
    dist=collections.defaultdict(lambda:float("inf"))
    dist[K] = 0
    for _ in range(N-1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return False
    return dist # get distance dict
    # return [dist.get(i, float("inf")) for i in range(N)] # get distance array

'''
如果我们已经求出了k个离源点距离最近的点，以及它们各自的距离，那么到源点距离第k+1近的点，它到源点的最短路径只能经过这前k个点——
如果经过了其他点，那么这个其他点显然离源点更近，那这个点一定不是第k+1近了。
既然只经过这前k个点，那么只用这前k个点放缩就可以找到那个最短路径了。再加上前k-1个点上一轮已经放缩过，所以每一轮只需要用新加入的节点进行放缩就行了。
'''
def Dijkstra(times: List[List[int]], N: int, K: int) -> int: # prim ver with pruning, but speed is similar
    # visited set can be dropped if solving grid problem since the edge is limited to adjacent nodes, see https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/discuss/2085640/JavaPython-3-Shortest-Path-w-brief-explanation-analysis-and-similar-problems.
    # used for sparse graph
    # O(ElogV+VlogV)， or O(ElogV, if not need to be connected)
    # no negative edge
    # times = edges = [from,to,weight]
    weight = collections.defaultdict(list)
    for u, v, w in times:
        weight[u].append((v,w))
    heap = [(0, K)]
    dist = [float("inf")]*N
    dist[K]=0
    visited=set()
    while heap and len(visited)<N:
        time, u = heapq.heappop(heap)
        if u not in visited:
            visited.add(u)
            for v,w in weight[u]:
                if v not in visited and dist[v]>time+w:
                    dist[v]=time+w
                    heapq.heappush(heap, (time+w, v))
    return dist            
    #return [dist.get(i, float("inf")) for i in range(N)]

def Dijkstra(times: List[List[int]], N: int, K: int) -> int: # Prim ver, but the speed is similar
    weight = collections.defaultdict(list)
    for u, v, w in times:
        weight[u].append((v,w))
    heap = [(0, K)]
    dist = [float("inf")]*N
    dist[K]=0
    visited=set()
    while heap and len(visited)<N:
        time, u = heapq.heappop(heap)
        if u not in visited:
            visited.add(u)
            for v,w in weight[u]:
                if v not in visited and dist[v]>time+w:
                    dist[v]=time+w
                    heapq.heappush(heap, (dist[v], v))
    return dist  
  

def Floyd(times: List[List[int]], N: int) -> int:
    # O(n^3)
    dist = [[float("inf") for _ in range(N)] for _ in range(N)]
    for u, v, w in times:
        dist[u][v] = min(w,dist[u][v])
    for i in range(N):
        dist[i][i] = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    return dist

def Prim(edges:List[List[int]] , N: int) -> int:
    # time complexity is same as dijkstra
    # used for dense graph
    weight = collections.defaultdict(list)
    for u, v, w in edges:
        weight[u].append((v,w))
    ans=0
    heap = [(0, 0)]
    visited=set()
    dist = [float('inf')]*N
    while heap and len(visited)<N:
        time, u = heapq.heappop(heap)
        if u not in visited:
            ans+=time
            visited.add(u)
            for v,w in weight[u]:
                if v not in visited and dist[v]>w:
                    dist[v]=w
                    heapq.heappush(heap, (w,v))
    return ans


class UnionFind():
    def __init__(self,n):
        self.p=list(range(n))
        self.rank=[1]*n

    def find(self,i):
        if i!=self.p[i]:
            self.p[i]=self.find(self.p[i])
        return self.p[i]

    def union(self,i,j): # or you can return False/True to check whether they are connected
        rooti=self.find(i)
        rootj=self.find(j)

        if rooti==rootj:
            return False

        if self.rank[rooti]>self.rank[rootj]:
            self.p[rootj]=rooti
        elif self.rank[rooti]<self.rank[rootj]:
            self.p[rooti]=rootj
        else:
            self.p[rootj]=rooti
            self.rank[rooti]+=1
        return True
    
def Kruskal(edges:List[List[int]], N:int) -> int: # regular implementation
    # used for sparse graph
    # O(ElogV+ElogE)
    # remember that we can only use half of the edges (arbitary direction for every undirected edge) to get the correct result.
    for edge in edges:
        edge[0],edge[1],edge[2]=edge[2],edge[0],edge[1]
    edges.sort()  # Sort increasing order by dist
    uf = UnionFind(N)
    ans = 0
    for d, u, v in edges:
        if uf.union(u, v):
            ans += d
            N -= 1
        if N == 1: break  # a bit optimize when we found enough n-1 edges!
    return ans

class UnionFind:
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

def Kruskal(edges: List[List[int]], N:int) -> int: # implement with heap, faster (why?)
    for edge in edges:
        edge[0],edge[1],edge[2]=edge[2],edge[0],edge[1]
    heapq.heapify(edges)
    res = 0
    UF = UnionFind(N)
    while edges and UF.count!=1:
        cost,u,v = heapq.heappop(edges)
        if UF.union(u,v):
            res += cost
    return res