import numpy as np
from typing import *
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        grid=np.array(grid)
        for _ in range(k):
            rightCol=grid[:,-1]

            for i in range(len(grid)-1,0,-1):
                grid[:,i]=grid[:,i-1]
            grid[:,0]=rightCol

            temp=grid[-1,0]
            for i in range(len(grid[0])-1,0,-1):
                grid[i,0]=grid[i-1,0]
            grid[0,0]=temp
        grid=list(grid)
        return grid
