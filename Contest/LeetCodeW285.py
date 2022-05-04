from tarfile import RECORDSIZE
from typing import *
import collections
from functools import cache

class Solution1:
    '''
    def countHillValley(self, nums: List[int]) -> int:
        ret=0
        for i,num in enumerate(nums):
            if i==0:
                continue
            if i==len(nums)-1:
                continue
            
            if nums[i]<nums[i+1] and nums[i]<nums[i-1]:
                ret+=1
            if nums[i]>nums[i+1] and nums[i]>nums[i-1]:
                ret+=1
    '''
    def countHillValley(self, nums: List[int]) -> int: # 看答案
        prev=0
        curr=1
        next=2
        ret=0
        while curr<len(nums)-1:
            if nums[curr]<nums[next] and nums[curr]<nums[prev]:
                ret+=1
                prev=curr
                curr=next
                next+=1
                continue
            if nums[curr]>nums[next] and nums[curr]>nums[prev]:
                ret+=1
                prev=curr
                curr=next
                next+=1
                continue
            if nums[curr]==nums[next]:
                curr=next
                next+=1
                continue
            prev=curr
            curr=next
            next+=1        
        return ret

class Solution2:
    def countCollisions(self, directions: str) -> int:
        LStrip=0
        RStrip=0
        for char in directions:
            if char=="L":
                LStrip+=1
            else:
                break
        for char in directions[::-1]:
            if char=="R":
                RStrip+=1
            else:
                break
        if RStrip!=0:
            sDirections=directions[LStrip:-RStrip] # rstrip=0?
        else:
            sDirections=directions[LStrip:]

        if len(sDirections)<=1:
            return 0

        count=0
        R=0
        for char in sDirections:
            if char=="R":
                R+=1
            elif char=="L":
                count+=R+1
                R=0
            else:
                count+=R
                R=0
        return count
        
class Solution3:
    '''
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        targets=[i+1 for i in aliceArrows]
        record=[0]*12
        @cache
        def dp(i,arrorsLeft):
            if arrorsLeft<0:
                return -float("inf")
            if i>11:
                return 0
            dp1= dp(i+1,arrorsLeft-targets[i])+i
            dp2= dp(i+1,arrorsLeft)
            if dp1>dp2:
                record[i]=targets[i]
            return max( dp1,dp2 )
        dp(0,numArrows)
        return record
    '''
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]: #看答案
        targets=[i+1 for i in aliceArrows]
        record=[0]*12
        
        @cache
        def wrapper(i,arrorsLeft):
            if arrorsLeft<0:
                return 
            if i>11:
                return
            @cache
            def dp(i,arrorsLeft):
                if arrorsLeft<0:
                    return -float("inf"),False
                if i>11:
                    return 0,False
                #print("dp res:",dp(i+1,arrorsLeft-targets[i]))
                dp1= dp(i+1,arrorsLeft-targets[i])[0]+i
                dp2= dp(i+1,arrorsLeft)[0]
                flag=False
                if dp1>dp2:
                    flag=True
                return max( dp1,dp2 ),flag # True means choose I
            
            res=dp(i,arrorsLeft)
            if res[1]==True:
                record[i]=targets[i]
                wrapper(i+1,arrorsLeft-targets[i])
            else:
                wrapper(i+1,arrorsLeft)

        wrapper(0,numArrows)
        
        record[0]=numArrows-sum(record)
        return record

    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]: # simplified
        targets=[i+1 for i in aliceArrows]
        record=[0]*12

        @cache
        def dp(i,arrorsLeft):
            if arrorsLeft<0:
                return -float("inf")
            if i>11:
                return 0
            dp1= dp(i+1,arrorsLeft-targets[i])+i
            dp2= dp(i+1,arrorsLeft)
            return max( dp1,dp2 ) # True means choose I

        arrowsLeft=numArrows
        for k in range(1,12):
            if dp(k,arrowsLeft)!=dp(k+1,arrowsLeft): # choose k
                record[k]=targets[k]
                arrowsLeft-=targets[k]
        
        record[0]=numArrows-sum(record)
        return record


class Solution4:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        