from collections import defaultdict
from collections import Counter
from functools import lru_cache
from typing import *
from functools import lru_cache
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

class Solution2: 
    '''
    def minimumOperations(self, nums: List[int]) -> int: # this one is horrible
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
    '''
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0
        pad=lambda x:x+[(None,2)*(2-len(x))]
        even=pad(Counter(nums[0::2]))
        odd=pad(Counter(nums[1::2]))
        if even.most_common[0][0]!=odd.most_common[0][0]:
           return len(nums)-even.most_common[0][1]-odd.most_common[0][1]
        else:
            return len(nums)-max( even.most_common[1][1]+odd.most_common[0][1], even.most_common[0][1]+odd.most_common[1][1]  )



class Solution3:
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

class Solution4:
    '''
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int: # TLE
        mask=2**(numSlots*2)-1 # 1:available 0:occupied
        # 99 <- 332211
        @lru_cache(None)
        def dp(startIdx,mask):
            if startIdx>=len(nums):
                return 0
            ans=0
            for i in range(numSlots*2):
                slotNum=i//2+1
                if mask&(1<<i):
                    ans=max( ans, (slotNum&nums[startIdx]) + dp(startIdx+1,mask^(1<<i)) )
            return ans
        return dp(0,mask)
    '''
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int: 
        mask1=2**(numSlots)-1 # 1:available 0:occupied
        mask2=mask1
        # 99 <- 332211
        @lru_cache(None)
        def dp(startIdx,mask1,mask2):
            if startIdx>=len(nums):
                return 0
            ans=0
            for i in range(numSlots):
                slotNum=i+1
                if mask1&(1<<i):
                    if mask2&(1<<i):
                        ans=max( ans, (slotNum&nums[startIdx]) + dp(startIdx+1,mask1,mask2^(1<<i) ) )
                    else:
                        ans=max( ans, (slotNum&nums[startIdx]) + dp(startIdx+1,mask1^(1<<i),mask2) ) 
            return ans
        return dp(0,mask1,mask2)
