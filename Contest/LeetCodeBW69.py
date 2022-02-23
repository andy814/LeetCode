from typing import *
import collections
class Solution1:
    def capitalizeTitle(self, title: str) -> str:
        strs=title.split(" ")
        ret=[]
        for curr in strs:
            if len(curr)<=2:
                curr=curr.lower()
            else:
                #curr=curr.lower()
                curr=curr.capitalize()
            ret.append(curr)
        return " ".join(strs)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution2:
    def pairSum(self, head: Optional[ListNode]) -> int:
        array=[]
        while head:
            array.append(head.val)
            head=head.next
        sumarray=[]
        for i in range(len(array)//2): 
            sumarray.append(array[i]+array[len(array)-1-i])   
        return max(sumarray)


class Solution3: 
    def longestPalindrome(self, words: List[str]) -> int:
        palNum=0
        wordCount=collections.defaultdict(lambda:0)
        for word in words:
            wordCount[word]+=1

        for i in range(len(words)):
            if self.isPal(words[i]):
                if wordCount[words[i]]>1:
                    palNum+=2
                    wordCount[words[i]]-=2
            else:
                if wordCount[words[i]]>0 and wordCount[self.rev(words[i])]>0:
                    palNum+=2
                    wordCount[words[i]]-=1
                    wordCount[self.rev(words[i])]-=1

        for word in wordCount:
            if wordCount[word]>0 and self.isPal(word):
                palNum+=1
                break

        return palNum*2

    def isPal2(self,str1,str2):
        return str1[0]==str2[1] and str1[1]==str2[0]

    def isPal(self,str1):
        return str1[0]==str1[1]

    def rev(self,str1):
        return str1[::-1]

    '''
    test:
    ["lc","cl","gg"]
    ["ab","ty","yt","lc","cl","ab"]
    ["cc","ll","xx"]
    ["aa","bb","aa","bb"]
    '''

class Solution4_TimeLimitExceeded:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.checkStamp(grid,j,i,stampHeight,stampWidth):
                    self.setVisited(grid,j,i,stampHeight,stampWidth)

        flag=True
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0: 
                    flag=False
                    break
        #print("grid:",grid)
        return flag

    def checkStamp(self,grid,x,y,h,w) ->bool: # (x,y): top-left of the stamp
        gridWidth=len(grid[0])
        gridHeight=len(grid)
        xstart=x
        xend=min(x+w,gridWidth)
        ystart=y
        yend=min(y+h,gridHeight)
        flag=True
        for i in range(ystart,yend):
            for j in range(xstart,xend):
                if grid[i][j]==1:
                    flag=False
                    break
        return flag

    def setVisited(self,grid,x,y,h,w):
        gridWidth=len(grid[0])
        gridHeight=len(grid)
        xstart=x
        xend=min(x+w,gridWidth)
        ystart=y
        yend=min(y+h,gridHeight)
        for i in range(ystart,yend):
            for j in range(xstart,xend):
                if grid[i][j]==0:
                    grid[i][j]=-1

import numpy as np
class Solution4:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m,n=len(grid),len(grid[0])
        occupyPrefix=self.calcPrefix(grid)
        stampgrid=np.zeros((m,n),dtype=int)
        for i in range(m-stampHeight+1):
            for j in range(n-stampWidth+1):
                if self.calcRectSum(occupyPrefix,i,j,i+stampHeight-1,j+stampWidth-1)==0:
                    stampgrid[i][j]=1
        stampPrefix=self.calcPrefix(stampgrid)
        flag=True
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    continue
                if self.calcRectSum(stampPrefix,max(0,i-stampHeight+1),max(0,j-stampWidth+1),i,j)==0:
                    return False
        return flag

    
    def calcPrefix(self,grid):
        m,n=len(grid)+1,len(grid[0])+1
        ret=[[0]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                ret[i][j]=ret[i-1][j]+ret[i][j-1]-ret[i-1][j-1]+grid[i-1][j-1]
        return ret

    def calcRectSum(self,grid,row1,col1,row2,col2):
        row1,col1,row2,col2=row1+1,col1+1,row2+1,col2+1
        return grid[row2][col2]-grid[row1-1][col2]-grid[row2][col1-1]+grid[row1-1][col1-1]

sol=Solution4()
print(sol.possibleToStamp([[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]],4,3))