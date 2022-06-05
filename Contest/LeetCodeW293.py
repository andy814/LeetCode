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
from sortedcontainers import SortedDict
class CountIntervals: 

    def __init__(self):
        self.intervals = SortedDict()
        self.counts=0

    def add(self, left: int, right: int) -> None: # time analysis: each interval add and leave the dict once, each operation takes O(logn)
        if len(self.intervals)==0:
            self.intervals[left]=right
            self.counts+=right-left+1
            return # first region
        
        if left in self.intervals and right==self.intervals[left]:
            return # duplicated region

        leftDone=False
        rightDone=False
        while not leftDone:
            if self.intervals.bisect_left(left)==0: # leftmost
                if left in self.intervals:
                    self.counts-=self.intervals[left]-left+1
                    #self.intervals[left]=max(right,self.intervals[left])
                    right=max(right,self.intervals[left])
                    self.intervals.pop(left)
                leftDone=True
                break
    
            leftInterval=self.intervals.peekitem(self.intervals.bisect_left(left)-1)
            leftStart=leftInterval[0]
            leftEnd=leftInterval[1]
            
            if leftEnd<left:
                leftDone=True
            else: # merge
                self.intervals.pop(leftStart)
                self.counts-= leftEnd-leftStart+1
                left=leftStart
                right=max(leftEnd,right)
        
        while not rightDone:
            if self.intervals.bisect_left(left)==len(self.intervals):
                rightDone=True
                break
            
            rightInterval=self.intervals.peekitem(self.intervals.bisect_left(left))
            rightStart=rightInterval[0]
            rightEnd=rightInterval[1]
            if rightStart>right:
                rightDone=True
            else: # merge
                self.intervals.pop(rightStart)
                self.counts-= rightEnd-rightStart+1
                left=left
                right=max(rightEnd,right)

        self.intervals[left]=right
        self.counts+=right-left+1
        
    def count(self) -> int:
        return self.counts