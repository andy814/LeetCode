from cmath import pi
from typing import *
import heapq
from numpy import interp
class Solution1:
    def minimumSum(self, num: int) -> int:
        numList=[]
        while num>0:
            numList.append(num%10)
            num//=10
        numList.sort()
        return numList[0]*10+numList[2]+numList[1]*10+numList[3]

class Solution2:

    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        '''
        #temp=[0]*len(nums)
        sTemp=[]
        lTemp=[]
        pivotCount=0
        ret=nums.copy()
        start=0
        end=len(nums)-1
        while start<end:
            while (start<end and nums[start]<=pivot):
                if nums[start]==pivot:

                start+=1
            while (start<end and nums[end]>=pivot):
                end-=1
            if start<end:
                lTemp.append(nums[start])
                sTemp.append(nums[end])
                ret.remove(nums[start])
                ret.remove(nums[end])    
                start+=1
                end-=1
        idx=ret.index(pivot)
        print("pvtIdxx:",idx)
        sTemp=sTemp[::-1]
        print("LT:",lTemp)
        print("ST:",sTemp)
        print("ret:",ret)
        ret=ret[:idx]+sTemp+[ret[idx]]+lTemp+ret[idx+1:]
        return ret
        '''
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        sTemp=[]
        eTemp=[]
        gTemp=[]
        for num in nums:
            if num<pivot:
                sTemp.append(num)
            elif num==pivot:
                eTemp.append(num)
            else:
                gTemp.append(num)
        return sTemp+eTemp+gTemp

class Solution3:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def standardInterpret(startAt,moveCost,pushCost,targetSeconds):
            min=targetSeconds//60
            sec=targetSeconds%60
            time=0
            interpret=[]
            
            interpret.append(min//10)
            interpret.append(min%10)

            interpret.append(sec//10)
            interpret.append(sec%10)

            metNon0=False
            for num in interpret:
                if num==0 and not metNon0:
                    continue
                if startAt!=num:
                    time+=moveCost
                time+=pushCost

                startAt=num
                if num!=0:
                    metNon0=True
            return (interpret,time)

        interpret,time1=standardInterpret(startAt,moveCost,pushCost,targetSeconds)

        if interpret[2]>=4 or (interpret[0]==0 and interpret[1]==0):
            return time1
        
        time2=0
        interpret[2]+=6
        if interpret[1]==0:
            interpret[1]=9
            interpret[0]-=1
        else:
            interpret[1]-=1

        metNon0=False
        for num in interpret:
            if num==0 and not metNon0:
                continue
            if startAt!=num:
                time2+=moveCost
            time2+=pushCost

            startAt=num
            if num!=0:
                metNon0=True
        
        return min(time1,time2)

class Solution4:
    def minimumDifference(self, nums: List[int]) -> int:
        n=len(nums)//3
        firstPart=nums[:n]
        middlePart=nums[n:2*n]
        lastPart=nums[2*n:]
        sumL=[sum(firstPart)]
        sumR=[sum(lastPart)]

        firstPart=[-num for num in firstPart]
        heapq.heapify(firstPart)
        currSum=sumL[0]
        for i in range(n):
            heapTop=heapq.heappop(firstPart)*(-1)
            minNbr=min(middlePart[i],heapTop)
            heapq.heappush(firstPart,minNbr*(-1))
            currSum=currSum-heapTop+minNbr
            sumL.append(currSum)

        heapq.heapify(lastPart)
        currSum=sumR[0]
        for i in range(n-1,-1,-1):
            heapTop=heapq.heappop(lastPart)
            maxNbr=max(middlePart[i],heapTop)
            heapq.heappush(lastPart,maxNbr)
            currSum=currSum-heapTop+maxNbr
            sumR.append(currSum)

        sumR=sumR[::-1]

        return min([sumL[i]-sumR[i] for i in range(n+1)])

