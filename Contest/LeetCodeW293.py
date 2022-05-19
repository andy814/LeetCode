from functools import cache
import collections
from typing import *
from collections import defaultdict
from sortedcontainers import SortedList
import math
import bisect
from sortedcontainers import SortedList

class Solution1:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        flag=True
        while flag:
            flag=False
            for i in range(1,len(words)):
                counter1=collections.Counter(words[i])
                counter2=collections.Counter(words[i-1])
                
                same=True
                for key in counter1:
                    if counter1[key]!=counter2[key]:
                        same=False
                        break
                for key in counter2:
                    if counter2[key]!=counter1[key]:
                        same=False
                        break
                
                if same:
                    del words[i]
                    flag=True
                    break
        return words

class Solution2:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        cands=[special[0]-bottom,top-special[-1]]
        for i in range(1,len(special)):
            cands.append(special[i]-special[i-1]-1)
        return max(cands)

class Solution3:
    def largestCombination(self, candidates: List[int]) -> int:
        counts=[0]*24
        for cand in candidates:
            cand=bin(cand)[2:][::-1]
            for i,ch in enumerate(cand):
                counts[i]+=int(ch)
        return max(counts)

from sortedcontainers import SortedList

class CountIntervals:
    def __init__(self):
        self.count=0
        self.intervals=SortedList()
    def add(self, left: int, right: int) -> None:
        if [left,right] in self.intervals:
            return
        idx=bisect.bisect_left(self.intervals,[left,right])
        if idx==len(self.intervals):
            self.intervals.add([left,right])
            if len(self.intervals)==1:
                self.count+=right-left
            else:
                lastRight=self.intervals[-2][1]
                if left<lastRight:
                    self.count+=right-lastRight
                else:
                    self.count+=right-left
        elif idx==0:
            self.intervals.add([left,right])
            if len(self.intervals)==1:
                self.count+=right-left
            else:
                lastLeft=self.intervals[1][0]
                if right>lastLeft:
                    self.count+=lastLeft-left
                else:
                    self.count+=right-left
        else:
            self.intervals.add([left,right])
            prevRight=self.intervals[idx-1][1]
            nextLeft=self.intervals[idx][0]
            trueLeft=max(left,prevRight)
            trueRight=min(right,nextLeft)
            self.count+=trueRight-trueLeft


    def count(self) -> int:
        return self.count



from sortedcontainers import SortedList

class CountIntervals:
    def __init__(self):
        self.intervals=SortedList()

    def add(self, left: int, right: int) -> None:
        self.intervals.add([left,right])

    def count(self) -> int:
        prevLeft=-1
        prevRight=-1
        countNbr=0
        for interval in self.intervals:
            left=interval[0]
            right=interval[1]
            if prevRight<=left:
                countNbr+=right-prevRight
            else:
                countNbr+=right-left+1
            prevLeft=left
            prevRight=right
        return countNbr

