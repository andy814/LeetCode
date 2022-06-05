from typing import *

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        leftMin=nums[0]
        verified=[True]*len(nums)
        for i,num in enumerate(nums):
            leftMin=min(leftMin,num)
            if num<=leftMin:
                verified[i]=False

        for i,num in enumerate(nums[::-1]):
            rightMax=max(rightMax,num)
            if num>=rightMax:
                verified[len(nums)-i-1]=False
        
        return True if True in verified else False
        