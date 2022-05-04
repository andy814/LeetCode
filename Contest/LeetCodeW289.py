from gc import collect
from heapq import nlargest
from typing import *
from collections import Counter
import collections 
from sortedcontainers import SortedList

class Solution1:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            groupNbr=len(s)//k+1
            groups=[0]*groupNbr
            for i in range(groupNbr):
                groups[i]=sum( [ int (ch) for ch in s[i*k:i*k+k] ] )
            s="".join([str(group) for group in groups])
        return s

class Solution2:
    def minimumRounds(self, tasks: List[int]) -> int:
        taskCounter=Counter()
        for task in tasks:
            taskCounter[task]+=1

        for key in taskCounter:
            if taskCounter[key]==1:
                return -1
        ans=0
        for key in taskCounter:
            ans+=(taskCounter[key]-1)//3+1
            #print("key,ans:",key,ans)
        return ans


class Solution3:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        
        width=len(grid[0])
        height=len(grid)
        
        factors=[[(0,0) for j in range(width)] for i in range(height)]
        for i in range(height):
            for j in range(width):
                twobase=1
                fivebase=1
                while grid[i][j]% (2**twobase)==0 and 2**twobase<=grid[i][j]:
                    twobase+=1
                while grid[i][j]% (5**fivebase)==0 and 5**fivebase<=grid[i][j]:
                    fivebase+=1
                num2=twobase-1
                num5=fivebase-1
                factors[i][j]=(num2,num5)
                
        
        leftright=[[(0,0) for j in range(width)] for i in range(height)]
        for i in range(height):
            num2=0
            num5=0
            for j in range(width):
                num2+=factors[i][j][0]
                num5+=factors[i][j][1]
                leftright[i][j]=(num2,num5)

        
        updown=[[(0,0) for j in range(width)] for i in range(height)]
        for j in range(width):
            num2=0
            num5=0
            for i in range(height):
                num2+=factors[i][j][0]
                num5+=factors[i][j][1]
                updown[i][j]=(num2,num5)
        
        ans=0
        for i in range(height):
            for j in range(width):
                left=(  leftright[i][j-1][0],leftright[i][j-1][1]   )  if j!=0 else (0,0)
                right=(  leftright[i][-1][0]-leftright[i][j][0],leftright[i][-1][1]-leftright[i][j][1]   )  if j!=width-1 else (0,0)
                up=( updown[i-1][j][0], updown[i-1][j][1]) if i!=0 else (0,0)
                down=( updown[-1][j][0]-updown[i][j][0], updown[-1][j][1]-updown[i][j][1] ) if i!=height-1 else (0,0)
                twobase=1
                fivebase=1
                while grid[i][j]% (2**twobase)==0 and 2**twobase<=grid[i][j]:
                    twobase+=1
                while grid[i][j]% (5**fivebase)==0 and 5**fivebase<=grid[i][j]:
                    fivebase+=1
                num2=twobase-1
                num5=fivebase-1
                r1=min(left[0]+up[0]+num2,left[1]+up[1]+num5)
                r2=min(left[0]+down[0]+num2,left[1]+down[1]+num5)
                r3=min(right[0]+up[0]+num2,right[1]+up[1]+num5)
                r4=min(right[0]+down[0]+num2,right[1]+down[1]+num5)
                #print(i,j,left,right,up,down)
                newans=max(r1,r2,r3,r4)
                ans=max(ans,newans)
        return ans

class Solution4:
    def longestPath(self, parent: List[int], s: str) -> int:
        childDict=collections.defaultdict(list)
        for i,j in enumerate(parent):
            if j!=-1:
                childDict[j].append(i)

        res=-1
        def dfs(curr):
            nonlocal res
            cand=[]
            for child in childDict[curr]:
                temp=dfs(child)
                if s[child]!=s[curr]:
                    cand.append(temp)
            if len(cand)>=2:
                res=max(res,sum(nlargest(2,cand))+1)
                return max(cand)+1
            elif len(cand)==1:
                res=max(res,cand[0]+1)
                return cand[0]+1
            else:
                res=max(res,1)
                return 1
        
        dfs(0)
        return res

            