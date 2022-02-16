from typing import *
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret=[]
        currIdx=0
        while currIdx<len(intervals)-1:
            leftBound=intervals[currIdx][0]
            rightBound=intervals[currIdx][1] 
            while currIdx<len(intervals)-1 and rightBound>=intervals[currIdx+1][0]:
                #print("leftBound,rightBound,currIdx:",leftBound,rightBound,currIdx)
                currIdx+=1
                rightBound=max(intervals[currIdx][1],rightBound)
            ret.append([leftBound,rightBound])
            currIdx+=1
        if currIdx<len(intervals):
            ret.append([intervals[-1][0],intervals[-1][1]])
        return ret