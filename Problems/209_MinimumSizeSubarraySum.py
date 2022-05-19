from typing import *
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int: # O(n)
        prev=0
        sum=0
        minLen=float("inf")
        for i,num in enumerate(nums):
            sum+=num
            if sum>=target:
                minLen=min(minLen,i-prev+1)
            while prev<i and sum-nums[prev]>=target:
                sum-=nums[prev]
                prev+=1
                minLen=min(minLen,i-prev+1)
        if minLen==float("inf"):
            return 0
        return minLen

    def minSubArrayLen(self, target: int, nums: List[int]) -> int: # O(nlogn)
        sum=0
        prefix=[]
        for num in nums:
            sum+=num
            prefix.append(sum)

        def checkLen(target:int, length: int):
            if length==0:
                return False
            if length==1:
                #print("returning:",max(nums),target)
                return max(nums)>=target

            ret=False
            for i in range(len(nums)-length+1):
                if i==0:
                    if prefix[i+length-1]>=target:
                        ret=True
                        break
                    
                else:
                    if prefix[i+length-1]-prefix[i-1]>=target:
                        ret=True
                        break
            return ret

        minLen=float("inf")
        start=0
        end=len(nums)
        while start<=end:
            
            mid=(start+end)//2
            print(start,end,mid)
            if checkLen(target,mid)==True:
                minLen=min(minLen,mid)
                end=mid-1
            else:
                start=mid+1

        if minLen==float("inf"):
            return 0
        return minLen