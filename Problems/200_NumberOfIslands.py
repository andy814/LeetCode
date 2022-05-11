from typing import *
import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        currMark=2

        def BFS(i,j):
            nonlocal currMark
            queue=collections.deque([(i,j)])
            while queue:
                curr_i,curr_j=queue.pop()
                grid[curr_i][curr_j]=str(currMark)
                for ni,nj in [(curr_i+1,curr_j),(curr_i-1,curr_j),(curr_i,curr_j+1),(curr_i,curr_j-1)]:
                    if 0<=ni<m and 0<=nj<n and grid[ni][nj]=="1":
                        queue.append((ni,nj))
            currMark+=1

        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    BFS(i,j)

        return currMark-2