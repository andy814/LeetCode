from typing import *
import numpy as np
class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.prefixMatrix=np.zeros((len(matrix)+1,len(matrix[0])+1),dtype=int)
        self.calcPrefix()

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        count=0
        for i in range(row1,row2+1):
            for j in range(col1,col2+1):
                count+=self.matrix[i][j]
        return count
    
    def sumRegionQuick(self, row1: int, col1: int, row2: int, col2: int) -> int: # constant time after creating Prefix matrix
        row1,col1,row2,col2=row1+1,col1+1,row2+1,col2+1
        return self.prefixMatrix[row2,col2]-self.prefixMatrix[row1-1,col2]-self.prefixMatrix[row2,col1-1]+self.prefixMatrix[row1-1][col1-1]

    def calcPrefix(self):
        for i in range(1,len(self.matrix)+1):
            for j in range(1,len(self.matrix[0])+1):
                self.prefixMatrix[i][j]=self.prefixMatrix[i-1][j]+self.prefixMatrix[i][j-1]-self.prefixMatrix[i-1][j-1]+self.matrix[i-1][j-1]
