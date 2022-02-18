from typing import *
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None: # space:O(m+n)
        row0=set()
        col0=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row0.add(i)
                    col0.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row0 or j in col0:
                    matrix[i][j]=0

    def setZeroes2(self, matrix: List[List[int]]) -> None: # space:O(1)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    for j2 in range(len(matrix[0])):
                        if matrix[i][j2]!=0:
                            matrix[i][j2]=float("inf")
                    for i2 in range(len(matrix)):
                        if matrix[i2][j]!=0:
                            matrix[i2][j]=float("inf")
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==float("inf"):
                    matrix[i][j]=0

