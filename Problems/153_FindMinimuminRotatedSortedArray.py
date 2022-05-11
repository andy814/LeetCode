from typing import *
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start=0
        end=len(nums)-1
        if len(nums)==1:
            return nums[0]
        if nums[0]<nums[-1]:  # no rotate
            return nums[0]         
        while start<=end:
            mid=(start+end)//2
            if mid==0:
                return min(nums[0],nums[1])
            if nums[mid]>nums[0]:
                start=mid+1
            elif nums[mid]<nums[0]:
                end=mid
            if start==end==mid:
                return nums[mid]
        #return nums[mid]