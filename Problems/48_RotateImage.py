from typing import *
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def rotateFour(i,j,matrix): # i,j: upper-left pos
            m=min(i,j)
            #offset=n-2*m-1

            # m[0][1]=m[2][0]
            # m[2][0]=m[3][2]
            # m[3][2]=m[1][3]
            # m[1][3]=m[0][1]  
            # i=0 j=1 m=0 n=4

            # m[2][1]=m[4][2]
            # m[4][2]=m[3][4]
            # m[3][4]=m[1][3]
            # m[1][3]=m[2][1]
            # i=2 j=1 m=1 n=6

            if m==i:
                temp=matrix[m][j]
                matrix[m][j]=matrix[n-j-1][m]
                matrix[n-j-1][m]=matrix[n-m-1][n-j-1]
                matrix[n-m-1][n-j-1]=matrix[j][n-m-1]
                matrix[j][n-m-1]=temp
            else:
                temp=matrix[i][m]
                matrix[i][m]=matrix[n-m-1][i]
                matrix[n-m-1][i]=matrix[n-i-1][n-m-1]
                matrix[n-i-1][n-m-1]=matrix[m][n-i-1]
                matrix[m][n-i-1]=temp

        n=len(matrix)
        if n%2==0:
            for i in range((n+1)//2):
                for j in range((n+1)//2):
                    rotateFour(i,j,matrix)    
        else:
            for i in range((n+1)//2-1):
                for j in range((n+1)//2):
                    rotateFour(i,j,matrix)   

        