from typing import *
from collections import Counter
import heapq
from functools import cache
from itertools import combinations
import collections
from nose import run_exit
from sortedcollections import SortedList

class Solution1:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count=0
        for word in words:
            isPrefix=True
            for i,ch in enumerate(word):
                if i>=len(s) or s[i]!=ch:
                    isPrefix=False
                    break
            if isPrefix:
                count+=1
        return count

class Solution2:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        
        numSum=sum(nums)
        currSum=0
        averageFront=[]
        averageRear=[]
        for i,num in enumerate(nums):
            currSum+=num
            front=currSum//(i+1)
            rear=(numSum-currSum)//(len(nums)-i-1)  if i<len(nums)-1 else 0
            averageFront.append( front )
            averageRear.append( rear )  
        #print(averageFront)
        #print(averageRear)
        ret=float("inf")
        retIdx=-1
        for i in range(len(nums)):
            if ret>abs(averageFront[i]-averageRear[i]):
                retIdx=i
                ret=abs(averageFront[i]-averageRear[i])
        return retIdx

from sortedcontainers import SortedList
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        horizontalGuards=collections.defaultdict(SortedList)
        verticalGuards=collections.defaultdict(SortedList)
        horizontalWalls=collections.defaultdict(SortedList)
        verticalWalls=collections.defaultdict(SortedList)
        for guard in guards:
            horizontalGuards[guard[0]].add(guard[1])
            verticalGuards[guard[1]].add(guard[0])
        for wall in walls:
            horizontalWalls[wall[0]].add(wall[1])
            verticalWalls[wall[1]].add(wall[0])
        count=0
        
        #print("horiGuards:",horizontalGuards)
        
        for i in range(m):
            for j in range(n):
                if j in horizontalGuards[i] or i in verticalGuards[j] or j in horizontalWalls[i] or i in verticalWalls[j]: # occupied
                    continue
                vertBlocked=False
                horiBlocked=False
                rightGuardIdx=horizontalGuards[i].bisect_left(j)
                leftGuardIdx=rightGuardIdx-1
                rightGuard=horizontalGuards[i][rightGuardIdx] if rightGuardIdx<len(horizontalGuards[i]) else -1
                leftGuard=horizontalGuards[i][leftGuardIdx] if leftGuardIdx>=0 else -1
                rightWallIdx=horizontalWalls[i].bisect_left(j)
                leftWallIdx=rightWallIdx-1
                rightWall=horizontalWalls[i][rightWallIdx] if rightWallIdx<len(horizontalWalls[i]) else -1
                leftWall=horizontalWalls[i][leftWallIdx] if leftWallIdx>=0 else -1
                
                leftBlocked=False
                rightBlocked=False
                if leftWall>leftGuard or leftGuard==-1:
                    leftBlocked=True
                if (rightWall!=-1 and rightWall<rightGuard) or rightGuard==-1:
                    rightBlocked=True
                if leftBlocked and rightBlocked:
                    horiBlocked=True


                downGuardIdx=verticalGuards[j].bisect_left(i)
                upGuardIdx=downGuardIdx-1
                downGuard=verticalGuards[j][downGuardIdx] if downGuardIdx<len(verticalGuards[j]) else -1
                upGuard=verticalGuards[j][upGuardIdx] if upGuardIdx>=0 else -1
                downWallIdx=verticalWalls[j].bisect_left(i)
                upWallIdx=downWallIdx-1
                downWall=verticalWalls[j][downWallIdx] if downWallIdx<len(verticalWalls[j]) else -1
                upWall=verticalWalls[j][upWallIdx] if upWallIdx>=0 else -1
                
                upBlocked=False
                downBlocked=False
                if upWall>upGuard or upGuard==-1:
                    upBlocked=True
                if (downWall!=-1 and downWall<downGuard) or downGuard==-1:
                    downBlocked=True
                if upBlocked and downBlocked:
                    vertBlocked=True
                
                #print(i,j)
                #print(upGuard,downGuard,leftGuard,rightGuard)
                #print(upWall,downWall,leftWall,rightWall)
                #print(upGuardIdx,downGuardIdx,leftGuardIdx,rightGuardIdx)
                #print(upWallIdx,downWallIdx,leftWallIdx,rightWallIdx)
                
                if horiBlocked and vertBlocked:
                    count+=1
        return count
                
                    




