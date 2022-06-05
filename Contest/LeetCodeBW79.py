import functools
from typing import *
from collections import Counter
import heapq
from functools import cache
from itertools import combinations
import collections
from matplotlib.style import available
from nose import run_exit
from sortedcollections import SortedList
from collections import deque
import bisect

class Solution1:
    def digitCount(self, num: str) -> bool:
        flag=True
        ctr=Counter(num)
        print(ctr)
        for i,n in enumerate(num):
            #print(i,num[i],ctr[str(i)])
            if int(num[i])!=ctr[str(i)]:
                flag=False
                break
        return flag

class Solution2:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        @functools.cache
        def countWords(message):
            return len(message.split(" "))
        ctr=collections.Counter
        for i,sender in enumerate(senders):
            for message in messages:
                ctr[sender]+=countWords(message)
        return ctr.most_common(1)[0][0]

class Solution3:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # degree=[0]*n

        ans=0
        degrees=collections.Counter()
        for road in roads:
            degrees[road[0]]+=1
            degrees[road[1]]+=1
        ranks=degrees.most_common()
        
        weights=collections.Counter()
        curr=n
        for rank in ranks:
            weights[rank[0]]=curr
            curr-=1

        for road in roads:
            ans+=weights[road[0]]+weights[road[1]]
        return ans


class BookMyShow:

    def __init__(self, n: int, m: int):
        self.available=SortedList([m]*n)
        self.minAvailableRow=0
        self.m=m
        self.n=n

    def gather(self, k: int, maxRow: int) -> List[int]:
        toUse=self.available.bisect_left(k)
        if toUse>maxRow:
            return []
        else:
            minColumn=self.m-self.available[toUse]
            self.available[toUse]-=k        
            return [toUse,minColumn]


    def scatter(self, k: int, maxRow: int) -> bool:
        while maxRow>=self.minAvailableRow and self.available[self.minAvailableRow]<k:
            k-=self.available[self.minAvailableRow]
            self.available[self.minAvailableRow]=0
            self.minAvailableRow+=1
        if k>0:
            return False
        else:
            return True


from sortedcontainers import SortedList
class BookMyShow:

    def __init__(self, n: int, m: int): 
        self.available=[m]*n
        self.minAvailableRow=0
        self.m=m
        self.n=n

    def gather(self, k: int, maxRow: int) -> List[int]:
        toUse=self.available.bisect_left(k)
        if toUse>maxRow:
            return []
        else:
            minColumn=self.m-self.available[toUse]
            print(k,toUse,self.available[toUse])
            self.available[toUse]=self.available[toUse]-k        
            return [toUse,minColumn]


    def scatter(self, k: int, maxRow: int) -> bool:
        while maxRow>=self.minAvailableRow and self.available[self.minAvailableRow]<k:
            k-=self.available[self.minAvailableRow]
            self.available[self.minAvailableRow]=0
            self.minAvailableRow+=1
        if k>0:
            return False
        else:
            return True