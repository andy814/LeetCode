from typing import *
from functools import cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        @cache
        def dp(i,j):
            res=grid[i][j]
            if i==m-1 and j==n-1:
                return res
            down,right=float("inf"),float("inf")
            if i+1<m:
                down=dp(i+1,j)
            if j+1<n:
                right=dp(i,j+1)
            return res+min(down,right)
        return dp(0,0)
            