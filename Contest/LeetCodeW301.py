from typing import *
from sortedcontainers import SortedList
from collections import Counter,defaultdict
from functools import cache
from collections import deque
from math import comb
from torch import namedtuple_sign_logabsdet

class Solution1:
    def fillCups(self, amount: List[int]) -> int:
        ans=0
        while sum(amount)>0:
            amount.sort(reverse=True)
            if amount[1]==0:
                amount[0]-=1
            else:
                amount[0]-=1
                amount[1]-=1
            ans+=1
        return ans

# check answer, sortedlist delete time complexity?
class SmallestInfiniteSet:

    def __init__(self):
        self.infSet=set(i for i in range(1,1002))
        self.infQueue=deque(i for i in range(1,1002))

    def popSmallest(self) -> int:
        ret=self.infQueue.popleft()
        self.infSet.remove(ret)
        return ret

    def addBack(self, num: int) -> None:
        if num in self.infSet:
            return
        else:
            for i in range(len(self.infQueue)):
                if self.infQueue[i]>num:
                    self.infQueue.insert(i,num)
                    self.infSet.add(num)
                    return


# sortedList (heap also works here)
class SmallestInfiniteSet: # sortedList (heap also works here)
    def __init__(self):
        self.infSet=set(i for i in range(1,1002))
        self.infQueue=SortedList(i for i in range(1,1002))

    def popSmallest(self) -> int:
        #print(len(self.infQueue))
        ret=self.infQueue.pop(0)
        self.infSet.remove(ret)
        return ret

    def addBack(self, num: int) -> None:
        if num in self.infSet:
            return
        else:
            self.infQueue.add(num)
            self.infSet.add(num)
            return


# 看答案
class Solution3:

    def canChange(self, start: str, target: str) -> bool: # bad solution
        startStrip=start.replace("_","")
        targetStrip=target.replace("_","")
        if startStrip!=targetStrip:
            return False
        if len(targetStrip)==0:
            return True

        startLCount=0
        targetLCount=0
        startRCount=0
        targetRCount=0
        for i in range(len(start)):
            if target[i]=="L":
                if start[i]=="R":
                    return False
                if start[i]=="L":
                    startLCount+=1
                targetLCount+=1
                if startRCount>targetRCount:
                    return False
            if target[i]=="_":
                if start[i]=="R":
                    startRCount+=1
                if start[i]=="L":
                    startLCount+=1
            if target[i]=="R":
                if start[i]=="R":
                    startRCount+=1
                if start[i]=="L":
                    return False
                targetRCount+=1
                if startLCount<targetLCount:
                    return False
                
            if startLCount>targetLCount:
                return False
            
            
        startLCount=0
        targetLCount=0
        startRCount=0
        targetRCount=0
        for i in range(len(start)-1,-1,-1):
            if target[i]=="L":
                if start[i]=="R":
                    return False
                if start[i]=="L":
                    startLCount+=1
                targetLCount+=1
                if startRCount<targetRCount:
                    return False
            if target[i]=="_":
                if start[i]=="R":
                    startRCount+=1
                if start[i]=="L":
                    startLCount+=1
            if target[i]=="R":
                if start[i]=="R":
                    startRCount+=1
                if start[i]=="L":
                    return False
                targetRCount+=1
                if startLCount>targetLCount:
                    return False
                
            if startRCount>targetRCount:
                return False
                
        return True

# i循环：对于每一次上升（i=x对应x+1个不同的数字）
# key循环：对于每一个作为结尾的数字
# j循环：寻找下一个可能的结尾数字
# freq[key]的定义：以key结尾的所有数组，转化为集合后总共有几种类型（在本次迭代下）
class Solution4: # let M=maxValue
    # time complexity=M*(logM)^2
    def idealArrays(self, n: int, maxValue: int) -> int:
        freq=dict((i,1) for i in range(1,maxValue+1)) 
        ans=maxValue      
        mod=10**9+7 
        # n-1 updates 
        for i in range(1,n): # iterate min(n,logM) times
            if len(freq)==0:
                break
            temp=Counter()
            for key in freq: # O(M)
                for j in range(2,maxValue//key+1): # (M,M/2,M/3,...,1)
                    # we got harmonic series using these two loops, thereby MlogM in total
                    temp[j*key]+=freq[key]
                    ans+=freq[key]*comb(n-1,i)
                    ans%=mod
            freq=temp
        return ans%mod
