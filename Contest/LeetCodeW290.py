from bisect import bisect_right,bisect_left
from typing import *
import collections
from numpy import square
from pyrsistent import inc 
from sortedcontainers import SortedList

class Solution1:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans=[]
        for i in range(1,1001):
            for li in nums:
                if i not in li:
                    break
            ans.append(i)
        return ans

class Solution2:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        
        @cache
        def square(x1):
            return x1**2
        
        @cache
        def sqrt(x1):
            return x1**0.5
        
        @cache
        def calcDist(x1,y1,x2,y2):
            return sqrt(square(x2-x1)+square(y2-y1))
        
        inCircle=set()
        
        for circle in circles:
            for i in range(circle[0]-circle[2],circle[0]+circle[2]+1):
                for j in range(circle[1]-circle[2],circle[1]+circle[2]+1):
                    if (i,j) not in inCircle:
                        if calcDist(i,j,circle[0],circle[1])<=circle[2]:
                            inCircle.add((i,j))
        return len(inCircle)

class Solution3:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        ans=[]
        heightDict=collections.defaultdict(list)
        for rec in rectangles:
            heightDict[rec[1]].append(rec[0])
        for key in heightDict:
            heightDict[key].sort()
            
        for point in points:
            insideNum=0
            point_x=point[0]
            point_y=point[1]
            for key in heightDict:
                if key>=point_y:
                    insideNum+=len(heightDict[key])-bisect_left(heightDict[key],point_x)
            ans.append(insideNum)
        return ans

class Solution4:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        starts=sorted(f[0] for f in flowers)
        ends=sorted(f[1] for f in flowers)
        ans=[]
        for person in persons:
            numFlowers=bisect_right(starts,person)-bisect_left(ends,person)
            ans.append(numFlowers)
        return ans
            