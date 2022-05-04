from typing import *
from collections import Counter
import heapq
from functools import cache
from itertools import combinations
import collections

from sortedcollections import SortedList

class Solution1(object):
    def findClosestNumber(self, nums):
        ret=min([abs(i) for i in nums])
        if ret not in nums:
            return -ret
        return ret

class Solution2(object):
    def waysToBuyPensPencils(self, total, cost1, cost2):
        maxPencil=total//cost2
        ret=0
        
        for pencil in range(maxPencil+1):
            moneyLeft=total-pencil*cost2
            ret+=moneyLeft//cost1
        
        return ret

class ATM:

    def __init__(self):
        self.notes=[0,0,0,0,0]
        self.face=[20,50,100,200,500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.notes[i]+=banknotesCount[i]
        
    def withdraw(self, amount: int) -> List[int]:
        #print("notes:",self.notes)
        ret=[0,0,0,0,0]
        for i in range(4,-1,-1):
            ret[i]=min(self.notes[i],amount//self.face[i])
            amount-=ret[i]*self.face[i]
        if amount!=0:
            return [-1]
        else:
            for i in range(4,-1,-1):
                self.notes[i]-=ret[i]
            return ret

    
from sortedcontainers import SortedList
class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        
        topAdj=collections.defaultdict(SortedList)
        for edge in edges:
            topAdj[edge[0]].add((scores[edge[1]],edge[1]))
            topAdj[edge[1]].add((scores[edge[0]],edge[0]))

        for key in topAdj:
            topAdj[key]=topAdj[key][::-1]
            keylen=len(topAdj[key])
            topAdj[key]=topAdj[key][:min(keylen,3)]
        
        ret=-1
        for edge in edges:
            mid1=edge[0]
            mid2=edge[1]
            for start in topAdj[mid1]:
                for end in topAdj[mid2]:
                    if start[1]!=mid2 and end[1]!=mid1 and start[1]!=end[1]:
                        ret=max(ret,scores[start[1]]+scores[end[1]]+scores[mid1]+scores[mid2])
        return ret