from typing import *
from collections import Counter
from functools import cache
class Solution1:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count=len(words)
        for word in words:
            if len(pref)>len(word):
                count-=1
                continue
            for i,char in enumerate(pref):
                if word[i]!=char:
                    count-=1
                    break
        return count

class Solution2: # 试试减号，subtract
    def minSteps(self, s: str, t: str) -> int:
        sCounter=Counter(list(s))
        tCounter=Counter(list(t))
        ret=0
        sCounter.subtract(tCounter)
        for key in sCounter:
            ret+=abs(sCounter[key])
        return ret

class Solution3:
    '''
    def minimumTime(self, time: List[int], totalTrips: int) -> int: # TLE
        
        def factorize(time): 
            ret=[]
            for i in range(1,time+1):
                if time%i==0:
                    ret.append(i)

        timeCounter=Counter(time)
        trips=0
        totalTime=0
        while trips<totalTrips:
            totalTime+=1
            factors=factorize(time)
            for factor in factors:
                trip+=timeCounter[factor]
        return totalTime
    '''

    def minimumTime(self, time: List[int], totalTrips: int) -> int: # worst: log2(10**14)*10^5, sometimes TLE
        timeCounter=Counter(time)
        def numTrips(queryTime): # 10^5 at worst
            totalTrips=0
            for key in timeCounter:
                totalTrips+=(queryTime//key)*timeCounter[key]
            return totalTrips
        start=0
        end=totalTrips*min(time) 
        res=[]
        while start<=end:
            queryTime=(start+end)//2
            if totalTrips<=numTrips(queryTime):
                end=queryTime-1
                res.append(queryTime)
            elif totalTrips>numTrips(queryTime):
                start=queryTime+1
        return min(res)

class Solution4:
    '''
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int: # TLE
        tires=[tuple(tire) for tire in tires]
        @cache
        def dp(currTire,currTime,numLaps):
            if numLaps==0:
                return 0
            ans=dp(currTire,currTime+1,numLaps-1)+currTire[0]*(currTire[1]**currTime)
            for tire in tires:
                ans=min(ans,dp(tire,1,numLaps-1)+changeTime+tire[0])
            return ans
        
        ans=float("inf")
        for tire in tires:
            ans=min(ans,dp(tire,0,numLaps))
        
        return ans
    '''

    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int: # TLE
        maxDepth=19
        tires=list(set(tuple(tire) for tire in tires))
        memo=[] # memo[tire][numLap]=(numLapTime,totalTime)
        for tire in tires:
            tireTime=[(0,0)] 
            for i in range(1,maxDepth+1):
                if i==1:
                    tireTime.append((tire[0],tire[0]))
                else:
                    tireTime.append( (tire[1]*tireTime[-1][0],tireTime[-1][1]+tire[1]*tireTime[-1][0]) )
            memo.append(tireTime)
        bestNumLaps=[0] # the minimum cost of continuous i-lap on the same tire

        for i in range(1,min(numLaps,maxDepth)+1): # 19
            bestNumLaps.append( min([ memo[tire][i][1] for tire in range(len(tires)) ])  ) # 10^5

        @cache
        def dp(laps): # constant transition
            ans=float("inf") if laps>maxDepth else bestNumLaps[laps]
            for i in range(1,min(maxDepth+1,laps)):
                ans=min(ans,bestNumLaps[i]+changeTime+dp(laps-i))
            return ans
        return dp(numLaps)

        # 思路是倒着想，先想dp怎么写，再想bestNumLap是怎么来的，最后再设计memo