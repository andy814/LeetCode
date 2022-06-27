from typing import *
from collections import deque
import itertools

class Solution:
    def trap(self,height): # extra space O(1) (if you don't use prefixsum)
        if len(height)==1:
            return 0

        prefixSum=[0]
        for h in height:
            prefixSum.append(h+prefixSum[-1])
        def getSum(a,b): # return sum[a,b]
            return prefixSum[b+1]-prefixSum[a]

        total=0
        currSum=0
        leftBarIdx=0
        for i in range(1,len(height)):
            h=height[i]
            if h>=height[leftBarIdx]:
                total+=currSum
                currSum=0
                leftBarIdx=i
                continue
            currSum+=height[leftBarIdx]-h
            #print(i,currSum)
        

        rightBarIdx=len(height)-1
        currSum=0
        for i in range(len(height)-2,-1,-1):
            h=height[i]
            if h>=height[rightBarIdx]:
                total+=currSum
                currSum=0
                rightBarIdx=i
                continue
            currSum+=height[rightBarIdx]-h
        
        overlap=0
        if abs(leftBarIdx-rightBarIdx)>1:
            minBar=min(height[leftBarIdx],height[rightBarIdx])
            #print(minBar,leftBarIdx,rightBarIdx)
            for i in range(rightBarIdx+1,leftBarIdx):
                overlap+=minBar-height[i]
        
        return total-overlap

    def trap(self,height): # extra space O(n)
        if len(height)<=2:
            return 0
        leftMax=[0]
        rightMax=[0]
        currMax=height[0]
        for i in range(1,len(height)):
            currMax=max(currMax,height[i-1])
            leftMax.append(currMax)
        currMax=height[-1]
        for i in range(len(height)-2,-1,-1):
            currMax=max(currMax,height[i+1])
            rightMax.append(currMax)
        rightMax=rightMax[::-1]
        total=0
        for i in range(1,len(height)-1):
            bar=min(leftMax[i],rightMax[i])
            total+=max(bar-height[i],0)
        return total 