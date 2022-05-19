from functools import cache
from typing import *
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                matrix[i][j]=int(matrix[i][j])
        #print(matrix)
        @cache
        def getSum(i,j):
            if i==j==0:
                return matrix[0][0]
            if i==0:
                return matrix[i][j]+getSum(i,j-1)
            if j==0:
                return matrix[i][j]+getSum(i-1,j)
            return matrix[i][j]-getSum(i-1,j)-getSum(i,j-1)+getSum(i-1,j-1)

        def area(iS,jS,iE,jE):
            if iS==jS==0:
                return getSum(iE,jE)
            if iS==0:
                return getSum(iE,jE)-getSum(iE,jS-1)
            if jS==0:
                return getSum(iE,jE)-getSum(iS-1,jE)

            return getSum(iE,jE)-getSum(iS-1,jE)-getSum(iE,jS-1)+getSum(iS-1,jS-1)

        @cache
        def check(length): # complexity:300*300
            nonlocal m,n
            if length>min(m,n):
                return False
            for i in range(m-length):
                for j in range(n-length):
                    if area(i,j,i+length,j+length)==length**2:
                        return True
            return False
        
        start=0
        end=min(m,n)
        ans=0
        while start<=end:
            mid=(start+end)//2
            if check(mid):
                ans=max(ans,mid)
                start=mid+1
            else:
                end=mid-1
        print(getSum(0,4))
        print(getSum(3,0))
        print(getSum(1,1))
        return ans
