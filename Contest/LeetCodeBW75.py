from typing import *
from collections import Counter
import heapq
from functools import cache
from itertools import combinations

from numpy import True_
class Solution1:
    def minBitFlips(self, start: int, goal: int) -> int:
        bins=bin(start)[2:]
        bing=bin(goal)[2:]
        if len(bins)<len(bing):
            bins=bins.rjust(len(bing),"0")
        elif len(bing)<len(bins):
            bing=bing.rjust(len(bins),"0")
        count=0
        for i in range(len(bins)):
            if bins[i]!=bing[i]:
                count+=1
        return count

class Solution2:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        while len(nums)>1:
            newNums=[0]*(len(nums)-1)
            for i in range(len(newNums)):
                newNums[i]=(nums[i]+nums[i+1])%10
            nums=newNums
        return nums[0]

class Solution3:
    def numberOfWays(self, s: str) -> int: # MLE
        groups=[]
        consecutive=0
        for i in range(len(s)-1):
            consecutive+=1
            if s[i+1]!=s[i]:
                groups.append(consecutive)
                consecutive=0
        groups.append(consecutive+1)
        if len(groups)<3:
            return 0

        combs=[]
        evens=list(combinations( range ( 0,len(groups),2 ),2 ) )
        for even in evens:
            start=even[0]
            end=even[1]
            for interval in range(start+1,end,2):
                newComb=list(even)
                newComb.append(interval)
                combs.append(newComb)

        odds=list(combinations( range ( 1,len(groups),2 ),2 ) )
        for odd in odds:
            start=odd[0]
            end=odd[1]
            for interval in range(start+1,end,2):
                newComb=list(odd)
                newComb.append(interval)
                combs.append(newComb)

        count=0
        for c in combs:
            #if (c[0]&1 and c[2]&1 and not c[1]&1) or ( not c[0]&1 and not c[2]&1 and c[1]&1):
            count+=groups[c[0]]*groups[c[1]]*groups[c[2]]
        return count



class Solution3:
    def numberOfWays(self, s: str) -> int: #TLE
        groups=[]
        consecutive=0
        for i in range(len(s)-1):
            consecutive+=1
            if s[i+1]!=s[i]:
                groups.append(consecutive)
                consecutive=0
        groups.append(consecutive+1)
        if len(groups)<3:
            return 0
        
        #print("groups:",groups)
        
        count=0
        def dfs(track,start):
            nonlocal count
            #print("track:",track)
            if len(track)==3:
                count+=groups[track[0]]*groups[track[1]]*groups[track[2]]
                #print("count:",count)
                return
            if start>=len(groups):
                return
            for i in range(start,len(groups)):
                if len(track)==0 or (track[-1]&1 and not i&1) or (not track[-1]&1 and i&1):
                    track.append(i)
                    dfs(track,i+1)
                    track.pop()
        dfs([],0)
        return count

class Solution3:
    def numberOfWays(self, s: str) -> int:
        count1=0
        counter=Counter()
        ret=0
        for i in range(len(s)):
            if int(s[i])==1:
                count1+=1
            counter[i]=count1
        for i in range(1,len(s)-1):
            if int(s[i])==1: # count 0
                left=i-counter[i-1]
                right=len(s)-i-1-(counter[len(s)-1]-counter[i])
            else:
                left=counter[i-1]
                right=counter[len(s)-1]-counter[i]
            ret+=left*right
        return ret

class Solution4:
    def sumScores(self, s: str) -> int:
        @cache
        def getScore(idx,s):
            if idx==len(s):
                return idx
            if idx==1:
                return 1 if s[-1]==s[0] else 0
            else:
                if s[-idx]!=s[0]:
                    return 0
                else:
                    return getScore(idx-1,s[1:])+1

        return sum(getScore(i,s) for i in range(1,len(s)+1))