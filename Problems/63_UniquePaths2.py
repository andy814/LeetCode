from typing import *
from functools import cache
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1]==1 or obstacleGrid[0][0]==1:
            return 0
        @cache
        def dp(i,j):
            if i==m-1 and j==n-1:
                return 1
            res=0
            if i+1<m and obstacleGrid[i+1][j]==0:
                res+=dp(i+1,j)
            if j+1<n and obstacleGrid[i][j+1]==0:
                res+=dp(i,j+1)
            return res
        return dp(0,0)
                
            