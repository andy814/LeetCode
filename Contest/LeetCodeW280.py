from collections import defaultdict
from typing import *
class Solution1:
    def countOperations(self, num1: int, num2: int) -> int:
        count=0
        while num1!=0 and num2!=0:
            if num1>=num2:
                num1-=num2
            else:
                num2-=num1
            count+=1
        return count

class Solution2: # 看答案
    def minimumOperations(self, nums: List[int]) -> int:
        oddCount=defaultdict(int)
        evenCount=defaultdict(int)
        oddList=nums[1::2]
        evenList=nums[0::2]
        for num in oddList:
            oddCount[num]+=1
        for num in evenList:
            evenCount[num]+=1

        oddCounts=sorted(oddCount.values(),reverse=True)
        evenCounts=sorted(evenCount.values(),reverse=True)
        
        if len(oddCounts)==0:
            maxOddCount=0
        else:
            maxOddCount=oddCounts[0]
        maxEvenCount=evenCounts[0]

        #sortedOddCounts=dict(sorted(oddCounts.items(), key=lambda item: item[1],reverse=True))
        #sortedEvenCounts=dict(sorted(evenCounts.items(), key=lambda item: item[1],reverse=True))
        maxOddElements=[num for num in oddCount if oddCount[num]==maxOddCount]
        maxEvenElements=[num for num in evenCount if evenCount[num]==maxEvenCount]

        if len(maxOddElements)==1 and len(maxEvenElements)==1 and maxEvenElements[0]==maxOddElements[0]:
            if len(oddCounts)==1:
                secOddCount=0
            else:
                secOddCount=oddCounts[1]
            if len(evenCounts)==1:
                secEvenCount=0
            else:    
                secEvenCount=evenCounts[1]
            if secOddCount<secEvenCount:
                #print("returning:",len(oddList)-maxOddCount + len(evenList)-secEvenCount)
                return len(oddList)-maxOddCount + len(evenList)-secEvenCount
            else:
                return len(oddList)-secOddCount + len(evenList)-maxEvenCount

        else:
            return len(oddList)-maxOddCount + len(evenList)-maxEvenCount

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        if len(beans)==1:
            return 0
        
        beans.sort()
        #print("beans:",beans)
        beanSum=sum(beans)
        beansTaken=0
        globalMin=beanSum-beans[0]*len(beans)
        for i in range(1,len(beans)): # for i: remove all prev beans.
            beansTaken+=beans[i-1]
            beanSum-=beans[i-1]
            beansToTake=beanSum-beans[i]*(len(beans)-i)
            globalMin=min(globalMin,beansTaken+beansToTake)
        return globalMin
